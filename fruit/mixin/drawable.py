#!/usr/bin/env python3.4
# coding: utf-8


class Drawable:
	"""
	Base class for drawable objects.
	"""

	def draw(self):
		"""
		Returns a Surface object.
		"""

		raise NotImplementedError(
			"Method `draw` is not implemented for {}".format(type(self)))
