#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) || (h > 0)) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      const s = 'X';
      console.log(s.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
