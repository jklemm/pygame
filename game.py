import pygame
from pygame.locals import *

FULLSCREEN = 0
BLACK = (0, 0, 0)
RED = (255, 0, 0)
MAX_WIDTH = 800
MAX_HEIGHT = 600
RESOLUTION = (MAX_WIDTH, MAX_HEIGHT)


def main():
    x = 50
    y = 50
    width = 40
    height = 60
    speed = 5

    pygame.init()

    bestdepth = pygame.display.mode_ok(RESOLUTION, FULLSCREEN, 32)
    screen = pygame.display.set_mode(RESOLUTION, FULLSCREEN, bestdepth)
    pygame.display.set_caption('Pygame')

    running = True
    while running:
        pygame.time.delay(30)

        for event in pygame.event.get():
            press_close_window = event.type == pygame.QUIT
            press_esc_button = (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)
            if press_close_window or press_esc_button:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 0:
            x -= speed
        if keys[pygame.K_RIGHT] and (x + width) < MAX_WIDTH:
            x += speed
        if keys[pygame.K_UP] and y > 0:
            y -= speed
        if keys[pygame.K_DOWN] and (y + height) < MAX_HEIGHT:
            y += speed

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, (x, y, width, height))
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
