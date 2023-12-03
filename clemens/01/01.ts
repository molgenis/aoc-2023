#!/usr/bin/env deno run --allow-read

import * as path from 'https://deno.land/std/path/mod.ts';

const aocNR = '01';

const dataPath = `./clemens/${aocNR}`;

console.log("Puzzel: ", path.basename(dataPath));

const MODE = 0;

const input = Deno.readTextFileSync(`${dataPath}/01.txt`);
const t1 = Deno.readTextFileSync(`${dataPath}/t1.txt`);
const t2 = Deno.readTextFileSync(`${dataPath}/t2.txt`);

const p1 = (inp:string) => {
    const replaceLetters = /[a-z]/gi;
    return inp.split('\n').map((v,_i,_a) => {
    const clean = v.replace(replaceLetters, '');
    return parseInt(clean[0] + clean[clean.length-1]);
}).reduce((p,c) => p + c, 0);
}

if (MODE <= 1) {
    console.log(`t1 ${p1(t1)}`);
    console.log(`v1 ${p1(input)}`);
}

const digitWords = [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
const digitAndDigitWord = digitWords.map((v,i) => `${i+1}|${v}`).join('|');

// Make sure not to fail on overlapping words ie `oneight`, `threeight`, `fiveight`, etc
const p2 = (inp:string) => {
    const replaceLetters = RegExp(`(${digitAndDigitWord})`, "g");
    return inp.split('\n').map((v) => {
        let matched = v.match(replaceLetters);
        if (!matched) return;
        const fromWord = (v:string) => {if (digitWords.indexOf(v) > -1) return digitWords.indexOf(v)+1; return v;}

        const firstMatch = matched[0];
        const lastMatch = matched[matched.length-1];
        const f = fromWord(firstMatch);
        let l = fromWord(lastMatch);

        // Test for overlap by research in trailing string
        let pos = v.lastIndexOf(lastMatch);
        let reSearch = v.slice(pos+1);
        matched = reSearch.match(replaceLetters);
        if (matched && matched.length>0) {
            //  console.log('\n>>', reSearch, l, ' XXXXXXXXXXX ', matched)
            l = fromWord(matched[0]);
        }
        return parseInt(`${f}${l}`);
    }).reduce((p,c) => p + c, 0);
}

if (MODE < 1 || MODE == 2) {
    // console.log(`t2 ${p2('oneight')}`);
    console.log(`t2 ${p2(t2)}`);
    // 54110 wrong
    // 54094 correct
    console.log(`v2 ${p2(input)}`);
}
