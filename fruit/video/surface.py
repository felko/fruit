#!/usr/bin/env python3.4
# coding: utf-8

import pygame

from fruit.mixin.drawable import Drawable
from fruit.types import Size


class Surface(Drawable):
	def __init__(self, size_or_surface):
		if isinstance(size_or_surface, (tuple, Size)):
			self._surface = pygame.Surface(tuple(size_or_surface))
			self._surface.fill(0x000000)
		elif isinstance(size_or_surface, pygame.Surface):
			self._surface = size_or_surface
		elif isinstance(size_or_surface, Surface):
			self._surface = size_or_surface._surface
		else:
			raise TypeError(
				'Excpected size or surface, got {!r}'.format(size_or_surface))

	@classmethod
	def load(cls, path):
		return Surface(pygame.image.load(path))

	def save(self, path):
		pygame.image.save(self._surface, path)

	@property
	def size(self):
		return Size(*self._surface.get_size())

	@size.setter
	def size(self, value):
		self._surface.set_size(value)

	def paste(self, drawable, pos):
		overlay = drawable.draw()
		self._surface.blit(overlay._surface, tuple(pos))

	def fill(self, color):
		self._surface.fill(color.pygame_color)

	def draw(self):
		return self
