import pygame

# Initialize the pygame
pygame.init()

# Display Screen
screen = pygame.display.set_mode((950, 700))

# Display Screen Title & Icon
pygame.display.set_caption("CO2 Invaders")
icon = pygame.image.load('images/co2.png')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('images/titleBackground.jpg')         # Currently set to title background

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Displayed Background Image
    screen.fill((0,0,0))
    screen.blit(background, (0,0))

    pygame.display.update()



