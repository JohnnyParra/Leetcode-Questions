import math

def isBadVersion(n):
  if (n >= 4):
    return True
  else:
    return False


def FirstBadVersion(n):
  left = 0
  while left < n:
    mid = (left + n) // 2
    if (isBadVersion(mid)):
      n = mid
    else:
      left = mid + 1
  return n

print(FirstBadVersion(5))