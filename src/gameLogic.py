import csv

from src.dependancyStuff.multipleScreens import Screen
from sprites import Player
from src.dependancyStuff.worldGenStuff.tileMaps import *
hearts = 5
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\ghamp\PycharmProjects\PythonProject\src\dependancyStuff\passwordStuff\musicfolder\My-Song-41.ogg")



class Game:
    def __init__(self):
        pygame.mixer.music.play(-1)
        pygame.init()
        pygame.display.set_caption("My Game")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.screen_rect = self.screen.get_rect()

        self.battleScreen = Screen("Battle Time!", BATTLESCREENWIDTH, BATTLESCREENHEIGHT)
        self.mainScreen = Screen("Game Time!", SCREEN_WIDTH, SCREEN_HEIGHT)


    def createMainTilemap(self, file_path, currentTile, tiles, width, height, scale):
        print(file_path)
        skippedLine = 0
        tiles = []
        with open(file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            #maybe assign a new dictionary per large tile map square?
            for i, row in enumerate(csvreader):
                for j, column in enumerate(row):
                    if column.__contains__("top"):
                        currentTile = "top"
                        skippedLine+=1
                        continue
                    if column.__contains__("middle"):
                        currentTile = "middle"
                        skippedLine+=1
                        continue
                    if column.__contains__("bottom"):
                        currentTile = "bottom"
                        skippedLine+=1
                        continue
                    if column.__contains__("P"):
                        self.playerclass = Player(self, j, i-skippedLine)
                    if currentTile == "top":
                        Block(self, column, j, i - skippedLine).findImage(j, i - skippedLine, column,currentTile)
                        if column == "R":
                            Buildings(self, column, i - skippedLine, j)
                    if currentTile == "middle":
                        Block(self, column, j + 16, i - (skippedLine+48)).findImage(j, i - skippedLine, column,currentTile)
                        if column == "R":
                            Buildings(self, column, i - (skippedLine+48), j)
                    if currentTile == "bottom":
                        Block(self, column, j+32, i-(skippedLine+96)).findImage(j, i-skippedLine, column,currentTile)
                        if column == "R":
                            Buildings(self, column, i-(skippedLine+96), j)


    def new(self):
        pygame.display.init()
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.player = pygame.sprite.GroupSingle()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.buildings = pygame.sprite.LayeredUpdates()
        self.createMainTilemap(r'C:\Users\ghamp\PycharmProjects\PythonProject\src\dependancyStuff\worldGenStuff\world1.csv', 0,10,TILESIZE,TILESIZE,1)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
    def update(self):
        self.all_sprites.update()
        self.player.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.buildings.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
    def battles(self):
        if self.playerclass.battletime() == True:
            print("battle time")
            self.battleScreen.makeCurrentScreen()
            return True
        else:
            self.mainScreen.makeCurrentScreen()
            return False
    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
    def game_over(self):
        for sprite in self.all_sprites:
            sprite.kill()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_f:
                        print("interact button")
            self.clock.tick(FPS)
            pygame.display.update()



