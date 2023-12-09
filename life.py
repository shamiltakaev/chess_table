import pygame
from board import Board

class Life(Board):
    def render(self, screen: pygame.Surface):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 0:
                    pygame.draw.rect(screen, (255, 255, 255), 
                                    (col * self.cell_size + self.left, 
                                    row * self.cell_size + self.top, 
                                    self.cell_size, self.cell_size),
                                    width=1)
                if self.board[row][col] == 1:
                    pygame.draw.rect(screen, (0, 255, 0), 
                                    (col * self.cell_size + self.left, 
                                    row * self.cell_size + self.top, 
                                    self.cell_size, self.cell_size))
                    
    def next_move(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                count_neighbours = 0
                for delta_row in range(-1, 2):
                    for delta_col in range(-1, 2):
                        if delta_row == delta_col == 0:
                            continue
                        if (row + delta_row >= len(self.board) or row + delta_row < 0 
                            or col + delta_col >= len(self.board[0]) or col + delta_col < 0):
                            continue
                        elif self.board[row + delta_row][col + delta_col] == 1:
                            count_neighbours += 1
                if self.board[row][col] == 0 and count_neighbours == 3:
                    self.board[row][col] = 1
                elif self.board[row][col] == 1 and not (2 <= count_neighbours <= 3):
                    self.board[row][col] = 0
