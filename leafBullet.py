import pygame

class LeafBullet():

    def __init__(self, screen, gunX, leaf_speed):
        self.screen = screen
        self.image = pygame.image.load('images/leaf.png')
        
        # resize image
        self.image = pygame.transform.scale(self.image, (30, 30))

        # initial location of leaf
        self.leafX = gunX                          # TODO function to get gunX location
        self.leafY = 0

        self.leaf_change = leaf_speed
        
    def drawLeafBullet(self, leafX, leafY):
        # print(leafX, leafY)
        self.screen.blit(self.image, (leafX,leafY)) # TODO find the center
