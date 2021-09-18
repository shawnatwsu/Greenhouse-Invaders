import pygame
from photosynthesisGun import PhotosynthesisGun
from leafBullet import LeafBullet

# Settings
WIDTH, HEIGHT = 950, 700
BACKGROUND_COLOR = (0,0,0)
MOVEMENT_SPEED = 5
LEAF_SPEED = 5
bullet_state = "ready"
class CO2Invaders:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))


    def main_loop(self):
        running = True
        # initial location of gun
        gunX = 440
        gunY = 600

        # initial location of leaf
        leafX = 0
        leafY = 0

        gun_change = 0
        leaf_change = LEAF_SPEED

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
                    # fire bullets
                    if event.key == pygame.K_SPACE:
                        global bullet_state
                        bullet_state = "fire"
                        leafX = gunX
                        leafY -= leaf_change

                if event.type == pygame.KEYUP:
                    # stop moving
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        gun_change = 0

            self._handle_input()
            self._process_game_logic()
            self._draw(gunX, gunY, leafX, leafY)

            gunX += gun_change
            
            # handle edges
            if gunX <= 0:
                gunX = 0
            elif gunX >= (WIDTH - 100): # 100 is width of image
                gunX = (WIDTH - 100)

            # bullet movement
            if leafY <= 0:
                leafY = 605
                bullet_state = "ready"

            if bullet_state is "fire":
                leafY -= leaf_change

            # update display
            pygame.display.update()

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

    def _draw(self, gunX, gunY, leafX, leafY):
        # background color
        self.screen.fill(BACKGROUND_COLOR)

        # load background image and put on screen
        background = pygame.image.load('images/titleBackground.jpg')         # Currently set to title background
        self.screen.blit(background, (0,0))

        # load bullet (currently hiding the bullet behind the gun)
        leafBullet = LeafBullet(self.screen)
        leafBullet.drawLeafBullet(leafX, leafY)


        # load photosynthesisGun 
        gun = PhotosynthesisGun(self.screen)
        gun.drawPhotosynthesisGun(gunX, gunY)


        # load CO2


    # def fireLeafBullet(self, leafX, leafY):
        # global bullet_state
        # bullet_state = "fire"
        # leafY -= leaf_change
    #     leafBullet = LeafBullet(self.screen)
    #     leafBullet.drawLeafBullet(leafX, leafY)

def main():
    game = CO2Invaders()
    game.main_loop()


if __name__ == '__main__':
    main()

        


    




