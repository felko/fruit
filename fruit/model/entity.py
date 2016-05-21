#!/usr/bin/env python3.4
# coding: utf-8

from fruit.model.node import Node
from fruit.video import *
from fruit.types import Rect


class Entity(Node):
	"""
	Base entity node.
	Subclass it to declare custom game objects.
	"""
