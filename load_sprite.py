import pygame
from pygame.image import load

"""
utility function for loading sprites into the game. Created by Kao to use. 
"""

def load_sprite(name, with_alpha=True):
    path = f"images/{name}"
    # print(path)
    loaded_sprite = load(path)
    loaded_sprite = pygame.transform.scale(loaded_sprite, (80,80))

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()