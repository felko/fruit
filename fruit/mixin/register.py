#!/usr/bin/env python3.4
# coding: utf-8

from fruit.mixin.meta import MixinMeta


class RegisterMeta(MixinMeta):
	def __new__(mcs, name, bases, attrs):
		attrs['__instances__'] = []

		if '__init__' in attrs:
			old_init = attrs['__init__']
		else:
			if bases:
				base, *_ = bases
			else:
				base = object

			old_init = base.__init__


		def __init__(self, *args, register=True, **kwds):
			old_init(self, *args, **kwds)

			if register:
				cls.register(self)

		attrs['__init__'] = __init__

		cls = super().__new__(mcs, name, bases, attrs)
		return cls

	def register(cls, instance):
		cls.__instances__.append(instance)

	def instances(cls):
		yield from cls.__instances__

		for subcls in cls.__subclasses__():
			yield from subcls.instances()


class Register(metaclass=RegisterMeta):
	pass
