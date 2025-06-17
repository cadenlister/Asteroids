import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys

def main():
     pygame.init()
     score = 0
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
     font = pygame.font.Font(None, 36)
     while True:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    return
          pygame.Surface.fill(screen, (0,0,0), rect=None, special_flags=0)
          updatable.update(dt)
          for asteroid in asteroids:
               if asteroid.collide(player) == True:
                    print("Game over!")
                    sys.exit()
               for bullet in shots:
                    if asteroid.collide(bullet):
                         asteroid.split(asteroids)
                         bullet.kill()
                         score += 1
          for thing in drawable:
               thing.draw(screen)
          text = font.render(f"Score: {score}", True, (255, 255, 255))
          text_rect = text.get_rect()
          text_rect.center = (SCREEN_WIDTH // 2, 50)
          screen.blit(text, text_rect)
          pygame.display.flip()
          dt = clock.tick(60) / 1000

if __name__ == "__main__":
     main()