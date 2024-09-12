#include <iostream>
#include <vector>
#include <unordered_set>

int countConsistentStrings(std::string allowed, std::vector<std::string>& words) {
  int count = 0;
  std::unordered_set<char> allowedSet;

  for (char x: allowed) {
    allowedSet.insert(x);
  }

  for (std::string word: words) {
    for (char x: word) {
      if (allowedSet.find(x) == allowedSet.end()) {
        count++;
        break;
      }
    }
  }

  return words.size() - count;
}


int main() {
  std::vector<std::string> vector = {"ad","bd","aaab","baa","badab"};
  std::cout << countConsistentStrings("ab", vector);
  return 0;
}