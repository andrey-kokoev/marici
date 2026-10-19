import { readFile, writeFile } from 'node:fs/promises';
import { previewSvg } from '../demos/minimal-data-packet/model.mjs';
import { loadFixture, electronSvg } from '../demos/minimal-data-packet/electron-model.mjs';

const demo = new URL('../demos/minimal-data-packet/', import.meta.url);
const trial = JSON.parse(await readFile(new URL('../results/electron-configuration-dimension-trial-v1.json', import.meta.url), 'utf8'));
const store = JSON.parse(await readFile(new URL('../results/electron_tetrahedral_spinor_store.json', import.meta.url), 'utf8'));
const fixture = loadFixture(trial, store);
await writeFile(new URL('preview.svg', demo), previewSvg());
await writeFile(new URL('tetra-preview.svg', demo), previewSvg(null, false, true, 'tetrahedral'));
await writeFile(new URL('electron-preview.svg', demo), electronSvg(fixture));
console.log('Generated lattice, tetrahedral and source-bound electron previews.');
