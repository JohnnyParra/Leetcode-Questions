from random import random
import math

class RandomizedSet():
  def __init__(self):
    self.indexes = {}
    self.data = []

  def size(self):
    return len(self.data) - 1

  def insert(self, val):
    if val in self.indexes.keys():
      return False
    
    self.data.append(val)
    self.indexes[val] = self.size()

    return True

  def remove(self, val):
    if (val not in self.indexes.keys()):
      return False

    temp = self.data[self.size()]
    self.data[self.size()] = val
    self.data[self.indexes[val]] = temp
    self.data.pop()
    self.indexes[temp] = self.indexes[val]
    del self.indexes[val]

    return True
  
  def getRandom(self):
    randomIndex = math.floor(random() * (self.size() + 1))
    return self.data[randomIndex]

obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.insert(2)
param_4 = obj.getRandom()
param_5 = obj.remove(1)
param_6 = obj.insert(2)
param_7 = obj.getRandom()
print([param_1,param_2,param_3,param_4,param_5,param_6,param_7])