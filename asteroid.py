import pygame
from circleshape import *
from constants import ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_KINDS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def draw(self,screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self, asteroids):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            p = self.position
            random_angle = random.uniform(20, 50)
            vector_1 = self.velocity.rotate(random_angle)
            vector_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(p.x, p.y, new_radius)
            asteroid_2 = Asteroid(p.x, p.y, new_radius)
            asteroid_1.velocity = vector_1 * 1.2
            asteroid_2.velocity = vector_2 * 1.2
            asteroids.add(asteroid_1)
            asteroids.add(asteroid_2)



        
