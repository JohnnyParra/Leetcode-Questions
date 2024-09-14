#include <iostream>
#include <vector>

std::vector<int> xorQueries(std::vector<int> arr, std::vector<std::vector<int>> queries) {
  std::vector<int> prefixSum = {arr[0]};
  for (int i = 1; i < arr.size(); i++) {
    prefixSum.push_back(arr[i] ^ prefixSum[i - 1]);
  }

  std::vector<int> ans = {};
  for (int i = 0; i < queries.size(); i++) {
    int left = queries[i][0];
    int right = queries[i][1];
    if (left == 0) {
      ans.push_back(prefixSum[right]);
    } else {
      ans.push_back(prefixSum[right] ^ prefixSum[left - 1]);
    }
  }

  return ans;
}

int main() {
  std::vector<int> arr = {1, 3, 4, 8};
  std::vector<std::vector<int>> queries = {{0,1},{1,2},{0,3},{3,3}};

  std::vector<int> solution = xorQueries(arr, queries);
  
  for (auto i: solution) {
    std::cout << i << ' ';
  }

  return 0;
}