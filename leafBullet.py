import pygame

class LeafBullet():

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/leaf.png')
        
        # resize image
        self.image = pygame.transform.scale(self.image, (30, 30))
        
    def drawLeafBullet(self, leafX, leafY):
        # print(leafX, leafY)
        self.screen.blit(self.image, (leafX,leafY)) # TODO find the center
