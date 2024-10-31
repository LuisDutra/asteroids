from circleshape import *
import pygame 
from constants import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def rotate(self, dt):
        self.rotation += ROTATION_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1)
        self.position += forward * self.velocity * dt
    

    def update(self, dt):
        self.move(dt)