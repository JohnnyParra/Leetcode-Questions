from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> List:
  for i in range(n):
    nums1[m+i] = nums2[i]

  nums1.sort()
  return nums1

print(merge([1,2,3,0,0,0], 3, [2,5,6], 2))
print(merge([1], 1, [], 0))