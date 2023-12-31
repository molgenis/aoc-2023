# Advent of code 2023

We want to participate with https://adventofcode.com/2023/about using if you can TypeScript as we use it in our projects EMX2 and Armadillo.

## Typescript

We will use https://deno.com as that is a one shot develop and run tool. So TypeScript saffies don't need the whole plumbing of node, npm, etc.

### Download and install

- your favourite text editor Codium, VSCode has Deno support
- https://deno.land/manual/getting_started/installation (using brew, winget, etc)
- make sure deno does typescript by enabling config `deno.enable`
- you can configure to run the current file
- or use the shell `deno run 00/00.ts`
- https://code.visualstudio.com/docs/editor/variables-reference for your launch config

## Puzzles

The puzzles appear on https://adventofcode.com/2023 at 6:00 but we will gather together from 10:00-11:00 each day on our slack channel.

A puzzle has test values in the running text and a download containing the real puzzel data.

Each day you have 2 challenges. The second part has new text and tests.

To keep organised make a 2-digit day folder containing code and download.


## Preparation

- Register through your GitHub account by https://adventofcode.com/2023/auth/login
- You will be added to the private leaderboard of Clemens.
- To practice visit https://adventofcode.com/2023/events and choose a year

## Structure

We make named subtree like `<name>/<day>/<day>.ts + <data>.txt`.

See the current tree.

## Example

See `./example/00/00.ts`

## Code snippets

```typescript
for (const [index, value] of data.entries()) { codeblock }

const p1 = (inp:string) => { codeblock }

// build regex option string "1|one|2|two..."
const digitWords = [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
const digitAndDigitWord = digitWords.map((v,i) => `${i+1}|${v}`).join('|');
```
