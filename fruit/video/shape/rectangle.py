#!/usr/bin/env python3.4
# coding: utf-8

from fruit.video.shape.shape import Shape
from fruit.video.surface import Surface


class Rectangle(Shape):
	"""
	A rectangle in 2D space.
	"""

	def __init__(self, size, color):
		super().__init__(color)
		self.size = size

	def draw(self):
		surface = Surface(self.size)
		surface._surface.fill(self.color.hex)
		return surface
