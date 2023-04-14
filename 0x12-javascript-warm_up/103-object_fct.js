#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = function (n) {
  n = this.value;
  n++;
}
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
