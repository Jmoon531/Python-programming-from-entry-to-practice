#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_events(screen, ai_settings, ship, bullets, aliens, play_button, sb):
	'''响应鼠标和键盘事件'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			save_high_score(sb)
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = True
			elif event.key == pygame.K_LEFT:
				ship.moving_left = True
			elif event.key == pygame.K_SPACE and ai_settings.game_active:
				bullets.add(Bullet(screen, ai_settings, ship))
			elif event.key == pygame.K_ESCAPE:
				save_high_score(sb)
				sys.exit()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False
			elif event.key == pygame.K_LEFT:
				ship.moving_left = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			if play_button.rect.collidepoint(mouse_x, mouse_y) and not ai_settings.game_active:
				pygame.mouse.set_visible(False) # 隐藏光标
				sleep(0.5)
				game_reset(screen, ai_settings, ship, bullets, aliens, sb)

def save_high_score(sb):
	with open('high_score', mode='w') as file_object:
		file_object.write(str(sb.high_score))

def game_reset(screen, ai_settings, ship, bullets, aliens, sb):
	ai_settings.game_active = True
	ai_settings.initialize_settings()
	sb.score = 0
	sb.level = 0
	aliens.empty()
	bullets.empty()
	create_fleet(screen, ai_settings, ship, bullets, aliens, sb)
	ship.ship_center()

def update_bullets(bullets):
	'''更新子弹的位置以及删除已消失的子弹'''
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def create_fleet(screen, ai_settings, ship, bullets, aliens, sb):
	'''创建一群外星人'''
	if len(aliens) == 0:
		ai_settings.increase_speed()
		sb.level += 1
		# 清空现有的子弹
		bullets.empty()
		alien = Alien(screen, ai_settings)
		alien_height = alien.rect.height
		ship_height = ship.rect.height
		row = (ai_settings.screen_height - 3 * alien_height - ship_height) // (2 * alien_height)
		alien_width = alien.rect.width
		col = (ai_settings.screen_width - 2 * alien_width) // (2 * alien_width)
		for i in range(row):
			for j in range(col):
				alien = Alien(screen, ai_settings)
				alien.rect.y = alien_height + i * 2 * alien_height
				alien.rect.x = alien_width + j * 2 * alien_width
				aliens.add(alien)

def check_fleet_edges(ai_settings, aliens):
	'''检查外星人群体中是否有外星人到达屏幕边缘'''
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	'''改变外星人群体方向'''
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.alien_drop_speed
	ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, aliens):
	'''更新外星人群体'''
	check_fleet_edges(ai_settings, aliens)
	aliens.update()

def game_revive(screen, ai_settings, ship, bullets, aliens, sb):
	'''复活游戏'''
	ai_settings.ship_left -= 1
	if ai_settings.ship_left == 0:
		ai_settings.game_active = False
		return
	ship.ship_center()
	aliens.empty()
	create_fleet(screen, ai_settings, ship, bullets, aliens, sb)
	sleep(0.5)

def check_collisions(screen, ai_settings, ship, bullets, aliens, sb):
	'''检测外星人与飞船的碰撞、外星人与子弹的碰撞以及是否有外星人到达屏幕底端'''
	# 检测外星人与飞船的碰撞
	if pygame.sprite.spritecollideany(ship, aliens):
		game_revive(screen, ai_settings, ship, bullets, aliens, sb)
		return
	# 检测是否外星人到达屏幕底端
	else:
		screen_rect = screen.get_rect()
		for alien in aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				game_revive(screen, ai_settings, ship, bullets, aliens, sb)
				return
	# 检测子弹与外星人的碰撞
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		for aliens in collisions.values():
			sb.score = sb.score + ai_settings.alien_point * len(aliens)
			if sb.score > sb.high_score:
				sb.high_score = sb.score

def update_screen(screen, ai_settings, ship, bullets, aliens, play_button, sb):
	'''刷新屏幕'''
	# 设置背景色
	screen.fill(ai_settings.bg_color)
	# 绘制飞船
	ship.blitme()
	# 绘制子弹
	for bullet in bullets.sprites():
		bullet.blitme()
	# 绘制外星人
	aliens.draw(screen)
	# 绘制按钮
	if not ai_settings.game_active:	play_button.blitme()
	# 绘制记分板
	sb.blitme()
	# 显示游戏窗口
	pygame.display.flip()


