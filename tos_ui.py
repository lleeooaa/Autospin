import pygame
from pygame.locals import *
import random

class Game:
    def __init__(self):
        pygame.init()
    
        self.surface = pygame.display.set_mode((1440,800))
        self.surface.fill((255,255,255))
        self.chou1=chou1(self.surface)
        self.chou1.draw()
        self.chou11=chou11(self.surface)
        self.chou11.draw()
        self.result=result(self.surface)

    def display_ui(self):
        font = pygame.font.SysFont('arial',25)
        freq = font.render(f"Frequency: {len(self.result.image)}", True, (0,0,0))
        self.surface.blit(freq, (1200,10))
        Result=font.render(f"Result:", True, (0,0,0))
        self.surface.blit(Result, (80,150))
        pygame.draw.line(self.surface,Color("black"), (0, 190), (1440, 190))
        pygame.draw.line(self.surface,Color("black"), (0, 290), (1440, 290))
        servant_5=font.render(f"5-star Servant:", True, (0,0,0))
        self.surface.blit(servant_5, (80,300))
        pygame.draw.line(self.surface,Color("black"), (0, 340), (1440, 340))
        pygame.draw.line(self.surface,Color("black"), (0, 440), (1440, 440))
        servant_4=font.render(f"4-star Servant:", True, (0,0,0))
        self.surface.blit(servant_4, (80,450))
        pygame.draw.line(self.surface,Color("black"), (0, 490), (1440, 490))
        pygame.draw.line(self.surface,Color("black"), (0, 590), (1440, 590))
        ce_5=font.render(f"5-star CE:", True, (0,0,0))
        self.surface.blit(ce_5, (80,600))
        pygame.draw.line(self.surface,Color("black"), (0, 640), (1440, 640))
        pygame.draw.line(self.surface,Color("black"), (0, 740), (1440, 740))
        pygame.display.flip()
    

    def run(self):
        running = True

        while running:
            self.result.length=0
            self.display_ui()
            self.chou1.draw()
            self.chou11.draw()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:   
                        running = False

                if event.type == QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if chou1(self.surface).image_rect.collidepoint(event.pos):
                        self.chou1.chou()
                        self.result.addpic()
                        self.result.draw()
                        
                    elif chou11(self.surface).image_rect.collidepoint(event.pos):
                        self.chou11.chou()
                        self.result.addpic()
                        self.result.draw()

                        
            

if __name__ == "__main__":
    game = Game()
    game.run()
