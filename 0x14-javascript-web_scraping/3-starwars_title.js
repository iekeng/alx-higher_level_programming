#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (err, res, bdy) => {
  if (err){
    console.error(err);
    return;
  }
  const body = JSON.parse(bdy);
  console.log(body.title);
})