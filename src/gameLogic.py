import csv
import os

from src.dependancyStuff.multipleScreens import Screen
from src.dependancyStuff.sprites.playerSprites import Player
from src.dependancyStuff.worldGenStuff.tileMaps import *
hearts = 5
pygame.mixer.init()
try:
    music_path = os.path.join(os.path.dirname(__file__), 'dependancyStuff', 'passwordStuff', 'musicfolder', 'My-Song-41.ogg')
    if os.path.exists(music_path):
        pygame.mixer.music.load(music_path)
except:
    pass  # Continue without music if file not found



class Game:
    def __init__(self):
        pygame.mixer.music.play(-1)
        pygame.init()
        pygame.display.set_caption("FNAD World")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.screen_rect = self.screen.get_rect()

        self.battleScreen = Screen("Battle Time!", BATTLESCREENWIDTH, BATTLESCREENHEIGHT)
        self.mainScreen = Screen("Game Time!", SCREEN_WIDTH, SCREEN_HEIGHT)


    def createMainTilemap(self, file_path, currentTile, tiles, width, height, scale, progress_callback=None):
        print(file_path)
        skippedLine = 0
        tiles = []
        total_rows = 0
        current_row = 0
        
        # Count total rows for progress
        if progress_callback:
            with open(file_path, 'r') as csvfile:
                total_rows = sum(1 for _ in csv.reader(csvfile))
        
        with open(file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            #maybe assign a new dictionary per large tile map square?
            for i, row in enumerate(csvreader):
                current_row = i
                
                # Update progress every 10 rows
                if progress_callback and total_rows > 0 and i % 10 == 0:
                    progress = 0.2 + (current_row / total_rows) * 0.7
                    progress_callback.update_progress(progress, f"Creating tiles... (row {i}/{total_rows})")
                    progress_callback.render()
                    progress_callback.handle_events()
                
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


    def new(self, use_loading_screen=False):
        pygame.display.init()
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.player = pygame.sprite.GroupSingle()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.buildings = pygame.sprite.LayeredUpdates()
        
        # Use relative path for world file
        world_file = os.path.join(os.path.dirname(__file__), 'dependancyStuff', 'worldGenStuff', 'world1.csv')
        
        if use_loading_screen:
            try:
                from src.dependancyStuff.loadingScreen import LoadingScreenContext
                with LoadingScreenContext() as loader:
                    loader.update_progress(0.1, "Loading world...")
                    self.createMainTilemap(world_file, 0, 10, TILESIZE, TILESIZE, 1, loader)
                    loader.update_progress(1.0, "Complete!")
                    
                # Restore proper game window after loading screen
                pygame.display.set_caption("FNAD World")
                self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                    
            except ImportError:
                print("Loading screen not available, loading normally...")
                self.createMainTilemap(world_file, 0, 10, TILESIZE, TILESIZE, 1)
        else:
            self.createMainTilemap(world_file, 0, 10, TILESIZE, TILESIZE, 1)

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



