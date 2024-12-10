from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
  prefix = 1
  postfix = 1
  results = []

  for i in range(len(nums)):
    results.append(prefix)
    prefix = prefix * nums[i]

  for i in range(len(nums) - 1, -1, -1):
    results[i] *= postfix
    postfix = postfix * nums[i]

  return results

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))