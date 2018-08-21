#!/usr/bin/python

class Settings():
    """存储游戏所有的设置参数"""

    def __init__(self):
        self.screen_width = 800
        self.screen_height= 600
        self.bg_color = (230, 230, 230)

        #飞船飞行速度
        self.ship_speed_factor = 1.5

        #设置子弹
        self.bullet_width = 3
        self.bullet_height=10
        self.bullet_color = 60, 60, 60
        self.bullet_speed_factor = 1
        self.bullet_size = 5

