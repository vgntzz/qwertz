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
