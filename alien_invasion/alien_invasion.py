#!usr/bin.env python
# -*- coding: utf-8 -*-

import pygame

from settings import Settings
from ship import Ship
import game_functions  as gf
from pygame.sprite import Group
from alien import Alien
from button import Button
from ScoreBoard import scoreboard

def run_game():
	# 初始化游戏并创建一个窗口对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	# 创建一个飞船对象
	ship = Ship(screen, ai_settings)
	# 创建一个用于存储子弹的编组
	bullets = Group()
	# 创建一个Play按钮
	play_button = Button(screen, 'Play')
	# 创建一个记分板
	sb = scoreboard(screen, ai_settings)
	# 创建一个用于存储外星人的编组
	aliens = Group()
	gf.create_fleet(screen, ai_settings, ship, bullets, aliens, sb)
	# 游戏的主循环
	while True:
		# 监视键盘和鼠标事件
		gf.check_events(screen, ai_settings, ship, bullets, aliens, play_button, sb)
		if ai_settings.game_active:
			# 创建外星人群体
			gf.create_fleet(screen, ai_settings, ship, bullets, aliens, sb)
			# 更新飞船
			ship.update()
			# 更新子弹
			gf.update_bullets(bullets)
			# 更新外星人
			gf.update_aliens(ai_settings, aliens)
			# 检测外星人与飞船的碰撞、外星人与子弹的碰撞以及是否有外星人到达屏幕底端
			gf.check_collisions(screen, ai_settings, ship, bullets, aliens, sb)
		else:
			pygame.mouse.set_visible(True) # 显示光标
		# 刷新屏幕
		gf.update_screen(screen, ai_settings, ship, bullets, aliens, play_button, sb)

run_game()
