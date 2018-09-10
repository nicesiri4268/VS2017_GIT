import pygame
class Ship():
    def __init__(self,ai_settings,screen):
        """初始化飞船并且设置其初始位置"""
        self.screen=screen
        self.ai_settings=ai_settings

        self.image=pygame.image.load(r'E:\VS2017_GIT\登录登出系统\登录登出系统\test_1.1\test_1.1\images\ship.bmp')
        self.rect=self.image.get_rect()
        #.rect这个是ship的属性
        #rect是矩形框,rect.XXX用来获取飞船属性
        self.screen_rect=screen.get_rect()
        #这个是屏幕的属性
        self.rect.centerx=self.screen_rect.centerx
        #把ship的中心设置为游戏屏幕的中心
        self.rect.bottom=self.screen_rect.bottom
        #把ship的下边缘y坐标设置为屏幕下边缘

        self.center = float(self.rect.centerx)
        #飞船的center储存小数值

        self.moving_right = False
        #设置向右移动标志
        self.moving_left = False
        #设置向左移动标志

    def updata(self):
        """更新ship的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            #添加的是if而不是elif
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center
        #根据float(center)来调整ship的位置

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
        
