from typing import List

def canJump(nums: List[int]) -> bool:
  goal = len(nums) - 1

  for i in range(len(nums) - 1, -1, -1):
    if i + nums[i] >= goal:
      goal = i

  return True if goal == 0 else False

print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))