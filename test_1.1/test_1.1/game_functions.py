import pygame
import sys
from bullet import Bullet
from alien import Alien

def check_events(ai_settings,screen,ship,bullets):
    """事件监测,监测鼠标和键盘的动作,检查退出,移动"""
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            sys.exit(0)
        check_keydown(event,ai_settings,screen,ship,bullets)
        check_keyup(event,ship)#按键检测,控制飞船左右移动


def check_keydown(event,ai_settings,screen,ship,bullets):
    if event.type == pygame.KEYDOWN:
        if event.key==pygame.K_d :
            ship.moving_right=True
        if event.key==pygame.K_a:
            ship.moving_left = True
        if event.key == pygame.K_SPACE:
            fire_bullet(ai_settings,screen,ship,bullets)
        if event.key == pygame.K_ESCAPE:#esc退出
            sys.exit(0)
        

def check_keyup(event,ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_d:
            ship.moving_right=False
        if event.key == pygame.K_a:
            ship.moving_left = False

def update_screen(ai_settings,screen,ship,aliens,bullets):
    """更新屏幕,并切换到新屏幕"""
    #创建屏幕
    screen.fill(ai_settings.bg_color)
    #飞船创建在屏幕之后
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullet(bullets):
    bullets.update()

    for bullet in bullets.copy(): 
            if bullet.rect.bottom <= 0 :
                bullets.remove(bullet)
    print(len(bullets))

def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        #创建新的子弹
        bullets.add(new_bullet)#将子弹添加到编组内



def get_number_aliens(ai_settings,alien_width):
    """创建一个外星人,并计算每行可以容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int (available_space_x / (1.5*alien_width))
    return number_aliens_x

def get_number_row(ai_settings,ship_height,alien_height):
    """计算屏幕可以容纳多少行外星人"""
    available_space_y = ai_settings.screen_height - (3*alien_height)- ship_height
    number_row = int(available_space_y / (1.5*alien_height))
    return number_row

def creat_alien(ai_settings, screen ,aliens , alien_number, row_number):
    """创建外星人群"""
    alien = Alien(ai_settings,screen )
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
    aliens.add(alien)

def creat_fleet(ai_settings,screen,ship,aliens):
    """创建外星人群"""
    #创建一个外星人,并计算一行可以容纳多少个外星人
    #外星人间距为外星人宽度
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    number_alien_x = get_number_aliens (ai_settings,alien_width)
    number_rows = get_number_row(ai_settings,ship.rect.height,alien.rect.height)

    #创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            creat_alien(ai_settings,screen,aliens,alien_number,row_number)