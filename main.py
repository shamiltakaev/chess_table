import pygame
from board import Board
from minesweeper import Minesweeper


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    fps = 50
    clock = pygame.time.Clock()
    running = True
    N = 15
    board = Minesweeper(N, N, 10)
    
    while True:
        screen.fill(pygame.Color("black"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
        clock.tick()
