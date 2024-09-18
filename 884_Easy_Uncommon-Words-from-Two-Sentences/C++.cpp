#include <iostream>
#include <sstream>
#include <vector>
#include <unordered_map>

std::vector<std::string> uncommonFromSentences(std::string s1, std::string s2) {
  std::string s = s1 + " " + s2;
  std::stringstream str(s);

  std::unordered_map<std::string, int> map;
  std::string temp;
  while(str >> temp) {
      map[temp]++;
  }

  std::vector<std::string> ans;
  for (auto [key, value]: map) {
      if(value == 1) {
          ans.push_back(key);
      }
  }

  return ans;
}

int main() {
  std::vector<std::string> test1 = uncommonFromSentences("this apple is sweet", "this apple is sour");
  std::vector<std::string> test2 =  uncommonFromSentences("apple apple", "banana");

  for (std::string word: test1) {
    std::cout << word << " ";
  }
  std::cout << std::endl;

  for (std::string word: test2) {
    std::cout << word << " ";
  }

  return 0;
}