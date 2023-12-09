from board import Board
import pygame
from random import randint

class Minesweeper(Board):
    def __init__(self, width, height, count_mines):
        super().__init__(width, height)
        self.count_mines = count_mines
        current_count = 0
        while True:
            if current_count > self.count_mines:
                break
            row, col = randint(1, self.height), randint(1, self.width)

            if self.board[row - 1][col - 1] == 0:
                self.board[row - 1][col - 1] = 10
                current_count += 1

    def open_cell(self, cell):
        row, col = cell

        if self.board[row][col] == 10:
            return

        s = 0
        for delta_row in range(-1, 2):
            for delta_col in range(-1, 2):
                if row + delta_row in [-1, self.height] or col + delta_col in [-1, self.width]:
                    continue
                s += self.board[row + delta_row][col + delta_col] == 10
        
        self.board[row][col] = s
    

    def render(self, screen: pygame.Surface):
        for row in range(self.height):
            for col in range(self.width):
                left = self.cell_size * col + self.left
                top = self.cell_size * row + self.top
                pygame.draw.rect(screen, pygame.Color("white"),
                                 (left, top, self.cell_size, self.cell_size), 1)
                if self.board[row][col] == 10:
                    pygame.draw.rect(screen, pygame.Color("red"),
                                     (left + 1, top + 1, self.cell_size - 2, self.cell_size - 2))
                if self.board[row][col] not in [0, 10]:
                    f1 = pygame.font.SysFont("Times new Roman", 24)
                    text = f1.render(str(self.board[row][col]), True, pygame.Color("green"))
                    screen.blit(text, (left + 5, top))


    def on_click(self, cell_coors):
        self.open_cell(cell_coors)