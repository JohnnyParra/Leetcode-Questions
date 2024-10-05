class CustomStack:

  def __init__(self, maxSize):
    self.stack = []
    self.inc = []
    self.maxSize = maxSize

  def push(self, x):
    if len(self.stack) < self.maxSize :
      self.stack.append(x)
      self.inc.append(0)

  def pop(self):
    if len(self.stack) > 0:
        index = len(self.stack) - 1
        result = self.stack[index] + self.inc[index]
        if index > 0:
            self.inc[index - 1] += self.inc[index]
        self.stack.pop()
        self.inc.pop()
        return result
    return -1
  
  def increment(self, k, val):
    index = min(k, len(self.stack)) - 1
    if index >= 0:
      self.inc[index] += val


obj = CustomStack(3)
obj.push(1)
obj.push(2)
print(obj.pop())
obj.push(2)
obj.push(3)
obj.increment(5, 100)
obj.increment(2, 100)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())