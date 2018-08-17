import pygame
import sys
from bullet import Bullet

def check_events(ai_settings,screen,ship,bullets):
    """事件监测,监测鼠标和键盘的动作,检查退出,移动"""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit(0)
        check_keydown(event,ai_settings,screen,ship,bullets)
        check_keyup(event,ship)#按键检测,控制飞船左右移动


def check_keydown(event,ai_settings,screen,ship,bullets):
    if event.type == pygame.KEYDOWN:
        if event.key==pygame.K_d:
            ship.moving_right=True
        if event.key==pygame.K_a:
            ship.moving_left = True
        if event.key == pygame.K_SPACE:
            new_bullet = Bullet(ai_settings,screen,ship)
            #创建新的子弹
            bullets.add(new_bullet)#将子弹添加到编组内

def check_keyup(event,ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_d:
            ship.moving_right=False
        if event.key == pygame.K_a:
            ship.moving_left = False

def update_screen(ai_settings,screen,ship,bullets ):
    """更新屏幕,并切换到新屏幕"""
    #创建屏幕
    screen.fill(ai_settings.bg_color)
    #飞船创建在屏幕之后
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()
