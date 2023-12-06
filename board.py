import pygame

class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

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
                    pygame.draw.rect(screen, (255, 255, 255), 
                                    (col * self.cell_size + self.left, 
                                    row * self.cell_size + self.top, 
                                    self.cell_size, self.cell_size))

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def on_click(self, cell):
        col, row = cell
        self.board[row][col] = 1 if self.board[row][col] == 0 else 0

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        return ((x - self.left) // self.cell_size, (y - self.top) // self.cell_size)
    