from typing import List

def removeDuplicates(nums: List[int]) -> int:
  i = 1
  
  for j in range(1, len(nums)):
    if nums[j] != nums[i - 1]:
      nums[i] = nums[j]
      i +=1
  
  return i

print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))