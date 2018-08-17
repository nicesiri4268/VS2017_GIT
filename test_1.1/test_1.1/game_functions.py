import pygame
import sys


def check_events(ship):
    """事件监测,监测鼠标和键盘的动作,检查退出,移动"""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit(0)
        check_keydown(event,ship)
        check_keyup(event,ship)#按键检测,控制飞船左右移动


def check_keydown(event,ship):
    if event.type == pygame.KEYDOWN:
        if event.key==pygame.K_d:
            ship.moving_right=True
        if event.key==pygame.K_a:
            ship.moving_left = True

def check_keyup(event,ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_d:
            ship.moving_right=False
        if event.key == pygame.K_a:
            ship.moving_left = False

def update_screen(ai_settings,screen,ship):
    """更新屏幕,并切换到新屏幕"""
    #创建屏幕
    screen.fill(ai_settings.bg_color)
    #飞船创建在屏幕之后
    ship.blitme()
    pygame.display.flip()
