def lengthOfLongestSubstring(s: str) -> int:
  seen = set()
  longest = 0
  left = 0
  right = 0

  while left <= len(s) - longest and right < len(s):
    if s[right] not in seen:
      longest = max(longest, right - left + 1)
      seen.add(s[right])
      right += 1
    else:
      seen.remove(s[left])
      left += 1

  return longest


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("pwwkew"))