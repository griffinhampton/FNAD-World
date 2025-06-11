from src.dependancyStuff.config import *
from src.dependancyStuff.sprites.playerSprites import Player
from src.img import *
from src.dependancyStuff.worldGenStuff.worldGenConfig import *
from src.dependancyStuff.sprites.playerSprites import Player
import pygame
import random

mountainFile = r"C:\Users\ghamp\PycharmProjects\PythonProject\src\img\mountain tiles.png"
plainFile = r"C:\Users\ghamp\PycharmProjects\PythonProject\src\img\plains tiles.png"
snowFile = r"C:\Users\ghamp\PycharmProjects\PythonProject\src\img\snow tiles.png"
houseFile = r"C:\Users\ghamp\PycharmProjects\PythonProject\src\img\2388-removebg-preview.png"

class Block(pygame.sprite.Sprite):
    def __init__(self, game, column, i, j):
        self.game = game
        self.groups = self.game.all_sprites,
        pygame.sprite.Sprite.__init__(self, *self.groups)

        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.rect.x = j * TILESIZE
        self.rect.y = i * TILESIZE

        self.mountainFile = mountainFile
        self.plainFile = plainFile
        self.snowFile = snowFile
        self.mountainTiles=[]
        self.plainTiles=[]
        self.snowTiles=[]
        self.loadSpriteSheets()

    def get_image(self, sheet, col, row, width, height, scale):
        rect = pygame.Rect(col * width, row * height, width, height)
        image = pygame.Surface(rect.size, pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), rect)
        if scale != 1:
            image = pygame.transform.scale(image, (width * scale, height * scale))
        return image

    def loadSpriteSheets(self):
        # Make sure tiles are only loaded once and not repeatedly
        if not self.mountainTiles:
            mountain_sheet = pygame.image.load(self.mountainFile).convert_alpha()
            plain_sheet = pygame.image.load(self.plainFile).convert_alpha()
            snow_sheet = pygame.image.load(self.snowFile).convert_alpha()

            # Extract tiles from the sprite sheets
            for i in range(10):  # Assuming 10 tiles
                row = i // 8  # Row index
                col = i % 8  # Column index
                self.mountainTiles.append(self.get_image(mountain_sheet, col, row, TILESIZE, TILESIZE, 1))
                self.plainTiles.append(self.get_image(plain_sheet, col, row, TILESIZE, TILESIZE, 1))
                self.snowTiles.append(self.get_image(snow_sheet, col, row, TILESIZE, TILESIZE, 1))

    def findImage(self,x,y,column,zone):
        if column!="1" and column!="R":
            self.groups = self.game.blocks
            pygame.sprite.Sprite.__init__(self, self.game.blocks)
        if zone == "top":
            if column == "B2":
                self.image = self.plainTiles[8]
            elif column == "B":
                self.image = self.plainTiles[7]
            elif column == "B1":
                self.image = self.plainTiles[9]
            elif column == "RCL":
                self.image = self.plainTiles[4]
            elif column == "RR":
                self.image = self.plainTiles[3]
                self.image = pygame.transform.flip(self.image, True, False)
            elif column == "RL":
                self.image = self.plainTiles[3]
            elif column == "RU":
                self.image = self.plainTiles[5]
                self.image = pygame.transform.rotate(self.image, -90)
            elif column == "RCR":
                self.image = self.plainTiles[4]
                self.image = pygame.transform.flip(self.image, True, False)
            elif column == "RCLU":
                self.image = self.plainTiles[4]
                self.image = pygame.transform.flip(self.image, False, True)
            elif column == "RCRU":
                self.image = self.plainTiles[4]
                self.image = pygame.transform.flip(self.image, True, True)
            elif column == "1":
                randomNumber = random.randint(0, 6)
                if randomNumber <= 3:
                    self.image = self.plainTiles[1]
                if randomNumber <= 5:
                    self.image = self.plainTiles[0]
                if randomNumber == 6:
                    self.image = self.plainTiles[6]
            else:
                self.image = self.plainTiles[1]
        elif zone == "middle":
            if column == "B":
                self.image = self.snowTiles[7]
            elif column == "B1":
                self.image = self.snowTiles[9]
            elif column == "B2":
                self.image = self.snowTiles[8]
            elif column == "RCL":
                self.image = self.snowTiles[4]
            elif column == "RU":
                self.image = self.snowTiles[5]
                self.image = pygame.transform.rotate(self.image, -90)
            elif column == "RL":
                self.image = self.snowTiles[3]
            elif column == "RR":
                self.image = self.snowTiles[3]
                self.image = pygame.transform.flip(self.image, True, False)
            elif column == "RCR":
                self.image = self.snowTiles[4]
                self.image = pygame.transform.flip(self.image, True, False)
            elif column == "RCLU":
                self.image = self.snowTiles[4]
                self.image = pygame.transform.flip(self.image, False, True)
            elif column == "RCRU":
                self.image = self.snowTiles[4]
                self.image = pygame.transform.flip(self.image, True, True)
            elif column == "1":
                randomNumber = random.randint(0, 6)
                if randomNumber <= 3:
                    self.image = self.snowTiles[1]
                if randomNumber <= 5:
                    self.image = self.snowTiles[0]
                if randomNumber == 6:
                    self.image = self.snowTiles[6]
            else:
                self.image = self.snowTiles[1]
        elif zone == "bottom":
            if column == "B":
                self.image = self.mountainTiles[7]
            elif column == "B1":
                self.image = self.mountainTiles[9]
            elif column == "B2":
                self.image = self.mountainTiles[8]
            elif column == "RCL":
                self.image = self.mountainTiles[4]
            elif column == "RU":
                self.image = self.mountainTiles[5]
                self.image = pygame.transform.rotate(self.image, -90)
            elif column == "RL":
                self.image = self.mountainTiles[3]
            elif column == "RR":
                self.image = self.mountainTiles[3]
                self.image = pygame.transform.flip(self.image, True, False)
            elif column == "RCR":
                self.image = self.mountainTiles[4]
                self.image = pygame.transform.flip(self.image, True, False)
            elif column == "RCLU":
                self.image = self.mountainTiles[4]
                self.image = pygame.transform.flip(self.image, False, True)
            elif column == "RCRU":
                self.image = self.mountainTiles[4]
                self.image = pygame.transform.flip(self.image, True, True)

            elif column == "1":
                randomNumber = random.randint(0, 6)
                if randomNumber <= 3:
                    self.image = self.mountainTiles[1]
                if randomNumber <= 5:
                    self.image = self.mountainTiles[0]
                if randomNumber == 6:
                    self.image = self.mountainTiles[6]
            else:
                self.image = self.mountainTiles[1]
        else:
            self.image = self.plainTiles[1]

class Buildings(pygame.sprite.Sprite):
    def __init__(self, game, column, i, j):
        self.game = game
        self.groups = self.game.all_sprites, self.game.buildings
        pygame.sprite.Sprite.__init__(self, *self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image = pygame.image.load(houseFile).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = j * TILESIZE
        self.rect.y = i * TILESIZE


