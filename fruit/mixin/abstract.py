#!/usr/bin/env python3.4
# coding: utf-8

from fruit.mixin.meta import MixinMeta


# Not using abc.ABCMeta to avoid metaclass conflict
class AbstractMeta(MixinMeta):
	def __new__(mcs, name, bases, attrs):
		virtuals = {}

		for base in bases:
			if isinstance(base, AbstractMeta):
				virtuals.update(base.__virtuals__)

		attrs['__virtuals__'] = virtuals


class AbstractClass(metaclass=AbstractMeta):
	pass


def abstractmethod(mth):



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
