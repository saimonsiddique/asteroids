import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        """
        Initialize the player with a given position and default radius.
        """
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    def triangle(self):
        """
        Calculate the vertices of the player's triangular shape.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        """
        Draw the player on the screen.
        """
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        """
        Rotate the player based on the turn speed and delta time.
        """
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        """
        Update the player's state, including movement, rotation, and shooting.
        """
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            if self.shoot_timer > 0:
                return
            else:
                self.shoot()
    
    def move(self, dt):
        """
        Move the player forward or backward based on the speed and delta time.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        """
        Shoot a projectile if the cooldown timer allows.
        """
        shot = Shot(*self.position)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN