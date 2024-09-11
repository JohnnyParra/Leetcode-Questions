const maxProfit = (prices) => {
  if (prices.length < 2) return 0;

  let left = 0;
  let right = 1;
  let max = 0;

  while (right < prices.length) {
      if (prices[left] < prices[right]) {
          max = Math.max(max, prices[right] - prices[left]);
      } else {
          left = right;
      }
      right++;
  }

  return max;
};

console.log(maxProfit([7, 1, 5, 3, 6, 4]));
console.log(maxProfit([7, 6, 4, 3, 1]));