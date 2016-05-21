#!/usr/bin/env python3.4
# coding: utf-8

from fruit.model.entity import Entity
from fruit.video import View, Surface
from fruit.types import Rect, Vec


class Scene:
	"""
	Represents a set of nodes on a window.
	"""

	def __init__(self, size, *nodes):
		self.nodes = set(nodes)
		self.view = View(Rect((0, 0), size), zoom=1)

	def nodes_recursive(self):
		for node in self.nodes:
			yield from self.node.children_recursive()

	def draw(self):
		"""
		Draws the scene to a surface.
		"""

		surface = Surface(tuple(self.view.rect.size))
		nodes = list(self.nodes)
		nodes.sort(key=lambda node: node.layer, reverse=True)

		for node in nodes:
			if node.rect & self.view.rect:
				_draw_node(surface, node, self.view)

		return surface


def _draw_node(surface, node, view, parent=None):
	"""
	Draws a node and its children recursively.
	"""

	if node.visible:
		surf = node.draw()

		pos = node.pos

		if parent is not None:
			pos += parent.pos

		pos -= view.rect.pos

		surface.paste(surf, pos)

		pred = lambda n: Rect(pos, node.size) & view.rect
		children = list(filter(pred, node.children))
		children.sort(key=lambda node: node.layer, reverse=True)

		for child in children:
			_draw_node(surface, child, view, node)
