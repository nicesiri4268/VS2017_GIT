import pygame
import sys
from snake import Snake

def check_events(screen,settings,snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                snake.moving_left = False
                snake.moving_right = True
            if event.key == pygame.K_a:
                snake.moving_right = False
                snake.moving_left = True
        
def update_screen(setting,screen,snake):
    
    screen.fill(setting.screen_color)
    snake.draw_snake()#绘制小蛇
    pygame.display.flip()#绘制屏幕
    