
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
    #创建一个外星人
    alien =Alien(ai_settings,screen)
    pygame.display.set_caption("Alian Invasion")
    

    while True:

        gf.check_events(ai_settings,screen,ship,bullets)
        #事件监测
        ship.updata()
        gf.update_bullet(bullets)
        gf.update_screen(ai_settings,screen,ship,alien,bullets)
        #更新屏幕

run_game()
print ("谢谢玩耍!")