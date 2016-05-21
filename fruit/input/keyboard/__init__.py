#!/usr/bin/env python3.4
# coding: utf-8

import pygame
from collections import defaultdict

from fruit.application.event import Update
from fruit.input.controller import Controller
from fruit.input.keyboard.event import *
from fruit.event import EventHook, EventHandler


class Keyboard(Controller):
	def __init__(self):
		self.pressed_keys = defaultdict(lambda: 0)
		self.repeat_delay = None
		self.repeat_interval = 0

	@property
	def repeat_delay(self):
		return self._repeat_delay

	@repeat_delay.setter
	def repeat_delay(self, value):
		self._repeat_delay = value

		if value is None:
			pygame.key.set_repeat()
		else:
			pygame.key.set_repeat(round(value * 1000), round(self.repeat_interval * 1000))

	@property
	def repeat_interval(self):
		return self._repeat_interval

	@repeat_interval.setter
	def repeat_interval(self, value):
		self._repeat_interval = value

		if self.repeat_delay is not None:
			pygame.key.set_repeat(round(self.repeat_interval * 1000), round(value * 1000))

	@EventHook.on(KeyPress)
	def handle_press(self, press):
		self.pressed_keys[press.key] = self.pressed_keys[press.key]

		key_queue = list(self.pressed_keys)
		key_queue.sort(key=lambda k: self.pressed_keys[k], reverse=True)

		if len(key_queue) >= 2:
			for i in range(2, len(key_queue)):
				seq, *keys = key_queue[-i:]
				for key in keys:
					seq += key

				EventHandler.post(seq)

	@EventHook.on(KeyRelease)
	def handle_release(self, release):
		if release.key in self.pressed_keys:
			del self.pressed_keys[release.key]

	@EventHook.on(Update)
	def update(self, update):
		for key in self.pressed_keys:
			self.pressed_keys[key] += update.dt
			EventHandler.post(IsPressed(key))
