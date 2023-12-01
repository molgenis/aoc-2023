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

const DEBUG=true;
const MODE=2;

const print = (s:string,i:number) => {
    if (MODE !== i) return;
    if (!DEBUG) return;
    console.log(s)
}

const p1 = (s:string) => print(s, 1);
const p2 = (s:string) => print(s, 2);

let input = Deno.readTextFileSync(dataFile);

let text = input;
// console.log(text);
let re = /[a-z]/gi;

let sum = 0;
text.split('\n').forEach(line => {
    line = line.replace(re, "");
    let num = parseInt(line[0]+line[line.length-1]);
    sum += num
    p1(`${num} ${line[0]+line[line.length-1]}`);
});
console.log("v1", sum);

sum = 0;
const digits = [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];

text = "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen";


function replaceFirstOccurrence(text:string) {

    text.split('\n').forEach(line => {
        const origLine = line;
        p2(origLine);
    
        // replace first occurrece of digit
        let minKey = "";
        do {
            let minValue = Infinity;
            minKey = "";
        
            digits.forEach((digit) => {
                const index = line.indexOf(digit);
                if (index> -1) {
                    if ( index < minValue) {
                        minValue = index;
                        minKey = digit;
                    }
                }
            });

            if (minKey !== "") {
                p2(`  ${minKey} : ${minValue} : ${line}`);
                const digitVal = digits.indexOf(minKey) + 1;
                p2(`  ${minKey} : ${digitVal}`);
                line = line.replace(minKey, `${digitVal}`);
            }

        } while (minKey !== "")

        line = line.replace(re, "");
        let num = parseInt(line[0]+line[line.length-1]);
        p2(`    ${origLine} -> ${num}`);
        sum += num;
        p2(`    ${num} : ${line[0]+line[line.length-1]}`);
    });
    // 53652 too low
    // 54110 too high
    console.log("v2", sum);
}

//replaceFirstOccurrence(text);

const replaceLetters = /[a-z]/gi;
text = input;
const v1 = text.split('\n').map((v,_i,_a) => { 
    const clean = v.replace(replaceLetters, '');
    const result = clean[0] + clean[clean.length-1];
    return parseInt(result);
}).reduce((p,c) => p + c, 0);
console.log(`v: ${v1}`);