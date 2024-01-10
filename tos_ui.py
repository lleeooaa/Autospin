import pygame
from pygame.locals import *
import random

class Rune:
    def __init__(self,parent_screen, value, coordinate):
        self.parent_screen = parent_screen
        self.value=value

        if self.value==0:
            self.image = pygame.image.load("tos_icon/heart.png")
        elif self.value==1:
            self.image = pygame.image.load("tos_icon/water.png")
        elif self.value==2:
            self.image = pygame.image.load("tos_icon/fire.png")
        elif self.value==3:
            self.image = pygame.image.load("tos_icon/wood.png")
        elif self.value==4:
            self.image = pygame.image.load("tos_icon/light.png")
        elif self.value==5:
            self.image = pygame.image.load("tos_icon/dark.png")
        elif self.value==6:
            self.image = pygame.image.load("tos_icon/empty.png")
        
        self.x = coordinate[0]
        self.y = coordinate[1]

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

class Gameboard:
    def __init__(self):
        self.gameboard=""
        for i in range(5):
            for j in range(6):
                self.gameboard+=str(random.randint(0,5))
    
    def draw(self):
        for i in range(5):
            for j in range(6):
                Rune(int(self.gameboard[i*6+j]),(84*(j+2),84*(i+2))).draw()
            

class Game:
    def __init__(self):
        pygame.init()
    
        self.surface = pygame.display.set_mode((1080,720))
        self.surface.fill((255,255,255))
    
    def render_background(self):
        for i in range(5):
            for j in range(6):
                if (i+j)%2==0:
                    self.surface.blit(pygame.image.load("tos_icon/board_back_1.png"), (84*(j+2),84*(i+2)))
                else:
                    self.surface.blit(pygame.image.load("tos_icon/board_back_2.png"), (84*(j+2),84*(i+2)))
    
        

    def display_ui(self):
        pass
    

    def run(self):
        running = True
        self.render_background()
        pygame.display.flip()
        while running:
            self.display_ui()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:   
                        running = False

                if event.type == QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    """
                    if chou1(self.surface).image_rect.collidepoint(event.pos):
                        self.chou1.chou()
                        self.result.addpic()
                        self.result.draw()
                        
                    elif chou11(self.surface).image_rect.collidepoint(event.pos):
                        self.chou11.chou()
                        self.result.addpic()
                        self.result.draw()
                    """
                    pass

                        
            

if __name__ == "__main__":
    game = Game()
    game.run()
