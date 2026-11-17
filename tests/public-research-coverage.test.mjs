import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import os from 'node:os'
import path from 'node:path'
import test from 'node:test'
import { fileURLToPath } from 'node:url'
import { normalizeNet } from '../src/conjecture-nets/model.js'
import { checkPublicResearchCoverage, assertHeadingFragment, assertBundledNetFragment, navigationLinks, staticHrefs } from '../scripts/check-public-research-coverage.mjs'
import { renderPublicResearchFrontier, preparePublicResearchFrontier } from '../scripts/prepare-public-research-frontier.mjs'
import { synthesisPages } from '../scripts/public-synthesis-content.mjs'
import { loadPublicResearchCoverage } from '../scripts/public-research-coverage-config.mjs'

const root = fileURLToPath(new URL('../', import.meta.url))
const read = file => fs.readFile(new URL('../' + file, import.meta.url), 'utf8')
const { contract } = await loadPublicResearchCoverage(root)
const snapshot = JSON.parse(await read('website/public/experiments/conjecture-nets.json'))
const nets = snapshot.nets.map(item => normalizeNet(item.contract, item.source, item.title))

test('frontier covers twelve selected results without reopening the completed assemblies', async () => {
  assert.equal(contract.frontier.length, 14)
  assert.equal(contract.scientific_dispositions_modified, false)
  for (const slug of contract.required_result_slugs) assert(contract.frontier.some(entry => entry.link === '/research/results/' + slug || entry.reported_completed?.includes('/research/results/' + slug)), slug)
  const text = renderPublicResearchFrontier(contract)
  assert(text.includes('**As of:**'))
  assert(text.includes('not a live workboard'))
  assert(text.includes('not a queue of waiting research leaves'))
  assert(text.includes('These are website consistency tests'))
  for (const entry of contract.frontier) assert(entry.first_missing.length > 40 && entry.acceptance.length > 40)
  await preparePublicResearchFrontier(root, { check: true })
  for (const file of ['docs/landing-page.md', 'docs/results-page.md', 'website/.vitepress/config.mts']) assert((await read(file)).includes('/research/frontier/current'), file)
})

test('frontier generation rejects absent acceptance, duplicate obligations and promoted dispositions', () => {
  const incomplete = structuredClone(contract)
  incomplete.frontier[0].acceptance = ''
  assert.throws(() => renderPublicResearchFrontier(incomplete), /Incomplete/)
  const duplicate = structuredClone(contract)
  duplicate.frontier.push(duplicate.frontier[0])
  assert.throws(() => renderPublicResearchFrontier(duplicate), /duplicate/)
  assert.throws(() => renderPublicResearchFrontier({ ...contract, scientific_dispositions_modified: true }), /Invalid/)
})

test('source coverage validates resolved navigation, static content links, all generated projections and five curated nets', async () => {
  const result = await checkPublicResearchCoverage(root)
  assert.equal(result.required_results, 12)
  assert.equal(result.research_currency.audited_files, 160)
  assert.equal(result.research_currency.unreviewed_changes, 0)
  assert.equal(result.research_currency.disposition_counts['pending-source-review'], 110)
  assert.deepEqual(result.reviewed_net_ids, contract.required_net_ids)
  assert.equal(result.frontier_obligations, 14)
  assert(result.markdown_pages >= 75)
  assert(result.navigation_links >= 55)
  assert(result.fragments > 400)
  assert(result.internal_links > 700)
  assert(result.scope.includes('not scientific verification'))
})

test('coverage rejects a declared but absent result before accepting publication', async () => {
  await assert.rejects(checkPublicResearchCoverage(root, { contract: { ...contract, required_result_slugs: [...contract.required_result_slugs, 'absent-source-result'] } }), /Missing required result coverage/)
})

test('coverage rejects a real-route navigation link with a nonexistent fragment', async () => {
  await assert.rejects(checkPublicResearchCoverage(root, { navigation: ['/research/theory/#absent-maintenance-heading'] }), /Missing publication fragment/)
})

test('net deep-link controls accept actual IDs and reject unbundled IDs, absent nodes and unsupported tabs', () => {
  const state = new URLSearchParams({ net: nets[0].id, node: nets[0].nodes[0].id, tab: 'ports' })
  assertBundledNetFragment(state.toString(), nets)
  assert.throws(() => assertBundledNetFragment('net=not-published', nets), /not bundled/)
  assert.throws(() => assertBundledNetFragment(new URLSearchParams({ net: nets[0].id, node: 'missing-node' }).toString(), nets), /node is absent/)
  assert.throws(() => assertBundledNetFragment(new URLSearchParams({ net: nets[0].id, tab: 'invented' }).toString(), nets), /Invalid advertised net tab/)
})

test('fragment checks decode Unicode IDs and do not mistake prose, comments or Vue bindings for anchors', () => {
  assertHeadingFragment('<h2 id="a—b">Title</h2>', 'a%E2%80%94b', '/page')
  for (const html of ['<h2 :id="not-static">Title</h2>', '<p>prose id="not-static"</p>', '<!-- <h2 id="not-static"> -->']) assert.throws(() => assertHeadingFragment(html, 'not-static', '/page'), /Missing publication fragment/)
  assert.deepEqual(staticHrefs('<a href="/actual">a</a><a :href="`/dynamic/${id}`">b</a><!-- <a href="/comment"> --><script>const s=\'<a href="/script">\'</script>'), ['/actual'])
  assert.deepEqual(navigationLinks([{ link: '/one' }, { items: [{ link: '/two' }] }]), ['/one', '/two'])
})

test('coverage rejects stale canonical projections and stale frontier output without modifying repository files', async () => {
  const temp = await fs.mkdtemp(path.join(os.tmpdir(), 'marici-coverage-'))
  try {
    const provenance = JSON.parse(await read('config/current-research-provenance.v1.json'))
    const successor = JSON.parse(await read('config/current-research-provenance.v2.json'))
    const files = new Set([
      'config/public-research-coverage.current.json', 'config/public-research-coverage.v1.json',
      'config/public-research-coverage.v2.json', 'config/current-research-provenance.v1.json',
      'config/current-research-provenance.v2.json', 'config/research-provenance-selection.v2.json',
      'website/public/research/provenance/current-results.v2.json',
      'website/public/research/frontier/current.json',
      'website/public/research/frontier/public-research-frontier-v1.json',
      'website/public/research/frontier/public-research-frontier-v2.json',
      'src/data/results-physics.json', 'website/public/research/provenance/current-results.v1.json',
      'website/research/frontier/current.md',
      ...synthesisPages.flatMap(item => [item.source, item.target]),
      ...provenance.entries.flatMap(entry => [...entry.source_packets, ...entry.checker_sources].map(pin => pin.path)),
      ...successor.entries.flatMap(entry => [...entry.source_packets, ...entry.checker_sources].map(pin => pin.path)),
    ])
    for (const file of files) {
      await fs.mkdir(path.dirname(path.join(temp, file)), { recursive: true })
      await fs.copyFile(path.join(root, file), path.join(temp, file))
    }
    const builtFrontier = path.join(temp, 'website/.vitepress/dist/research/frontier')
    await fs.mkdir(builtFrontier, { recursive: true })
    await fs.writeFile(path.join(builtFrontier, 'current.json'), await read('website/public/research/frontier/current.json') + '\n')
    await assert.rejects(checkPublicResearchCoverage(temp, { built: true }), /Stale built frontier snapshot/)
    for (const name of ['current.json', 'public-research-frontier-v1.json', 'public-research-frontier-v2.json']) await fs.copyFile(path.join(temp, 'website/public/research/frontier', name), path.join(builtFrontier, name))
    const builtProvenance = path.join(temp, 'website/.vitepress/dist/research/provenance')
    await fs.mkdir(builtProvenance, { recursive: true })
    await fs.copyFile(path.join(root, 'website/public/research/provenance/current-results.v1.json'), path.join(builtProvenance, 'current-results.v1.json'))
    await fs.writeFile(path.join(builtProvenance, 'current-results.v2.json'), '{}')
    await assert.rejects(checkPublicResearchCoverage(temp, { built: true }), /Stale built provenance snapshot/)
    await fs.appendFile(path.join(temp, synthesisPages[0].target), '\nStale output')
    await assert.rejects(checkPublicResearchCoverage(temp), /Stale synthesis projection/)
    await fs.copyFile(path.join(root, synthesisPages[0].target), path.join(temp, synthesisPages[0].target))
    await fs.appendFile(path.join(temp, 'website/research/frontier/current.md'), '\nStale frontier')
    await assert.rejects(checkPublicResearchCoverage(temp), /Stale generated research frontier/)
  } finally { await fs.rm(temp, { recursive: true, force: true }) }
})

test('coverage rejects a changed public net selection without contract review', async () => {
  await assert.rejects(checkPublicResearchCoverage(root, { contract: { ...contract, required_net_sources: [...contract.required_net_sources, 'research/unreviewed.json'] } }), /Public net selection differs/)
})
