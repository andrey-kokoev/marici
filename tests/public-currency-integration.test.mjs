import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import path from 'node:path'
import test from 'node:test'
import { fileURLToPath } from 'node:url'
import { resolveUserConfig } from 'vitepress'
import { checkPublicResearchCoverage } from '../scripts/check-public-research-coverage.mjs'
import { loadPublicResearchCoverage } from '../scripts/public-research-coverage-config.mjs'
import { dispositionsFile, observeResearchMarkdown } from '../scripts/research-currency.mjs'

const root = fileURLToPath(new URL('../', import.meta.url))
const readJSON = async file => JSON.parse(await fs.readFile(path.join(root, file), 'utf8'))
const { contract } = await loadPublicResearchCoverage(root)

for (const slug of ['source-certified-coherent-assembly', 'ramsey-retained-assembly-coherence']) test('required coverage cannot omit selected completed result: ' + slug, async () => {
  await assert.rejects(checkPublicResearchCoverage(root, { contract: { ...contract, required_result_slugs: contract.required_result_slugs.filter(item => item !== slug) } }), /Selected provenance result omitted/)
})

test('duplicate required results cannot inflate selected coverage', async () => {
  await assert.rejects(checkPublicResearchCoverage(root, { contract: { ...contract, required_result_slugs: [...contract.required_result_slugs, contract.required_result_slugs[0]] } }), /Duplicate required result/)
})

test('actual public net IDs, not just source paths, are reviewed; held net is not promoted', async () => {
  assert.equal(contract.required_net_ids.length, 5)
  await assert.rejects(checkPublicResearchCoverage(root, { contract: { ...contract, required_net_ids: [...contract.required_net_ids, 'unreviewed-held-net'] } }), /Public net IDs differ/)
})

test('normal gate cannot drop or redirect the research disposition mechanism', async () => {
  for (const selection of [undefined, '../unreviewed.json']) await assert.rejects(checkPublicResearchCoverage(root, { contract: { ...contract, research_change_dispositions: selection } }), /research currency queue selection/)
})

test('reviewed routes cover both viewers, authored status guides and no public typed application', async () => {
  for (const route of ['/experiments/two-attractor-field/index.html', '/experiments/simplex-step-span/index.html', '/experiments/field-and-shell-viewers', '/experiments/typed-wiring-development', '/experiments/pe-net-publication-status', '/research/programs/ramsey-mathematical-programme-2026-11', '/research/provenance/current-results']) assert(contract.required_pages.includes(route), route)
  const typed = await readJSON('config/typed-editor-publication.v1.json')
  assert.equal(typed.disposition, 'development-only')
  assert.deepEqual(typed.public_application_routes, [])
  assert.equal(contract.research_change_dispositions, dispositionsFile)
})

// Real filesystem fixture, not a supplied observation or a skipped gate.
// Copy source bytes rather than hardlinking files that could affect owners.
async function publicationFixture(t) {
  const temp = await fs.mkdtemp(path.join(root, '.ai', 'currency-gate-'))
  t.after(() => fs.rm(temp, { recursive: true, force: true }))
  // Exercise the current reviewed tree, including subsequent exact-hash dispositions.
  // Copy bytes, never hardlink or modify the owners' live sources.
  const observed = await observeResearchMarkdown(root)
  const files = new Set(observed.map(item => item.path))
  for (const name of ['config/current-research-provenance.v1.json', 'config/current-research-provenance.v2.json']) {
    for (const entry of (await readJSON(name)).entries) for (const pin of [...entry.source_packets, ...entry.checker_sources]) files.add(pin.path)
  }
  for (const file of contract.required_net_sources) files.add(file)
  for (const file of ['docs/landing-page.md', 'docs/theory-page.md', 'docs/results-page.md', 'docs/system-characteristics.md', 'examples/isotope-wiring/index.html', 'src/data/results-physics.json']) files.add(file)
  const list = [...files]
  for (let offset = 0; offset < list.length; offset += 32) await Promise.all(list.slice(offset, offset + 32).map(async file => {
    await fs.mkdir(path.dirname(path.join(temp, file)), { recursive: true })
    await fs.copyFile(path.join(root, file), path.join(temp, file))
  }))
  await fs.cp(path.join(root, 'config'), path.join(temp, 'config'), { recursive: true })
  await fs.cp(path.join(root, 'src/conjecture-nets'), path.join(temp, 'src/conjecture-nets'), { recursive: true })
  const websiteFiles = []
  async function websiteFilesBelow(directory) {
    for (const entry of await fs.readdir(path.join(root, 'website', directory), { withFileTypes: true })) {
      const file = directory ? directory + '/' + entry.name : entry.name
      if (file === '.vitepress/config.mts' || file.startsWith('.vitepress/config.mts.timestamp-') || file.startsWith('.vitepress/cache') || file.startsWith('.vitepress/.temp') || file.startsWith('.vitepress/dist/assets') || entry.name === 'node_modules') continue
      if (entry.isDirectory()) await websiteFilesBelow(file)
      else if (entry.isFile()) websiteFiles.push('website/' + file)
    }
  }
  await websiteFilesBelow('')
  for (let offset = 0; offset < websiteFiles.length; offset += 32) await Promise.all(websiteFiles.slice(offset, offset + 32).map(async file => {
    await fs.mkdir(path.dirname(path.join(temp, file)), { recursive: true })
    await fs.copyFile(path.join(root, file), path.join(temp, file))
  }))
  const [config] = await resolveUserConfig(path.join(root, 'website'), 'build', 'production')
  // Keep the actual reviewed nav/sidebar and Markdown plugin. Do not import
  // the production config's publisher hook into a test fixture.
  await fs.writeFile(path.join(temp, 'website/.vitepress/config.mts'), `import { katex } from '@mdit/plugin-katex'\nexport default { markdown: { config(md) { md.use(katex, { throwOnError: false, strict: 'error' }) } }, themeConfig: ${JSON.stringify({ nav: config.themeConfig.nav, sidebar: config.themeConfig.sidebar })} }\n`)
  return temp
}

test('normal source AND built gates detect an actual undispositioned research addition without changing owners or selections', { timeout: 180000 }, async t => {
  const fixture = await publicationFixture(t)
  for (const built of [false, true]) {
    const result = await checkPublicResearchCoverage(fixture, { built })
    assert.equal(result.research_currency.unreviewed_changes, 0)
    assert.equal(result.required_results, 12)
    assert.deepEqual(result.reviewed_net_ids, contract.required_net_ids)
  }
  const synthetic = 'research/currency-negative-control/undispositioned-addition.md'
  await fs.mkdir(path.dirname(path.join(fixture, synthetic)), { recursive: true })
  await fs.writeFile(path.join(fixture, synthetic), '# Synthetic unreviewed source\n\nNo scientific claim or public selection.\n')
  for (const built of [false, true]) await assert.rejects(checkPublicResearchCoverage(fixture, { built }), error => error.message.includes('Unreviewed research Markdown: added ' + synthetic))
  await assert.rejects(fs.access(path.join(root, synthetic)), { code: 'ENOENT' })
  const queue = JSON.parse(await fs.readFile(path.join(fixture, dispositionsFile), 'utf8'))
  assert.equal(queue.inventory.length, 160)
  assert.deepEqual(queue.subsequent_dispositions, (await readJSON(dispositionsFile)).subsequent_dispositions)
  assert.equal(queue.scientific_dispositions_modified, false)
})
