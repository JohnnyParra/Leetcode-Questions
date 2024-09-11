from typing import List

def pivotIndex(nums: List[int]) -> int:
  rightSum = sum(nums)
  leftSum = 0

  for i in range(0, len(nums)):
      rightSum -= nums[i]
      if (rightSum == leftSum):
          return i
      leftSum += nums[i]
      
  return -1

print(pivotIndex([1, 7, 3, 6, 5, 6]))
print(pivotIndex([1, 2, 3]))