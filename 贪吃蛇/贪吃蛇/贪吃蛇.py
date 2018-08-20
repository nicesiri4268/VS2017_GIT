import pygame
import sys
from settings import Settings
import game_functions as gf
import snake as sn

def run_game():
    pygame.init()
    snake_settings = Settings()
    screen = pygame.display.set_mode((snake_settings.screen_wight,snake_settings.screen_height))
    pygame.display.set_caption(" 贪吃蛇 ")
    snake = sn.Snake(screen,snake_settings)

    screen_color = snake_settings.screen_color
    
    while True:
        gf.check_events(screen,snake_settings,snake)
        snake.update_snake()

        gf.update_screen(snake_settings,screen,snake)#更新屏幕并且绘制小蛇的位置

run_game()