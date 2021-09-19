import pygame
import math


class PhotosynthesisGun:

    def __init__(self, screen, gunX, gunY, width):
        self.screen = screen
        self.image = pygame.image.load('images/sapling.png')

        # initial location of gun
        self.gunX = gunX
        self.gunY = gunY
        self.gun_change = 0
        self.width = width
        
        # resize image
        self.image = pygame.transform.scale(self.image, (100, 70))


    def get_gunX(self):
        return self.gunX

    def get_gunY(self):
        return self.gunY

    def set_gun_change(self, gun_change):
        self.gun_change = gun_change

    def drawPhotosynthesisGun(self):
        # print(gunX, gunY)
        self.gunX += self.gun_change

        # handle edges
        if self.gunX <= 0:
            self.gunX = 0
        elif self.gunX >= (self.width - 100): # 100 is self.width of image
            self.gunX = (self.width - 100)

        self.screen.blit(self.image, (self.gunX, self.gunY)) 

        
    def has_collided(self, enemy_x, enemy_y):
        distance = math.sqrt((math.pow(enemy_x - self.gunX, 2)) + (math.pow(enemy_y - self.gunY, 2)))

        if distance < 50:
            self.collided = True
            return True

        return False
