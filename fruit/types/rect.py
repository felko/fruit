#!/usr/bin/env python3
# coding: utf-8

import itertools

from fruit.types.vec import Vec
from fruit.types.size import Size
from fruit.helper import property_alias, clamp0x


class Rect:
	"""
	Rectangle in 2D space.
	"""

	def __init__(self, *args, **kwds):
		if len(args) == 4:
			self.x, self.y, self.w, self.h = args
		elif len(args) == 2:
			pos, size = args
			self.x, self.y = pos
			self.w, self.h = size
		elif len(args) == 0:
			if len(kwds) == 4:
				self.x, self.y = kwds['x'], kwds['y']
				self.w, self.h = kwds['w'], kwds['h']
			elif len(kwds) == 2:
				self.x, self.y = kwds['pos']
				self.w, self.h = kwds['size']
			else:
				raise ValueError('Not enough keyword arguments')
		else:
			raise ValueError('Not enough positional arguments')

	def __repr__(self):
		return 'Rect({0.x}, {0.y}, {0.w}, {0.h})'.format(self)

	width = property_alias('w')
	height = property_alias('h')

	@classmethod
	def link(cls, a, b):
		return Vec(a, b - a)

	@property
	def area(self):
		return clamp0x(self.w) * clamp0x(self.h)

	@property
	def pos(self):
		return Vec(self.x, self.y)

	@pos.setter
	def pos(self, value):
		self.x, self.y = value

	@property
	def size(self):
		return Size(self.w, self.h)

	@size.setter
	def size(self, value):
		self.w, self.h = value

	@property
	def topleft(self):
		return self.pos

	@topleft.setter
	def topleft(self, value):
		self.top, self.left = value

	@property
	def topright(self):
		return Vec(self.x + self.w, self.y)

	@topright.setter
	def topright(self, value):
		self.top, self.right = value

	@property
	def bottomleft(self):
		return Vec(self.x, self.y + self.h)

	@bottomleft.setter
	def bottomleft(self, value):
		self.bottom, self.left = value

	@property
	def bottomright(self):
		return Vec(self.x + self.w, self.y + self.h)

	@bottomright.setter
	def bottomright(self, value):
		self.bottom, self.right = value

	@property
	def corners(self):
		yield self.topleft
		yield self.topright
		yield self.bottomleft
		yield self.bottomright

	@property
	def center(self):
	    return self.pos + Vec.link(self.topleft, self.bottomright) / 2

	@center.setter
	def center(self, value):
		x, y = value
		self.x, self.y = value - Vec.link(self.topleft, self.bottomright) / 2

	@property
	def top(self):
		return self.y

	@top.setter
	def top(self, value):
		self.h += self.y - value
		self.y = value

	@property
	def bottom(self):
		return self.y + self.h

	@bottom.setter
	def bottom(self, value):
		self.h += value - self.y
		self.y = value - self.h

	@property
	def left(self):
		return self.x

	@left.setter
	def left(self, value):
		self.w += self.x - value
		self.x = value

	@property
	def right(self):
		return self.x + self.w

	@right.setter
	def right(self, value):
		self.w += value - self.x
		self.x = value - self.w

	def copy(self):
		return Rect(self.pos, self.size)

	def __iter__(self):
		for x, y in itertools.product(
				range(self.left, self.right),
				range(self.top, self.bottom)):
			yield Vec(x, y)

	def __contains__(self, vec_or_rect):
		if isinstance(vec_or_rect, (tuple, Vec)):
			x, y = vec_or_rect

			return x in range(self.left, self.right) and\
				y in range(self.top, self.bottom)
		elif isinstance(vec_or_rect, Rect):
			return all(p in self for p in vec_or_rect.corners)
		else:
			raise TypeError("x in rect: x should be a tuple, a vector or a rect")

	def __bool__(self):
		return bool(self.area)

	def __and__(self, other):
		return any(p in self for p in other.corners) or\
			any(p in other for p in self.corners)

	def __xor__(self, other):
		return all(p in self for p in other.corners)
