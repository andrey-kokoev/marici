import fs from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const root = fileURLToPath(new URL('../', import.meta.url))
const heldOutputRoots = ['apps/isotope-wiring', 'experiments/typed-isotope-wiring', 'experiments/isotope-wiring-app', 'experiments/isotope-wiring-typed']
const read = file => fs.readFile(file, 'utf8')
async function exists(file) {
  try { await fs.access(file); return true }
  catch (error) { if (error.code === 'ENOENT') return false; throw error }
}

export async function checkTypedEditorPublication(base = root, { built = false, selection } = {}) {
  const config = selection ?? JSON.parse(await read(path.join(base, 'config/typed-editor-publication.v1.json')))
  if (config.schema !== 'marici.typed-editor-publication.v1' || config.disposition !== 'development-only' || config.scientific_dispositions_modified !== false) throw Error('Unreviewed typed editor publication disposition')
  if (!Array.isArray(config.public_application_routes) || config.public_application_routes.length) throw Error('Development-only typed editor has public routes')
  if (config.application_source !== 'apps/isotope-wiring' || config.hosted_source !== 'examples/isotope-wiring/index.html' || config.public_explanation !== '/experiments/typed-wiring-development' || JSON.stringify(config.hosted_routes) !== JSON.stringify(['/experiments/isotope-wiring', '/experiments/isotope-wiring-standalone.html'])) throw Error('Hosted/development editor identity changed without selection review')
  const wrapper = await read(path.join(base, 'website/.vitepress/components/IsotopeWiring.vue'))
  if (!wrapper.includes("from '../../../examples/isotope-wiring/index.html?raw'") || !wrapper.includes(':srcdoc="source"') || wrapper.includes('apps/isotope-wiring')) throw Error('Hosted editor source changed: expected unchanged legacy iframe')
  const expected = await fs.readFile(path.join(base, config.hosted_source))
  const outputs = ['website/public', ...(built ? ['website/.vitepress/dist'] : [])]
  for (const output of outputs) {
    for (const held of heldOutputRoots) if (await exists(path.join(base, output, held))) throw Error('Development-only application output: ' + output + '/' + held)
    const actual = await fs.readFile(path.join(base, output, 'experiments/isotope-wiring-standalone.html'))
    if (!actual.equals(expected)) throw Error('Hosted standalone differs from the declared legacy source: ' + output)
  }
  return { disposition: config.disposition, built, public_application_routes: 0,
    scope: 'Publication selection, protected output paths and hosted source identity only; not application, Morse or physical verification' }
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  if (process.argv.slice(2).some(arg => arg !== '--built')) throw Error('Only --built is supported')
  console.log(JSON.stringify(await checkTypedEditorPublication(root, { built: process.argv.includes('--built') })))
}
