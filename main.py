# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
  pygame.init()
  print("Starting asteroids!")
  print("Screen width:", SCREEN_WIDTH)
  print("Screen height:", SCREEN_HEIGHT)

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  
  dt = 0
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
      
    for player in updatable:
      player.update(dt)
    
    screen.fill("black")
    
    for player in drawable:
      player.draw(screen)

    pygame.display.flip()

    # limit the frame rate to 60 FPS
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()