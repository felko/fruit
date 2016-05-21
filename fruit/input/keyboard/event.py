#!/usr/bin/env python3.4
# coding: utf-8

import pygame
from enum import Enum

from fruit.input.event import InputEvent

class KeyboardEvent(InputEvent):
	pass

class KeySequence(KeyboardEvent):
	def __init__(self, *keys):
		self.keys = list(keys)

	def __add__(self, key):
		return KeySequence(self.keys + [key])

from fruit.input.keyboard.key import Key
from fruit.types import Vec


class KeyPress(KeyboardEvent):
	"""
	Posted when the user pressed a key.
	"""

	def __init__(self, key):
		self.key = key

	def __eq__(self, other):
		if isinstance(other, KeyPress):
			return self.key == other.key
		else:
			return False

	def __hash__(self):
		return hash(self.key)

	@classmethod
	def from_pygame_event(cls, event):
		if event.type == pygame.KEYDOWN:
			try:
				key = Key(event.key)
			except ValueError:
				pass
			else:
				return KeyPress(key)


class Arrow(KeyPress, Enum):
	"""
	Posted when the users presses an arrow.
	"""

	def __init__(self, key, rel):
		KeyPress.__init__(self, key)
		self.rel = Vec(*rel)

	@classmethod
	def from_pygame_event(cls, event):
		if event.type == pygame.KEYDOWN:
			try:
				key = Key(event.key)
			except ValueError:
				pass
			else:
				for arr in Arrow:
					if arr.key == key:
						return arr

	UP = Key.UP, (+0, -1)
	DOWN = Key.DOWN, (+0, +1)
	RIGHT = Key.RIGHT, (+1, +0)
	LEFT = Key.LEFT, (-1, +0)


class KeyRelease(KeyboardEvent):
	"""
	Posted when a key is released.
	"""

	def __init__(self, key):
		self.key = key

	def __eq__(self, other):
		if isinstance(other, KeyRelease):
			return self.key == other.key
		else:
			return False

	def __hash__(self):
		return hash(self.key)

	@classmethod
	def from_pygame_event(cls, event):
		if event.type == pygame.KEYUP:
			try:
				key = Key(event.key)
			except ValueError:
				pass
			else:
				return KeyRelease(key)


class IsPressed(KeyboardEvent):
	"""
	Posted every frame as long as the key is pressed.
	"""

	def __init__(self, key):
		self.key = key

	def __hash__(self):
		return hash(self.key)
