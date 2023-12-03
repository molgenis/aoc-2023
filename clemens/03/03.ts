#!/usr/bin/env deno run --allow-read

import * as path from 'https://deno.land/std/path/mod.ts';

const aocNR = '03';

const dataPath = `./clemens/${aocNR}`;

console.log("Puzzel: ", path.basename(dataPath));

const MODE = 2;

const input = Deno.readTextFileSync(`${dataPath}/${aocNR}.txt`);
const t1 = Deno.readTextFileSync(`${dataPath}/t1.txt`);
const t2 = Deno.readTextFileSync(`${dataPath}/t2.txt`);

const range = (length:number, start = 0) => Array.from({ length: length }, (_, index) => start + index);
// console.log(range(4), range(3, -1))

const makeDicts = (inp:string) => {
    const numbers = {};
    const symbols = {}

    inp.split('\n').map((line,y,_a) => {
        const digitSequencePattern = /(\d+|[^0-9\.])/g;

        let match;
        while ((match = digitSequencePattern.exec(line)) !== null) {
            const sequence = match[0];
            const position = match.index;
            if (parseInt(sequence)) {
                sequence.split('').forEach((_v,x) => numbers[`${position+x},${y}`] = parseInt(sequence));
            }
            else {
                symbols[`${position},${y}`] = sequence;
            }
        }
    });
    return [symbols, numbers]
}

const buildSymbolTree = (inp) => {
    const [symbols, numbers] = makeDicts(inp);

    const tree = {};
    Object.keys(symbols).forEach((symbolPos) => {
        const [cx,cy] = symbolPos.split(',').map((v) => parseInt(v));
        for (let y of range(3, -1)) {
            let prevX = -1;
            for (let x of range(3, -1)) {
                if (x == 0 && y == 0) continue;
                const numberPos = `${cx+x},${cy+y}`;
                if (!numbers[numberPos]) continue;
                if (prevX == numbers[numberPos]) continue;

                tree[symbolPos] = tree[symbolPos] || {}
                tree[symbolPos][numberPos] = numbers[numberPos];
                prevX = numbers[numberPos];
            }
        }
        // console.log(symbolPos,cx,cy);
    });
    return [tree, symbols, numbers];
};

if (MODE<=1) {

    const p1 = (inp:string) => {
        const [tree, _] = buildSymbolTree(inp);

        const v = Object.keys(tree).map((symbolPos) => {
            const numbers = tree[symbolPos];
            return Object.keys(numbers).map((numberPos) => numbers[numberPos]).reduce((p,c) => p + c, 0);
        }).reduce((p,c) => p + c, 0);

        return v;
    }

    console.log(`t1 ${p1(t1)}`);
    console.log(`v1 ${p1(input)}`);
}

if (MODE<1 || MODE==2) {

    const p2 = (inp:string) => {
        const [tree, symbols] = buildSymbolTree(inp)
        return Object.keys(tree).map((symbolPos) => {
            if (symbols[symbolPos] !== '*') return 0;
            console.log(tree[symbolPos]);
            const values = Object.keys(tree[symbolPos]).map((objectPos) => tree[symbolPos][objectPos])
            if (values.length == 2) return values.reduce((p,v) => p*v, 1);
            return 0;
        }).reduce((p,v) => p + v,0);
    }
    console.log(`t2 ${p2(t2)}`);
    console.log(`v2 ${p2(input)}`);

}
