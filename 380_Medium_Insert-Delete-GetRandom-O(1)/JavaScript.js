class RandomizedSet {
  constructor() {
    this.indexes = {};
    this.data = [];
  }

  insert(val) {
    if(val in this.indexes) return false;

    this.data.push(val);
    this.indexes[val] = this.data.length - 1;
    return true;
  }

  remove(val) {
    if (!(val in this.indexes)) return false;

    const temp = this.data[this.data.length - 1];
    this.data[this.data.length - 1] = val;
    this.data[this.indexes[val]] = temp;
    this.data.pop();
    this.indexes[temp] = this.indexes[val];
    delete this.indexes[val];

    return true;
  }

  getRandom() {
    let randomIndex = Math.floor(Math.random() * (this.data.length));
    return this.data[randomIndex];
  }
}

const obj = new RandomizedSet();
let param_1 = obj.insert(1);
let param_2 = obj.remove(2);
let param_3 = obj.insert(2);
let param_4 = obj.getRandom();
let param_5 = obj.remove(1);
let param_6 = obj.insert(2);
let param_7 = obj.getRandom();
console.log([param_1,param_2,param_3,param_4,param_5,param_6,param_7]);