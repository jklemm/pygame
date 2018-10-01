import pygame
from pygame.locals import *

FULLSCREEN = 0
BLACK = (0, 0, 0)
RED = (255, 0, 0)


def main():
    x = 50
    y = 50
    width = 40
    height = 60
    vel = 5

    pygame.init()

    bestdepth = pygame.display.mode_ok((800, 600), FULLSCREEN, 32)
    screen = pygame.display.set_mode((800, 600), FULLSCREEN, bestdepth)
    pygame.display.set_caption('Pygame')

    running = True
    while running:
        pygame.time.delay(100)

        for event in pygame.event.get():
            press_close_window = event.type == pygame.QUIT
            press_esc_button = (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)
            if press_close_window or press_esc_button:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= vel
        if keys[pygame.K_RIGHT]:
            x += vel
        if keys[pygame.K_UP]:
            y -= vel
        if keys[pygame.K_DOWN]:
            y += vel

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, (x, y, width, height))
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
