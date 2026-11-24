// Meme Sprint 3: AI Agent Goes Rogue — entry program (Node 22, stdlib only).
//
// The meme is drawn ahead of time by draw.py (PIL, DejaVu) and shipped
// beside this file as entry.png; the program just places it where the
// grader reads it. Deterministic: same bytes in, same bytes out.
//
// Local run:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { chmodSync, copyFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
if (!existsSync(outDir)) {
  mkdirSync(outDir, { recursive: true });
}
const dest = join(outDir, "entry.png");
copyFileSync(join(here, "entry.png"), dest);
chmodSync(dest, 0o644);
