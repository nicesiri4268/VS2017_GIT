import pygame
import settings
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        """在ship所处位置绘制一颗子弹"""
        super().__init__()
        #继承sprite的属性
        self.screen = screen

        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float (self.rect.y)
        #储存用小数表示子弹的位置
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_spreed_factor
    
    def update(self):
        """更新子弹的位置"""
        self.y -= self.speed_factor
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)