#!/usr/bin/env deno run --allow-read

import * as path from 'https://deno.land/std/path/mod.ts';
import { stripTrailingSeparators } from 'https://deno.land/std@0.208.0/path/_common/strip_trailing_separators.ts';

const aocNR = '06';

const dataPath = `./clemens/${aocNR}`;

console.log("Puzzel: ", path.basename(dataPath));

const input = Deno.readTextFileSync(`${dataPath}/${aocNR}.txt`);
const t1 = Deno.readTextFileSync(`${dataPath}/t1.txt`);
const t2 = Deno.readTextFileSync(`${dataPath}/t2.txt`);

const MODE = 0;

const p1 = (inp:string) => {
    const r = inp.split('\n').map((v) => [v.split(':')[0],v.split(':')[1].trim().split(/\s+/g)])
    const times = r[0][1]
    const distances = r[1][1]
    let asTable = times.map((item, index) => [item, distances[index]]);

    // console.log(asTable)
    return winners(asTable)
}
const winners = (asTable) => {
    return asTable.map((v) => {
        const [time, distance] = v;
        const t = [];
        for (let i:number = 1; i<time; i++) {
            const d = (time-i)*i;
            // console.log(i, d)
            t.push([i,d])
        }
        const max = t.reduce((p,c) => c[1]>p[1] ? c : p)[1]
        const count = t.filter((v) => v[1] > distance).length
        // console.log(max, count)
        return count
    }).reduce((p,c)=> p*c)
}

if (MODE<=1) {
    console.log(`t1 ${p1(t1)}`);
    console.log(`v1 ${p1(input)}`);
}

const p2 = (inp:string) => {
    const r = inp.split('\n').map((v) => [v.split(':')[0],v.split(':')[1].replaceAll(' ', '')])
    const time:number = parseInt(r[0][1]);
    const distance = parseInt(r[1][1]);
    const asTable = [[time, distance]]

    // distance(x) = (time-x)*x
    // f(x) = -x*x + time * x > distance
    // -b +- sqrt( b*b - 4 * a * c) / 2 a
    const solver = [
        (-time - Math.sqrt(time * time - 4 * ( -1 * -distance)))/ (2*-1),
        (-time + Math.sqrt(time * time - 4 * ( -1 * -distance)))/ (2*-1),
    ]
    return Math.floor(solver[0] - Math.ceil(solver[1]))
}

if (MODE<1 || MODE==2) {
    console.log(`t2 ${p2(t2)}`);
    console.log(`v2 ${p2(input)}`);

}

console.log("== END ==".repeat(10))