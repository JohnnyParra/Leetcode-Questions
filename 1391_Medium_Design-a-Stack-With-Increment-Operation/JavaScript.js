class CustomStack {
  // constructor(maxSize) {
  //   this.stack = [];
  //   this.maxSize = maxSize;
  // }
  constructor(maxSize) {
    this.stack = [];
    this.inc = [];
    this.maxSize = maxSize;
  }

  size() { //O(1)
    return this.stack.length;
  }

  // push(val) { //O(1)
  //   if (this.size() < this.maxSize) {
  //     this.stack.push(val);
  //   }
  // }
  push(val) {//O(1)
    if (this.size() < this.maxSize) {
      this.stack.push(val);
      this.inc.push(0);
    }
  }

  // pop() { //O(1)
  //   if (this.size() > 0) {
  //     return this.stack.pop();
  //   }
  //   return -1;
  // }
  pop() { //O(1)
    if (this.size() > 0) {
      let increment = this.inc.pop();
      this.inc[this.size() - 2] += increment;
      return this.stack.pop() + increment;
    }
    return -1;
  }

  // increment(k, val) { //O(n)
  //   let i = 0;
  //   while (i < k && i < this.stack.length) {
  //     this.stack[i] += val;
  //     i++;
  //   }
  // }
  increment(k, val) { //O(1)
    let index = Math.min(k, this.size()) - 1;
    if (index >= 0 ){
      this.inc[index] += val;
    }
  }
}

const obj = new CustomStack(3);
obj.push(1);
obj.push(2);
console.log(obj.pop());
obj.push(2);
obj.push(3);
obj.increment(5, 100);
obj.increment(2, 100);
console.log(obj.pop());
console.log(obj.pop());
console.log(obj.pop());
console.log(obj.pop());