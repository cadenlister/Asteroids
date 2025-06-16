import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys

def main():
     pygame.init()
     updatable = pygame.sprite.Group()
     drawable = pygame.sprite.Group()
     asteroids = pygame.sprite.Group()
     shots = pygame.sprite.Group()
     Player.containers = (updatable, drawable)
     Asteroid.containers = (asteroids, updatable, drawable)
     AsteroidField.containers = (updatable,)
     Shot.containers = (shots, updatable, drawable)
     print("Starting Asteroids!")
     print(f"Screen width: {SCREEN_WIDTH}")
     print(f"Screen height: {SCREEN_HEIGHT}")
     player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
     asteroid_field = AsteroidField()
     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
     clock = pygame.time.Clock()
     dt = 0
     while True:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    return
          pygame.Surface.fill(screen, (0,0,0), rect=None, special_flags=0)
          updatable.update(dt)
          for thing in asteroids:
               if thing.colide(player) == True:
                    print("Game over!")
                    sys.exit()
          for thing in drawable:
               thing.draw(screen)
          pygame.display.flip()
          dt = clock.tick(60) / 1000

if __name__ == "__main__":
     main()