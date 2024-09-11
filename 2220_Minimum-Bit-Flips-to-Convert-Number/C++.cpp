#include <iostream>

int minBitFlips(int start, int goal) {
  int x = start ^ goal;
  int count = 0;
  while (x > 0) {
    x = x & (x - 1);
    count++;
  }

  return count;
}

int main() {
  std::cout << minBitFlips(10,7) << std::endl;
  std::cout << minBitFlips(3, 4);

  return 0;
}