#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	'''表示子弹的类'''
	def __init__(self, screen, ai_settings, ship):
		super().__init__()
		self.screen = screen
		#创建子弹图像并设置其位置
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		#self.y = float(self.rect.y)
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
	
	def update(self):
		'''更新子弹位置'''
		self.rect.y -= self.speed_factor
	
	def blitme(self):
		'''绘制子弹'''
		pygame.draw.rect(self.screen, self.color, self.rect)
