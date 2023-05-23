#!/usr/bin/node

const request = require('request');

const filmsUrl = process.argv[2];
const personId = 18;
const personUrl = 'https://swapi-api.alx-tools.com/api/people/' + personId + '/';
let n = 0;

request(filmsUrl, (err, res, bdy) => {
  if (err) {
    console.log(err);
    return;
  }
  const body = JSON.parse(bdy);
  const results = body.results;
  for (const result of results) {
    for (const character of result.characters) {
      if (character === personUrl) {
        n = n + 1;
      }
    }
  }
  console.log(n);
});