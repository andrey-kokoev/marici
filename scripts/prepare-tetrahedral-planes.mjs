import fs from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { build } from 'vite'
import vue from '@vitejs/plugin-vue'

export async function prepareTetrahedralPlanes(root) {
  const output = path.join(root, 'website/public/experiments/tetrahedral-planes')
  await build({ configFile: false, root: path.join(root, 'examples/tetrahedral-planes'),
    base: './', plugins: [vue()], logLevel: 'warn',
    build: { outDir: output, emptyOutDir: true, target: 'es2022' } })
  await fs.copyFile(path.join(root, 'node_modules/three/LICENSE'), path.join(output, 'THREE-LICENSE.txt'))
  await fs.copyFile(path.join(root, 'examples/tetrahedral-planes/preview.svg'), path.join(output, 'preview.svg'))
  // Preserve the original public URL, not just a redirect. Both pages use the same bundles.
  const html = await fs.readFile(path.join(output, 'index.html'), 'utf8')
  await fs.writeFile(path.join(root, 'website/public/experiments/tetrahedron_planes_free_rotation.html'),
    html.replaceAll('./assets/', './tetrahedral-planes/assets/'), 'utf8')
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  await prepareTetrahedralPlanes(path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..'))
}
