#!/usr/bin/node
//writes to file

const fs = require('fs');

fs.writeFile (process.argv[2], process.argv[3], 'utf-8', (error) => {
    if (err) console.log(err);
});