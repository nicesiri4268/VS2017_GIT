
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
import pygame
import bullet


def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship=Ship(ai_settings,screen)
    bullets = Group()
    pygame.display.set_caption("Alian Invasion")
    
    while True:

        gf.check_events(ai_settings,screen,ship,bullets)
        #事件监测
        ship.updata()
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,bullets)
        #更新屏幕

run_game()