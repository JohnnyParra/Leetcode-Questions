def countPalindromicSubsequence(s: str) -> int:
  letters = set(s)
  count = 0

  for letter in letters:
    i, j = s.index(letter), s.rindex(letter)
    
    if j - i > 1:
      count += len(set(s[i + 1 : j]))

  return count

print(countPalindromicSubsequence("aabca"))
print(countPalindromicSubsequence("bbcbaba"))