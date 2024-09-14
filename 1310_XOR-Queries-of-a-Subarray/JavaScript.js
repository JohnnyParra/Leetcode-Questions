const xorQueries = (arr, queries) => {
  let prefixSum = [arr[0]];
  for (let i = 1; i < arr.length; i++) {
    prefixSum.push(arr[i] ^ prefixSum[i - 1]);
  }

  let ans = [];
  for (let [left, right] of queries) {
    if (left === 0) {
      ans.push(prefixSum[right]);
    } else {
      ans.push(prefixSum[right] ^ prefixSum[left - 1]);
    }
  }

  return ans;
}

console.log(xorQueries([1, 3, 4, 8], [[0,1],[1,2],[0,3],[3,3]]));