#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	'''表示飞船的类'''
	def __init__(self, screen, ai_settings):
		super().__init__()
		'''初始化飞船并设置其初始位置'''
		self.screen = screen
		self.ai_settings = ai_settings
		# 加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# 将飞船置于窗口底部中央
		self.center = float(self.screen_rect.centerx)
		self.rect.x = 10 + (self.ai_settings.ship_left - 1) * (10 +  self.rect.width)
		self.rect.y = 10
		# 移动标志
		self.moving_right = False
		self.moving_left = False
	
	def update(self):
		'''更新飞船的位置'''
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		self.rect.centerx = self.center
	
	def blitme(self):
		'''在窗口指定位置绘制飞船'''
		self.screen.blit(self.image, self.rect)
	
	def ship_center(self):
		'''将飞船置于窗口底部的中央'''
		self.rect.bottom = self.screen_rect.bottom
		self.center = self.screen_rect.centerx