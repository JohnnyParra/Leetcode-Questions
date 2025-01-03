from typing import List

def waysToSplitArray(nums: List[int]) -> int:
  rightSum = sum(nums)
  leftSum = 0
  valid = 0
  

  for i in range(len(nums) - 1):
    leftSum += nums[i]
    rightSum -= nums[i]

    if leftSum >= rightSum:
      valid += 1


  return valid


print(waysToSplitArray([1, 2, 2, 2, 5, 0]))
print(waysToSplitArray([10, 4, -8, 7]))
