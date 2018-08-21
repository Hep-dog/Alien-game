#!/usr/bin/python
import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect  = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom  = self.screen_rect.bottom

        #飞船center转化为float
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        #移动标识
        self.moving_right = False
        self.moving_left  = False
        self.moving_foward= False
        self.moving_backward = False

    def update(self):
        """根据移动标识移动飞船"""
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and (self.rect.left > 0):
            self.center -= self.ai_settings.ship_speed_factor
        elif self.moving_foward and (self.rect.top > 0):
            self.bottom -= self.ai_settings.ship_speed_factor
        elif self.moving_backward and (self.rect.bottom < self.screen_rect.bottom):
            self.bottom += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center
        self.rect.bottom  = self.bottom


    def blitme(self):
        self.screen.blit(self.image, self.rect)
