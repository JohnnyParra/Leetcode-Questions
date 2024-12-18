from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:
  left = 0
  right = 0
  sumOfWindow = 0
  results = float('inf')

  for right in range(len(nums)):
    sumOfWindow += nums[right]

    while sumOfWindow >= target:
      results = min(results, right - left + 1)
      sumOfWindow -= nums[left]
      left += 1

  return results if results != float('inf') else 0


print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))