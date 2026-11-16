import fs from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer, resolveUserConfig } from 'vitepress'
import { normalizeNet } from '../src/conjecture-nets/model.js'
import { prepareConjectureNets } from './prepare-conjecture-nets.mjs'
import { synthesisPages, normalizePublicSynthesis, predictionTargets } from './public-synthesis-content.mjs'
import { preparePublicResearchFrontier } from './prepare-public-research-frontier.mjs'
import { prepareCurrentResearchProvenance } from './prepare-current-research-provenance.mjs'

const root = fileURLToPath(new URL('../', import.meta.url))
const read = file => fs.readFile(file, 'utf8')
const unescape = value => value.replaceAll('&amp;', '&').replaceAll('&quot;', '"').replaceAll('&#39;', "'")
export function navigationLinks(value, links = []) {
  if (Array.isArray(value)) for (const item of value) navigationLinks(item, links)
  else if (value && typeof value === 'object') {
    if (typeof value.link === 'string') links.push(value.link)
    for (const [key, item] of Object.entries(value)) if (key !== 'link') navigationLinks(item, links)
  }
  return links
}
const staticTags = html => html.replace(/<!--[\s\S]*?-->|<(script|style)\b[^>]*>[\s\S]*?<\/\1\s*>/gi, '').match(/<[a-z][^>]*>/gi) ?? []
export const staticHrefs = html => staticTags(html).flatMap(tag => [...tag.matchAll(/\shref=["']([^"']+)["']/g)].map(match => match[1]))
export function assertHeadingFragment(html, fragment, route) {
  const ids = new Set(staticTags(html).flatMap(tag => [...tag.matchAll(/\sid=["']([^"']+)["']/g)].map(match => unescape(match[1]))))
  if (!ids.has(decodeURIComponent(fragment))) throw Error(`Missing publication fragment: ${route}#${fragment}`)
}
export function assertBundledNetFragment(fragment, nets) {
  const state = new URLSearchParams(unescape(fragment))
  const id = state.get('net')
  const net = nets.find(item => item.id === id)
  if (!net) throw Error('Advertised net is not bundled: ' + id)
  if (state.has('node') && !net.nodes.some(node => node.id === state.get('node'))) throw Error('Advertised net node is absent: ' + state.get('node'))
  if (state.has('tab') && !['dependencies', 'ports'].includes(state.get('tab'))) throw Error('Invalid advertised net tab')
}
async function markdownFiles(dir) {
  const result = []
  for (const entry of await fs.readdir(dir, { withFileTypes: true })) {
    if (entry.isDirectory()) {
      if (['public', '.vitepress', 'ledger', 'node_modules'].includes(entry.name)) continue
      result.push(...await markdownFiles(path.join(dir, entry.name)))
    } else if (entry.name.endsWith('.md')) result.push(path.join(dir, entry.name))
  }
  return result
}

export async function checkPublicResearchCoverage(base = root, { built = false, contract: suppliedContract, navigation: suppliedNavigation } = {}) {
  const website = path.join(base, 'website')
  const contract = suppliedContract ?? JSON.parse(await read(path.join(base, 'config/public-research-coverage.v1.json')))
  if (contract.schema !== 'marici.public-research-coverage.v1' || contract.scientific_dispositions_modified !== false) throw Error('Invalid or overstated coverage contract')
  const inventory = JSON.parse(await read(path.join(base, 'src/data/results-physics.json')))
  if (new Set(inventory.map(item => item.slug)).size !== inventory.length) throw Error('Duplicate public result slug')
  for (const slug of contract.required_result_slugs) if (!inventory.some(item => item.slug === slug)) throw Error('Missing required result coverage: ' + slug)
  const provenance = await prepareCurrentResearchProvenance(base, { check: true })
  for (const slug of contract.required_result_slugs) if (!provenance.slugs.includes(slug)) throw Error('Required result has no pinned provenance: ' + slug)
  await preparePublicResearchFrontier(base, { check: true })
  for (const item of synthesisPages) {
    if (await read(path.join(base, item.target)) !== normalizePublicSynthesis(await read(path.join(base, item.source)))) throw Error('Stale synthesis projection: ' + item.target)
  }
  if (await read(path.join(website, 'research/predictions/index.md')) !== predictionTargets(await read(path.join(base, 'docs/landing-page.md')))) throw Error('Stale comparison-target projection')
  for (const item of inventory) {
    const page = await read(path.join(website, 'research/results', item.slug + '.md'))
    if (!page.includes(item.details) || !page.includes(`**${item.status}**`)) throw Error('Stale generated result: ' + item.slug)
  }
  const catalog = JSON.parse(await read(path.join(base, 'src/conjecture-nets/catalog.json')))
  if (JSON.stringify(catalog.nets.map(item => item.path)) !== JSON.stringify(contract.required_net_sources)) throw Error('Public net selection differs from reviewed coverage contract')
  await prepareConjectureNets(base, { check: true })
  if (built) for (const name of ['conjecture-nets.json', 'conjecture-nets.html']) {
    if (await read(path.join(website, '.vitepress/dist/experiments', name)) !== await read(path.join(website, 'public/experiments', name))) throw Error('Stale built public net: ' + name)
  }
  const snapshot = JSON.parse(await read(path.join(website, 'public/experiments/conjecture-nets.json')))
  if (JSON.stringify(snapshot.nets.map(item => item.source)) !== JSON.stringify(contract.required_net_sources)) throw Error('Stale or extra bundled public net')
  const nets = snapshot.nets.map(item => normalizeNet(item.contract, item.source, item.title))
  const [config] = await resolveUserConfig(website, 'build', 'production')
  const md = await createMarkdownRenderer(website, config.markdown ?? {})
  const nav = suppliedNavigation ?? navigationLinks({ nav: config.themeConfig?.nav, sidebar: config.themeConfig?.sidebar })
  const cache = new Map()
  let internalLinks = 0, fragments = 0, netLinks = 0
  async function resolvePage(pathname) {
    if (cache.has(pathname)) return cache.get(pathname)
    const relative = decodeURIComponent(pathname).replace(/^\/+/, '')
    if (relative.split('/').includes('..') || relative.includes('\\')) throw Error('Unsafe site path: ' + pathname)
    const plain = relative.replace(/\/$/, '')
    const candidates = []
    if (/\.[a-z0-9]+$/i.test(plain)) {
      candidates.push(path.join(website, 'public', plain))
      if (plain.endsWith('.html')) candidates.push(path.join(website, plain.slice(0, -5) + '.md'))
    } else {
      candidates.push(path.join(website, plain + '.md'), path.join(website, plain, 'index.md'), path.join(website, 'public', plain, 'index.html'))
    }
    let source
    for (const candidate of candidates) if ((await fs.stat(candidate).catch(() => null))?.isFile()) {
      if (source && source !== candidate) throw Error('Public route collision: ' + pathname)
      source = candidate
    }
    if (!source) throw Error('Missing public destination: ' + pathname)
    const isPublic = source.startsWith(path.join(website, 'public') + path.sep)
    const relativeOutput = path.relative(isPublic ? path.join(website, 'public') : website, source).replace(/\.md$/, '.html')
    const output = path.join(website, '.vitepress/dist', relativeOutput)
    if (built) await fs.access(output)
    const text = await read(built ? output : source)
    const html = built || !source.endsWith('.md') ? text : md.render(text)
    const result = { source, html }
    cache.set(pathname, result)
    return result
  }
  async function checkLink(href, current = '/') {
    href = unescape(href)
    if (/^(?:https?:|mailto:|tel:|data:)/i.test(href)) return
    const url = new URL(href, 'https://publication.invalid' + current)
    if (url.origin !== 'https://publication.invalid') throw Error('Unsupported publication link: ' + href)
    const page = await resolvePage(url.pathname)
    internalLinks++
    if (url.hash) {
      const fragment = url.hash.slice(1)
      if (fragment.startsWith('net=')) {
        if (url.pathname !== '/experiments/conjecture-nets.html') throw Error('Net fragment outside public explorer')
        assertBundledNetFragment(fragment, nets)
        netLinks++
      }
      else { assertHeadingFragment(page.html, fragment, url.pathname); fragments++ }
    }
  }
  for (const route of contract.required_pages) await checkLink(route)
  for (const entry of contract.frontier) await checkLink(entry.link)
  for (const link of nav) await checkLink(link)
  const files = await markdownFiles(website)
  for (const file of files) {
    const relative = path.relative(website, file).split(path.sep).join('/')
    const route = '/' + (relative.endsWith('/index.md') ? relative.slice(0, -8) : relative === 'index.md' ? '' : relative.slice(0, -3))
    const html = md.render(await read(file))
    for (const href of staticHrefs(html)) await checkLink(href, route)
  }
  return { scope: 'publication consistency only; not scientific verification', snapshot_id: contract.snapshot_id, built, markdown_pages: files.length, navigation_links: nav.length, internal_links: internalLinks, fragments, net_links: netLinks, required_results: contract.required_result_slugs.length, frontier_obligations: contract.frontier.length }
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  console.log(JSON.stringify(await checkPublicResearchCoverage(root, { built: process.argv.includes('--built') })))
}
