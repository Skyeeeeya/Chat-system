#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 05:31:32 2019

@author: wanyiyang
"""

import random
import pygame


# 植物
class Plant(pygame.sprite.Sprite):
	def __init__(self, WIDTH=320, HEIGHT=250):
		pygame.sprite.Sprite.__init__(self)
		self.WIDTH = WIDTH
		self.HEIGHT = HEIGHT
		# 统计分数时用的
		self.added_score = False
		self.speed = 5
		self.imgs = ['/Users/wanyiyang/Desktop/pygame/plant_big.png','/Users/wanyiyang/Desktop/pygame/plant_small.png']

		self.generate_random()
		#self.imgs = ['/Users/wanyiyang/Desktop/pygame/plant1.png', '/Users/wanyiyang/Desktop/pygame/plant2.png','/Users/wanyiyang/Desktop/pygame/plant3.png', '/Users/wanyiyang/Desktop/pygame/plant4.png']
	# 随机生成障碍物
	def generate_random(self):
		idx = random.randint(0, 1)
		temp = pygame.image.load(self.imgs[idx]).convert_alpha()
		if idx == 0:
			self.plant = temp.subsurface((70*random.randint(0, 2), 0), (70, 70))
		else:
			self.plant = temp.subsurface((60*random.randint(0, 2), 0), (60, 62))
		self.rect = self.plant.get_rect()
		self.rect.left, self.rect.top = self.WIDTH+60, int(self.HEIGHT/2 + 20)
	# 不停往左移动
	def move(self):
		self.rect.left = self.rect.left-self.speed
	# 把自己画到屏幕上去
	def draw(self, screen):
		screen.blit(self.plant, self.rect)


# 飞龙
class Ptera(pygame.sprite.Sprite):
	def __init__(self, WIDTH=640, HEIGHT=500):
		pygame.sprite.Sprite.__init__(self)
		self.WIDTH = WIDTH
		self.HEIGHT = HEIGHT
		# 统计分数时用的
		self.added_score = False
		self.imgs = ['Users/wanyiyang/Desktop/pygame/ptera.png']
		# 为了飞行特效
		self.flying_count = 0
		self.flying_flag = True
		# 统计分数时用的
		self.speed = 7
		self.generate()
	# 生成飞龙
	def generate(self):
		self.ptera = pygame.image.load(self.imgs[0]).convert_alpha()
		self.ptera_0 = self.ptera.subsurface((0, 0), (92, 81))
		self.ptera_1 = self.ptera.subsurface((92, 0), (92, 81))
		self.rect = self.ptera_0.get_rect()
		self.rect.left, self.rect.top = self.WIDTH+30, int(self.HEIGHT/20)
	# 不停往左移动
	def move(self):
		self.rect.left = self.rect.left-self.speed
	# 把自己画到屏幕上去
	def draw(self, screen):
		self.flying_count += 1
		if self.flying_count % 6 == 0:
			self.flying_flag = not self.flying_flag
		if self.flying_flag:
			screen.blit(self.ptera_0, self.rect)
		else:
			screen.blit(self.ptera_1, self.rect)
