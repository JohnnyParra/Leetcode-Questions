class MyCalenderTwo {
  constructor() {
    this.single = [];
    this.double = [];
  }

  book(start, end) {
    for (let [s, e] of this.double) {
      if (Math.max(s, start) < Math.min(e, end)) {
        return false;
      }
    }

  for (let [s, e] of this.single) {
      if (Math.max(s, start) < Math.min(e, end)) {
         this.double.push([Math.max(s, start), Math.min(e, end)]);
      }
  }

  this.single.push([start, end]);
  return true;
  }
}

const obj = new MyCalenderTwo();
console.log(obj.book(10, 20));
console.log(obj.book(50, 60));
console.log(obj.book(10, 40));
console.log(obj.book(5, 15));
console.log(obj.book(5, 10));
console.log(obj.book(25, 55));