import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { build } from 'vite';
import vue from '@vitejs/plugin-vue';

// Same publication and pinned vendor pair as prepare-threejs-reference.mjs.
export async function prepareTwoAttractorField(root) {
  const output = path.join(root, 'website/public/experiments/two-attractor-field');
  await build({ configFile: false, root: path.join(root, 'examples/two-attractor-field'), base: './', plugins: [vue()],
    logLevel: 'warn', build: { outDir: output, emptyOutDir: true, target: 'es2022' } });
  await fs.mkdir(path.join(output, 'vendor'), { recursive: true });
  for (const name of ['three.min.js', 'OrbitControls.js', 'THREE-LICENSE.txt']) {
    await fs.copyFile(path.join(root, 'research/nima/demos/paw-cycle/vendor', name), path.join(output, 'vendor', name));
  }
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url))
  await prepareTwoAttractorField(path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..'));
