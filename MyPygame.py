import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display (window) dimensions
window_width = 1920
window_height = 1080
window_size = (window_width, window_height)

image = pygame.image.load("World/FirstLevel/FirstLevel.png")
background = pygame.image.load("World/FirstLevel/Background.png")

resized_image = pygame.transform.scale(image, (window_width, window_height))
resized_backgroundImage = pygame.transform.scale(background, (window_width, window_height))
# Create the window
screen = pygame.display.set_mode(window_size)

# Set the window title
pygame.display.set_caption("Basic Pygame Window")

numberOne = 4
numberTwo = 3 

boolean = numberTwo > numberOne

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen with a white background
    screen.fill((255, 255, 255))
    screen.blit(resized_backgroundImage, (0,0))
    screen.blit(resized_image, (0,0))
    # Draw your graphics here (if needed)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()

