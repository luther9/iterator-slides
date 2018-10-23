# from iterators import *


def squares_then_normal(n):
  for i in range(n):
    yield i**2
  yield from range(n)


class ListReverser(list):

  def __iter__(self):
    return iter(reversed(self))


# list(ListReverser(['cat.', 'my', 'is', 'This']))


class ListReverser2(list):

  def __iter__(self):
    for x in reversed(self):
      yield x


# list(ListReverser2(['cat.', 'my', 'is', 'This']))


class RangeIter:

  def __init__(self, start, stop):
    self.current = start
    self.stop = stop

  def __iter__(self):
    return self

  def __next__(self):
    value = self.current
    if value >= self.stop:
      raise StopIteration
    self.current += 1
    return value


# list(RangeIter(0, 10))
