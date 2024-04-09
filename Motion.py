import pygame
from Parser import Parser
from Rule import Rule
from TuringMachine import TuringMachine
from tkinter import messagebox

class Motion():
    def __init__(self,tm:TuringMachine)->None:
        self.tm = tm
        pygame.init()
        size = (500,150)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Simulador')
    
    def drawInfo(self,steps:int)->None:
        #Current status
        myfont = pygame.font.SysFont("monospace", 20)
        label = myfont.render(str(self.tm.getStatus()),1,(0,0,1))
        self.screen.blit(label,(25,100))
        #Current status title
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render("Current Status",1,(0,0,1))
        self.screen.blit(label,(25,85))

        #Steps
        myfont = pygame.font.SysFont("monospace", 20)
        label = myfont.render(str(steps),1,(0,0,1))
        self.screen.blit(label,(457,100))
        #Steps title
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render("Steps",1,(0,0,1))
        self.screen.blit(label,(440,85))


    def drawHead(self)->None:
        posx = 25+(18*self.tm.getIndex())
        pygame.draw.rect(self.screen,(255,0,0),(posx,60,18,18))
        pygame.draw.polygon(self.screen,(255,0,0),[(posx,60),(posx+17,60),(posx+9,55)])

    def drawString(self)->None:
        symbolTape = self.tm.getSymbolTape()
        string = ''.join(symbolTape)
        myfont = pygame.font.SysFont("monospace", 30)
        label = myfont.render(string,1,(0,0,1))
        self.screen.blit(label,(25,10))

    def runMotion(self)->None:
        framerate = 2
        clock = pygame.time.Clock()
        i = 0
        nextFlag = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            self.screen.fill((255,255,255))
            self.drawString()
            self.drawHead()
            self.drawInfo(i)
            if not nextFlag:
                try:
                    nextFlag = self.tm.Next()
                    i += 1
                except Exception:
                    messagebox.showerror("Error de ejecucion","Error lógico o string fuera de rango")
                    pygame.quit()
            else:
                framerate = 30
            pygame.display.flip()
            clock.tick(framerate)