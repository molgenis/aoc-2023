// deno run --allow-read

import * as path from 'https://deno.land/std/path/mod.ts';

const aocNR = '00';

const fullPath:string = import.meta.url;
const __dirname = path.dirname(fullPath);
const __filename = path.basename(fullPath);

// const dataFile = `${__dirname}/${aocNR}.txt`;
const dataFile = `./${aocNR}/${aocNR}.txt`;

console.log("Running ", fullPath);
console.log("Data file", dataFile);

const decoder = new TextDecoder('utf-8');

const text = Deno.readTextFileSync(dataFile);
console.log(text);

// lambda function countWords
const countWords = (s: string): number => s.split(/\s+/g).filter(w => /[a-z0-9]/.test(w)).length;
const count = countWords(text);
console.log(`File ${dataFile} has ${count} words.`);

console.log(text.replaceAll("\n",' '));
