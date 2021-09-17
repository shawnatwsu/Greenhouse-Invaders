import pygame
from pygame.image import load

def load_sprite(name, with_alpha=True):
    path = f"images/{name}"
    print(path)
    loaded_sprite = load(path)
    loaded_sprite = pygame.transform.scale(loaded_sprite, (150,150))

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()