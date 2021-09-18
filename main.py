import pygame

from load_sprite import load_sprite
from CO2Astroids import CO2Astroids


class CO2Invaders:
    def __init__(self):
        self._init_pygame()

        self._screen_size = (950, 700)
        self.screen = pygame.display.set_mode(self._screen_size)
        self._background = pygame.image.load('images/titleBackground.png')
        self._state = "title"   # title, intro, unfinished, won, lost, lost2
        self.co2_particle = CO2Astroids((9, 9), load_sprite('co2.png', False), (0, 0))
        self.clock = pygame.time.Clock()
        self.lives = 3
        self.lives_image = pygame.image.load('images/lives_3.png')
        self.kills = 0
        self.not_fine = pygame.image.load('images/this_is_not_fine.png')

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

                # ____________________________________ TEMPORARY ____________________________________________
                # Need code to determine when player loses a life
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
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
        self.screen.fill((0, 0, 0))
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

        if self._state == "lost":
            over_font = pygame.font.Font('freesansbold.ttf', 64)
            over_text = over_font.render("GAME OVER!", True, (255, 255, 255))
            self.screen.blit(over_text, (280, 250))

        if self._state == "won":
            over_font = pygame.font.Font('freesansbold.ttf', 64)
            over_text = over_font.render("YOU WON!", True, (255, 255, 255))
            self.screen.blit(over_text, (280, 250))

        pygame.display.update()


def main():
    game = CO2Invaders()
    game.main_loop()


if __name__ == '__main__':
    main()
