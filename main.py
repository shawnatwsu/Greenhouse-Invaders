import pygame

class CO2Invaders:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((950, 700))


    def main_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("CO2 Invaders")

    def _handle_input(self):
        pass

    def _process_game_logic(self):
        pass

    def _draw(self):
        self.screen.fill((0,0,0))
        background = pygame.image.load('images/titleBackground.jpg')         # Currently set to title background
        self.screen.blit(background, (0,0))
        icon = pygame.image.load('images/co2.png')
        pygame.display.set_icon(icon)
        pygame.display.update()


def main():
    game = CO2Invaders()
    game.main_loop()


if __name__ == '__main__':
    main()

        


    




