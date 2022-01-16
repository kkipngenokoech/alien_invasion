import pygame
class war_ship:
    #a class to manage the war ship
    def __init__(self,ai_game):#ai_game allows the ship class to access all the alien_invasion properties
        #initialize the ship and its starting position
        self.screen=ai_game.screen#we assign the alien_invasion screen to a screen instance in this module
        self.screen_rect=ai_game.screen.get_rect()#width and height of the screen access
        self.image=pygame.image.load('ship.bmp')#allows us to load a ship image to the screen
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom
    def blit_me(self):
        #draws the ship current location
        self.screen.blit(self.image,self.rect)