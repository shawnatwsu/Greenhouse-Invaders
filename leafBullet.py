import pygame
from load_sprite import load_sprite
import math

class LeafBullet:

    def __init__(self, screen, gunX, bullet_state, leaf_speed):
        self.screen = screen
        self.image = pygame.image.load('images/leaf.png')
        
        # resize image
        self.image = pygame.transform.scale(self.image, (30, 30))

        # init
        self.leafX = gunX                          # TODO function to get gunX location
        self.leafY = 0
        self.bullet_state = bullet_state
        self.leaf_change = leaf_speed

        
    def drawLeafBullet(self):
        # print(leafX, leafY)
        # bullet logic -------------------------------------------
        if self.leafY <= 0:
            self.leafY = 605
            self.bullet_state = "ready"
        
        if self.bullet_state == "fire":
            self.leafY -= self.leaf_change

        if self.bullet_state == "fire":
            self.screen.blit(self.image, (self.leafX,self.leafY))


    def has_collided(self, enemy_x, enemy_y):
        
        distance = math.sqrt((math.pow(enemy_x - self.leafX, 2)) + (math.pow(enemy_y - self.leafY, 2)))
        # print(distance)
        if distance < 100:
            self.collided = True
            return True

        return False

