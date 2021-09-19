import pygame
import random


class nitrogenAsteroids:

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/nitrogen_sprite.png')

        self._x = random.randint(0, 800)
        self._y = random.randint(50, 150)
        #rendering the image of the particle
        self.image = pygame.transform.scale(self.image, (100, 180))

        self._x_change = 25
        self._y_change = 25
        self._num_of_particles = 3

    def move(self, screen_size: tuple):
        # shows the movement of methane particles

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
        blit_position = (self._x, self._y)
        surface.blit(self.image, blit_position)
