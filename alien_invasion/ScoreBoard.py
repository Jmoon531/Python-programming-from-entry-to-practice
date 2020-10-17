#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame.font
from pygame.sprite import Group

from ship import Ship

class scoreboard():
	'''表示记分板的类'''
	def __init__(self, screen, ai_settings):
		self.score = 0 # 当前得分
		self.level = 0 # 当前关卡等级
		# 最高得分
		with open('high_score', mode='r') as file_object:
			self.high_score = int(file_object.read().rstrip())
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.ai_settings = ai_settings
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 30)
	
	def blitme(self):
		# 当前得分图像
		str_score = "{0}'/alien ".format(self.ai_settings.alien_point) + "scored: {:,}".format(round(self.score, -1))
		self.score_image = self.font.render(str_score, True, self.text_color, self.ai_settings.bg_color)
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
		self.screen.blit(self.score_image, self.score_rect)
		# 当前关卡等级图像
		str_level = "level: {0}".format(self.level)
		self.level_image = self.font.render(str_level, True, self.text_color, self.ai_settings.bg_color)
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.screen_rect.right - 20
		self.level_rect.top = self.score_rect.bottom + 10
		self.screen.blit(self.level_image, self.level_rect)
		# 最高得分图像
		str_high_score = "Highest score: {0}".format(self.high_score)
		self.high_score_image = self.font.render(str_high_score, True, self.text_color, self.ai_settings.bg_color)
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.center = self.screen_rect.center
		self.high_score_rect.top = 20
		self.screen.blit(self.high_score_image, self.high_score_rect)
		# 剩余飞船图像
		self.ships = Group()
		for ship_number in range(self.ai_settings.ship_left - 1):
			ship = Ship(self.screen, self.ai_settings)
			ship.rect.y = 10
			ship.rect.x = 10 + ship_number * (10 +  ship.rect.width)
			self.ships.add(ship)
		self.ships.draw(self.screen)
