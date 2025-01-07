import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        """
        Initialize a shot with a given position and default radius.
        """
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        """
        Draw the shot on the screen.
        """
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        """
        Update the shot's position based on its velocity and delta time.
        """
        self.position += self.velocity * dt