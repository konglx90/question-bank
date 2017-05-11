# -*- coding: utf-8 -*-

class Const(object):

	class ConstError(TypeError):
		pass

	class ConstCaseError(ConstError):
		pass

	reserved_keys = ('keys',
					'values',
					'get',
					'update',
					'_items',
					'_values',
					'__getattr__',
					'__setattr__',
					'__contains__')

	def __init__(self, *args, **kwargs):

		for reserved_key in self.reserved_keys:
			if reserved_key in args or reserved_key in kwargs:
				raise ValueError('Const name {0} is not allowed.'.format(reserved_key))

		for key in kwargs.keys():
			if not key.isupper():
				raise self.ConstCaseError, "const name '%s' is not all uppercase" % key

		self._items = dict(zip(args, range(len(args))), **kwargs)
		self._values = set(self._items.values())

	def __getattr__(self, name):
		return self._items[name]

	def __setattr__(self, name, value):
		if not name.isupper() and name not in self.reserved_keys:
			raise self.ConstCaseError, "const name '%s' is not all uppercase" % name
		if name not in self.reserved_keys:
			if self.__dict__['_items'].has_key(name):
				raise self.ConstError, "Can't rebind const instance attribute (%s)" % name
			self.__dict__['_items'][name] = value

		self.__dict__[name] = value

	def __contains__(self, value):
		return value in self._values

	def get(self, name, default=None):
		return self._items.get(name, default)

	def update(self, pairs):
		self._items.update(pairs)
		self._values = set(self._items.values())

	def keys(self):
		return self._items.keys()

	def values(self):
		return self._values


# 题目的类型
QUESTION_TYPE = Const(
	# 单项选择题
	SINGLE_CHOICE='SINGLE_CHOICE',
	# 多项选择题
	MORE_CHOICE='MORE_CHOICE',
	# 概述解答题
	SUMMARY='SUMMARY'
)
