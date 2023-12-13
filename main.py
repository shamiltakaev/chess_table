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
    image = pygame.transform.scale(image, (60, 60))

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Creature(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = load_image("arrow.png")
        self.rect = self.image.get_rect()

    def update(self, *args, **kwargs):
        if args:
            if args[0][pygame.K_LEFT]:
                self.rect.x -= 10
            if args[0][pygame.K_RIGHT]:
                self.rect.x += 10
            if args[0][pygame.K_UP]:
                self.rect.y -= 10
            if args[0][pygame.K_DOWN]:
                self.rect.y += 10
            
        return super().update(*args, **kwargs)


if __name__ == '__main__':
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    running = True
    all_sprites = pygame.sprite.Group()
    Creature(all_sprites)

    while running:
        screen.fill((255, 255, 255))
        keys = pygame.key.get_pressed()
        all_sprites.draw(screen)
        if any(keys):
            all_sprites.update(keys)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        clock.tick(100)

    pygame.quit()