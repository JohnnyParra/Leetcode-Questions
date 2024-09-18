#include <iostream>
#include <algorithm>
#include <vector>

std::string largestNumber(std::vector<int>& nums) {
  std::vector<std::string> arr;
  for (int num: nums) {
    arr.push_back(std::to_string(num));
  }

  sort(arr.begin(), arr.end(), [](std::string a, std::string b) {
    return a + b > b + a;
  });

  if (arr[0] == "0") {
    return "0";
  }

  std::string ans;
  for (std::string a: arr) {
    ans += a;
  }

  return ans;
}

int main() {
  std::vector<int> vector1 = {10, 2};
  std::vector<int> vector2 = {3, 30, 34, 5, 9};
  std::vector<int> vector3 = {0,0};
  std::vector<int> vector4 = {999999998,999999997,999999999};

  std::cout << largestNumber(vector1) << std::endl;
  std::cout << largestNumber(vector2) << std::endl;
  std::cout << largestNumber(vector3) << std::endl;
  std::cout << largestNumber(vector4) << std::endl;
  return 0;
}