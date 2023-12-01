#!/ deno run --allow-read

import * as path from 'https://deno.land/std/path/mod.ts';

const aocNR = '01';

const fullPath:string = import.meta.url;
const __dirname = path.dirname(fullPath);
const __filename = path.basename(fullPath);

// const dataFile = `${__dirname}/${aocNR}.txt`;
const dataFile = `./clemens/${aocNR}/${aocNR}.txt`;

console.log("Running ", fullPath);
console.log("Data file", dataFile);

const decoder = new TextDecoder('utf-8');

const text = Deno.readTextFileSync(dataFile);

console.log(text);
let re = /[a-z]/gi;

let sum = 0;
text.split('\n').forEach(line => {
    line = line.replace(re, "");
    let num = line[0]+line[line.length-1];
    let v = 0;
    v = parseInt(num);
    sum += v
    console.log(v, line[0]+line[line.length-1]);
});
console.log("v1", sum);

sum = 0
const digits = [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];

text.split('\n').forEach(line => {
    digits.forEach((digit, i) => {
        const dig = i+1
        line = line.replaceAll(digit, `${i+1}`)
    });
    line = line.replace(re, "");
    let num = line[0]+line[line.length-1];
    let v = 0;
    v = parseInt(num);
    sum += v
    console.log(v, line[0]+line[line.length-1]);
});
console.log("v2", sum);

