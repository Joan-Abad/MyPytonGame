import pygame
import sys
from Game import Game

# Initialize Pygame
pygame.init()

game = Game()

game.Start()
game.Update()

# Quit Pygame
pygame.quit()
sys.exit()