#!/usr/bin/node
//logs movie title

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);
  const result = JSON.parse(body);
  console.log(result.title);
});
