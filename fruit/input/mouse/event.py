#!/usr/bin/env python3.4
# coding: utf-8

import pygame

from fruit.input.event import InputEvent
from fruit.input.mouse.button import Button
from fruit.types import Vec


class MouseEvent(InputEvent):
	pass


class Click(MouseEvent):
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
	pass


class MouseScrollUp(MouseScroll):
	@classmethod
	def from_pygame_event(cls, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 4:
				return MouseScrollUp()


class MouseScrollDown(MouseScroll):
	@classmethod
	def from_pygame_event(cls, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 5:
				return MouseScrollUp()


class MouseMotion(MouseEvent):
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
	pass


class Unfocus(ActiveEvent):
	@classmethod
	def from_pygame_event(cls, event):
		if event.type == pygame.ACTIVEEVENT:
			if event.state == 0:
				return Unfocus()


class Focus(ActiveEvent):
	@classmethod
	def from_pygame_event(cls, event):
		if event.type == pygame.ACTIVEEVENT:
			if event.state == 1:
				return Focus()


class IsClicked(MouseEvent):
	def __init__(self, button):
		self.button = button
