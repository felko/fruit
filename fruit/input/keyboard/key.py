#!/usr/bin/env python3.4
# coding: utf-8

import pygame
from enum import Enum

from fruit.input.keyboard.event import KeySequence


class Key(Enum):
	"""
	A key from a standard keyboard.
	"""

	def __add__(self, key):
		return KeySequence(self, key)

	BACKSPACE = pygame.K_BACKSPACE
	DELETE = pygame.K_DELETE

	RETURN = pygame.K_RETURN
	SPACE = pygame.K_SPACE
	TAB = pygame.K_TAB

	CLEAR = pygame.K_CLEAR
	PAUSE = pygame.K_PAUSE
	INSERT = pygame.K_INSERT
	ESCAPE = pygame.K_ESCAPE

	HOME = pygame.K_HOME
	END = pygame.K_END
	PAGEUP = pygame.K_PAGEUP
	PAGEDOWN = pygame.K_PAGEDOWN

	UP = pygame.K_UP
	DOWN = pygame.K_DOWN
	RIGHT = pygame.K_RIGHT
	LEFT = pygame.K_LEFT

	EXCLAIM = pygame.K_EXCLAIM
	QUOTE = pygame.K_QUOTEDBL
	HASH = pygame.K_HASH
	DOLLAR = pygame.K_DOLLAR
	AMPERSAND = pygame.K_AMPERSAND
	APOSTROPHE = pygame.K_QUOTE
	LPAREN = pygame.K_LEFTPAREN
	RPAREN = pygame.K_RIGHTPAREN
	ASTERISK = pygame.K_ASTERISK
	PLUS = pygame.K_PLUS
	COMMA = pygame.K_COMMA
	MINUS = pygame.K_MINUS
	PERIOD = pygame.K_PERIOD
	SLASH = pygame.K_SLASH

	K0 = pygame.K_0
	K1 = pygame.K_1
	K2 = pygame.K_2
	K3 = pygame.K_3
	K4 = pygame.K_4
	K5 = pygame.K_5
	K6 = pygame.K_6
	K7 = pygame.K_7
	K8 = pygame.K_8
	K9 = pygame.K_9

	P0 = pygame.K_KP0
	P1 = pygame.K_KP1
	P2 = pygame.K_KP2
	P3 = pygame.K_KP3
	P4 = pygame.K_KP4
	P5 = pygame.K_KP5
	P6 = pygame.K_KP6
	P7 = pygame.K_KP7
	P8 = pygame.K_KP8
	P9 = pygame.K_KP9

	COLON = pygame.K_COLON
	SEMICOLON = pygame.K_SEMICOLON
	LESS = pygame.K_LESS
	EQUALS = pygame.K_EQUALS
	GREATER = pygame.K_GREATER
	QUESTION = pygame.K_QUESTION
	AT = pygame.K_AT
	BACKSLASH = pygame.K_BACKSLASH
	LBRACKET = pygame.K_LEFTBRACKET
	RBRACKET = pygame.K_RIGHTBRACKET
	CARET = pygame.K_CARET
	UNDERSCORE = pygame.K_UNDERSCORE
	BACKQUOTE = pygame.K_BACKQUOTE

	A = pygame.K_a
	B = pygame.K_b
	C = pygame.K_c
	D = pygame.K_d
	E = pygame.K_e
	F = pygame.K_f
	G = pygame.K_g
	H = pygame.K_h
	I = pygame.K_i
	J = pygame.K_j
	K = pygame.K_k
	L = pygame.K_l
	M = pygame.K_m
	N = pygame.K_n
	O = pygame.K_o
	P = pygame.K_p
	Q = pygame.K_q
	R = pygame.K_r
	S = pygame.K_s
	T = pygame.K_t
	U = pygame.K_u
	V = pygame.K_v
	W = pygame.K_w
	X = pygame.K_x
	Y = pygame.K_y
	Z = pygame.K_z

	F1 = pygame.K_F1
	F2 = pygame.K_F2
	F3 = pygame.K_F3
	F4 = pygame.K_F4
	F5 = pygame.K_F5
	F6 = pygame.K_F6
	F7 = pygame.K_F7
	F8 = pygame.K_F8
	F9 = pygame.K_F9
	F10 = pygame.K_F10
	F11 = pygame.K_F11
	F12 = pygame.K_F12
	F13 = pygame.K_F13
	F14 = pygame.K_F14
	F15 = pygame.K_F15

	NUMLOCK = pygame.K_NUMLOCK
	CAPSLOCK = pygame.K_CAPSLOCK
	SCROLLOCK = pygame.K_SCROLLOCK
	RSHIFT = pygame.K_RSHIFT
	LSHIFT = pygame.K_LSHIFT
	RCTRL = pygame.K_RCTRL
	LCTRL = pygame.K_LCTRL
	RALT = pygame.K_RALT
	LALT = pygame.K_LALT
	RMETA = pygame.K_RMETA
	LMETA = pygame.K_LMETA
	LSUPER = pygame.K_LSUPER
	RSUPER = pygame.K_RSUPER
	MODE = pygame.K_MODE
	HELP = pygame.K_HELP
	PRINT = pygame.K_PRINT
	SYSREQ = pygame.K_SYSREQ
	BREAK = pygame.K_BREAK
	MENU = pygame.K_MENU
	POWER = pygame.K_POWER
	EURO = pygame.K_EURO
