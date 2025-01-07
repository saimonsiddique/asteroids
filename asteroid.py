import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        first_spawn_velocity = self.velocity.rotate(random_angle)
        second_spawn_velocity = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        first_spawn_asteroid = Asteroid(*self.position, new_radius)
        first_spawn_asteroid.velocity = first_spawn_velocity * 1.2
        second_spawn_asteroid = Asteroid(*self.position, new_radius)
        second_spawn_asteroid.velocity = second_spawn_velocity * 1.2

