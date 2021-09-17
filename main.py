import pygame

# Initialize the pygame
pygame.init()

# Display
screen = pygame.display.set_mode((950, 700))

running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False

