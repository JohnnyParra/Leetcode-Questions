// const countConsistentStrings = (allowed, words) => {
//   let count = 0;
//   let obj = {};
//   for (let char of allowed) {
//     obj[char] = 1;
//   }

//   for (let string of words) {
//     if (isStringValid(string, obj)) {
//       count++;
//     }
//   }

//   return count;
// };

// const isStringValid = (word, allowed) => {
//   for (let char of word) {
//     if (!(char in allowed)) {
//       return false;
//     }
//   }

//   return true;
// }

var countConsistentStrings = function(allowed, words) {
  let count = 0;

  for (let string of words) {
    for (let char of string) {
      if (allowed.indexOf(char) < 0) {
        count++;
        break;
      }
    }
  }

  return words.length - count;
};

console.log(countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]));