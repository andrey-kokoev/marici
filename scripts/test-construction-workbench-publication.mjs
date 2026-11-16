import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import path from 'node:path'
import http from 'node:http'
import { fileURLToPath } from 'node:url'
import { chromium, expect } from '@playwright/test'

// Test the built publication, not a dev server or a separately rebuilt app.
const root = fileURLToPath(new URL('../', import.meta.url))
const dist = path.join(root, 'website/.vitepress/dist')
const mime = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png' }
const server = http.createServer(async (req, res) => {
  try {
    let file = path.resolve(dist, '.' + decodeURIComponent(new URL(req.url, 'http://local').pathname))
    if (!file.startsWith(dist + path.sep)) throw Error('Outside publication root')
    const stat = await fs.stat(file).catch(() => null)
    if (stat?.isDirectory()) file = path.join(file, 'index.html')
    else if (!stat && !path.extname(file)) file += '.html'
    res.setHeader('Content-Type', mime[path.extname(file)] || 'application/octet-stream')
    res.end(await fs.readFile(file))
  } catch { res.writeHead(404); res.end('Not found') }
})
await new Promise(resolve => server.listen(0, '127.0.0.1', resolve))
const base = `http://127.0.0.1:${server.address().port}`
let browser
const checked = []
try {
  browser = await chromium.launch({ args: ['--enable-unsafe-swiftshader'] })
  async function isolatedPage(viewport = { width: 1440, height: 1000 }) {
    const page = await browser.newPage({ viewport })
    const external = [], errors = [], failedLocal = []
    page.setDefaultTimeout(20000)
    page.on('pageerror', error => errors.push(error.message))
    page.on('response', response => { if (response.status() >= 400) failedLocal.push(response.url()) })
    await page.route('**/*', route => {
      const url = new URL(route.request().url())
      if (['http:', 'https:'].includes(url.protocol) && url.origin !== base) {
        external.push(url.href); return route.abort()
      }
      return route.continue()
    })
    return { page, external, errors, failedLocal }
  }
  async function assertClean(run) {
    assert.deepEqual(run.external, [], 'Bundle attempted an external runtime dependency')
    assert.deepEqual(run.errors, [], 'Browser execution error')
    assert.deepEqual(run.failedLocal, [], 'Missing published asset')
    await run.page.close()
  }
  for (const viewport of [{ width: 1440, height: 1000 }, { width: 390, height: 844 }]) {
    const run = await isolatedPage(viewport), { page } = run
    await page.goto(base + '/experiments/construction-workbench')
    await expect(page.getByRole('heading', { level: 1 })).toContainText('Construction workbench')
    assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth))
    await page.getByRole('link', { name: 'Open the bundled workbench', exact: true }).click()
    await page.waitForFunction(() => document.querySelector('#process-select') && !document.querySelector('#process-select').disabled)
    if (await page.locator('#close-scene').isVisible()) await page.locator('#close-scene').click()
    if (!(await page.locator('#process-select').isVisible())) await page.locator('#open-process').click()
    await page.selectOption('#process-select', 'beryllium-8')
    await page.check('#seed-show-reference')
    await expect(page.locator('.reference-strand')).toHaveCount(8)
    await page.selectOption('#process-select', 'beryllium-9')
    await page.selectOption('#beryllium-9-view', 'branching-seed')
    await page.check('#seed-show-reference')
    await expect(page.locator('.reference-strand')).toHaveCount(8)
    await expect(page.locator('#be9-central-sleeve')).toBeVisible()
    await page.uncheck('#be9-central-sleeve')
    await expect(page.locator('.reference-strand')).toHaveCount(8)
    await page.check('#be9-central-sleeve')
    await page.reload()
    await page.waitForFunction(() => globalThis.normalRayAudit?.processId === 'beryllium-9')
    if (await page.locator('#close-scene').isVisible()) await page.locator('#close-scene').click()
    if (!(await page.locator('#process-select').isVisible())) await page.locator('#open-process').click()
    await page.selectOption('#process-select', 'sulfur-32')
    for (const mode of ['retained-expansion', 'cellulation', 'hex-strands', 'wiring', 'channels', 'nnpe-composition']) {
      await page.selectOption('#sulfur-32-view', mode)
      await expect(page.locator('#sulfur-32-view')).toHaveValue(mode)
      await page.waitForTimeout(120)
      await expect(page.locator('#error')).toHaveCount(0)
    }
    await page.waitForFunction(() => globalThis.normalRayCompositionAudit?.components === 16)
    await page.getByRole('button', { name: 'S1:N', exact: true }).click()
    await page.getByRole('button', { name: 'S2:N', exact: true }).click()
    await page.waitForFunction(() => normalRayCompositionAudit.joins === 1)
    assert.deepEqual(await page.evaluate(() => normalRayCompositionAudit.inventory), { N: 16, P: 16 })
    await page.check('#nnpe-collapse')
    await page.click('#nnpe-undo')
    await page.waitForFunction(() => normalRayCompositionAudit.joins === 0)
    checked.push(`guide controls, persistence and NNPE retained inventory at ${viewport.width}px`)
    await assertClean(run)
  }
  const reference = await isolatedPage()
  await reference.page.goto(base + '/experiments/native-belt/cellulation.html')
  await reference.page.waitForFunction(() => globalThis.cellulationAudit?.cells > 0)
  checked.push('standalone whole-cell reference without external runtime requests')
  await assertClean(reference)
  for (const route of ['/experiments/threejs-reference/index.html', '/experiments/tetrahedral-planes/index.html', '/experiments/realization-lattice/index.html', '/experiments/minimal-data-packet/', '/experiments/retained-demos/relational-growth/index.html', '/experiments/retained-demos/paw-cycle/index.html', '/experiments/retained-demos/two-paws/index.html']) {
    const run = await isolatedPage()
    await run.page.goto(base + route)
    await expect(run.page.locator('canvas').first()).toBeVisible()
    await run.page.waitForTimeout(300)
    checked.push(`${route}: rendered with external requests blocked`)
    await assertClean(run)
  }
  for (const route of ['/experiments/threejs-reference/index.html', '/experiments/minimal-data-packet/']) {
    const fallback = await isolatedPage()
    await fallback.page.addInitScript(() => {
      const original = HTMLCanvasElement.prototype.getContext
      HTMLCanvasElement.prototype.getContext = function(type, ...args) {
        return /webgl/.test(type) ? null : original.call(this, type, ...args)
      }
    })
    await fallback.page.goto(base + route)
    await expect(fallback.page.locator('#fallback')).toBeVisible()
    checked.push(`${route}: static fallback with WebGL denied`)
    await assertClean(fallback)
  }
  for (const name of ['proton-neutron-assembly', 'three-arrow-receiver', 'potential-fold-explorer', 'electron-spinor-construction', 'fourth-construction', 'proton-source-assembly', 'retained-direction-observatory']) {
    const html = await fs.readFile(path.join(dist, 'experiments', name + '.html'), 'utf8')
    const map = JSON.parse(html.match(/<script\b[^>]*type="importmap"[^>]*>([\s\S]*?)<\/script>/)[1])
    assert(Object.values(map.imports).some(value => /^https:\/\//.test(value)), name)
  }
  checked.push('legacy CDN requirements confirmed from all seven published import maps')
  console.log(JSON.stringify({ status: 'passed', scope: 'Built website controls and offline-runtime packaging, not scientific verification', checked }, null, 2))
} finally {
  await browser?.close()
  await new Promise(resolve => server.close(resolve))
}
