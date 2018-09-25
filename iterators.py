class ListReverser:

  def __init__(self, lst):
    self.list = lst

  def __iter__(self):
    return iter(reversed(self.list))


class ListReverser2:

  def __init__(self, lst):
    self.list = lst

  def __iter__(self):
    lst = self.list
    for i in range(len(lst) - 1, -1, -1):
      yield lst[i]


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
