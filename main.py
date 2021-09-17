import pygame
from photosynthesisGun import PhotosynthesisGun

WIDTH, HEIGHT = 950, 700
BACKGROUND_COLOR = (0,0,0)

class CO2Invaders:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))


    def main_loop(self):
        running = True
        gunX = 440
        gunY = 600
        gun_change = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    # move right
                    if event.key == pygame.K_RIGHT:
                        gun_change = 5
                    # move left
                    if event.key == pygame.K_LEFT:
                        gun_change = -5
                if event.type == pygame.KEYUP:
                    # stop moving
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        gun_change = 0

            self._handle_input()
            self._process_game_logic()
            self._draw(gunX, gunY)
            gunX += gun_change

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("CO2 Invaders")
        # game icon
        icon = pygame.image.load('images/co2.png')
        pygame.display.set_icon(icon)

    def _handle_input(self):
        pass

    def _process_game_logic(self):
        pass

    def _draw(self, gunX, gunY):
        # background color
        self.screen.fill(BACKGROUND_COLOR)

        # load background image and put on screen
        background = pygame.image.load('images/titleBackground.jpg')         # Currently set to title background
        self.screen.blit(background, (0,0))

        # load photosynthesisGun 
        gun = PhotosynthesisGun(self.screen)
        gun.drawPhotosynthesisGun(gunX, gunY)

        # load CO2

        # load bullets

        # update display
        pygame.display.update()


def main():
    game = CO2Invaders()
    game.main_loop()


if __name__ == '__main__':
    main()

        


    




