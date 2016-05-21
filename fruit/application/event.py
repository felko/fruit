#!/usr/bin/env python3.4
# coding: utf-8

from fruit.event import Event


class AppEvent(Event):
	"""
	Base app event type.
	"""


class StartApp(AppEvent):
	"""
	Posted when the application is started.
	"""


class QuitApp(AppEvent):
	"""
	Posted when the application is stopped.
	"""


class Update(AppEvent):
	def __init__(self, dt):
		self.dt = dt
