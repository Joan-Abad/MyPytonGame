import pygame

class PlayerInput: 

    def __init__(self):
        self

    def ProcessInput(self, gameState): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameState["isGameRunning"] = False
                print("Quitting game")
        
