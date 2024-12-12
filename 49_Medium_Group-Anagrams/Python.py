from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
  obj = {}

  for i in range(len(strs)):
    string = ''.join(sorted(strs[i]))
    if string not in obj:
      obj[string] = []
    obj[string].append(strs[i])

  return list(obj.values())

print(groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))