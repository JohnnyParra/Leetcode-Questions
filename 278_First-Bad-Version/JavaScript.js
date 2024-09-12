function isBadVersion(n) {
  if (n >= 4) {
    return true;
  } else {
    return false;
  }
} 

const FirstBadVersion= (n) => {
  let left = 0;
  while (left < n) {
    let mid = Math.floor((left + n) / 2);
    if (isBadVersion(mid)) {
      n = mid;
    } else {
      left = mid + 1;
    }
  }

  return n;
}

console.log(FirstBadVersion(5));