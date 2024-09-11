/* 
Key: use XOR to get the difference between the two numbers in bits
Time Complexity: O(n), n is the number of bits of the larger number
Space Complexity: 0(1)
*/

const minBitFlips = (start, goal) => {
  let xor = start ^ goal;
  let count = 0;
  while (xor > 0) {
      xor = xor & (xor - 1);
      count++;
  }

  return count;
}

console.log(minBitFlips(10, 7));
console.log(minBitFlips(3, 4));