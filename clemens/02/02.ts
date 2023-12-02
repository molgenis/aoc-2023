#!/usr/bin/env deno run --allow-read

import * as path from 'https://deno.land/std/path/mod.ts';

const aocNR = '02';

const dataPath = `./clemens/${aocNR}`;

console.log("Puzzel: ", path.basename(dataPath));

const MODE = 0;

let input = Deno.readTextFileSync(`${dataPath}/${aocNR}.txt`);
let t1 = Deno.readTextFileSync(`${dataPath}/t1.txt`);
let t2 = Deno.readTextFileSync(`${dataPath}/t2.txt`);

const makeDicts = (inp:string) => {
    return inp.split('\n').map((v,_i,_a) => {
        const dict = {};
        const [game, set] = v.split(':', 2);
        const gameId = parseInt(game.split(' ')[1]);
        const takes = set.split(';');
        takes.map((take) => {
            take.split(',').forEach((v) => {
                const [_, num, color] = v.split(' ');
                dict[color] = Math.max(dict[color] || 0, parseInt(num));
            })
        })
        return [gameId, dict];
    })
}

if (MODE<=1) {

    const can_play = { red:12, green:13, blue:14, };
    const p1 = (inp:string) => {

        return makeDicts(inp).map((v) => {
            const [gameId, dict] = v;
            const isValid = compareDicts(can_play, dict)

            if (isValid) return gameId;
            return 0;
        }).reduce((p,c) => p + c, 0);
    }

    console.log(`t1 ${p1(t1)}`);
    console.log(`v1 ${p1(input)}`);
}

if (MODE<1 || MODE==2) {

    const p2 = (inp:string) => {
        return makeDicts(inp).map((v) => {
            const [gameId, dict] = v;
            return dict.red * dict.green * dict.blue;        
        }).reduce((p,c) => p + c, 0);
    }
    console.log(`t2 ${p2(t2)}`);
    console.log(`v2 ${p2(input)}`);

}

// ChatGPT without editing
function compareDicts(dict1: { [key: string]: number }, dict2: { [key: string]: number }): boolean {
    for (let key in dict2) {
        if (!dict1.hasOwnProperty(key)) {
            return false; // dict2 has a key that dict1 doesn't
        }
        if (dict1[key] < dict2[key]) {
            return false; // dict1's value is less than dict2's
        }
    }
    return true; // all checks passed
}

// let dict1 = { red: 12, green: 13, blue: 14 };
// let dict2 = { red: 10, green: 13, blue: 14 };

// console.log(compareDicts(dict1, dict2)); // should print true
