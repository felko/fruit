#!/usr/bin/env python3
# coding: utf-8

from math import sqrt, sin, cos, atan2


class Vec:
	"""
	Two dimensional vector.
	"""

	__slots__ = ['x', 'y']

	def __init__(self, x, y):
		self.x, self.y = x, y

	def __repr__(self):
		return 'Vec(x={}, y={})'.format(*self)

	@classmethod
	def link(cls, a, b):
		return Vec(b.x - a.x, b.y - a.y)

	@classmethod
	def polar(cls, norm, theta):
		v = Vec(0, 0)
		v.norm = norm
		v.theta = theta

	def __add__(self, other):
		dx, dy = other
		return Vec(self.x + dx, self.y + dy)

	def __sub__(self, other):
		dx, dy = other
		return Vec(self.x - dx, self.y - dy)

	def __mul__(self, other):
		if isinstance(other, (Vec, tuple)):
			kx, ky = other
			return Vec(self.x * kx, self.y * ky)
		else:
			return Vec(self.x * other, self.y * other)

	def __truediv__(self, other):
		if isinstance(other, (Vec, tuple)):
			kx, ky = other
			return Vec(self.x / kx, self.y / ky)
		else:
			return Vec(self.x / other, self.y / other)

	def __floordiv__(self, other):
		if isinstance(other, (Vec, tuple)):
			x, y = other
			return Vec(self.x // x, self.y // y)
		else:
			return Vec(self.x // other, self.y // other)

	def __radd__(self, other):
		dx, dy = other
		return Vec(self.x + dx, self.y + dy)

	def __rsub__(self, other):
		dx, dy = other
		return Vec(self.x - dx, self.y - dy)

	def __rmul__(self, other):
		if isinstance(other, (Vec, tuple)):
			kx, ky = other
			return Vec(self.x * kx, self.y * ky)
		else:
			return Vec(self.x * other, self.y * other)

	def __neg__(self):
		return Vec(-self.x, -self.y)

	def __bool__(self):
		return bool(self.norm)

	def __iter__(self):
		return iter((self.x, self.y))

	def __hash__(self):
		return hash((self.x, self.y))

	def __lt__(self, other):
		return self.norm < other.norm

	def __gt__(self, other):
		return self.norm > other.norm

	def int(self):
		return Vec(int(self.x), int(self.y))

	def round(self):
		return Vec(round(self.x), round(self.y))

	@property
	def norm(self):
		return sqrt(self.x ** 2 + self.y ** 2)

	@norm.setter
	def norm(self, value):
		self.x, self.y = self.unit * value

	@property
	def unit(self):
		return self // int(self.norm)

	@unit.setter
	def unit(self, value):
		self.x, self.y = value.unit * self.norm

	@property
	def theta(self):
		return atan2(self.y, self.y)

	@theta.setter
	def theta(self, value):
		self.x = self.norm * cos(value)
		self.y = self.norm * sin(value)

	def copy(self):
		return Vec(self.x, self.y)
