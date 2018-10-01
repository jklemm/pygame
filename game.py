import pygame
from pygame.locals import *

FULLSCREEN = 0
BLACK = (0, 0, 0)
RED = (255, 0, 0)
MAX_WIDTH = 800
MAX_HEIGHT = 600
RESOLUTION = (MAX_WIDTH, MAX_HEIGHT)


def redraw_screen(screen, width, height, x, y):
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (x, y, width, height))
    pygame.display.update()


def main():
    x = 50
    y = 500
    width = 40
    height = 60
    speed = 0.25
    is_jumping = False
    jump_count = 10

    pygame.init()

    bestdepth = pygame.display.mode_ok(RESOLUTION, FULLSCREEN, 32)
    screen = pygame.display.set_mode(RESOLUTION, FULLSCREEN, bestdepth)
    pygame.display.set_caption('Pygame')

    clock = pygame.time.Clock()

    running = True
    while running:
        dt = clock.tick(30)

        for event in pygame.event.get():
            press_close_window = event.type == pygame.QUIT
            press_esc_button = (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)
            if press_close_window or press_esc_button:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 0:
            x -= speed * dt
        if keys[pygame.K_RIGHT] and (x + width) < MAX_WIDTH:
            x += speed * dt

        if not is_jumping:
            if keys[pygame.K_UP] and y > 0:
                y -= speed * dt
            if keys[pygame.K_DOWN] and (y + height) < MAX_HEIGHT:
                y += speed * dt
            if keys[pygame.K_SPACE]:
                is_jumping = True
        else:
            if jump_count >= -10:
                neg = 1
                if jump_count < 0:
                    neg = -1
                y -= (jump_count ** 2) * 0.5 * neg
                jump_count -= 1
            else:
                is_jumping = False
                jump_count = 10

        redraw_screen(screen, width, height, x, y)

    pygame.quit()


if __name__ == '__main__':
    main()
