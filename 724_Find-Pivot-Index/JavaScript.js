const pivotIndex = (nums) => {
  let rightSum = nums.reduce((acc, curr) => acc + curr, 0);
  let leftSum = 0;

  for (let i = 0; i < nums.length; i++) {
      rightSum -= nums[i];
      if (rightSum === leftSum) return i;
      leftSum += nums[i];
  }

  return -1;
};

console.log(pivotIndex([1, 7, 3, 6, 5, 6]));
console.log(pivotIndex([1, 2, 3]));