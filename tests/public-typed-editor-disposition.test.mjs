import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import path from 'node:path'
import os from 'node:os'
import { fileURLToPath } from 'node:url'
import test from 'node:test'
const root = fileURLToPath(new URL('../', import.meta.url))
const read = file => fs.readFile(path.join(root, file), 'utf8')
const guideRoute = '/experiments/typed-wiring-development'
const guide = () => read('website' + guideRoute + '.md')
const selection = () => read('config/typed-editor-publication.v1.json').then(JSON.parse)
function requireBoundary(text) {
  for (const phrase of ['development-only', 'not the hosted iframe editor', 'not a computed smooth atlas', 'not a gradient flow', 'not experimental validation']) assert(text.includes(phrase), 'Missing editor distinction: ' + phrase)
}

test('typed application is explicitly development-only without changing its implementation scope', async () => {
  assert((await read('apps/isotope-wiring/README.md')).includes('Publication status: development-only'))
  const text = await guide()
  requireBoundary(text)
  for (const phrase of ['PWA', 'broader browser acceptance', 'not waived', 'not rerun']) assert(text.includes(phrase), phrase)
})

test('public explanation identifies both hosted surfaces and the exact unchanged implementation source', async () => {
  const text = await guide()
  for (const phrase of ['/experiments/isotope-wiring', '/experiments/isotope-wiring-standalone.html', 'examples/isotope-wiring/index.html', 'apps/isotope-wiring/', 'srcdoc', 'not interchangeable']) assert(text.includes(phrase), phrase)
  const wrapper = await read('website/.vitepress/components/IsotopeWiring.vue')
  assert(wrapper.includes("from '../../../examples/isotope-wiring/index.html?raw'"))
  assert(!wrapper.includes('apps/isotope-wiring'))
})

test('Morse explanation retains authored rotation, handle contraction and all nonpromotions', async () => {
  const text = await guide()
  for (const phrase of ['12 vertices and 26 edges', 'genus 5', 'six boundary', '−14', '15', '12 minima and 26 saddles', '10 minima and 24 saddles', 'edges 8 and 9', 'genus 0', 'sixteen boundary', 'not intrinsic', 'untwisted', 'non-junction crossings', 'no interior maxima', 'acyclic', 'necessary', 'not physical nuclear geometry']) assert(text.includes(phrase), phrase)
  for (const file of ['apps/isotope-wiring/MORSE_SURFACE.md', 'research/strominger/checkers/check_ne20_morse_surface.py']) {
    assert(text.includes(file))
    await fs.access(path.join(root, file))
  }
})

test('explanation is discoverable without exposing an application route or replacing pinned editor bytes', async () => {
  const text = await guide()
  for (const file of ['website/experiments/isotope-wiring-limitations.md', 'website/experiments/index.md', 'website/.vitepress/config.mts']) assert((await read(file)).includes(guideRoute), file)
  const config = await selection()
  assert.equal(config.disposition, 'development-only')
  assert.deepEqual(config.public_application_routes, [])
  assert.equal(config.public_explanation, guideRoute)
  const pointer = JSON.parse(await read('config/public-research-coverage.current.json'))
  assert(JSON.parse(await read(pointer.config)).required_pages.includes(guideRoute))
  assert((await read('scripts/check-public-research-coverage.mjs')).includes('checkTypedEditorPublication'))
  assert(text.includes('public explanation is not a published application'))
})

async function fixture() {
  const base = await fs.mkdtemp(path.join(os.tmpdir(), 'typed-editor-hold-'))
  for (const file of ['config/typed-editor-publication.v1.json', 'examples/isotope-wiring/index.html', 'website/.vitepress/components/IsotopeWiring.vue']) {
    await fs.mkdir(path.dirname(path.join(base, file)), { recursive: true })
    await fs.copyFile(path.join(root, file), path.join(base, file))
  }
  await fs.mkdir(path.join(base, 'website/public/experiments'), { recursive: true })
  await fs.copyFile(path.join(root, 'examples/isotope-wiring/index.html'), path.join(base, 'website/public/experiments/isotope-wiring-standalone.html'))
  return base
}

test('development hold checks actual hosted identity and rejects silent iframe replacement', async () => {
  const { checkTypedEditorPublication } = await import('../scripts/check-typed-editor-publication.mjs')
  const base = await fixture()
  try {
    assert.equal((await checkTypedEditorPublication(base)).disposition, 'development-only')
    const wrapper = path.join(base, 'website/.vitepress/components/IsotopeWiring.vue')
    await fs.writeFile(wrapper, '<iframe src="/apps/isotope-wiring/index.html"></iframe>')
    await assert.rejects(checkTypedEditorPublication(base), /Hosted editor source changed/)
  } finally { await fs.rm(base, { recursive: true, force: true }) }
})

test('false public selection, injected development output and stale standalone bytes fail without mutating production', async () => {
  const { checkTypedEditorPublication } = await import('../scripts/check-typed-editor-publication.mjs')
  const base = await fixture()
  try {
    const config = await selection()
    await assert.rejects(checkTypedEditorPublication(base, { selection: { ...config, public_application_routes: ['/apps/isotope-wiring'] } }), /Development-only typed editor has public routes/)
    const forbidden = path.join(base, 'website/public/apps/isotope-wiring')
    await fs.mkdir(forbidden, { recursive: true })
    await fs.writeFile(path.join(forbidden, 'index.html'), '<main>accidentally published application</main>')
    await assert.rejects(checkTypedEditorPublication(base), /Development-only application output/)
    await fs.rm(forbidden, { recursive: true })
    await fs.appendFile(path.join(base, 'website/public/experiments/isotope-wiring-standalone.html'), '\nchanged')
    await assert.rejects(checkTypedEditorPublication(base), /Hosted standalone differs/)
    await fs.copyFile(path.join(base, 'examples/isotope-wiring/index.html'), path.join(base, 'website/public/experiments/isotope-wiring-standalone.html'))
    await fs.mkdir(path.join(base, 'website/.vitepress/dist/experiments'), { recursive: true })
    await fs.copyFile(path.join(base, 'examples/isotope-wiring/index.html'), path.join(base, 'website/.vitepress/dist/experiments/isotope-wiring-standalone.html'))
    await fs.mkdir(path.join(base, 'website/.vitepress/dist/apps/isotope-wiring'), { recursive: true })
    await fs.writeFile(path.join(base, 'website/.vitepress/dist/apps/isotope-wiring/index.html'), 'accidental built app')
    await assert.rejects(checkTypedEditorPublication(base, { built: true }), /Development-only application output/)
  } finally { await fs.rm(base, { recursive: true, force: true }) }
})

test('removing the hosted/development/Morse distinctions fails the editorial control', async () => {
  const text = await guide()
  requireBoundary(text)
  for (const phrase of ['development-only', 'not the hosted iframe editor', 'not a computed smooth atlas', 'not a gradient flow']) assert.throws(() => requireBoundary(text.replaceAll(phrase, '')), /Missing editor distinction/)
})
