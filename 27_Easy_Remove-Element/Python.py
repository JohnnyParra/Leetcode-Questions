from typing import List

def removeElement(nums: List[int], val: int) -> int:
  i = 0
  j = len(nums) - 1

  while i <= j:
    if nums[i] == val:
      nums[i] = nums[j]
      j -= 1
    elif nums[i] != val:
      i += 1

  return i

print(removeElement([3,2,2,3], 3))
print(removeElement([0,1,2,2,3,0,4,2], 2))