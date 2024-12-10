from typing import List

def hIndex(citations: List[int]) -> int:
  length = len(citations)
  h_index = [0] * (length + 1)
  
  for i in range(length):
    if citations[i] > length:
      h_index[length] += 1
    else:
      h_index[citations[i]] += 1

  total = 0

  for i in range(length, -1, -1):
    total += h_index[i]
    if total >= i:
      return i
    
print(hIndex([3,0,6,1,5]))
print(hIndex([0,11,15]))