#!/usr/bin/env python3.4
# coding: utf-8

import pygame

from fruit.event import Event
from fruit.types.size import Size


class WindowEvent(Event):
	"""
	Basic window event type.
	"""


class ResizeWindow(WindowEvent):
	"""
	Posted when the user resizes the window.
	"""

	def __init__(self, size):
		self.size = size

	@classmethod
	def from_pygame_event(cls, event):
		if event.type == pygame.VIDEORESIZE:
			return ResizeWindow(Size(event.w, event.h))


class CloseWindow(WindowEvent):
	"""
	Posted when the user presses the "red cross" button.
	"""

	@classmethod
	def from_pygame_event(cls, event):
		if event.type == pygame.QUIT:
			return CloseWindow()
