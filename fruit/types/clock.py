#!/usr/bin/env python3.4
# coding: utf-8

import pygame


class Clock:
	"""
	Handles time delta.
	"""

	def __init__(self):
		self._clock = pygame.time.Clock()

	def tick(self):
		dt = self._clock.tick() / 1000
		return dt
