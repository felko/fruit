#!/usr/bin/env python3.4
# coding: utf-8


def clamp(m, x, M):
	return max(m, min(x, M))


def clamp0(x, M):
	return clamp(0, x, M)


def clamp0x(x):
	return max(0, x)


def property_alias(name):
	def fget(self):
		return getattr(self, name)

	def fset(self, value):
		setattr(self, name, value)

	def fdel(self):
		delattr(self, name)

	return property(fget, fset, fdel)


def resolve_defining_class(mth):
	qname = mth.__qualname__.split('.')

	if len(qname) < 2:
		raise ValueError(
			'Method {!r} is not defined in a class.'.format(mth.__qualname__))

	cls_name = qname[-2]
	cls_mod = mth.__module__

	for cls in object.__subclasses__():
		if cls.__qualname__ == cls_name and cls.__module__ == cls_mod:
			return cls

	# Should be unreachable
	raise TypeError(
		'The class {}.{} does not appear to be defined'.format(cls_mod, cls_name))
