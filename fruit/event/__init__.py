#!/usr/bin/env python3.4
# coding: utf-8

from fruit.event.event import *
from fruit.event.handler import EventHandler
from fruit.event.hook import EventHook


def on(*event_or_types, priority=1):
	def _wrapper(fn):
		return EventHook(fn, event_or_types)
	return _wrapper


def post(*events):
	EventHandler.post(*events)
