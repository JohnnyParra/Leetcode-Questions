#include <iostream>

bool isBadVersion(int n) {
  if (n >= 4) {
    return true;
  } else {
    return false;
  }
}

int firstBadVersion(int n) {
  int left = 0;
  while (left < n) {
      int mid = left + ((n - left) / 2);
      if (isBadVersion(mid)) {
          n = mid;
      } else {
          left = mid + 1;
      }
  }
  return n;
}

int main() {
  std::cout << firstBadVersion(5);

  return 0;
}