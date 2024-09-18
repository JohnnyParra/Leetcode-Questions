from typing import List
from functools import cmp_to_key

def largestNumber(nums: List[int]) -> str:
  arr = list(map(str, nums))
  def sortKey(a, b):
    if a + b > b + a:
      return -1
    else:
      return 1

  arr.sort(key=cmp_to_key(sortKey))

  if arr[0] == "0":
    return "0"

  return "".join(arr)


print(largestNumber([10, 2]))
print(largestNumber([3, 30, 34, 5, 9]))
print(largestNumber([0,0]))
print(largestNumber([999999998,999999997,999999999]))