import pygame
from photosynthesisGun import PhotosynthesisGun
from load_sprite import load_sprite
from CO2Astroids import CO2Astroids
from components.button import Button


# Settings
WIDTH, HEIGHT = 950, 700
BACKGROUND_COLOR = (0,0,0)
MOVEMENT_SPEED = 5
class CO2Invaders:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self._background = pygame.image.load('images/titleBackground.jpg')        # Currently set to title background
        self._button = pygame.image.load('images/titlePageIMG/buttonStart.png')
        self._state = "title"                                                     # title, intro, unfinished, finished
        self.co2_particle = CO2Astroids((9,9), load_sprite('co2.png', False), (0,0))
         self.clock = pygame.time.Clock()

    def set_background(self, new_background):
        self._background = new_background

    def main_loop(self):
        running = True
        # initial location of gun
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
                        gun_change = MOVEMENT_SPEED
                    # move left
                    if event.key == pygame.K_LEFT:
                        gun_change = -MOVEMENT_SPEED
                if event.type == pygame.KEYUP:
                    # stop moving
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        gun_change = 0

            self._handle_input()

            self._process_game_logic()
            self._draw(gunX, gunY)
            gunX += gun_change
            
            # handle edges
            if gunX <= 0:
                gunX = 0
            elif gunX >= (WIDTH - 100): # 100 is width of image
                gunX = (WIDTH - 100)

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("CO2 Invaders")
        # game icon
        icon = pygame.image.load('images/co2.png')
        pygame.display.set_icon(icon)

    def _handle_input(self, status):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


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
        icon = pygame.image.load('images/co2.png')
        pygame.display.set_icon(icon)
        self.co2_particle.draw(self.screen)
        self.co2_particle.move((950, 700))
        
        # load bullets

        # update display
        pygame.display.update()
        


def main():
    game = CO2Invaders()
    game.main_loop()


if __name__ == '__main__':
    main()

        


    




