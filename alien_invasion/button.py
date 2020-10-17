#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

class Button():
	'''表示按钮的类'''
	def __init__(self, screen, msg):
		'''初始化按钮的属性'''
		self.screen = screen
		# 设置按钮尺寸和背景颜色
		self.width, self.height = 200, 50
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen.get_rect().center
		self.button_color = (255, 0, 0)
		# 设置文本颜色及字体
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)
		# 将文本渲染成图片并设置其位置居中
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.screen.get_rect().center
	
	def blitme(self):
		'''绘制按钮'''
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
