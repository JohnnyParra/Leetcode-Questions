#include <iostream>
#include <vector>

int maxProfit(std::vector<int>& prices) {
  int left = 0;
  int right = 1;
  int maxProfit = 0;

  while (right < prices.size()) {
    if (prices[left] < prices[right]) {
      maxProfit = std::max(maxProfit, prices[right] - prices[left]);
    } else {
      left = right;
    }
    right++;
  }

  return maxProfit;
}

int main() {
  std::vector<int> prices1 = {7, 1, 5, 3, 6, 4};

  std::cout << maxProfit(prices1);

  return 0;
}