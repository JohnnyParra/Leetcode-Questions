from typing import List

def xorQueries(arr: List[int], queries: List[List[int]]) -> List[int]:
  prefixSum = [arr[0]]
  for i in range(1, len(arr)):
    prefixSum.append(arr[i] ^ prefixSum[i - 1])

  ans = []
  for left, right in queries:
    if left == 0:
      ans.append(prefixSum[right])
    else:
      ans.append(prefixSum[right] ^ prefixSum[left - 1])

  return ans

print(xorQueries([1, 3, 4, 8], [[0,1],[1,2],[0,3],[3,3]]))