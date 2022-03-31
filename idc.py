@type.__call__
class model:
  def __enter__(self):
    import sys
    self.reset = sys._getframe(1).f_globals.copy()
    sys._getframe(1).f_globals.clear()
  def __exit__(self, *_whatever):
    import sys
    k = sys._getframe(1)
    r = type('model',(),k.f_globals)()
    k.f_globals.clear()
    k.f_globals.update(self.reset|{'model':r})
    return 0

with model:
  n, a = 3, 7
  b = 2, 6
assert not[*{(model.n,model.a),(3,7)}][1:]
assert not[*{model.b,(2,6)}][1:]
print(model)

def implicit_equals(*ab):return not[*{*ab}][1:]
for*k,in[(0**0,1,1>0),((),()),(0,0<0),((1,2),)*3,(1,2,3)]:print(implicit_equals(*k))

import dis,types
a=lambda:print(*[*map(chr,[104,101,108,108,111])],sep='')
b = types.CodeType(0,0,0,0,6,67,bytes([116,0,103,0,116,1,116,2,103,0,100,1,162,1,131,2,162,1,100,2,100,3,105,1,142,1,83,0]),(None, [104, 101, 108, 108, 111], 'sep', ''),('print','map','chr'),(),'','',1,bytes([0,0]))
print(a.__code__.co_argcount == b.co_argcount)
print(a.__code__.co_nlocals == b.co_nlocals)
print(a.__code__.co_varnames == b.co_varnames)
print(a.__code__.co_flags == b.co_flags)
print(a.__code__.co_stacksize == b.co_stacksize)
print(a.__code__.co_consts, b.co_consts)
print(a.__code__.co_names == b.co_names)
print(a.__code__.co_varnames == b.co_varnames)
print(b.co_code == a.__code__.co_code)
a()
exec(b)
