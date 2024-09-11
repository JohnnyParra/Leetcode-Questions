from typing import List

def maxProfit(prices: List[int]) -> int:
  left = 0
  right = 1
  maxProfit = 0

  while (right < len(prices)):
    if (prices[left] < prices[right]):
      maxProfit = max(maxProfit, prices[right] - prices[left])
    else:
      left = right
    right += 1
  
  return maxProfit

print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))