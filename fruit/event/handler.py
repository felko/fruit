#!/usr/bin/env python3.4
# coding: utf-8

import pygame
from collections import defaultdict

from fruit.mixin.register import RegisterMeta
from fruit.event.event import Event
from fruit.event.hook import EventHook


class EventHandlerMeta(RegisterMeta):
	"""
	Metaclass that implements instance-level event handling.
	"""

	def __new__(mcs, name, bases, attrs):
		attrs['__hooks__'] = defaultdict(list)
		attrs['queue'] = []
		return super().__new__(mcs, name, bases, attrs)

	def __init__(cls, name, bases, attrs):
		for attr in attrs.values():
			if isinstance(attr, EventHook):
				cls.on(*attr.event_or_types,
					priority=attr.priority)(attr.callback)

	def hooks(cls):
		"""
		Returns a dictionary of the hooks of the class and its base classes.
		"""

		hooks = cls.__hooks__.copy()

		for supcls in cls.__bases__:
			if isinstance(supcls, EventHandlerMeta):
				suphooks = supcls.hooks()
				events = set(hooks.keys()) | set(suphooks.keys())

				for event in events:
					hooks[event] = list(set(hooks[event] + suphooks[event]))

		return hooks

	def post(cls, *events):
		"""
		Adds events to the event queue.
		"""

		for event in events:
			if isinstance(event, Event):
				cls.queue.append(event)
			else:
				cls.queue.extend(Event.get_event_queue(event))

	def run(cls):
		"""
		Run all the events hooks in the queue.
		"""

		hook_queue = []

		for instance in cls.instances():
			for event in cls.queue:
				for event_or_type, hooks in type(instance).hooks().items():
					trigger = False

					if isinstance(event_or_type, type):
						if issubclass(event_or_type, Event):
							trigger = isinstance(event, event_or_type)
						else:
							raise TypeError(
								'Expected a subclass of Event or an event object')
					elif isinstance(event_or_type, Event):
						trigger = event == event_or_type
					else:
						raise TypeError(
							'Expected an event object or an event type')

					if trigger:
						for hook in hooks:
							hook_queue.append((hook, instance, event))

		# todo: maybe use multiprocessing
		for callback, instance, event in hook_queue:
			callback(instance, event)

		cls.queue.clear()

	def on(cls, *event_or_types, priority=1):
		"""
		Decorator that registers a hook.
		"""

		def _wrapper(hook):
			for event_or_type in event_or_types:
				index = min(priority, len(cls.__hooks__)) - 1
				cls.__hooks__[event_or_type].insert(index, hook)

		return _wrapper


class EventHandler(metaclass=EventHandlerMeta):
	"""
	Base class for event handling classes, use this rather than declaring
	explicitly EventHandlerMeta as the metaclass (unless you know what you're
	doing).
	"""
