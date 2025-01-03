from math import inf

def maxScore(s: str) -> int:
  ones = 0
  zeroes = 0
  best = -inf

  for i in range(len(s) - 1):
    if s[i] == '0':
      zeroes += 1
    else:
      ones += 1

    best = max(best, zeroes - ones)

  if s[-1] == '1':
    ones += 1


  return ones + best

print(maxScore("011101"))
print(maxScore("00111"))