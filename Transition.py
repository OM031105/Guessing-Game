import pygame

# Initialize Pygame
pygame.init()

# Set up the Pygame window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Image Transition with Button")

# Load the images
image1 = pygame.image.load("c.GuessMyNumber.png")
image2 = pygame.image.load("PP - Files/INSTRUCTIONS.png")

# Load the button image
button_image = pygame.image.load("imageedit_1_4188881968.png")
button_x, button_y = 0, -10
button_visible = True  # Track the visibility of the button

current_image = image1
transitioning = False

def transition_to_image(image):
    global current_image, transitioning
    current_image = image
    transitioning = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_visible and button_x < mouse_x < button_x + button_image.get_width() and \
               button_y < mouse_y < button_y + button_image.get_height():
                transitioning = True
                button_visible = False  # Hide the button

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the current image on the screen
    screen.blit(current_image, (0, 0))

    # Draw the button image on the screen if it's visible
    if button_visible:
        screen.blit(button_image, (button_x, button_y))

    # Update the display
    pygame.display.update()

    # Transition to the next image if needed
    if transitioning:
        pygame.time.delay(1000)  # Delay for one second for the transition effect
        transition_to_image(image2)
