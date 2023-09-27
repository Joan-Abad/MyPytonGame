import pygame

class GameWindow: 

    
    def __init__(self, windowWidth, windowHeight, windowTitle):
        self.windowHeight = windowHeight
        self.windowWidth = windowWidth
        self.windowTitle = windowTitle
        self.runWindow = True

    def CreateWindow(self): 
        self.window_size = (self.windowWidth, self.windowHeight)
        # Create the window
        self.screen = pygame.display.set_mode(self.window_size)

        # Set the window title
        pygame.display.set_caption(self.windowTitle)

    def DrawWindow(self): 
        
            # Clear the screen with a white background
            self.screen.fill((255, 255, 255))
            #self.screen.blit(resized_backgroundImage, (0,0))
            #self.screen.blit(resized_image, (0,0))
            # Draw your graphics here (if needed)

            # Update the display
            pygame.display.update()

