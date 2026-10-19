// Publication checks only: not a research proof or physical acceptance test.
import fs from 'node:fs'
import path from 'node:path'
import assert from 'node:assert/strict'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer } from 'vitepress'
import { katex } from '@mdit/plugin-katex'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const site = path.join(root, 'website')
const distMode = process.argv.includes('--dist')
const read = file => fs.readFileSync(file, 'utf8')
const exists = file => fs.existsSync(file)
const rows = JSON.parse(read(path.join(root, 'src/data/results-physics.json')))
assert.equal(new Set(rows.map(row => row.slug)).size, rows.length, 'Duplicate result slug')
const pages = [
  'index.md', 'research/theory/index.md', 'research/results/index.md',
  'research/system-characteristics/index.md', 'research/predictions/index.md',
  'research/programs/nima-amplitudes.md', 'explore/graph/index.md',
  'matter/standard-model-graph.md', 'about/team/index.md', 'experiments/index.md',
  'experiments/barycentric-witness.md',
  ...rows.map(row => `research/results/${row.slug}.md`),
]
const md = await createMarkdownRenderer(site, {
  config(md) { md.use(katex, { throwOnError: true, strict: 'error' }) },
})
const rendered = new Map()
function render(file) {
  if (!rendered.has(file)) {
    const html = md.render(read(file))
    assert(!/\bclass=["'][^"']*\bkatex-error\b/.test(html), `Source math error: ${file}`)
    rendered.set(file, html)
  }
  return rendered.get(file)
}
let links = 0, pointers = 0
for (const row of rows) {
  assert(!/\bEstablished\b/.test(row.status), `Overbroad physics status: ${row.slug}`)
  const text = read(path.join(site, `research/results/${row.slug}.md`))
  assert(text.includes(row.details) && text.includes(`**${row.status}**`), `Stale result: ${row.slug}`)
  assert(text.includes('not a new proof certificate or experimental confirmation'), row.slug)
  for (const pointer of (row.checker || '').matchAll(/research\/[^; ()]+\.py/g)) {
    assert(exists(path.join(root, pointer[0])), `Missing checker: ${pointer[0]}`); pointers++
  }
  for (const pointer of (row.result || '').split(';').map(s => s.trim()).filter(Boolean)) {
    assert(exists(path.join(root, pointer)), `Missing receipt: ${pointer}`); pointers++
  }
}
for (const page of pages) {
  const file = path.join(site, page)
  const text = read(file)
  render(file) // Strict math, including the authored summaries.
  const tokens = md.parse(text, {})
  for (const token of tokens.flatMap(token => token.children || [])) {
    if (token.type !== 'link_open') continue
    const href = token.attrGet('href')
    if (!href || /^(?:[a-z]+:|\/\/)/i.test(href)) continue
    const url = new URL(href, `https://local.invalid/${page.replace(/index\.md$/, '').replace(/\.md$/, '')}`)
    const pathname = decodeURIComponent(url.pathname).replace(/^\//, '')
    const candidates = [
      path.join(site, pathname || 'index.md'),
      path.join(site, `${pathname.replace(/\/$/, '')}.md`),
      path.join(site, pathname, 'index.md'),
      path.join(site, 'public', pathname),
      path.join(site, 'public', pathname, 'index.html'),
    ]
    const target = candidates.find(f => exists(f) && fs.statSync(f).isFile())
    assert(target, `${page}: missing link ${href}`)
    if (url.hash) {
      const html = target.endsWith('.md') ? render(target) : read(target)
      const ids = new Set([...html.matchAll(/\bid="([^"]+)"/g)].map(m => m[1]))
      assert(ids.has(decodeURIComponent(url.hash.slice(1))), `${page}: missing fragment ${href}`)
    }
    links++
  }
  if (distMode) {
    const output = path.join(site, '.vitepress/dist', page.replace(/\.md$/, '.html'))
    assert(exists(output), `Missing built page: ${output}`)
    const html = read(output)
    assert(!/\bclass=["'][^"']*\bkatex-error\b/.test(html), `Built math error: ${page}`)
    if (page.startsWith('research/results/') && page !== 'research/results/index.md') {
      assert(html.includes('not a new proof certificate or experimental confirmation'), `Stale built result: ${page}`)
      assert(!html.includes('<strong>Established</strong>'), `Overbroad built status: ${page}`)
    }
  }
}
assert(!read(path.join(site, 'research/predictions/index.md')).includes('**Falsified if:**'))
assert(read(path.join(site, '.vitepress/config.mts')).includes('ignoreDeadLinks: false'))
console.log(`Publication checks passed: ${pages.length} pages, ${rows.length} scoped results, ${links} local links/fragments, ${pointers} evidence paths${distMode ? ', built HTML' : ''}.`)
console.log('Evidence paths establish existence only, not fresh research verification or physical acceptance.')
