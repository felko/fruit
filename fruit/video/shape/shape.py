#!/usr/bin/env python3.4
# coding: utf-8

from fruit.mixin.drawable import Drawable


class Shape(Drawable):
	"""
	An abstract shape.
	"""

	def __init__(self, color):
		self.color = color
