from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED, PLAYER_SHOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import *
import pygame
import pygame.math

class Player(CircleShape):
    def __init__(self,x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.position
        self.timer = 0
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def update(self, dt):
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
            if self.timer <= 0:
                self.shoot(self.position)
                self.timer = PLAYER_SHOOT_COOLDOWN
        self.timer -= dt

    def shoot(self, position):
        v = position
        bullet = Shot(v.x, v.y)
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        bullet.velocity = forward * PLAYER_SHOT_SPEED

