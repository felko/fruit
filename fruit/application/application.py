#!/usr/bin/env python3.4
# coding: utf-8

import pygame

from fruit.event import EventHandler, EventHook
from fruit.application.event import *
from fruit.input import *
from fruit.video.event import *
from fruit.types.clock import Clock


class Application(EventHandler):
	def __init__(self, scene, window):
		self.scene = scene
		self.window = window
		self.keyboard = Keyboard()
		self.mouse = Mouse()
		self.clock = Clock()
		self.running = False

	def handle_events(self):
		for pygame_event in pygame.event.get():
			EventHandler.post(pygame_event)

	def handle_events(self):
		for event in pygame.event.get():
			EventHandler.post(event)

	def display(self):
		scene_surf = self.scene.draw()
		self.window.clear()
		self.window.surface.paste(scene_surf, (0, 0))

	def start(self):
		self.running = True
		EventHandler.post(StartApp())

		#import pdb; pdb.set_trace()
		while self.running:
			dt = self.clock.tick()
			self.handle_events()
			EventHandler.post(Update(dt))
			EventHandler.run()
			self.display()
			pygame.display.flip()

		self.quit()

	def quit(self):
		self.running = False
		EventHandler.post(QuitApp())

	@EventHook.on(CloseWindow)
	def red_cross_button(self, event):
		self.quit()
