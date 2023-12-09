# https://github.com/shamiltakaev/chess_table
import pygame
from board import Board
from life import Life

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 1000
    clock = pygame.time.Clock()
    fps = 50

    screen = pygame.display.set_mode(size)
    life = Life(30, 30)
    life.set_view(100, 100, 20)
    speed = 300
    MYEVENTTYPE = pygame.USEREVENT + 1
    pygame.time.set_timer(MYEVENTTYPE, speed)
    t_speed = speed
    running = True
    is_play = False
    is_touch = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    life.get_click(event.pos)
                    is_touch = True
                elif event.button == 4:
                    speed //= 2
                elif event.button == 5:
                    speed *= 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_play = not is_play
            if event.type == MYEVENTTYPE:
                if is_play:
                    life.next_move()
            if event.type == pygame.MOUSEMOTION and is_touch:
                life.get_click(event.pos)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                is_touch = False
        screen.fill((0, 0, 0))
        if t_speed != speed:
            t_speed = speed
            pygame.time.set_timer(MYEVENTTYPE, speed)

        life.render(screen)
        clock.tick(fps)

        pygame.display.flip()