import pygame#tools to build a game
import sys#incase we want to exit the game
from game_settings import game_settings
from war_ship import war_ship
class alien_invasion:
    #"overall class to manage asserts and behavours"
    def __init__(self):
        #innitalizes the game,and creates game resources
        pygame.init()
        """
        self.screen=pygame.display.set_mode((1200,800))#screen to play the game
        self.background_color=(230,230,230)#sets a background color(red,green,blue)-mixture
        """
        self.settings=game_settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("ALIEN INVASION")
        self.ship=war_ship(self)
    def run_game(self):
        #starts the main loop of the game
        while True:
            self._check_events()#you dont have to call or instatiate the check event  method()
            self._update_screen()#we wont need to call the update screen
            #keep track of the keyboard and mouse events
    def _check_events(self):
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    sys.exit()
    def _update_screen(self):#updates images on the screen and flipto the new screen
        self.screen.fill(self.settings.background_color)  # makes the background color visible
        self.ship.blit_me()
        pygame.display.flip()  # makes the drawn screen visible
if __name__=='__main__':
    ai=alien_invasion()
    ai.run_game()
