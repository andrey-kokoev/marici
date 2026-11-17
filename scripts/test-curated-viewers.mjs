import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import http from 'node:http'
import path from 'node:path'
import { createHash } from 'node:crypto'
import { fileURLToPath } from 'node:url'
import { chromium, expect } from '@playwright/test'
import { fetchCuratedViewerAsset } from './curated-viewer-http-contract.mjs'

const root = fileURLToPath(new URL('../', import.meta.url))
const dist = path.join(root, 'website/.vitepress/dist')
const live = process.argv.includes('--live')
const outputArg = process.argv.indexOf('--output')
if (outputArg >= 0 && !process.argv[outputArg + 1]) throw Error('--output requires an ignored .ai directory')
const output = path.resolve(root, outputArg < 0 ? '.ai/curated-viewers' : process.argv[outputArg + 1])
assert(output.startsWith(path.join(root, '.ai') + path.sep), 'Evidence must stay under .ai/')
await fs.mkdir(output, { recursive: true })
const names = ['two-attractor-field', 'simplex-step-span']
const mode = live ? 'live' : 'local'
const hash = bytes => createHash('sha256').update(bytes).digest('hex')
async function files(directory, prefix = '') {
  const result = []
  for (const entry of await fs.readdir(directory, { withFileTypes: true })) {
    if (entry.isDirectory()) result.push(...await files(path.join(directory, entry.name), prefix + entry.name + '/'))
    else result.push(prefix + entry.name)
  }
  return result.sort()
}
const mime = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.png': 'image/png' }
let server, browser
const report = { schema: 'marici.curated-viewer-browser-evidence.v1', mode, status: 'running', captured_at: new Date().toISOString(), scope: 'Website bytes and Chromium software behavior only; not scientific or physical acceptance', assets: [], sources: {}, cases: [], errors: [], failed_responses: [], external_requests: [] }
try {
  let base = 'https://marici.andrei-kokoev.workers.dev'
  if (!live) {
    server = http.createServer(async (req, res) => {
      try {
        let file = path.resolve(dist, '.' + decodeURIComponent(new URL(req.url, 'http://local').pathname))
        assert(file.startsWith(dist + path.sep), 'Outside publication root')
        const stat = await fs.stat(file).catch(() => null)
        if (stat?.isDirectory()) file = path.join(file, 'index.html')
        else if (!stat && !path.extname(file)) file += '.html'
        res.setHeader('Content-Type', mime[path.extname(file)] || 'application/octet-stream')
        res.end(await fs.readFile(file))
      } catch { res.writeHead(404); res.end('Not found') }
    })
    await new Promise(resolve => server.listen(0, '127.0.0.1', resolve))
    base = `http://127.0.0.1:${server.address().port}`
  }
  report.base = base
  browser = await chromium.launch({ args: ['--enable-unsafe-swiftshader'] })
  report.chromium_version = browser.version()
  report.runtime = { node: process.version, platform: process.platform, arch: process.arch,
    playwright: JSON.parse(await fs.readFile(path.join(root, 'node_modules/@playwright/test/package.json'), 'utf8')).version }
  report.revision_basis = 'Recorded source/build byte digests; runner does not independently resolve a Git revision or assert a clean worktree'
  report.runner_sha256 = hash(await fs.readFile(fileURLToPath(import.meta.url)))
  report.sources['scripts/curated-viewer-http-contract.mjs'] = hash(await fs.readFile(path.join(root, 'scripts/curated-viewer-http-contract.mjs')))
  for (const name of names) {
    for (const file of await files(path.join(root, 'examples', name))) report.sources['examples/' + name + '/' + file] = hash(await fs.readFile(path.join(root, 'examples', name, file)))
    const publisher = 'scripts/prepare-' + name + '.mjs'
    report.sources[publisher] = hash(await fs.readFile(path.join(root, publisher)))
  }
  for (const file of ['package.json', 'pnpm-lock.yaml', 'website/experiments/field-and-shell-viewers.md']) report.sources[file] = hash(await fs.readFile(path.join(root, file)))
  function configure(page) {
    page.on('pageerror', error => report.errors.push(error.message))
    page.on('response', response => { if (response.status() >= 400) report.failed_responses.push(response.url()) })
    return page.route('**/*', route => {
      const url = new URL(route.request().url())
      if (['http:', 'https:'].includes(url.protocol) && url.origin !== base) { report.external_requests.push(url.href); return route.abort() }
      return route.continue()
    })
  }
  const probe = await browser.newPage()
  // Check every built viewer file, not just the entry HTML or observed requests.
  // In --live mode these must be the exact bytes of the reviewed local build.
  for (const name of names) for (const file of await files(path.join(dist, 'experiments', name))) {
    const route = '/experiments/' + name + '/' + file
    const { response, finalRoute, redirectStatus } = await fetchCuratedViewerAsset(probe.request, base, route)
    const expected = hash(await fs.readFile(path.join(dist, 'experiments', name, file)))
    assert.equal(hash(await response.body()), expected, 'Served bytes differ from reviewed build: ' + route)
    const type = response.headers()['content-type'] || ''
    if (file.endsWith('.js')) assert.match(type, /javascript/, route)
    if (file.endsWith('.css')) assert.match(type, /text\/css/, route)
    if (file.endsWith('.html')) assert.match(type, /text\/html/, route)
    report.assets.push({ route, final_route: finalRoute, redirect_status: redirectStatus, sha256: expected, status: 200 })
  }
  await probe.close()
  for (const viewport of [{ width: 1440, height: 1000 }, { width: 390, height: 844 }]) for (const name of names) {
    const page = await browser.newPage({ viewport })
    await configure(page)
    await page.goto(base + '/experiments/')
    await page.locator(`.construction-preview[href="/experiments/${name}/index.html"]`).click()
    await page.waitForFunction(() => window.ReferenceViewer?.snapshot().calls > 0)
    assert.equal(await page.evaluate(() => THREE.REVISION), '128')
    await expect(page.locator('#model-boundary')).toBeVisible()
    await expect(page.locator('#fallback')).toBeHidden()
    const camera = await page.evaluate(() => ReferenceViewer.snapshot().azimuth)
    await page.locator('#right').click()
    await page.waitForFunction(before => ReferenceViewer.snapshot().azimuth !== before, camera)
    await page.locator('#reset').click()
    if (name === 'two-attractor-field') {
      const initial = await page.evaluate(() => ReferenceViewer.snapshot())
      assert.equal(initial.running, false)
      assert.equal(initial.particles.length, 0)
      await page.locator('#weight-a').focus()
      await page.keyboard.press('ArrowRight')
      await page.waitForFunction(() => ReferenceViewer.snapshot().panel.weightA > 1)
      await page.locator('#damping').fill('0.1')
      const canvas = page.locator('canvas')
      await canvas.scrollIntoViewIfNeeded()
      const box = await canvas.boundingBox()
      await canvas.click({ position: { x: box.width * 0.4, y: box.height * 0.45 } })
      await page.waitForFunction(() => ReferenceViewer.snapshot().steps > 3)
      await page.locator('#run').click()
      await page.waitForFunction(() => !ReferenceViewer.snapshot().running)
      const paused = await page.evaluate(() => ReferenceViewer.snapshot())
      assert.equal(paused.particles.length, 1)
      assert(Math.hypot(paused.particles[0].vx, paused.particles[0].vy) > 0)
      await page.waitForTimeout(150)
      const steps = await page.evaluate(() => ReferenceViewer.snapshot().steps)
      await page.waitForTimeout(150)
      assert.equal(await page.evaluate(() => ReferenceViewer.snapshot().steps), steps)
    } else {
      assert.equal(await page.evaluate(() => ReferenceViewer.snapshot().triangleCount), 196)
      assert.equal(await page.evaluate(() => ReferenceViewer.snapshot().calls), 2)
      assert.equal(await page.locator('#step, #green-mode').count(), 0)
      await page.locator('#opacity').fill('0.18')
      await page.waitForFunction(() => ReferenceViewer.snapshot().opacity === 0.18)
    }
    // Mobile controls can scroll the scene offscreen; let its visibility-driven
    // renderer paint the current state before capture.
    await page.locator('canvas').scrollIntoViewIfNeeded()
    await page.waitForTimeout(100)
    assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), name + ': viewport overflow')
    assert(await page.locator('canvas').evaluate(canvas => canvas.width > 0 && canvas.height > 0))
    const screenshot = `${mode}-${name}-${viewport.width}.png`
    await page.screenshot({ path: path.join(output, screenshot), fullPage: true })
    if (name === 'two-attractor-field') {
      await page.locator('#reset-particles').click()
      await page.waitForFunction(() => ReferenceViewer.snapshot().particles.length === 0)
      assert.equal(await page.evaluate(() => ReferenceViewer.snapshot().steps), 0)
    }
    await page.getByRole('link', { name: 'Model guide and limits', exact: true }).click()
    await expect(page.getByRole('heading', { level: 1, name: /^Switched-attractor field and ESD7 shell/ })).toBeVisible()
    await page.close()
    const noJS = await browser.newPage({ viewport, javaScriptEnabled: false })
    await configure(noJS)
    await noJS.goto(base + '/experiments/' + name + '/index.html')
    await expect(noJS.locator('#model-boundary')).toBeVisible()
    await expect(noJS.locator('#fallback')).toBeVisible()
    await noJS.close()
    const noGL = await browser.newPage({ viewport })
    await configure(noGL)
    await noGL.addInitScript(() => { HTMLCanvasElement.prototype.getContext = () => null })
    await noGL.goto(base + '/experiments/' + name + '/index.html')
    await noGL.waitForFunction(() => window.ReferenceViewer?.snapshot().phase === 'fallback')
    await expect(noGL.locator('#fallback')).toBeVisible()
    await expect(noGL.locator('#model-boundary')).toBeVisible()
    await noGL.close()
    report.cases.push({ viewer: name, width: viewport.width, status: 'pass', controls: 'pass', no_js: 'pass', unavailable_webgl: 'pass', screenshot })
    console.log(`PASS ${mode} ${name} ${viewport.width}px: gallery, controls, disclosures, fallback and local assets`)
  }
  assert.deepEqual(report.errors, [])
  assert.deepEqual(report.failed_responses, [])
  assert.deepEqual(report.external_requests, [])
  report.status = 'pass'
} catch (error) {
  report.status = 'failed'
  report.failure = String(error.stack || error)
  throw error
} finally {
  report.finished_at = new Date().toISOString()
  await fs.writeFile(path.join(output, mode + '-viewer-evidence.json'), JSON.stringify(report, null, 2) + '\n')
  if (browser) await browser.close()
  if (server) await new Promise(resolve => server.close(resolve))
}
