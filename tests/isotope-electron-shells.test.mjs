import { readFile } from 'node:fs/promises'
import assert from 'node:assert/strict'
import test from 'node:test'

const html = await readFile(new URL('../research/kitaev/isotope-electron-shells.html', import.meta.url), 'utf8')
const rows = [...html.matchAll(/<tr><th scope="row">([^<]+)<\/th>((?:<td>[^<]+<\/td>){8})<\/tr>/g)].map(([, name, cells]) => {
  const values = [...cells.matchAll(/<td>([^<]+)<\/td>/g)].map(([, value]) => value === '—' ? 0 : Number(value))
  return { name, protons: values[0], neutrons: values[1], shells: values.slice(2) }
})

test('covers all 80 elements with observationally stable isotopes, without radioactive-only elements', () => {
  assert.equal(rows.length, 96)
  assert.equal(new Set(rows.map(row => row.name)).size, 96)
  const expected = Array.from({ length: 82 }, (_, i) => i + 1).filter(z => z !== 43 && z !== 61)
  assert.deepEqual([...new Set(rows.map(row => row.protons))].sort((a, b) => a - b), expected)
})

test('nuclear mass numbers, electron totals, shell capacities and isotope-independent populations agree', () => {
  const populations = new Map()
  for (const { name, protons, neutrons, shells } of rows) {
    assert.equal(protons + neutrons, Number(name.split('-').at(-1)), name)
    assert.equal(shells.reduce((sum, n) => sum + n, 0), protons, name)
    assert(neutrons >= 0, name)
    shells.forEach((n, i) => assert(Number.isInteger(n) && n >= 0 && n <= 2 * (i + 1) ** 2, name))
    if (populations.has(protons)) assert.deepEqual(shells, populations.get(protons), name)
    populations.set(protons, shells)
  }
})

test('retains exceptional ground-state populations rather than sequential shell filling', () => {
  const expected = {
    'Chromium-52': [2, 8, 13, 1, 0, 0],
    'Copper-63': [2, 8, 18, 1, 0, 0],
    'Niobium-93': [2, 8, 18, 12, 1, 0],
    'Palladium-106': [2, 8, 18, 18, 0, 0],
    'Cerium-140': [2, 8, 18, 19, 9, 2],
    'Gadolinium-158': [2, 8, 18, 25, 9, 2],
    'Platinum-195': [2, 8, 18, 32, 17, 1],
    'Gold-197': [2, 8, 18, 32, 18, 1],
  }
  for (const [name, shells] of Object.entries(expected)) assert.deepEqual(rows.find(row => row.name === name)?.shells, shells, name)
})

test('keeps only table controls and data, with a 90vh table', () => {
  assert.doesNotMatch(html, /<(?:header|footer|caption|h1)\b/i)
  assert.match(html, /\.table-wrap \{[^}]*height: 90vh/)
})
