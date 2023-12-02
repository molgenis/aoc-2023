#!/usr/bin/env deno run --allow-read

import * as path from 'https://deno.land/std/path/mod.ts';

const aocNR = '01';

const dataPath = `./clemens/${aocNR}`;

console.log("Puzzel: ", path.basename(dataPath));

const DEBUG = true;
const MODE = 2;

const print = (s:string,i:number) => {
    if (MODE !== i) return;
    if (!DEBUG) return;
    console.log(s)
}

let input = Deno.readTextFileSync(`${dataPath}/01.txt`);
let t1 = Deno.readTextFileSync(`${dataPath}/t1.txt`);
let t2 = Deno.readTextFileSync(`${dataPath}/t2.txt`);


const p1 = (inp:string) => {
    const replaceLetters = /[a-z]/gi;
    return inp.split('\n').map((v,_i,_a) => { 
    const clean = v.replace(replaceLetters, '');
    return parseInt(clean[0] + clean[clean.length-1]);
}).reduce((p,c) => p + c, 0);
}

if (MODE==1) {
    console.log(`t1 ${p1(t1)}`);
    console.log(`v1 ${p1(input)}`);
}
const digits = [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
let digitAndDigitWord = digits.map((v,i) => `${i+1}|${v}`).join('|');
console.log(digitAndDigitWord);

const p2 = (inp:string) => {
    const replaceLetters = RegExp(`(${digitAndDigitWord})`, "gi");
    return inp.split('\n').map((v,_i,_a) => { 
        const matched = v.match(replaceLetters);
        const fromWord = (v) => {if (digits.indexOf(v) > -1) v = digits.indexOf(v)+1; return v;}
        const f = fromWord(matched[0]);
        const l = fromWord(matched[matched.length-1]);
        return parseInt(`${f}${l}`);
    }).reduce((p,c) => p + c, 0);
}
console.log(`t2 ${p2(t2)}`);
console.log(`v2 ${p2(input)}`);

