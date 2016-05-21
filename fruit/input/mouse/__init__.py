#!/usr/bin/env python3.4
# coding: utf-8

import pygame
from collections import defaultdict

from fruit.application.event import Update
from fruit.input.controller import Controller
from fruit.input.mouse.button import *
from fruit.input.mouse.event import *
from fruit.event import EventHook, EventHandler


class Mouse(Controller):
	"""
	Controller for the mouse.
	Handles pygame mouse events, including movement, clicking and scrolling.
	Cursor position, visibility and texture can be set from this class.
	"""

	def __init__(self):
		self.button_pressed = defaultdict(lambda: 0)
		self.visible = True

	@property
	def pos(self):
		return Vec(*pygame.mouse.get_pos())

	@pos.setter
	def pos(self, value):
		pygame.mouse.set_pos(tuple(value))

	@property
	def visible(self):
		return self._visible

	@visible.setter
	def visible(self, value):
		self._visible = value
		pygame.mouse.set_visible(value)

	@EventHook.on(Click)
	def handle_click(self, click):
		self.button_pressed[click.button] = self.button_pressed[click.button]

	@EventHook.on(Release)
	def handle_release(self, release):
		if release.button in self.button_pressed:
			del self.button_pressed[release.button]

	@EventHook.on(Update)
	def update(self, update):
		for button in self.button_pressed:
			self.button_pressed[button] += update.dt
