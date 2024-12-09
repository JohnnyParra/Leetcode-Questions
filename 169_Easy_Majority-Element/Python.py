from typing import List

def majorityElement(nums: List[int]) -> int:
  count = 0
  majority = -1

  for i in range(len(nums)):
    if count == 0:
      majority = nums[i]
      count += 1
    elif nums[i] == majority:
      count += 1
    else:
      count -= 1

  return majority

print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))