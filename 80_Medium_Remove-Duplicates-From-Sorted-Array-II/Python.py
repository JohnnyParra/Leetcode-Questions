from typing import List


def removeDuplicates(nums: List[int]) -> int:
  i = 2
  for j in range(2, len(nums)):
    if nums[j] != nums[i - 2]:
      nums[i] = nums[j]
      i += 1

  return i

print(removeDuplicates([1,1,1,2,2,3]))
print(removeDuplicates([0,0,1,1,1,1,2,3,3]))