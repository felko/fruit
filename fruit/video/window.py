#!/usr/bin/env python3.4
# coding: utf-8

import pygame
import os

from fruit.video.surface import Surface
from fruit.video.event import *
from fruit.video.color import *
from fruit.event import *

DEFAULT_ICON_PATH = os.path.join(os.sep.join(__file__.split(os.sep)[:-2]), 'default_icon.png')


class Window(EventHandler):
	"""
	A singleton object that wraps the screen.
	"""

	def __init__(self, surface):
		self.surface = surface
		self.title = "Fruit window"
		self.icon = Surface.load(DEFAULT_ICON_PATH)
		self.default_color = Color.BLACK

	@classmethod
	def create(cls, size, resizable=True):
		"""
		Instantiate the window at a given size.
		"""

		surface = Surface(size)

		flag = 0

		if resizable:
			flag = pygame.RESIZABLE

		surface._surface = pygame.display.set_mode(tuple(size), flag)
		return cls(surface)

	@EventHook.on(ResizeWindow)
	def resize(self, event):
		self.surface.size = event.size

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, value):
		self._title = value
		pygame.display.set_caption(value)

	@property
	def icon(self):
		return self._icon

	@icon.setter
	def icon(self, value):
		self._icon = value
		pygame.display.set_icon(value._surface)

	def clear(self):
		"""
		Fills the screen with the window's default color.
		"""

		self.surface.fill(self.default_color)
