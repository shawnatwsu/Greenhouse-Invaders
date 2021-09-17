import pygame

class PhotosynthesisGun():

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/sapling.png')
        
        # resize image
        self.image = pygame.transform.scale(self.image, (100, 70))
        
    def drawPhotosynthesisGun(self, gunX, gunY):
        print(gunX, gunY)
        self.screen.blit(self.image, (gunX,gunY)) # TODO find the center
