#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const x = parseInt(process.argv[2]);
  const y = 'X';
  for (let i = 0; i < x; i++) {
    console.log(y.repeat(x));
  }
}
