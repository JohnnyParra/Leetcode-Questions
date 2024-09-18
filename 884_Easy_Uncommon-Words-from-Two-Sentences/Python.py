from typing import List

def uncommonFromSentences(s1: str, s2: str) -> List[str]:
  arr = [*s1.split(" "), *s2.split(" ")]
  obj = {}

  for word in arr:
    if word not in obj:
      obj[word] = 0
    obj[word] += 1

  ans = []
  for key, value in obj.items():
    if value == 1:
      ans.append(key)

  return ans

print(uncommonFromSentences("this apple is sweet", "this apple is sour"))
print(uncommonFromSentences("apple apple", "banana"))