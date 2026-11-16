import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import os from 'node:os'
import path from 'node:path'
import { createHash } from 'node:crypto'
import { fileURLToPath } from 'node:url'
import test from 'node:test'
import { prepareIsotopeReference } from '../scripts/prepare-isotope-reference.mjs'

const root = fileURLToPath(new URL('../', import.meta.url))
const read = relative => fs.readFile(path.join(root, relative), 'utf8')
const source = await fs.readFile(path.join(root, 'research/kitaev/isotope-electron-shells.html'))
const guide = await read('website/experiments/isotope-reference.md')

test('publisher preserves every source byte and records its SHA-256', async () => {
  const temp = await fs.mkdtemp(path.join(os.tmpdir(), 'marici-reference-'))
  try {
    const input = path.join(temp, 'research/kitaev/isotope-electron-shells.html')
    await fs.mkdir(path.dirname(input), { recursive: true })
    await fs.writeFile(input, source)
    const result = await prepareIsotopeReference(temp)
    const published = await fs.readFile(path.join(temp, result.target))
    const end = published.indexOf('-->\n') + 4
    assert(end > 4)
    assert(published.subarray(end).equals(source))
    assert.equal(result.sha256, createHash('sha256').update(source).digest('hex'))
    assert(published.subarray(0, end).toString().includes(result.sha256))
    await prepareIsotopeReference(temp, { check: true })
  } finally { await fs.rm(temp, { recursive: true, force: true }) }
})

test('copy check rejects missing output and source drift without refreshing either silently', async () => {
  const temp = await fs.mkdtemp(path.join(os.tmpdir(), 'marici-reference-drift-'))
  try {
    const input = path.join(temp, 'research/kitaev/isotope-electron-shells.html')
    await fs.mkdir(path.dirname(input), { recursive: true })
    await fs.writeFile(input, source)
    await assert.rejects(prepareIsotopeReference(temp, { check: true }), /Stale isotope reference/)
    const result = await prepareIsotopeReference(temp)
    const before = await fs.readFile(path.join(temp, result.target))
    await fs.appendFile(input, '\n<!-- changed source -->')
    await assert.rejects(prepareIsotopeReference(temp, { check: true }), /Stale isotope reference/)
    assert((await fs.readFile(path.join(temp, result.target))).equals(before))
  } finally { await fs.rm(temp, { recursive: true, force: true }) }
})

test('normal preparation publishes a fresh generated copy excluded from Git', async () => {
  await prepareIsotopeReference(root, { check: true })
  assert((await read('scripts/prepare-visualization-assets.mjs')).includes('await prepareIsotopeReference(root)'))
  assert((await read('.gitignore')).includes('/website/public/experiments/isotope-electron-shells.html'))
})

test('guide preserves source qualifications and separates reference coverage from models', () => {
  for (const phrase of ['96 selected isotope', '80 elements', 'uncertainties omitted', 'need not sum to 100%', 'no observed radioactive decay', 'half-life lower limit', 'not a measured decay lifetime', 'not a prediction', 'not refresh', 'NIST', 'ENSDF']) assert(guide.includes(phrase), phrase)
  assert(guide.includes('/experiments/isotope-wiring'))
  assert(guide.includes('/experiments/isotope-space'))
  assert(guide.includes('SHA-256'))
})

test('table and guide have different public filenames and all discovery surfaces link the guide', async () => {
  assert(guide.includes('/experiments/isotope-electron-shells.html'))
  for (const file of ['docs/landing-page.md', 'website/index.md', 'website/experiments/index.md', 'website/.vitepress/config.mts']) {
    assert((await read(file)).includes('/experiments/isotope-reference'), file)
  }
})
