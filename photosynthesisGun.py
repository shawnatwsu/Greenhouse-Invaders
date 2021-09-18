import pygame


class PhotosynthesisGun:

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/sapling.png')

        # initial location of gun
        self.gunX = 440
        self.gunY = 600
        self.gun_change = 0
        
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
        self.screen.blit(self.image, (self.gunX,self.gunY)) # TODO find the center


