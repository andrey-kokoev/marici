import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import path from 'node:path'
import { createHash } from 'node:crypto'
import { fileURLToPath } from 'node:url'
import test from 'node:test'
import http from 'node:http'
import { fetchCuratedViewerAsset } from '../scripts/curated-viewer-http-contract.mjs'
import { prepareTwoAttractorField } from '../scripts/prepare-two-attractor-field.mjs'
import { prepareSimplexStepSpan } from '../scripts/prepare-simplex-step-span.mjs'
const root = fileURLToPath(new URL('../', import.meta.url))
const read = file => fs.readFile(path.join(root, file), 'utf8')
const guideRoute = '/experiments/field-and-shell-viewers'
const names = ['two-attractor-field', 'simplex-step-span']
const routes = names.map(name => '/experiments/' + name + '/index.html')
const guide = () => read('website' + guideRoute + '.md')
function requireSelection(text) {
  for (const route of routes) assert(text.includes(route), 'Missing selected viewer: ' + route)
  for (const phrase of ['Public selection', 'selection is not deployment acceptance', 'not physical validation']) assert(text.includes(phrase), phrase)
}

test('two viewers are explicitly selected with local-versus-live and model boundaries', async () => {
  const text = await guide()
  requireSelection(text)
  for (const phrase of ['one active pole', 'both fields', '0.8', '0.6', 'not a guaranteed periodic orbit', 'numerical approximation', '100 vertices', '294 edges', '196 triangles', '49 triangles', 'not nuclear geometry', 'not a 23-step path']) assert(text.includes(phrase), phrase)
})

test('standalone source disclosures and guide navigation survive without JavaScript', async () => {
  for (const name of names) {
    const html = await read('examples/' + name + '/index.html')
    assert(html.includes('id="model-boundary"'), name)
    assert(html.includes(guideRoute), name)
    assert(html.includes('id="fallback"'), name)
    assert(!/<script[^>]+src=["']https?:/.test(html), name)
  }
})

test('gallery and navigation advertise both actual viewers rather than the retired path interpretation', async () => {
  const gallery = await read('website/experiments/index.md')
  for (const route of routes) assert(gallery.includes('href="' + route + '"'), route)
  assert(gallery.includes(guideRoute))
  assert((await read('website/.vitepress/config.mts')).includes(guideRoute))
  assert(gallery.includes('switched-attractor'))
  assert(gallery.includes('outer shell'))
})

test('selected source coverage requires the guide and both explicit HTML routes', async () => {
  const pointer = JSON.parse(await read('config/public-research-coverage.current.json'))
  const coverage = JSON.parse(await read(pointer.config))
  for (const route of [guideRoute, ...routes]) assert(coverage.required_pages.includes(route), route)
})

test('guide reproduction points at existing authoritative sources and publishers, not editable bundles', async () => {
  const text = await guide()
  for (const name of names) {
    for (const file of ['examples/' + name + '/README.md', 'scripts/prepare-' + name + '.mjs', 'tests/' + name + '.test.mjs']) {
      assert(text.includes(file), file)
      await fs.access(path.join(root, file))
    }
  }
  for (const phrase of ['local r128', 'HTTP', 'static fallback', 'not a complete offline bundle']) assert(text.includes(phrase), phrase)
})

test('missing selection and erasing the deployment boundary fail the publication control', async () => {
  const text = await guide()
  for (const route of routes) assert.throws(() => requireSelection(text.replaceAll(route, '')), /Missing selected viewer/)
  assert.throws(() => requireSelection(text.replaceAll('selection is not deployment acceptance', 'selection is deployment acceptance')), /deployment acceptance/)
})

async function manifest(directory, prefix = '') {
  const result = {}
  for (const item of await fs.readdir(directory, { withFileTypes: true })) {
    const key = prefix + item.name
    if (item.isDirectory()) Object.assign(result, await manifest(path.join(directory, item.name), key + '/'))
    else result[key] = createHash('sha256').update(await fs.readFile(path.join(directory, item.name))).digest('hex')
  }
  return Object.fromEntries(Object.entries(result).sort(([a], [b]) => a.localeCompare(b)))
}

test('both source publishers are byte-reproducible and remove stale assets in an isolated fixture', async () => {
  const fixture = await fs.mkdtemp(path.join(root, '.ai', 'viewer-publication-test-'))
  try {
    const vendor = 'research/nima/demos/paw-cycle/vendor'
    await fs.mkdir(path.join(fixture, vendor), { recursive: true })
    for (const file of ['three.min.js', 'OrbitControls.js', 'THREE-LICENSE.txt']) await fs.copyFile(path.join(root, vendor, file), path.join(fixture, vendor, file))
    for (const [i, prepare] of [prepareTwoAttractorField, prepareSimplexStepSpan].entries()) {
      const name = names[i]
      await fs.cp(path.join(root, 'examples', name), path.join(fixture, 'examples', name), { recursive: true })
      await prepare(fixture)
      const out = path.join(fixture, 'website/public/experiments', name)
      const first = await manifest(out)
      assert(first['index.html'] && first['vendor/THREE-LICENSE.txt'])
      assert(Object.keys(first).some(file => file.startsWith('assets/') && file.endsWith('.js')))
      await fs.writeFile(path.join(out, 'assets/obsolete.js'), 'stale sentinel')
      await prepare(fixture)
      assert.deepEqual(await manifest(out), first, name + ': source-driven bytes or stale cleanup drift')
      for (const file of ['three.min.js', 'OrbitControls.js', 'THREE-LICENSE.txt']) assert.equal(first['vendor/' + file], createHash('sha256').update(await fs.readFile(path.join(root, vendor, file))).digest('hex'))
    }
  } finally { await fs.rm(fixture, { recursive: true, force: true }) }
})

const response = (status, location) => ({ status: () => status, headers: () => ({ location }) })
const entry = '/experiments/two-attractor-field/index.html'
const origin = 'https://publication.invalid'
function requestFixture(responses) {
  const calls = []
  return { calls, async get(url, options) { calls.push({ url, options }); assert.equal(options.maxRedirects, 0); return responses.shift() } }
}

test('viewer HTTP contract retains direct 200 assets and their response bytes', async () => {
  const original = response(200)
  const request = requestFixture([original])
  const result = await fetchCuratedViewerAsset(request, origin, entry)
  assert.equal(result.response, original)
  assert.equal(result.finalRoute, entry)
  assert.equal(result.redirectStatus, null)
  assert.equal(request.calls.length, 1)
})

test('viewer HTTP contract accepts real canonical entry redirects but still fetches the final response', async t => {
  let code = 307
  const server = http.createServer((req, res) => {
    if (req.url === entry) { res.writeHead(code, { location: '/experiments/two-attractor-field/' }); res.end() }
    else if (req.url === '/experiments/two-attractor-field/') { res.writeHead(200); res.end('exact final bytes') }
    else { res.writeHead(404); res.end() }
  })
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve))
  t.after(() => new Promise(resolve => server.close(resolve)))
  const base = `http://127.0.0.1:${server.address().port}`
  const request = { async get(url, options) {
    assert.equal(options.maxRedirects, 0)
    const r = await fetch(url, { redirect: 'manual' })
    return { status: () => r.status, headers: () => Object.fromEntries(r.headers), body: () => r.text() }
  } }
  for (code of [301, 302, 307, 308]) {
    const result = await fetchCuratedViewerAsset(request, base, entry)
    assert.equal(result.redirectStatus, code)
    assert.equal(result.finalRoute, '/experiments/two-attractor-field/')
    assert.equal(await result.response.body(), 'exact final bytes')
  }
})

test('viewer HTTP contract rejects external redirects before following them', async () => {
  const request = requestFixture([response(307, 'https://outside.invalid/experiments/two-attractor-field/')])
  await assert.rejects(fetchCuratedViewerAsset(request, origin, entry), /canonical redirect destination/)
  assert.equal(request.calls.length, 1)
})

test('viewer HTTP contract rejects unrelated same-origin redirect destinations', async () => {
  const request = requestFixture([response(307, '/experiments/unreviewed/')])
  await assert.rejects(fetchCuratedViewerAsset(request, origin, entry), /canonical redirect destination/)
  assert.equal(request.calls.length, 1)
})

test('viewer HTTP contract rejects redirected JavaScript/vendor assets', async () => {
  const request = requestFixture([response(307, '/other.js')])
  await assert.rejects(fetchCuratedViewerAsset(request, origin, '/experiments/two-attractor-field/assets/app.js'), /Unexpected viewer asset redirect/)
  assert.equal(request.calls.length, 1)
})

test('viewer HTTP contract rejects redirect chains and final missing entries', async () => {
  for (const final of [response(307, '/again/'), response(404)]) {
    const request = requestFixture([response(307, '/experiments/two-attractor-field/'), final])
    await assert.rejects(fetchCuratedViewerAsset(request, origin, entry), /must end at 200/)
    assert.equal(request.calls.length, 2)
  }
})
