import pygame

from load_sprite import load_sprite
from CO2Astroids import CO2Astroids
from components.button import Button

class CO2Invaders:
    def __init__(self):
        self._init_pygame()

        self._screen_size = (950, 700)
        self.screen = pygame.display.set_mode(self._screen_size)
        self._background = pygame.image.load('images/titleBackground.jpg')        # Currently set to title background
        self._button = pygame.image.load('images/titlePageIMG/buttonStart.png')
        self._state = "title"                                                     # title, intro, unfinished, finished
        self.co2_particle = CO2Astroids((9,9), load_sprite('co2.png', False), (0,0))
         self.clock = pygame.time.Clock()

    def set_background(self, new_background):
        self._background = new_background

    def main_loop(self):
        running = True
        while running:
            self._handle_input(running)
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("CO2 Invaders")

    def _handle_input(self, status):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


    def _process_game_logic(self):
        pass

    def _draw(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self._background, (0,0))
        self.screen.blit(self._button, (300, 420))
        icon = pygame.image.load('images/co2.png')
        pygame.display.set_icon(icon)
        self.co2_particle.draw(self.screen)
        self.co2_particle.move((950, 700))
        pygame.display.update()
        


def main():
    game = CO2Invaders()
    game.main_loop()


if __name__ == '__main__':
    main()

        


    




