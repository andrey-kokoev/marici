// Bounded verification of the authored public update and its website projection.
// Does not rebuild ledger pages or publish the site.
import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import MarkdownIt from 'markdown-it'
import { katex } from '@mdit/plugin-katex'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..')
const markdown = new MarkdownIt({ html: true }).use(katex, { throwOnError: true, strict: 'error' })
const pages = [
  ['docs/landing-page.md', 'website/index.md'],
  ['docs/theory-page.md', 'website/research/theory/index.md'],
  ['docs/results-page.md', 'website/research/results/index.md'],
]
// Match the existing authored-page projection, not a new publication convention.
function project(content) {
  return content
    .replaceAll('](/results/#bridges)', '](#postnikov-descent)')
    .replaceAll('](/results/#control)', '](#the-universe-as-a-feedback-system)')
    .replaceAll('](/results/#frontier)', '](/research/results/)')
    .replaceAll('](/results/', '](/research/results/')
    .replaceAll('](/theory/', '](/research/theory/')
    .replace(/\]\(\.\.\/research\/([^)]*)\)/g, (_, relative) => `](https://github.com/andrey-kokoev/marici/blob/main/research/${relative})`)
    .replaceAll('](theory-page.md', '](/research/theory/')
}
const sources = new Map()
let formulas = 0
for (const [source, target] of pages) {
  const text = await fs.readFile(path.join(root, source), 'utf8')
  sources.set(source, text)
  assert.equal(await fs.readFile(path.join(root, target), 'utf8'), project(text), `${target}: stale projection`)
  const html = markdown.render(text)
  assert(!html.includes('katex-error'), `${source}: math rendering error`)
  formulas += (html.match(/class="katex"/g) || []).length
}
const theory = sources.get('docs/theory-page.md')
const update = theory.split('## The single object and its three projections')[0]
const expectedHeadings = [
  'Finite-place incidence and physical descent',
  'Tate residue-to-valuation incidence',
  'The circuit-to-cosmology comparison certificate',
  'Green homotopy rather than an arbitrary absolute lift',
]
for (const heading of expectedHeadings) {
  assert(update.split(/\r?\n/).some(line => /^#{2,3} /.test(line) && line.endsWith(` ${heading}`)), `Missing heading: ${heading}`)
  const anchor = heading.toLowerCase().replace(/ /g, '-')
  const links = [...sources.values()].join('\n')
  assert(links.includes(`/theory/#${anchor}`), `No public navigation to ${anchor}`)
}
let evidenceLinks = 0
for (const match of update.matchAll(/\]\((\.\.\/research\/[^)]+)\)/g)) {
  await fs.access(path.resolve(root, 'docs', match[1]))
  evidenceLinks++
}
for (const match of update.matchAll(/https:\/\/github\.com\/andrey-kokoev\/marici\/blob\/main\/(src\/ledger\/[^)]+)/g)) {
  await fs.access(path.join(root, decodeURIComponent(match[1])))
  evidenceLinks++
}
assert(!update.includes('\\boxed'), 'Mathematical boxes are not permitted')
console.log(`PASS: ${pages.length} authored/generated page pairs; ${formulas} KaTeX formulas; ${expectedHeadings.length} linked headings; ${evidenceLinks} local evidence targets.`)
console.log('Scope: projection consistency, math rendering, navigation and evidence-path existence; not scientific admission or deployment.')
