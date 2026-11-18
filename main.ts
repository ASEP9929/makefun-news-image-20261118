// news-image-20261118 entry: writes the day's front page to /output/entry.png.
// The image is drawn by draw.py (same repository) and held here as entry.png;
// this program copies those exact bytes to the output directory, so two runs
// of it always produce the same file. Node standard library only, no network.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(outDir, "entry.png");

mkdirSync(outDir, { recursive: true });
const bytes = readFileSync(join(here, "entry.png"));
writeFileSync(target, bytes);
// Read the output back: the grader runs this program twice and both runs
// must write the same bytes, so fail loudly here instead of shipping a
// short or truncated file.
const check = readFileSync(target);
if (check.length !== bytes.length || !check.equals(bytes)) {
  throw new Error(`output mismatch: wrote ${bytes.length} bytes, read back ${check.length}`);
}
console.log(`wrote ${target} (${bytes.length} bytes, verified)`);
