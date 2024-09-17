const findMinDifference = (timePoints) => {
  let minutes = [];
  for (let time of timePoints) {
      let split = time.split(":");
      minutes.push(Number(split[0]) * 60 + Number(split[1]));
  }

  minutes.sort((a, b) => a - b);

  let minDiff = Infinity;
  for (let i = 0; i < timePoints.length - 1; i++) {
      minDiff = Math.min(minDiff, minutes[i + 1] - minutes[i])
  }

  return Math.min(minDiff, (minutes[0] + (1440 - minutes[minutes.length - 1])));
};

console.log(findMinDifference(["23:59","00:00"]));
console.log(findMinDifference(["00:00","23:59","00:00"]));
console.log(findMinDifference(["12:12","00:13"]));