#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Settings():
	'''存储所有设置的类'''
	def __init__(self):
		# 游戏活跃标志
		self.game_active = False
		
		# 窗口设置
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (230, 230, 230)
		
		# 飞船设置
		self.ship_speed_factor = 1.5
		self.ship_left = 4
		
		# 子弹设置
		self.bullet_speed_factor = 2
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		
		# 外星人设置
		self.alien_speed_factor = 1
		self.alien_drop_speed = 10
		self.fleet_direction = 1  # 1表示向右，-1表示向左
		
		# 加快游戏节奏
		self.speed_scale = 1.1
		
		# 击落一个外星人的得分
		self.alien_point = 10
		
	def initialize_settings(self):
		'''初始化随游戏进行而变化的设置'''
		self.ship_left = 4
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 1
		self.alien_speed_factor = 1
		self.alien_drop_speed = 10
		self.fleet_direction = 1
		self.alien_point = 10
		
	def increase_speed(self):
		'''提高游戏速度'''
		self.ship_speed_factor *= self.speed_scale
		self.bullet_speed_factor *= self.speed_scale
		self.alien_speed_factor *= self.speed_scale
		self.alien_drop_speed *= self.speed_scale
		self.fleet_direction *= self.speed_scale
		self.alien_point += 20
