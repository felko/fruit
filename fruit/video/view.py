#!/usr/bin/env python3.4
# coding: utf-8


class View:
	"""
	Represents the field of view of the scene.
	"""

	def __init__(self, rect, zoom=1):
		self.rect = rect
		self.zoom = zoom
