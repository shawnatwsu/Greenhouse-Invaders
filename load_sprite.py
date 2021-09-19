import pygame
from pygame.image import load

"""
utility function for loading sprites into the game. Created by Kao to use. 
"""

def load_sprite(name, size=None, with_alpha=True):
    path = f"images/{name}"
    # print(path)
    loaded_sprite = load(path)
    if size is not None:
        loaded_sprite = pygame.transform.scale(loaded_sprite, size)

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()