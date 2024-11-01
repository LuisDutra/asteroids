import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

    def colision(self, object):
        distance = self.position.distance_to(object.position)
        return  distance <  self.radius + object.radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass