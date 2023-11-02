import pygame
import sys

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image Transition")

# Load the images
image1 = pygame.image.load("PP - Files/INSTRUCTIONS.png")
image2 = pygame.image.load("PP - Files/LEVEL 1 SCREEN.png")
current_image = image1

transition = False  # Track whether a mouse click has occurred

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not transition:
          
            transition = True
            current_image = image2

    screen.fill((255, 255, 255))  # Clear the screen with a white background
    screen.blit(current_image, (0, 0))
    pygame.display.update()

pygame.quit()
sys.exit()
