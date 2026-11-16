import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import os from 'node:os'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import test from 'node:test'
import { prepareConjectureNets } from '../scripts/prepare-conjecture-nets.mjs'

const root = fileURLToPath(new URL('../', import.meta.url))
const read = relative => fs.readFile(path.join(root, relative), 'utf8')
const catalog = JSON.parse(await read('src/conjecture-nets/catalog.json'))
const development = JSON.parse(await read('src/conjecture-nets/development-catalog.json'))
const approved = [
  'research/scattering/seed-composition/contracts/seed-composition-work-net.v1.json',
  'research/scattering/low-energy/contracts/low-energy-scattering-work-net.v3.json',
  'research/nima/contracts/scattering-core-bridge-work-net.v7.json',
  'research/scattering/high-energy/contracts/high-energy-scattering-conjecture-net.v1.json',
  'research/nima/contracts/current-problem-conjecture-net.v1.json',
]
const held = 'research/strominger/contracts/persistent-seam-pe-conjecture-net.v1.json'

test('public selection stays at its reviewed source set while pending local selection is preserved', () => {
  assert.deepEqual(catalog.nets.map(net => net.path), approved)
  assert(development.nets.some(net => net.path === held))
  for (const source of approved) assert(development.nets.some(net => net.path === source))
})

test('public generated selection contains exactly its catalogue, not held local inputs', async () => {
  const snapshot = JSON.parse(await read('website/public/experiments/conjecture-nets.json'))
  assert.deepEqual(snapshot.nets.map(net => net.source), approved)
  assert(!snapshot.nets.some(net => net.source === held))
  assert.equal((await prepareConjectureNets(root, { check: true })).development, false)
})

test('public output is reproducible in a fixture with only public source contracts', async () => {
  const temp = await fs.mkdtemp(path.join(os.tmpdir(), 'marici-public-nets-'))
  try {
    const src = path.join(temp, 'src/conjecture-nets')
    await fs.mkdir(src, { recursive: true })
    for (const name of ['catalog.json', 'app.html', 'model.js', 'ports.js', 'port-view.js', 'app.js']) await fs.copyFile(path.join(root, 'src/conjecture-nets', name), path.join(src, name))
    for (const source of approved) {
      await fs.mkdir(path.dirname(path.join(temp, source)), { recursive: true })
      await fs.copyFile(path.join(root, source), path.join(temp, source))
    }
    await assert.rejects(fs.access(path.join(temp, held)), { code: 'ENOENT' })
    const result = await prepareConjectureNets(temp)
    assert.equal(result.nets, 5)
    await prepareConjectureNets(temp, { check: true })
    const output = path.join(temp, 'website/public/experiments/conjecture-nets.html')
    const before = await fs.readFile(output)

    const pending = 'research/development/fixture.json'
    await fs.mkdir(path.dirname(path.join(temp, pending)), { recursive: true })
    await fs.writeFile(path.join(temp, pending), JSON.stringify({ id: 'synthetic-pending', conjectures: [{ id: 'unreviewed-fixture' }] }))
    await fs.writeFile(path.join(src, 'development-catalog.json'), JSON.stringify({ nets: [...catalog.nets, { title: 'Synthetic local fixture', path: pending }] }))
    const local = await prepareConjectureNets(temp, { development: true })
    assert.equal(local.nets, 6)
    assert.equal(local.development, true)
    await fs.access(path.join(temp, '.ai/conjecture-nets/development/conjecture-nets.html'))
    assert((await fs.readFile(output)).equals(before), 'Development output overwrote public HTML')
    await fs.unlink(path.join(temp, pending))
    await prepareConjectureNets(temp, { check: true })
    await assert.rejects(prepareConjectureNets(temp, { development: true }), { code: 'ENOENT' })
    assert((await fs.readFile(output)).equals(before))
  } finally { await fs.rm(temp, { recursive: true, force: true }) }
})

test('gallery defers the held deep link and documentation names isolated development output', async () => {
  const gallery = await read('website/experiments/index.md')
  assert(!gallery.includes('#net=marici.persistent-seam-pe.v1'))
  assert(gallery.includes('not advertised as bundled public selections'))
  const docs = await read('docs/conjecture-net-explorer.md')
  assert(docs.includes('selection of five source contracts'))
  assert(docs.includes('--development'))
  assert(docs.includes('.ai/conjecture-nets/development/conjecture-nets.html'))
})
