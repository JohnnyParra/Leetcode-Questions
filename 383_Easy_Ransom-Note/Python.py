
def canConstruct(ransomNote: str, magazine: str) -> bool:
  freq = {}

  for c in magazine:
    freq[c] = 1 + freq.get(c, 0)

  for c in ransomNote:
    if c not in freq or freq[c] <= 0:
      return False
    else:
      freq[c] -= 1
  
  return True

print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))