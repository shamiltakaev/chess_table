# https://github.com/shamiltakaev/chess_table
import pygame
from board import Board
from life import Life

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 1000
    clock = pygame.time.Clock()
    fps = 10

    screen = pygame.display.set_mode(size)
    life = Life(10, 10)
    life.set_view(100, 100, 50)
    running = True
    is_play = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                life.get_click(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_play = not is_play
        screen.fill((0, 0, 0))
        life.render(screen)
        if is_play:
            life.next_move()
        clock.tick(fps)

        pygame.display.flip()