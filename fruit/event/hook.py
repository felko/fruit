#!/usr/bin/env python3.4
# coding: utf-8


class EventHook:
	"""
	Represent a single event hook, used for metaclass tricks.
	"""

	def __init__(self, callback, event_or_types, priority=1):
		self.callback = callback
		self.event_or_types = event_or_types
		self.priority = priority

	def __call__(self, instance, event):
		return self.callback(instance, event)

	@classmethod
	def on(cls, *event_or_types):
		"""
		Decorator that registers a hook.
		"""

		def _wrapper(fn):
			return EventHook(fn, event_or_types)
		return _wrapper
