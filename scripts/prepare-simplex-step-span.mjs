import fs from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { build } from 'vite'
import vue from '@vitejs/plugin-vue'

export async function prepareSimplexStepSpan(root) {
  const source = path.join(root, 'examples/simplex-step-span')
  const output = path.join(root, 'website/public/experiments/simplex-step-span')
  // This directory is owned exclusively by this publisher. Hashed assets are rebuilt.
  await build({
    configFile: false,
    root: source,
    base: './',
    plugins: [vue()],
    logLevel: 'warn',
    build: { outDir: output, emptyOutDir: true, target: 'es2022' },
  })
  await fs.mkdir(path.join(output, 'vendor'), { recursive: true })
  for (const name of ['three.min.js', 'OrbitControls.js', 'THREE-LICENSE.txt']) {
    await fs.copyFile(path.join(root, 'research/nima/demos/paw-cycle/vendor', name), path.join(output, 'vendor', name))
  }
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  await prepareSimplexStepSpan(path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..'))
}
