import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import path from 'node:path'
import http from 'node:http'
import { fileURLToPath } from 'node:url'
import { chromium, expect } from '@playwright/test'
import { prepareTetrahedralPlanes } from './prepare-tetrahedral-planes.mjs'
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
await prepareTetrahedralPlanes(root)
const publicRoot = path.join(root, 'website/public')
const server = http.createServer(async (req, res) => {
  try {
    let file = path.resolve(publicRoot, '.' + new URL(req.url, 'http://local').pathname)
    if (!file.startsWith(publicRoot + path.sep)) throw new Error('Bad path')
    if ((await fs.stat(file)).isDirectory()) file = path.join(file, 'index.html')
    res.setHeader('Content-Type', ({ '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css' })[path.extname(file)] || 'text/plain')
    res.end(await fs.readFile(file))
  } catch { res.writeHead(404); res.end('Not found') }
})
await new Promise(resolve => server.listen(0, '127.0.0.1', resolve))
const base = `http://127.0.0.1:${server.address().port}`
let browser
try {
  browser = await chromium.launch({ args: ['--enable-unsafe-swiftshader'] })
  for (const [route, viewport] of [
    ['/experiments/tetrahedron_planes_free_rotation.html', { width: 1440, height: 1000 }],
    ['/experiments/tetrahedral-planes/', { width: 390, height: 844 }],
  ]) {
    const page = await browser.newPage({ viewport })
    const errors = [], external = []
    page.on('pageerror', error => errors.push(error.message))
    await page.route('**/*', route => {
      if (new URL(route.request().url()).hostname !== '127.0.0.1') { external.push(route.request().url()); return route.abort() }
      return route.continue()
    })
    await page.goto(base + route)
    await expect(page.locator('html')).toHaveAttribute('data-view', 'webgl')
    await expect(page.locator('#status')).toContainText('4 vertices · 4 faces · 4 disks')
    await expect.poll(() => page.evaluate(() => TetrahedralPlanes.snapshot().calls)).toBeGreaterThan(0)
    const start = await page.evaluate(() => TetrahedralPlanes.snapshot())
    await page.locator('#opacity').fill('0.45')
    await expect(page.locator('#opacityOut')).toHaveText('0.45')
    await page.locator('#viewport').scrollIntoViewIfNeeded()
    await expect.poll(() => page.evaluate(() => TetrahedralPlanes.snapshot().opacity)).toBe(0.45)
    assert.equal(await page.evaluate(() => TetrahedralPlanes.snapshot().rebuilds), start.rebuilds)
    await page.locator('#repeats').fill('3')
    await expect(page.locator('#status')).toContainText('12 disks')
    await page.locator('#size').fill('4')
    await page.check('#showEdges'); await page.uncheck('#showSolid'); await page.uncheck('#showIntersections')
    await page.locator('#viewport').scrollIntoViewIfNeeded()
    await expect.poll(() => page.evaluate(() => TetrahedralPlanes.snapshot().segments)).toBe(0)
    await page.locator('#offset').fill('0')
    await expect(page.locator('#status')).toContainText('collapsed to a point')
    await expect(page.locator('#volume')).toContainText('0.0000')
    assert.equal(await page.evaluate(() => TetrahedralPlanes.snapshot().vertices), 1)
    await page.locator('#offset').fill('0.67')
    await page.locator('#roll-right').focus(); await page.keyboard.press('Enter')
    const rolled = await page.evaluate(() => TetrahedralPlanes.snapshot())
    assert.notDeepEqual(rolled.up, start.up)
    await page.locator('#right').click()
    assert.notDeepEqual(await page.evaluate(() => TetrahedralPlanes.snapshot().position), start.position)
    await page.locator('#zoom-in').click()
    assert.ok(await page.evaluate(() => TetrahedralPlanes.snapshot().zoom) > start.zoom)
    await page.locator('#reset').click()
    const reset = await page.evaluate(() => TetrahedralPlanes.snapshot())
    assert.deepEqual(reset.position, start.position); assert.deepEqual(reset.up, start.up); assert.equal(reset.zoom, start.zoom)
    // Actual pointer drag, not just state changes from keyboard buttons.
    await page.locator('#viewport').scrollIntoViewIfNeeded()
    const box = await page.locator('canvas').boundingBox()
    await page.mouse.move(box.x + box.width / 2, box.y + box.height / 2)
    await page.mouse.down(); await page.mouse.move(box.x + box.width / 2 + 60, box.y + box.height / 2 + 35, { steps: 8 }); await page.mouse.up()
    await expect.poll(() => page.evaluate(() => TetrahedralPlanes.snapshot().position)).not.toEqual(start.position)
    await expect.poll(() => page.evaluate(() => TetrahedralPlanes.snapshot().scheduled)).toBe(false)
    // Rebuilds must release old resources rather than grow the GPU geometry count.
    for (const distance of ['0.5', '0.9', '0.5', '0.9']) {
      await page.locator('#offset').fill(distance)
      await page.locator('#viewport').scrollIntoViewIfNeeded()
      await expect.poll(() => page.evaluate(() => TetrahedralPlanes.snapshot().scheduled)).toBe(false)
    }
    assert.ok(await page.evaluate(() => TetrahedralPlanes.snapshot().geometries) < 10)
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false)
    assert.deepEqual(errors, []); assert.deepEqual(external, [])
    await page.evaluate(() => TetrahedralPlanes.dispose())
    await expect(page.locator('#fallback')).toBeVisible(); await expect(page.locator('canvas')).toHaveCount(0)
    await page.close()
  }
  for (const mode of ['webgl-failure', 'context-loss', 'missing-renderer']) {
    const page = await browser.newPage()
    const errors = []; page.on('pageerror', error => errors.push(error.message))
    if (mode === 'missing-renderer') await page.route('**/assets/scene-*.js', route => route.abort())
    if (mode === 'webgl-failure') await page.addInitScript(() => {
      const get = HTMLCanvasElement.prototype.getContext
      HTMLCanvasElement.prototype.getContext = function (type, ...args) { return /webgl/.test(type) ? null : get.call(this, type, ...args) }
    })
    await page.goto(base + '/experiments/tetrahedral-planes/')
    if (mode === 'context-loss') {
      await expect(page.locator('html')).toHaveAttribute('data-view', 'webgl')
      await page.evaluate(() => document.querySelector('canvas').dispatchEvent(new Event('webglcontextlost', { cancelable: true })))
    }
    await expect(page.locator('html')).toHaveAttribute('data-view', 'fallback')
    await expect(page.locator('#fallback')).toBeVisible()
    await expect(page.locator('#reset')).toBeDisabled()
    assert.deepEqual(errors, []); await page.close()
  }
  const pending = await browser.newPage()
  let release, signalRequest
  const gate = new Promise(resolve => { release = resolve })
  const requested = new Promise(resolve => { signalRequest = resolve })
  await pending.route('**/assets/scene-*.js', async route => { signalRequest(); await gate; await route.continue() })
  await pending.goto(base + '/experiments/tetrahedral-planes/', { waitUntil: 'domcontentloaded' })
  await requested
  await pending.evaluate(() => TetrahedralPlanes.dispose())
  release(); await pending.waitForLoadState('networkidle')
  await expect(pending.locator('html')).toHaveAttribute('data-view', 'fallback')
  await expect(pending.locator('canvas')).toHaveCount(0)
  await pending.close()
  const context = await browser.newContext({ javaScriptEnabled: false })
  const page = await context.newPage()
  await page.goto(base + '/experiments/tetrahedron_planes_free_rotation.html')
  await expect(page.locator('#fallback')).toBeVisible()
  await expect(page.locator('#status')).toContainText('Static diagram shown')
  await context.close()
  console.log('PASS: Vue planes on original/canonical URLs; desktop/mobile; local bundles; all sliders/layers; collapse; keyboard roll/orbit/zoom/reset; pointer Trackball drag; idle rendering; bounded geometry resources; pending-start cancellation; WebGL/context-loss/missing-renderer/no-JS fallback.')
} finally {
  await browser?.close(); await new Promise(resolve => server.close(resolve))
}
