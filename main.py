import pygame
import random

from pygame import mixer
from fireworks import *

from load_sprite import load_sprite
from CO2Astroids import CO2Astroids
from photosynthesisGun import PhotosynthesisGun
from leafBullet import LeafBullet
from CH4Asteroids import CH4Asteroids
from nitrogen import nitrogenAsteroids

# Settings
WIDTH, HEIGHT = 950, 700
BACKGROUND_COLOR = (0, 0, 0)
MOVEMENT_SPEED = 5
LEAF_SPEED = 5
GUN_X = 440
GUN_Y = 600
WIN_KILLS = 5
VOLUME = 0.5

# SOURCES:
# Images:
#   Title background - Martina Badini/Shutterstock.com
#   Scientist, leaf, gun, co2, recycling - Flaticon.com
#   Not Fine Meme - KC Green’s 2013 webcomic "On Fire."
# Sounds:
#   Bullets, collisions - https://freesound.org/browse/tags/game-sound/
#   Music - https://www.chosic.com/free-music/games/
# Others:
#   Fireworks - https://github.com/LytixDev/pygame_fireworks/blob/master/fireworks.py

class CO2Invaders:
    def __init__(self):
        self._init_pygame()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self._background = pygame.image.load('images/titleBackground.png')
        self.background_pos = 0
        self.clock = pygame.time.Clock()

        self._state = "title"  # title, intro, instructions, unfinished, won, won2, lost, lost2
        self.lives = 3
        self.lives_image = pygame.image.load('images/lives_3.png')
        self.kills = 0  # keeps track of total kills
        self.clear_kills = 0  # resets to 0 when new clear background is placed
        self.background_pos = 0
        self.not_fine = pygame.image.load('images/this_is_not_fine.png')


        # Components
        self.co2_particle = CO2Astroids((9, 9), load_sprite('co2.png', (80, 80), True), (0, 0))
        self.gun = PhotosynthesisGun(self.screen, 440, 600, WIDTH)
        self.leaf = LeafBullet(self.screen, self.gun.gunX + 30, "ready", LEAF_SPEED)
        self.fireworks = [Firework() for i in range(2)]
        self.ch4_particle = CH4Asteroids(self.screen)
        self.nitrogen_particle = nitrogenAsteroids(self.screen)

    def main_loop(self):
        running = True
        while running:
            self.clock.tick(60)
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Greenhouse Invaders")

        # Background Music
        mixer.music.load("sounds/themeSong.mp3")
        mixer.music.play(-1)
        mixer.music.set_volume(VOLUME)

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
                        self.leaf.bullet_state = "fire"
                        self.leaf.leafX = self.gun.gunX + 30
                        # Sound when gun is fired
                        bullet_sound = mixer.Sound('sounds/bullet2.wav')
                        bullet_sound.play()

                if event.type == pygame.KEYUP:
                    # stop moving
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        self.gun.set_gun_change(0)

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

            elif self._state == "won":
                if event.type == pygame.KEYDOWN:
                    self._state = "won2"
                    self._background = pygame.image.load('images/game_2.jpg')
                    self.reverts_attributes()

            else:  # state is won2
                if event.type == pygame.KEYDOWN:
                    self._state = "title"
                    self._background = pygame.image.load('images/titleBackground.png')

    def _process_game_logic(self):
        # collision detection
        # enemy and leaf
        if self.leaf.has_collided(self.co2_particle._x, self.co2_particle._y) and self.leaf.bullet_state == 'fire':
            self.kills += 1
            self.clear_kills += 1
            self.leaf.bullet_state = 'ready'
            self.leaf.leafY = 0
            self.co2_particle._x = random.randint(100, WIDTH)
            self.co2_particle._y = random.randint(100, HEIGHT // 2)

            # Sound when leaf collides with enemy
            explosion_sound = mixer.Sound('sounds/explosion2.wav')
            explosion_sound.play()

        elif self.leaf.has_collided(self.nitrogen_particle._x, self.nitrogen_particle._y) and self.leaf.bullet_state == 'fire':
            # print(self.leaf.bullet_state)
            self.kills += 1
            self.clear_kills += 1
            self.leaf.bullet_state = 'ready'
            self.leaf.leafY = 0
            self.nitrogen_particle._x = random.randint(100, WIDTH)
            self.nitrogen_particle._y = random.randint(100, HEIGHT // 2)
            # Sound when leaf collides with enemy
            explosion_sound = mixer.Sound('sounds/explosion2.wav')
            explosion_sound.play()
            # print(self.leaf.bullet_state)

        elif self.leaf.has_collided(self.ch4_particle._x, self.ch4_particle._y) and self.leaf.bullet_state == 'fire':
            self.kills += 1
            self.clear_kills += 1
            self.leaf.bullet_state = 'ready'
            self.leaf.leafY = 0
            self.ch4_particle._x = random.randint(100, WIDTH)
            self.ch4_particle._y = random.randint(100, HEIGHT // 2)
            # Sound when leaf collides with enemy
            explosion_sound = mixer.Sound('sounds/explosion2.wav')
            explosion_sound.play()

        # gun and enemy
        # CO2
        if self.gun.has_collided(self.co2_particle._x, self.co2_particle._y):
            self.lives -= 1
            self.co2_particle._x = random.randint(100, WIDTH)
            self.co2_particle._y = random.randint(100, HEIGHT // 2)
            # Sound when gun collides with enemy
            explosion_sound = mixer.Sound('sounds/explosion2.wav')
            explosion_sound.play()

        # Nitrogen
        elif self.gun.has_collided(self.nitrogen_particle._x, self.nitrogen_particle._y):
            self.lives -= 1
            self.nitrogen_particle._x = random.randint(100, WIDTH)
            self.nitrogen_particle._y = random.randint(100, HEIGHT // 2)
            # Sound when gun collides with enemy
            explosion_sound = mixer.Sound('sounds/explosion2.wav')
            explosion_sound.play()
        
        # CH4
        elif self.gun.has_collided(self.ch4_particle._x, self.ch4_particle._y):
            self.lives -= 1
            self.ch4_particle._x = random.randint(100, WIDTH)
            self.ch4_particle._y = random.randint(100, HEIGHT // 2)

            # Sound when gun collides with enemy
            explosion_sound = mixer.Sound('sounds/explosion2.wav')
            explosion_sound.play()

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

        # Background gets cleaner as enemies are killed
        clear_per_kills = WIN_KILLS // 5

        if self.clear_kills == clear_per_kills and self._state == "unfinished":
            background_arr = [
                pygame.image.load('images/game_2.jpg'),
                pygame.image.load('images/game_3.jpg'),
                pygame.image.load('images/game_4.jpg'),
                pygame.image.load('images/game_5.jpg'),
                pygame.image.load('images/game_6.jpg')]
            self._background = background_arr[self.background_pos]
            self.background_pos += 1
            # print(self.background_pos)
            self.clear_kills = 0

        # Player killed enough enemies, they win
        if self.kills == WIN_KILLS:
            self._state = "won"
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

        if self._state == "intro":
            intro_font = pygame.font.Font('freesansbold.ttf', 25)

            # Display intro text, format:[text, x-coordinate]
            intro_text = [
                ["It's the year 3020 and the toxic gasses ", 305],
                ["in Earth's atmosphere has reached ", 305],
                ["dangerous levels. Luckily, the smartest scientists", 160],
                ["have created the Photosynthesis Gun that turns", 160],
                ["greenhouse gasses into oxygen. It is your job to shoot at", 160],
                ["the molecules and help clean the air.", 160],
                ["- Dr. Climate", 600]]
            y_coordinate = 110  # start y_coordinate at 110, increase 40 per new line
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

            # Render CH4 particle
            self.ch4_particle.draw(self.screen)
            self.ch4_particle.move((950, 700))

            # Render N2 Particle
            self.nitrogen_particle.draw(self.screen)
            self.nitrogen_particle.move((950, 700))

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
            self.screen.blit(over_text, (300, 200))
            # Render fireworks
            if randint(0, 30) == 1:  # create new firework
                self.fireworks.append(Firework())
            update(self.screen, self.fireworks)

        if self._state == "won2":
            over_font = pygame.font.Font('freesansbold.ttf', 64)
            over_text = over_font.render("NEXT DAY...", True, (255, 255, 255))
            self.screen.blit(over_text, (280, 200))

        # update display
        pygame.display.update()


def main():
    game = CO2Invaders()
    game.main_loop()


if __name__ == '__main__':
    main()
