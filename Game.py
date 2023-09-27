from GameWindow import GameWindow
from PlayerInput import PlayerInput

class Game: 

    #Initialize the framerate
    #initialize the map and the player
    def Start(self): 
        self.window = GameWindow(1920, 1080, "Down to Town")
        self.window.CreateWindow()
        self.playerInput = PlayerInput()
        self.game_state = {"isGameRunning" : True}

    def Update(self): 

        while self.game_state["isGameRunning"]: 
            self.playerInput.ProcessInput(self.game_state)
            self.window.DrawWindow()

    
