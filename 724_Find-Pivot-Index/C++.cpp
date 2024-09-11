#include <iostream>
#include <vector>

int pivotIndex(std::vector<int>& nums) {
  int rightSum = 0;
  int leftSum = 0;

  for (int num : nums) {
    rightSum += num;
  }

  for (int i = 0; i < nums.size(); i++) {
    rightSum -= nums[i];
    if (rightSum == leftSum) {
        return i;
    }
    leftSum += nums[i];
  }
  
  return -1;
}

int main() {
  std::vector<int> nums1 = {1, 7, 3, 6, 5, 6};
  std::vector<int> nums2 = {1, 2, 3};

  std::cout << pivotIndex(nums1) << std::endl;
  std::cout << pivotIndex(nums2);
  return 0;
}