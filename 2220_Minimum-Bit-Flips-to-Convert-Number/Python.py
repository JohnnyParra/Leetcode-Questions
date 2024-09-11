def minBitFlips(start: int, goal: int) -> int:
  xor = start ^ goal
  count = 0
  while (xor > 0):
      xor = xor & (xor - 1)
      count += 1
      
  return count

print(minBitFlips(10, 7))
print(minBitFlips(3, 4))