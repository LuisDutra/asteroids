import pygame
from constants import *
from player import *


def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    fps =  pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = fps.tick(60) / 1000

        for update in updatable:
            update.update(dt)
        
        for objects in drawable:
            objects.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
