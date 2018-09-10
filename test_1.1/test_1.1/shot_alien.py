
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
import pygame
import bullet


def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship=Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    gf.creat_fleet(ai_settings,screen,ship,aliens)
    #创建一群外星人
    pygame.display.set_caption("Alian Invasion")
    

    while True:

        gf.check_events(ai_settings,screen,ship,bullets)
        #事件监测
        ship.updata()
        gf.update_bullet(bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
        #更新屏幕

run_game()
#master分支测试
#print ("谢谢玩耍!")