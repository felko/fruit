#!/usr/bin/env python3.4
# coding: utf-8


class Event:
	"""
	Base class of all events.
	"""

	@classmethod
	def from_pygame_event(cls, event):
		pass

	@staticmethod
	def get_event_queue(raw_event):
		return _convert_event(Event, raw_event)


def _convert_event(cls, raw_event):
	if raw_event is not None:
		for subcls in cls.__subclasses__():
			event = subcls.from_pygame_event(raw_event)

			if event is not None:
				yield event

			yield from _convert_event(subcls, raw_event)
