import pygame
import random

from load_sprite import load_sprite
from CO2Astroids import CO2Astroids
from photosynthesisGun import PhotosynthesisGun
from leafBullet import LeafBullet

# Settings
WIDTH, HEIGHT = 950, 700
BACKGROUND_COLOR = (0,0,0)
MOVEMENT_SPEED = 5
LEAF_SPEED = 5
GUN_X = 440
GUN_Y =600
WIN_KILLS = 5  # Has to be a multiple of 5

class CO2Invaders:
    def __init__(self):
        self._init_pygame()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self._background = pygame.image.load('images/titleBackground.png')
        self.clock = pygame.time.Clock()
        self._state = "title"                                   # title, intro, unfinished, won, lost, lost2
        self.lives = 3
        self.lives_image = pygame.image.load('images/lives_3.png')
        self.kills = 0                                          # keeps track of total kills
        self.clear_kills = 0                                    # resets to 0 when new clear background is placed
        self.background_pos = 0
        self.not_fine = pygame.image.load('images/this_is_not_fine.png')

        # Components
        self.co2_particle = CO2Astroids((9,9), load_sprite('co2.png', (80,80), True), (0,0))
        self.gun = PhotosynthesisGun(self.screen, 440, 600, WIDTH)
        self.leaf = LeafBullet(self.screen, self.gun.gunX+30, "ready", LEAF_SPEED) 

    def main_loop(self):
        running = True
        while running:
            self._handle_input()
            self._process_game_logic()
            self._draw()
            # print(self.lives)

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("CO2 Invaders")

        # game icon
        icon = pygame.image.load('images/co2.png')
        pygame.display.set_icon(icon)

    def reverts_attributes(self):
        """Reverts attributes to their original values for new game"""
        self.lives = 3
        self.kills = 0
        self.background_pos = 0
        self.clear_kills = 0

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
                        self._background = pygame.image.load('images/game_1.jpg')
            elif self._state == "unfinished":

                # Keys to control gun
                if event.type == pygame.KEYDOWN:
                    # move right
                    if event.key == pygame.K_RIGHT:
                        self.gun.set_gun_change(MOVEMENT_SPEED)
                    # move left
                    if event.key == pygame.K_LEFT:
                        self.gun.set_gun_change(-MOVEMENT_SPEED)

                    # fire bullets
                    if event.key == pygame.K_SPACE and self.leaf.bullet_state == "ready":
                        # self.leaf.set_bullet_state("fire")
                        self.leaf.bullet_state = "fire"
                        self.leaf.leafX = self.gun.gunX+30
                    
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

            elif self._state == "lost2":
                if event.type == pygame.KEYDOWN:
                    self._state = "title"
                    self._background = pygame.image.load('images/titleBackground.png')
                    self.reverts_attributes()

            else:                                                    # state == won
                if event.type == pygame.KEYDOWN:
                    self._state = "title"
                    self._background = pygame.image.load('images/titleBackground.png')
                    self.reverts_attributes()

    def _process_game_logic(self):

        # collision detection
        # enemy and leaf
        if self.leaf.has_collided(self.co2_particle._x, self.co2_particle._y):
            self.kills += 1
            self.clear_kills += 1
            self.leaf.bullet_state = 'ready'
            self.leaf.leafY = 0
            self.co2_particle._x = random.randint(100, WIDTH)
            self.co2_particle._y = random.randint(100, HEIGHT//2)

        # gun and enemy
        if self.gun.has_collided(self.co2_particle._x, self.co2_particle._y):
            self.lives -= 1
            self.co2_particle._x = random.randint(100, WIDTH)
            self.co2_particle._y = random.randint(100, HEIGHT//2)

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
        if self.kills == WIN_KILLS:
            self._state = "won"

        # Background gets cleaner as enemies are killed
        clear_per_kills = WIN_KILLS // 5
        if self.clear_kills == clear_per_kills:
            background_arr = [
                pygame.image.load('images/game_2.jpg'),
                pygame.image.load('images/game_3.jpg'),
                pygame.image.load('images/game_4.jpg'),
                pygame.image.load('images/game_5.jpg'),
                pygame.image.load('images/game_6.jpg')]
            self._background = background_arr[self.background_pos]
            self.background_pos += 1
            self.clear_kills = 0

    def _draw(self):
        # background color
        self.screen.fill(BACKGROUND_COLOR)

        # load background image and put on screen
        self.screen.blit(self._background, (0, 0))

        if self._state == "intro":
            intro_font = pygame.font.Font('freesansbold.ttf', 25)

            # Display intro text, format:[text, x-coordinate]
            intro_text = [
                ["It's the year 3020 and the CO2 levels ", 305],
                ["in Earth's atmosphere has reached ", 305],
                ["dangerous levels. Luckily, the smartest scientists", 160],
                ["have created the Photosynthesis Gun that turns CO2 into", 160],
                ["oxygen. It is your job to shoot at the CO2 molecules and", 160],
                ["help clean the air.", 160],
                ["- Dr. Climate", 600]]
            y_coordinate = 110                     # start y_coordinate at 110, increase 40 per new line
            for each_line in intro_text:
                intro_text = intro_font.render(each_line[0], True, (0, 0, 0))
                self.screen.blit(intro_text, (each_line[1], y_coordinate))
                y_coordinate += 40
        
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

            # Render leaf
            self.leaf.drawLeafBullet()

            # Render photosynthesisGun
            self.gun.drawPhotosynthesisGun()
        
        if self._state == "lost":
            over_font = pygame.font.Font('freesansbold.ttf', 64)
            over_text = over_font.render("GAME OVER!", True, (255, 255, 255))
            self.screen.blit(over_text, (280, 250))

        if self._state == "won":
            over_font = pygame.font.Font('freesansbold.ttf', 64)
            over_text = over_font.render("YOU WON!", True, (255, 255, 255))
            self.screen.blit(over_text, (280, 250))

        # update display
        pygame.display.update()


def main():
    game = CO2Invaders()
    game.main_loop()


if __name__ == '__main__':
    main()
