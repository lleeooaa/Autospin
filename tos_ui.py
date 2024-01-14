import pygame
from pygame.locals import *
import random
import autospin
import time

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
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.gameboard = ""
        self.runes=[]
        for i in range(5):
            for j in range(6):
                if (i+j)%2==0:
                    self.parent_screen.blit(pygame.image.load("tos_icon/board_back_1.png"), (84*(j+2),84*(i+2)))
                else:
                    self.parent_screen.blit(pygame.image.load("tos_icon/board_back_2.png"), (84*(j+2),84*(i+2))) 
        for i in range(5):
            for j in range(6):
                self.gameboard+=str(random.randint(0,5))
    
    def draw(self):
        self.runes=[]
        for i in range(5):
            for j in range(6):
                self.runes.append(Rune(self.parent_screen, int(self.gameboard[i*6+j]), (84*(j+2),84*(i+2))))
                self.runes[-1].draw()
        

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1080,720))
        self.surface.fill((255,255,255))
        self.game=Gameboard(self.surface)
        self.button_list=[]
        for i in range(6):
            self.button_list.append(Rune(self.surface,i,(150+i*100,50)))
        for button in self.button_list:
            button.draw()

        font = pygame.font.SysFont("Arial",35)
        self.run_button=font.render("Move", True, (0,0,0))
        self.run_button_rect=self.run_button.get_rect(center=(850,200))
        pygame.draw.rect(self.surface, (100,100,100), self.run_button_rect)
        self.surface.blit(self.run_button,self.run_button_rect)

        self.auto_button=font.render("Auto Move", True, (0,0,0))
        self.auto_button_rect=self.auto_button.get_rect(center=(850,300))
        pygame.draw.rect(self.surface, (100,100,100), self.auto_button_rect)
        self.surface.blit(self.auto_button,self.auto_button_rect)        


    def swap(self, node1, node2):
        self.game.gameboard=list(self.game.gameboard)
        self.game.gameboard[6*node1[0]+node1[1]],self.game.gameboard[6*node2[0]+node2[1]]=self.game.gameboard[6*node2[0]+node2[1]],self.game.gameboard[6*node1[0]+node1[1]]
        self.game.gameboard=''.join(self.game.gameboard)
        if (node1[0]+node1[1])%2==0:
            self.surface.blit(pygame.image.load("tos_icon/board_back_1.png"), (84*(node1[1]+2),84*(node1[0]+2)))
        else:
            self.surface.blit(pygame.image.load("tos_icon/board_back_2.png"), (84*(node1[1]+2),84*(node1[0]+2))) 
        if (node2[0]+node2[1])%2==0:
            self.surface.blit(pygame.image.load("tos_icon/board_back_1.png"), (84*(node2[1]+2),84*(node2[0]+2)))
        else:
            self.surface.blit(pygame.image.load("tos_icon/board_back_2.png"), (84*(node2[1]+2),84*(node2[0]+2))) 
        self.game.draw()

    def change(self, node, val):
        self.game.gameboard=list(self.game.gameboard)
        self.game.gameboard[6*node[0]+node[1]]=str(val)
        self.game.gameboard=''.join(self.game.gameboard)
        if (node[0]+node[1])%2==0:
            self.surface.blit(pygame.image.load("tos_icon/board_back_1.png"), (84*(node[1]+2),84*(node[0]+2)))
        else:
            self.surface.blit(pygame.image.load("tos_icon/board_back_2.png"), (84*(node[1]+2),84*(node[0]+2)))
        self.game.draw()
        
    def auto_move(self, starting_point, path):
        for node in path:
            pygame.draw.circle(self.surface, (200,0,0), (84*(starting_point[1]+2.5),84*(starting_point[0]+2.5)),10)
            pygame.display.update()
            time.sleep(0.3)
            if node=='N':
                self.swap(starting_point,(starting_point[0]-1,starting_point[1]))
                starting_point=(starting_point[0]-1,starting_point[1])
            elif node=='S':
                self.swap(starting_point,(starting_point[0]+1,starting_point[1]))
                starting_point=(starting_point[0]+1,starting_point[1])
            elif node=='E':
                self.swap(starting_point,(starting_point[0],starting_point[1]+1))
                starting_point=(starting_point[0],starting_point[1]+1)
            elif node=='W':
                self.swap(starting_point,(starting_point[0],starting_point[1]-1))
                starting_point=(starting_point[0],starting_point[1]-1)
            elif node=='NW':
                self.swap(starting_point,(starting_point[0]-1,starting_point[1]-1))
                starting_point=(starting_point[0]-1,starting_point[1]-1)
            elif node=='NE':
                self.swap(starting_point,(starting_point[0]-1,starting_point[1]+1))
                starting_point=(starting_point[0]-1,starting_point[1]+1)
            elif node=='SW':
                self.swap(starting_point,(starting_point[0]+1,starting_point[1]-1))
                starting_point=(starting_point[0]+1,starting_point[1]-1)
            elif node=='SE':
                self.swap(starting_point,(starting_point[0]+1,starting_point[1]+1))
                starting_point=(starting_point[0]+1,starting_point[1]+1)
             

    def run(self):
        running = True
        pygame.display.flip()
        curr_rune=None
        change_rune_val=None
        self.game.draw()
        moving=False
        
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:   
                        running = False

                if event.type == QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for num, rune in enumerate(self.button_list):
                        if rune.image.get_rect(topleft=(rune.x,rune.y)).collidepoint(event.pos):
                            moving=False
                            change_rune_val=rune.value

                    if self.run_button_rect.collidepoint(event.pos):
                        moving=True

                    if self.auto_button_rect.collidepoint(event.pos):
                        moving=False
                        change_rune_val=None
                        starting_point, path=autospin.start(self.game.gameboard)
                        self.auto_move(starting_point,path)

                    for num, rune in enumerate(self.game.runes):
                        if rune.image.get_rect(topleft=(rune.x,rune.y)).collidepoint(event.pos):
                            if moving:
                                curr_rune=num
                            elif change_rune_val:
                                self.change(divmod(num,6),change_rune_val)    

                if moving and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    curr_rune=None

                if moving and event.type == pygame.MOUSEMOTION and curr_rune!=None:
                    for num, rune in enumerate(self.game.runes):
                        if num==curr_rune:
                            continue
                        if rune.image.get_rect(topleft=(rune.x,rune.y)).collidepoint(event.pos):
                            self.swap(divmod(curr_rune,6),divmod(num,6))
                            curr_rune=num
                            

                        
            

if __name__ == "__main__":
    game = Game()
    game.run()
