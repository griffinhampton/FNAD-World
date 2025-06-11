from src.dependancyStuff.config import *
from src.dependancyStuff.multipleScreens import Screen
import pygame
upimages = r"C:\Users\ghamp\PycharmProjects\PythonProject\src\img\Up Animations.png"
downimages = r"C:\Users\ghamp\PycharmProjects\PythonProject\src\img\Down Animations.png"
leftimages = r"C:\Users\ghamp\PycharmProjects\PythonProject\src\img\Left Animations.png"
rightimages = r"C:\Users\ghamp\PycharmProjects\PythonProject\src\img\Right Animations.png"

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYERLAYER
        self.groups = (self.game.all_sprites, self.game.player)
        pygame.sprite.Sprite.__init__(self, *self.groups)
        self.x = SCREEN_WIDTH/2
        self.y = SCREEN_HEIGHT/2
        self.width = TILESIZE
        self.height = TILESIZE
        self.dx = 0
        self.dy = 0
        self.up_filepath = upimages
        self.down_filepath = downimages
        self.left_filepath = leftimages
        self.right_filepath = rightimages
        self.up_images = []
        self.down_images = []
        self.left_images = []
        self.right_images = []
        self.loadSpriteSheets()
        self.direction = "down"
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image=self.down_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.frame = 0
        self.battle = False
        self.colliding = False
        self.interact = False
        self.battlescreen = Screen("Battle Time!", BATTLESCREENWIDTH, BATTLESCREENHEIGHT)
        self.mainScreen = Screen("Game Time!", SCREEN_WIDTH, SCREEN_HEIGHT)
    def get_image(self, sheet, col, row, width, height, scale):
        rect = pygame.Rect(col * width, row * height, width, height)
        image = pygame.Surface(rect.size, pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), rect)
        if scale != 1:
            image = pygame.transform.scale(image, (width * scale, height * scale))
        return image

    def loadSpriteSheets(self):
        # Make sure tiles are only loaded once and not repeatedly
        if not self.up_images:
            upSheet = pygame.image.load(self.up_filepath).convert_alpha()
            downSheet = pygame.image.load(self.down_filepath).convert_alpha()
            leftSheet = pygame.image.load(self.left_filepath).convert_alpha()
            rightSheet = pygame.image.load(self.right_filepath).convert_alpha()

            # Extract tiles from the sprite sheets
            for i in range(5):
                row = i // 5  # Row index
                col = i % 5  # Column index
                self.up_images.append(self.get_image(upSheet, col, row, TILESIZE, TILESIZE, 1))
                self.down_images.append(self.get_image(downSheet, col, row, TILESIZE, TILESIZE, 1))
                self.left_images.append(self.get_image(leftSheet, col, row, TILESIZE, TILESIZE, 1))
                self.right_images.append(self.get_image(rightSheet, col, row, TILESIZE, TILESIZE, 1))
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.frame +=.1
            self.direction = "left"
            self.animate(self.direction, int(self.frame%5))
            self.dx = 5
            for sprite in self.game.all_sprites:
                sprite.rect.x += self.dx
        if keys[pygame.K_RIGHT] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.frame +=.1
            self.direction = "right"
            self.animate(self.direction, int(self.frame%5))
            self.dx = -5
            for sprite in self.game.all_sprites:
                sprite.rect.x += self.dx
        if keys[pygame.K_UP] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.direction = "up"
            self.frame +=.1
            self.animate(self.direction, int(self.frame%5))
            self.dy = 5
            for sprite in self.game.all_sprites:
                sprite.rect.y += self.dy
        if keys[pygame.K_DOWN] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.direction = "down"
            self.frame +=.1
            self.animate(self.direction, int(self.frame%5))
            self.dy = -5
            for sprite in self.game.all_sprites:
                sprite.rect.y += self.dy
        if keys[pygame.K_f]:
            self.interact = True

        if keys[pygame.K_ESCAPE]:
            pass
    def battletime(self):
        return self.battle
    def animate(self, direction,frame):
        if direction == "left":
            self.image = self.left_images[frame]
        if direction == "right":
            self.image = self.right_images[frame]
        if direction == "up":
            self.image = self.up_images[frame]
        if direction == "down":
            self.image = self.down_images[frame]
    def collision(self):
        for blocks in self.game.blocks:
            if pygame.sprite.collide_rect(self, blocks):
                self.colliding = True
                if self.direction == "left":
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= self.dx
                if self.direction == "right":
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= self.dx
                if self.direction == "up":
                    for sprite in self.game.all_sprites:
                        sprite.rect.y -= self.dy
                if self.direction == "down":
                    for sprite in self.game.all_sprites:
                        sprite.rect.y -= self.dy
        for buildings in self.game.buildings:
            if pygame.sprite.collide_rect(self, buildings):
                if self.interact:
                    self.mainScreen.CurrentState = False
                    self.image = self.up_images[0]
                    self.interact = False
                    self.colliding = False
                    self.frame = 0
                    self.dy = TILESIZE
                    self.dx = TILESIZE
                    self.battle = True
                    self.battletime()
                    self.battlescreen.makeCurrentScreen()
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += self.dy
                        sprite.rect.x += self.dx
                else:
                    if self.battlescreen.CurrentState:
                        self.mainScreen.makeCurrentScreen()
                        self.battlescreen.CurrentState = False
    def update(self):
        self.collision()
        self.movement()
        self.rect.x = self.x
        self.rect.y = self.y



