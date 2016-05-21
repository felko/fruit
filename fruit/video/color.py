#!/usr/bin/env python3.4
# coding: utf-8

import pygame

from fruit.helper import property_alias


class Color:
	def __init__(self, *args):
		if len(args) == 1:
			hexcode, *_ = args

			if isinstance(hexcode, int):
				self.hex = hexcode
			elif isinstance(hexcode, str):
				self.hex = int(hexcode.strip('#'), base=16)

			self.a = 0xFF

		elif len(args) == 3:
			self.r, self.g, self.b = args
			self.a = 0xFF

		elif len(args) == 4:
			self.r, self.g, self.b, self.a = args

		else:
			raise ValueError('Invalid arguments')

	red = property_alias('r')
	green = property_alias('g')
	blue = property_alias('b')
	alpha = property_alias('a')

	@property
	def hex(self):
		return (self.r << 16)\
			+ (self.g << 8)\
			+ (self.b << 0)

	@hex.setter
	def hex(self, value):
		self.r = (value & 0xFF0000) >> 16
		self.g = (value & 0x00FF00) >> 8
		self.b = (value & 0x0000FF) >> 0

	@property
	def rgba_hex(self):
		return (self.r << 32)\
			+ (self.g << 16)\
			+ (self.b << 8)\
			+ (self.a << 0)

	@hex.setter
	def rgba_hex(self, value):
		self.r = (value & 0xFF000000) >> 32
		self.g = (value & 0x00FF0000) >> 16
		self.b = (value & 0x0000FF00) >> 8
		self.a = (value & 0x000000FF) >> 0

	@property
	def pygame_color(self):
		return pygame.Color(self.r, self.g, self.b, self.a)

	@pygame_color.setter
	def pygame_color(self, value):
		self.r = value.r
		self.g = value.g
		self.b = value.b
		self.a = value.a


Color.WHITE = Color(0xFFFFFF)
Color.BLACK = Color(0x000000)
Color.RED = Color(0xFF0000)
Color.GREEN = Color(0x00FF00)
Color.BLUE = Color(0x0000FF)
