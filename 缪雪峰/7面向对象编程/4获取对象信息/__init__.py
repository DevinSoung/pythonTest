print(type(123))

print(type(123)==type(456))

import types

print(type(abs)==types.BuiltinFunctionType)


print(dir('ABC'))

print('ABC'.__len__())

class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x

obj=MyObject()

print(hasattr(obj,'x'))