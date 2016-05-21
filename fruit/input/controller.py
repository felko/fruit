#!/usr/bin/env python3.4
# coding: utf-8

from fruit.event import EventHandler


class Controller(EventHandler):
	"""
	Base class for controllers.
	Note: controllers are meant to be singleton classes.
	"""
