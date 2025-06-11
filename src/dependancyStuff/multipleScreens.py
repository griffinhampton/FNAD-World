import pygame
class Screen():
    def __init__(self, title, width, height,fill=(0, 0, 255)):
        self.height = height
        self.title = title
        self.width = width
        self.fill = fill
        self.CurrentState = False
    def makeCurrentScreen(self):
        pygame.display.set_caption(self.title)
        self.CurrentState = True
        self.screen = pygame.display.set_mode((self.width,self.height))
    def endCurrentScreen(self):
        self.CurrentState = False
    def checkUpdate(self, fill):
        self.fill = fill
        return self.CurrentState
    def screenUpdate(self):
        if self.CurrentState:
            self.screen.fill(self.fill)
    def returnTitle(self):
        return self.screen