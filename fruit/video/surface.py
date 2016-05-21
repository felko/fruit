#!/usr/bin/env python3.4
# coding: utf-8

import pygame

from fruit.mixin.drawable import Drawable
from fruit.types import Size


class Surface(Drawable):
	"""
	Fruit wrapper for pygame.Surface.
	Use it to draw your objects.
	"""

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
		"""
		Loads an image from a given file.
		"""

		return Surface(pygame.image.load(path))

	def save(self, path):
		"""
		Save the image to a given file.
		"""

		pygame.image.save(self._surface, path)

	@property
	def size(self):
		return Size(*self._surface.get_size())

	@size.setter
	def size(self, value):
		self._surface.set_size(value)

	def paste(self, drawable, pos):
		"""
		Paste a given surface on the image, equivalent to pygame's blit.
		"""

		overlay = drawable.draw()
		self._surface.blit(overlay._surface, tuple(pos))

	def fill(self, color):
		"""
		Uniformly fill the window with a given color.
		"""

		self._surface.fill(color.pygame_color)

	def draw(self):
		return self
