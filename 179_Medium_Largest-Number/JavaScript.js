const largestNumber = (nums) => {
  let array = nums.map(String);
  array.sort((a,b) => {
      if (a + b > b + a) {
          return -1;
      } else {
          return 1;
      }
  });
  
  if (array[0] === "0") return "0";

  return array.join("");
};

console.log(largestNumber([10, 2])); //210
console.log(largestNumber([3, 30, 34, 5, 9])); //9534330
console.log(largestNumber([0,0])); //0
console.log(largestNumber([999999998,999999997,999999999])); //"999999999999999998999999997"