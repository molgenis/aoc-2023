#!/usr/bin/env deno run --allow-read

import * as path from 'https://deno.land/std/path/mod.ts';

const aocNR = '05';

const dataPath = `./clemens/${aocNR}`;

console.log("Puzzel: ", path.basename(dataPath));

const MODE = 2;

const input = Deno.readTextFileSync(`${dataPath}/${aocNR}.txt`);
const t1 = Deno.readTextFileSync(`${dataPath}/t1.txt`);
const t2 = Deno.readTextFileSync(`${dataPath}/t2.txt`);

class FromToMap {
    name = '';
    fromToRanges:FromToRange[] = [];

    forward = false;

    constructor(name:string) {
        this.name = name;
    }

    dropPassThrough() {
        this.fromToRanges = this.fromToRanges.filter((v) => !v.isPassThrough())
    }

    addPassThrough() {
        this.setForward(this.forward);
        let newRanges:FromToRange[] = [];
    }

    getOutput(n:number) {
        const options = this.fromToRanges.map((ftm) => ftm.sourceToDest(n))
        // console.log(n, options);
        let hasAny = options.filter((v) => v !== -1)
        if (hasAny.length>0) {
            return hasAny.shift();
        }
        return n;
    }

    getOutputFromRanges(r:Range[]): Range[] {
        let result:Range[] = [];

        const options = this.fromToRanges.map(
            (ftm) => ftm.sourceToDestByRanges(range))

        return []
    }

    setForward(f:boolean) {
        this.forward = f;
        this.fromToRanges.sort((a,b) => f ? (a.src < b.src ? 1 : -1) : (a.dest < b.dest ? 1 : -1))
    }
    addRange(ftr:FromToRange) {
        this.fromToRanges.push(ftr);
    }

    toString() {
        return `${this.name} \n  ` +this.fromToRanges.map((v)=> v.toString()).join("\n  ");
    }
}

class Range {
    start: number
    length: number

    constructor(start, length) {
        this.start = start
        this.length = length
    }
}

class FromToRange {
    dest!: number;
    src!: number;
    length!: number;

    isPassThrough():boolean {
        return this.src == this.dest
    }

    sourceToDest(src:number):number {
        if (this.src <= src && src < this.src + this.length) {
            return this.dest + src - this.src;
        }
        return -1
    }

    destToSource(dest:number):number {
        if (this.dest <= dest && dest < this.dest + this.length) {
            return this.src + dest - this.dest;
        }
        return -1
    }

    fromString(s:string) {
        [this.dest, this.src, this.length] = s.split(' ').map((v) => parseInt(v));
        return this;
    }

    toString() {
        return (this.isPassThrough()? "PASS: " : '') + `s:${this.src}-${this.src + this.length-1} d:${this.dest}-${this.dest+ this.length-1}`
    }
}


let maps: Map<string, FromToMap[]>= new Map();

const buildMap = (inp:string) => {
    maps = new Map();

    let lines = inp.split('\n');
    const seeds = lines.shift()?.split(': ')[1].split(' ').map((v) => parseInt(v));
    console.log("seeds", seeds);
    lines.shift();
    let name = lines.shift();
    maps[name] = new FromToMap(name);
    while (lines.length) {
        const line = lines.shift();
        // console.log(line)
        if (line !== "") {
            const ftr:FromToRange = (new FromToRange()).fromString(line);
            maps[name].addRange(ftr);
        }
        else if(line == '') {
            name = lines.shift();
            maps[name] = new FromToMap(name);
        }
    }

    const mapNames = Object.keys(maps);
    // console.log(mapNames.length, mapNames);
    return [seeds, maps, mapNames];
}
if (MODE<=1) {
    const p1 = (inp:string) => {
        const [seeds, maps, mapNames] = buildMap(inp)
        mapNames.forEach((v) => maps[v].setForward(true));
        mapNames.forEach((v) => {
            const ftm:FromToMap = maps[v];
            // console.log(`${ftm}`);
            // ftm.dropPassThrough();
            // console.log("PASS", `${ftm}`);
        });

        let seedLocations = seeds.map((seed) => {
            let sentinel = seed;
            mapNames.forEach((mapName) => {
                const ftm:FromToMap = maps[mapName];
                sentinel = ftm.getOutput(sentinel)
            });
            return [seed, sentinel];
        })
        // console.log(seedLocations);
        return seedLocations.map((v) => v[1]).sort((a,b) => a < b? -1: 1)[0]
    }


    console.log(`t1 ${p1(t1)}`);
    // 1241009111 too high
    console.log(`v1 ${p1(input)}`);
}

function seedsToRange(seeds:number[]): Range[] {
    const result:Range[] = [];
    while (seeds.length) {
        let start = seeds.shift();
        let length = seeds.shift();
        result.push(new Range(start, length));
    }
    return result
}

if (MODE<1 || MODE==2) {
    const p2 = (inp:string) => {
        const [seeds, maps, mapNames] = buildMap(inp)
        const seedRanges: Range[] = seedsToRange(seeds);

        mapNames.forEach((v) => maps[v].setForward(true));

        let seedLocations = seedRanges.map((seedRange) => {
            let sentinel:Range[] = [seedRange];
            mapNames.forEach((mapName) => {
                const ftm:FromToMap = maps[mapName];
                const sentinel = ftm.getOutputFromRanges(sentinel)
            });
            return [seedRange, sentinel];
        })
        // console.log(seedLocations);
        return seedLocations.map((v) => v[1]).sort((a,b) => a < b? -1: 1)[0]

    }
    console.log(`t2 ${p2(t2)}`);
    // console.log(`v2 ${p2(input)}`);

}
