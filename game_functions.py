#!/usr/bin/python

import sys
import pygame
from bullet import Bullet

def check_keyup_events(event, ship):
    #向左移动飞船
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left  = False
    elif event.key == pygame.K_UP:
        ship.moving_foward = False
    elif event.key == pygame.K_DOWN:
        ship.moving_backward = False


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    #向右移动飞船
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left  = True
    elif event.key == pygame.K_UP:
        ship.moving_foward = True
    elif event.key == pygame.K_DOWN:
        ship.moving_backward = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)


def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)

    #在飞船和外星人后画出所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets:
        #消除消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        #print(len(bullets))

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_size:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

