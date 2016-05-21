#!/usr/bin/env python3.4
# coding: utf-8

import pygame

from fruit.mixin.drawable import Drawable
from fruit.event.handler import EventHandler
from fruit.types import *


class Node(Drawable, EventHandler):
	"""
	Base node class, subclass it to make custom graphic objects for your
	application.
	"""

	def __init__(self, pos=Vec(0, 0), size=Size(0, 0), layer=1, visible=True):
		self.rect = Rect(pos, size)
		self.layer = layer
		self.children = set()
		self.visible = visible

	def children_recursive(self):
		"""
		Yields every children or the instance, recursively.
		"""

		for child in self.children:
			yield from child.children_recursive()

	@property
	def pos(self):
		return self.rect.pos

	@pos.setter
	def pos(self, value):
		self.rect.pos = value

	@property
	def size(self):
		return self.rect.size

	@size.setter
	def size(self, value):
		self.rect.size = value
