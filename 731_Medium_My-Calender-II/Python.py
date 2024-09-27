class MyCalendarTwo:
  def __init__(self):
    self.single = []
    self.double = []

  def book(self, start: int, end: int) -> bool:
    for s, e in self.double:
      if max(s, start) < min(e, end):
        return False

    for s, e in self.single:
      if max(s, start) < min(e, end):
        self.double.append([max(s, start), min(e, end)])

    self.single.append([start, end])
    return True
  

obj = MyCalendarTwo()
print(obj.book(10, 20))
print(obj.book(50, 60))
print(obj.book(10, 40))
print(obj.book(5, 15))
print(obj.book(5, 10))
print(obj.book(25, 55))