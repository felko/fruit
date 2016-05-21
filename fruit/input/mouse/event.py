#!/usr/bin/env python3.4
# coding: utf-8

import pygame

from fruit.input.event import InputEvent
from fruit.input.mouse.button import Button
from fruit.types import Vec


class MouseEvent(InputEvent):
	"""
	Base mouse event.
	"""


class Click(MouseEvent):
	"""
	Posted when the user clicks a mouse button.
	"""

	def __init__(self, button, pos):
		self.button = button
		self.pos = pos

	@classmethod
	def from_pygame_event(cls, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			try:
				button = Button(event.button)
			except ValueError:
				pass
			else:
				pos = Vec(*event.pos)
				return Click(button, pos)


class Release(MouseEvent):
	"""
	Posted when a mouse button is released.
	"""

	def __init__(self, button, pos):
		self.button = button
		self.pos = pos

	@classmethod
	def from_pygame_event(cls, event):
		if event.type == pygame.MOUSEBUTTONUP:
			try:
				button = Button(event.button)
			except ValueError:
				pass
			else:
				pos = Vec(*event.pos)
				return Click(button, pos)


class MouseScroll(MouseEvent):
	"""
	Abstract mouse scrolling event.
	"""


class MouseScrollUp(MouseScroll):
	"""
	Posted when the user scrolls up.
	"""

	@classmethod
	def from_pygame_event(cls, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 4:
				return MouseScrollUp()


class MouseScrollDown(MouseScroll):
	"""
	Posted when the user scrolls down.
	"""

	@classmethod
	def from_pygame_event(cls, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 5:
				return MouseScrollUp()


class MouseMotion(MouseEvent):
	"""
	Posted when the mouse cursor is moved across the window.
	"""

	def __init__(self, pos, rel):
		self.pos = Vec(*pos)
		self.rel = Vec(*rel)

	@property
	def dest(self):
		return self.pos + self.rel

	@classmethod
	def from_pygame_event(cls, event):
		if event.type == pygame.MOUSEMOTION:
			return MouseMotion(event.pos, event.rel)


class ActiveEvent(MouseEvent):
	"""
	Abstract event for focusing and unfocusing the window.
	"""


class Unfocus(ActiveEvent):
	"""
	Posted when the mouse cursor exits the window.
	"""

	@classmethod
	def from_pygame_event(cls, event):
		if event.type == pygame.ACTIVEEVENT:
			if event.state == 0:
				return Unfocus()


class Focus(ActiveEvent):
	"""
	Posted when the mouse cursor enters the window.
	"""

	@classmethod
	def from_pygame_event(cls, event):
		if event.type == pygame.ACTIVEEVENT:
			if event.state == 1:
				return Focus()


class IsClicked(MouseEvent):
	"""
	Posted every frame as long as the mouse button is clicked.
	"""

	def __init__(self, button):
		self.button = button
