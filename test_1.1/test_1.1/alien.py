import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__ (self,ai_settings,screen):
        super(Alien,self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen 

        #加载外星人图像,并设置其rect的值
        self.image =pygame.image.load(r"E:\VS2017_GIT\登录登出系统\登录登出系统\test_1.1\test_1.1\images\飞碟.bmp")#绝对路径要加r
        self.rect = self.image.get_rect()

        #设置外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #储存外星人的准确位置
        self.x = float(self.rect.x)
    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image,self.rect)
