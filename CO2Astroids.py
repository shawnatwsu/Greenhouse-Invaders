from pygame.math import Vector2
import pygame
import random

class CO2Astroids:

    def __init__(self, position, sprite, velocity):

        # inherit the constructor properties of the GameObject class
        self._x = 0
        self._y = 0
        self.sprite = sprite
        
        self._x_change = 100 # chagne back to 0
        self._y_change = 100 # TODO change back to 50
        self._num_of_particles = 6
        self.velocity = Vector2(velocity)
        self.radius = sprite.get_width() / 2


    def move(self, screen_size:tuple):
        """ defines movement of the CO2 'astroids' """

        # if particle hits the left side of screen, change its direction
        # also move the particle down some y-value
        if self._x <= 0:
            self._x_change = 3
            self._y += self._y_change
        # if particle hits the right side of screen, change its direction
        # also move the particle down some y-value
        elif self._x >= screen_size[0]:
            self._x_change = -3
            self._y += self._y_change

        self._x += self._x_change

    def draw(self, surface):
        blit_position = Vector2(self._x, self._y) - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)


