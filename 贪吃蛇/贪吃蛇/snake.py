import pygame
from settings import Settings
from pygame.sprite import Sprite

class Snake(Sprite):
    def __init__(self,screen,Settings):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = Settings

        self.rect = pygame.Rect(0,0,self.settings.rect_wight,self.settings.rect_height)
        #调整矩形的位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        #设置矩形的x,y坐标

        self.y = float (self.rect.y)
        self.color = Settings.rect_color#颜色
        self.spreed = Settings.rect_spreed#速度

        self.center_x = self.rect.centerx
        self.center_y = self.rect.centery
        #移动更新坐标

        self.moving_right = False
        self.moving_left = False
        #左右移动标志

    def update_snake (self):
        if self.rect.right < self.screen_rect.right:
            if self.moving_right :
                self.center_x += self.spreed
        if self.rect.left > 0:
            if self.moving_left :
                self.center_x -= self.spreed
        self.rect.centerx = self.center_x

    def draw_snake(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
 