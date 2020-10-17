#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	'''描述外星人的类'''
	def __init__(self,  screen, ai_settings):
		'''初始化外星人并设置其起始位置'''
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		# 加载外星人的图像
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
	
	def check_edges(self):
		'''检查外星人是否到达了屏幕边缘'''
		if self.rect.right >= self.screen_rect.right:
			return True
		elif self.rect.x <= 0:
			return True
		else:
			return False
	
	def update(self):
		'''移动外星人'''
		self.rect.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
	
	def blitme(self):
		'''在指定位置绘制外星人'''
		self.screen.blit(self.image, self.rect)

