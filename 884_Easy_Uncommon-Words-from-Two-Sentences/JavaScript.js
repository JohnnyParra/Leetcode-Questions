const uncommonFromSentences = (s1, s2) => {
  let arr1 = s1.split(" ");
  let arr2 = s2.split(" ");

  let map = new Map();
  let i = 0;
  while (i < arr1.length || i < arr2.length) {
      if(arr1[i]) {
          map.set(arr1[i], (map.get(arr1[i]) || 0) + 1)
      }
      if(arr2[i]) {
          map.set(arr2[i], (map.get(arr2[i]) || 0) + 1)
      }
      i++;
  }

  let ans = [];
  for (let [key, value] of map) {
      if (value === 1) {
          ans.push(key);
      }
  }

  return ans;
};

console.log(uncommonFromSentences("this apple is sweet", "this apple is sour"));
console.log(uncommonFromSentences("apple apple", "banana"));