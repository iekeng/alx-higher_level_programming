#!/usr/bin/node
//pipe from url to file

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request.get(url).pipe(fs.createWriteStream(file));
