#!/usr/bin/env python3.4
# coding: utf-8

from fruit.helper import property_alias


class Size:
	"""
	An object representing two dimensions.
	"""

	__slots__ = ['width', 'height']

	def __init__(self, width, height):
		self.width, self.height = width, height

	w = property_alias('width')
	h = property_alias('height')

	def __repr__(self):
		return 'Size(width={}, height={})'.format(*self)

	def __add__(self, other):
		dw, dh = other
		return Vec(self.width + dw, self.height + dh)

	def __sub__(self, other):
		dw, dh = other
		return Size(self.width - dw, self.height - dh)

	def __mul__(self, other):
		return Size(self.width * other, self.height * other)

	def __truediv__(self, other):
		return Size(self.width / other, self.height / other)

	def __floordiv__(self, other):
		return Size(self.width // other, self.height // other)

	def __radd__(self, other):
		dw, dh = other
		return Size(self.width + dw, self.height + dh)

	def __rsub__(self, other):
		dw, dh = other
		return Size(self.width - dw, self.height - dh)

	def __rmul__(self, other):
		return Size(self.width * other, self.height * other)

	def __bool__(self):
		return bool(self.area)

	def __iter__(self):
		return iter((self.width, self.height))

	def __hash__(self):
		return hash((self.width, self.height))

	def int(self):
		return Size(int(self.width), int(self.height))

	def round(self):
		return Size(round(self.width), round(self.height))
