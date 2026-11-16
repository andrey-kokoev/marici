import assert from 'node:assert/strict'
import { readFile } from 'node:fs/promises'
import test from 'node:test'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer } from 'vitepress'

const read = path => readFile(new URL(`../${path}`, import.meta.url), 'utf8')
const config = await read('website/.vitepress/config.mts')
const results = await read('docs/results-page.md')
const published = await read('website/research/results/index.md')
const md = await createMarkdownRenderer(fileURLToPath(new URL('../', import.meta.url)))
const resultFragments = [...config.matchAll(/link:\s*'\/research\/results\/#([^']+)'/g)].map(match => match[1])
const headingIds = text => new Set([...md.render(text).matchAll(/<h[1-6]\b[^>]*\bid="([^"]+)"/g)].map(match => match[1]))

function checkFragments(text, fragments) {
  const ids = headingIds(text)
  for (const fragment of fragments) assert(ids.has(fragment), `Missing results heading: #${fragment}`)
}

const beltHeading = '## October 25: native N-cut belt attachment'
function beltSection(text) {
  const start = text.indexOf(beltHeading)
  assert(start >= 0, 'Missing belt results section')
  const next = text.indexOf('\n## ', start + beltHeading.length)
  return text.slice(start, next < 0 ? undefined : next).trim()
}

test('results sidebar fragments resolve to actual VitePress heading IDs', () => {
  assert(resultFragments.includes('october-25-native-n-cut-belt-attachment'))
  checkFragments(results, resultFragments)
  checkFragments(published, resultFragments)
})

test('fragment validation rejects a nonexistent heading', () => {
  assert.throws(() => checkFragments(results, ['not-a-published-heading']), /Missing results heading/)
})

test('generated belt result matches its canonical section and retains scope and provenance', () => {
  const section = beltSection(results)
  assert.equal(beltSection(published), section, 'Regenerate public results from docs/results-page.md')
  assert.match(section, /\/experiments\/native-belt-guide/)
  assert.match(section, /4331/)
  assert.match(section, /whole-cell/)
  assert.match(section, /field transport/)
  assert.match(section, /binding energy/)
  assert.match(section, /reported|reports/)
})
