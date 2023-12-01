// deno run --allow-read

import * as path from 'https://deno.land/std/path/mod.ts';
import { readLines } from "https://deno.land/std@0.208.0/io/read_lines.ts";

const aocNR = '00';

const fullPath:string = import.meta.url;
const __dirname = path.dirname(fullPath);
const __filename = path.basename(fullPath);

// const dataFile = `${__dirname}/${aocNR}.txt`;
const dataFile = `./${aocNR}/${aocNR}.txt`;

console.log("Running ", fullPath);
console.log("Data file", dataFile);

let total = 0;
const f = await Deno.open(dataFile);
for await (const l of readLines(f)) {
    console.log("l:", l);
    let number1 = 'x';
    let index = 0;
    while (number1 === 'x') {
        const c = l.at(index)
        if(c >= '0' && c <= '9') {
            number1 = c;
        } else {
            index++;
        }
    }

    index = l.length - 1;
    let number2 = 'x';
    while (number2 === "x") {
        const c = l.at(index);
        if (c >= "0" && c <= "9") {
            number2 = c;
        } else {
            index--;
        }
    }
    console.log("number1:", number1, "number2:", number2);
    console.log("combi:", number1 + number2);
    const lineSum = parseInt(number1 + number2);
    total += lineSum;
}

console.log("total:", total);

// console.log(text);

// lambda function countWords
// const countWords = (s: string): number => s.split(/\s+/g).filter(w => /[a-z0-9]/.test(w)).length;
// const count = countWords(text);
// console.log(`File ${dataFile} has ${count} words.`);

// console.log(text.replaceAll("\n",' '));
