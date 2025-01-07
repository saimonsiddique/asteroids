import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        """
        Initialize an asteroid with a given position and radius.
        """
        super().__init__(x, y, radius)

    def draw(self, screen):
        """
        Draw the asteroid on the screen.
        """
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        """
        Update the asteroid's position based on its velocity and delta time.
        """
        self.position += self.velocity * dt
    
    def split(self):
        """
        Split the asteroid into smaller pieces if its radius is above the minimum threshold.
        """
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(RANDOM_ANGLE_MIN, RANDOM_ANGLE_MAX)
        first_spawn_velocity = self.velocity.rotate(random_angle)
        second_spawn_velocity = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        first_spawn_asteroid = Asteroid(*self.position, new_radius)
        first_spawn_asteroid.velocity = first_spawn_velocity * VELOCITY_MULTIPLIER
        second_spawn_asteroid = Asteroid(*self.position, new_radius)
        second_spawn_asteroid.velocity = second_spawn_velocity * VELOCITY_MULTIPLIER