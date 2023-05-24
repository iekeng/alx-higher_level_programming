#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(argv[2], (err, res, body) => {
  if (err) {
    throw err;
  }
  fs.writeFile(argv[3], body, 'utf8', (err) => {
    if (err) {
      throw err;
    }
  });
});
