#!/usr/bin/env deno run --allow-read

import * as path from 'https://deno.land/std/path/mod.ts';

const aocNR = '04';

const dataPath = `./clemens/${aocNR}`;

console.log("Puzzel: ", path.basename(dataPath));

const MODE = 1;

const input = Deno.readTextFileSync(`${dataPath}/${aocNR}.txt`);
const t1 = Deno.readTextFileSync(`${dataPath}/t1.txt`);
const t2 = Deno.readTextFileSync(`${dataPath}/t2.txt`);


if (MODE<=1) {

    const p1 = (inp:string) => {
        return inp.split('\n').map((v) => v.split(':')).map((v) => {
            const twoLists = v[1].trim().split(' | ');
            const wins = twoLists[0].trim().split(/\s+/).map((v) => parseInt(v));
            const mine = twoLists[1].trim().split(/\s+/).map((v) => parseInt(v));

            let intersection = mine.filter(value => wins.includes(value));
            console.log(v[0], intersection , wins, mine);
            
            return [v[0], intersection.length > 0 ? Math.pow(2, intersection.length - 1): 0];
        }).reduce((p, v) => p + v[1], 0);
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
