import pygame

import os
import sys


pygame.init()
size = width, height = 800, 400
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    image = pygame.transform.scale(image, (25, 25))

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Arrow(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = load_image("arrow.png")
        self.rect = self.image.get_rect()

    def update(self, *args, **kwargs):
        if args and args[0].type == pygame.MOUSEMOTION:
            self.rect.center = args[0].pos
        return super().update(*args, **kwargs)


if __name__ == '__main__':

    pygame.mouse.set_visible(False)

    clock = pygame.time.Clock()
    running = True
    all_sprites = pygame.sprite.Group()
    Arrow(all_sprites)

    while running:
        screen.fill((255, 255, 255))
        if pygame.mouse.get_focused():
            all_sprites.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                all_sprites.update(event)
        clock.tick(60)
        pygame.display.flip()

    pygame.quit()
