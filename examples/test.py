#!/usr/bin/env python3.4
# coding: utf-8

from fruit import *

TILE_SIZE = 16


class Game(Application):
	def __init__(self):
		window = Window.create((800, 600))
		self.player = Player(Vec(0, 0))
		self.level = Level(self.player, (16, 16))
		scene = Scene((800, 600), self.level)
		super().__init__(scene, window)

	@EventHook.on(Update)
	def update(self, update):
		print(self.player.pos)

	@EventHook.on(KeyPress(Key.SPACE))
	def toggle_repeat(self, event):
		self.keyboard.repeat_delay = 1
		self.keyboard.repeat_interval = 0.001


class Level(Node):
	def __init__(self, player, size):
		super().__init__(size=Size(*size) * TILE_SIZE)
		self.children.add(player)
		self.player = player

	#@EventHook.on(*(IsPressed(arr) for arr in Arrow))
	@EventHook.on(IsPressed(Key.UP), IsPressed(Key.DOWN), IsPressed(Key.LEFT), IsPressed(Key.RIGHT))
	def move(self, press):
		newpos = self.player.pos.copy()
		newpos += press.key.rel * self.player.speed

		if Rect(newpos, self.player.size) in self.rect:
			self.player.pos = newpos

	@EventHook.on(Click)
	def teleport(self, click):
		if click.button == Button.LEFT:
			newrect = self.player.rect.copy()
			newrect.center = click.pos

			if newrect in self.rect:
				self.player.rect.center = click.pos

	def draw(self):
		surface = Surface(self.size)
		surface.fill(Color.WHITE)
		return surface


class Player(Entity):
	def __init__(self, pos, layer=1, visible=True):
		super().__init__(pos, Size(16, 16), layer=layer, visible=visible)
		self.speed = 1

	def draw(self):
		rectangle = Rectangle(Size(16, 16), Color.RED)
		return rectangle.draw()


if __name__ == '__main__':
	game = Game()
	game.start()
