import pygame
from player import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        screen = pygame.draw.polygon(screen, (255,255,255), self.triangle())

    def update(self, dt):
        # sub-classes must override
        pass

    def collide(self, other_object):
        distance = self.position.distance_to(other_object.position)
        if distance <= (self.radius + other_object.radius):
            return True
        else:
            return False
