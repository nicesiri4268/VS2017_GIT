
from settings import Settings
from ship import Ship
import game_functions as gf
import pygame


def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship=Ship(ai_settings,screen)
    pygame.display.set_caption("Alian Invasion")
    
    while True:

        gf.check_events(ship)
        #事件监测
        ship.updata()
        gf.update_screen(ai_settings,screen,ship)
        #更新屏幕

run_game()