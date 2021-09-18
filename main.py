import pygame

from load_sprite import load_sprite
from CO2Astroids import CO2Astroids
from photosynthesisGun import PhotosynthesisGun
from leafBullet import LeafBullet

# Settings
WIDTH, HEIGHT = 950, 700
BACKGROUND_COLOR = (0,0,0)
MOVEMENT_SPEED = 5
LEAF_SPEED = 10

class CO2Invaders:
    def __init__(self):
        self._init_pygame()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self._background = pygame.image.load('images/titleBackground.png')
        self.clock = pygame.time.Clock()
        self._state = "title"   # title, intro, unfinished, won, lost, lost2
        self.lives = 3
        self.lives_image = pygame.image.load('images/lives_3.png')
        self.kills = 0
        self.not_fine = pygame.image.load('images/this_is_not_fine.png')

        # Components
        self.co2_particle = CO2Astroids((9,9), load_sprite('co2.png', False), (0,0))
        self.gun = PhotosynthesisGun(self.screen, 440, 600, WIDTH)
        self.bullet_state = "ready"


    def main_loop(self):
        running = True
        while running:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("CO2 Invaders")

        # game icon
        icon = pygame.image.load('images/co2.png')
        pygame.display.set_icon(icon)

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if self._state == "title":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self._state = "intro"
                        self._background = pygame.image.load('images/introBackground.png')
            elif self._state == "intro":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self._state = "unfinished"
                        self._background = pygame.image.load('images/game_1.png')
            elif self._state == "unfinished":

                # Keys to control gun
                if event.type == pygame.KEYDOWN:
                    # move right
                    if event.key == pygame.K_RIGHT:
                        # self.gun.gunX += 5
                        self.gun.move(MOVEMENT_SPEED)
                        # self.gun.set_gun_change(MOVEMENT_SPEED)
                    # move left
                    if event.key == pygame.K_LEFT:
                        # self.gun.set_gun_change(-MOVEMENT_SPEED)
                        # self.gun.gunX -= 5
                        self.gun.move(-MOVEMENT_SPEED)

                    # # fire bullets
                    # if event.key == pygame.K_SPACE and self.bullet_state == "ready":
                    #     self.bullet_state = "fire"
                    #     leafX = gunX
                    #
                    # #     self.fireLeafBullet(gunX, leafY)

                if event.type == pygame.KEYUP:
                    # stop moving
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        self.gun.set_gun_change(0)

                # ____________________________________ TEMPORARY ____________________________________________
                # Need code to determine when player loses a life
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.lives -= 1

                # Need code to determine when player kills an enemy
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        self.kills += 1
                # ____________________________________ TEMPORARY ____________________________________________

            elif self._state == "lost":
                if event.type == pygame.KEYDOWN:
                    self._state = "lost2"
                    self._background = pygame.image.load('images/lost2Background.png')
                    self.lives = 3
                    self.kills = 0

            elif self._state == "lost2":
                if event.type == pygame.KEYDOWN:
                    self._state = "title"
                    self._background = pygame.image.load('images/titleBackground.png')

            else:                                                    # state == won
                if event.type == pygame.KEYDOWN:
                    self._state = "title"
                    self._background = pygame.image.load('images/titleBackground.png')
                    self.lives = 3
                    self.kills = 0

    def _process_game_logic(self):

        # Determines how many lives are displayed
        if self.lives == 3:
            self.lives_image = pygame.image.load('images/lives_3.png')
        elif self.lives == 2:
            self.lives_image = pygame.image.load('images/lives_2.png')
        elif self.lives == 1:
            self.lives_image = pygame.image.load('images/lives_1.png')

        # No lives left, player loses
        if self.lives == 0:
            self._state = "lost"

        # Player killed enough enemies, they win
        if self.kills == 5:
            self._state = "won"


    def _draw(self):
        # background color
        self.screen.fill(BACKGROUND_COLOR)

        # load background image and put on screen
        self.screen.blit(self._background, (0, 0))
        
        if self._state == "unfinished":
            # Render lives
            self.screen.blit(self.lives_image, (0, 0))

            # Render Kill Count
            kill_font = pygame.font.Font('freesansbold.ttf', 30)
            text_kill = "COUNT: " + str(self.kills)
            kill_display = kill_font.render(text_kill, True, (255, 255, 255))
            self.screen.blit(kill_display, (780, 20))

            # Render CO2 molecule
            icon = pygame.image.load('images/co2.png')
            pygame.display.set_icon(icon)
            self.co2_particle.draw(self.screen)
            self.co2_particle.move((950, 700))

            # # Render bullet
            # if self.bullet_state is "fire":
            #     leafBullet = LeafBullet(self.screen)
            #     leafBullet.drawLeafBullet(leafX + 30, leafY + 30)
            #

            # load photosynthesisGun
            self.gun.drawPhotosynthesisGun()
        
        if self._state == "lost":
            over_font = pygame.font.Font('freesansbold.ttf', 64)
            over_text = over_font.render("GAME OVER!", True, (255, 255, 255))
            self.screen.blit(over_text, (280, 250))

        if self._state == "won":
            over_font = pygame.font.Font('freesansbold.ttf', 64)
            over_text = over_font.render("YOU WON!", True, (255, 255, 255))
            self.screen.blit(over_text, (280, 250))

        # # gun logic -------------------------------------------
        # gunX += gun_change
        #
        # # handle edges
        # if gunX <= 0:
        #     gunX = 0
        # elif gunX >= (WIDTH - 100): # 100 is width of image
        #     gunX = (WIDTH - 100)
        #
        # # bullet logic -------------------------------------------
        # if leafY <= 0:
        #     leafY = 605
        #     bullet_state = "ready"
        #
        # if bullet_state is "fire":
        #     leafY -= leaf_change

        # update display
        pygame.display.update()


def main():
    game = CO2Invaders()
    game.main_loop()


if __name__ == '__main__':
    main()
