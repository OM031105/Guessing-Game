import pygame
import Transition
import instructions

pygame.init()

# Set up the Pygame window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Guessing game")

# Load the background image
background_image = pygame.image.load("c.GuessMyNumber.png").convert_alpha()

# Load the button image
button_image = pygame.image.load("imageedit_1_4188881968.png").convert_alpha()

# Define the initial positions
background_x, background_y = 0, 0
button_x, button_y = 0, -10

# Create a function to check if the mouse is over the button
def is_mouse_over_button(mouse_x, mouse_y):
    return button_x < mouse_x < button_x + button_image.get_width() and \
           button_y < mouse_y < button_y + button_image.get_height()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if is_mouse_over_button(mouse_x, mouse_y):
                print("Button clicked")

    # Clear the screen and draw the background image
    screen.blit(background_image, (background_x, background_y))

    # Draw the button image on top of the background
    screen.blit(button_image, (button_x, button_y))

    pygame.display.update()
