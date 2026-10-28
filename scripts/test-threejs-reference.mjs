import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import path from 'node:path'
import http from 'node:http'
import { fileURLToPath } from 'node:url'
import { chromium, expect } from '@playwright/test'
import { prepareThreejsReference } from './prepare-threejs-reference.mjs'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
await prepareThreejsReference(root)
const publicRoot = path.join(root, 'website/public')
const mime = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css' }
const server = http.createServer(async (req, res) => {
  try {
    let file = path.resolve(publicRoot, '.' + new URL(req.url, 'http://local').pathname)
    if (!file.startsWith(publicRoot + path.sep)) throw new Error('Bad path')
    if ((await fs.stat(file)).isDirectory()) file = path.join(file, 'index.html')
    res.setHeader('Content-Type', mime[path.extname(file)] || 'text/plain')
    res.end(await fs.readFile(file))
  } catch { res.writeHead(404); res.end('Not found') }
})
await new Promise(resolve => server.listen(0, '127.0.0.1', resolve))
const url = `http://127.0.0.1:${server.address().port}/experiments/threejs-reference/`
let browser
try {
  browser = await chromium.launch({ args: ['--enable-unsafe-swiftshader'] })
  for (const viewport of [{ width: 1440, height: 900 }, { width: 390, height: 844 }]) {
    const page = await browser.newPage({ viewport, reducedMotion: 'reduce' })
    const errors = [], external = []
    page.on('pageerror', error => errors.push(error.message))
    await page.route('**/*', route => {
      if (new URL(route.request().url()).hostname !== '127.0.0.1') { external.push(route.request().url()); return route.abort() }
      return route.continue()
    })
    await page.goto(url)
    await expect(page.locator('html')).toHaveAttribute('data-view', 'webgl')
    await expect.poll(() => page.evaluate(() => ReferenceViewer.snapshot().calls)).toBeGreaterThan(0)
    await expect(page.locator('#spin')).toHaveAttribute('aria-pressed', 'false')
    await page.emulateMedia({ reducedMotion: 'no-preference' })
    const azimuth = await page.evaluate(() => ReferenceViewer.snapshot().azimuth)
    await page.locator('#right').focus(); await page.keyboard.press('Enter')
    assert.ok(await page.evaluate(() => ReferenceViewer.snapshot().azimuth) > azimuth)
    const elevation = await page.evaluate(() => ReferenceViewer.snapshot().elevation)
    await page.locator('#up').focus(); await page.keyboard.press('Enter')
    assert.ok(await page.evaluate(() => ReferenceViewer.snapshot().elevation) < elevation)
    assert.equal(await page.evaluate(() => ReferenceViewer.snapshot().rotation), 0)
    await page.locator('#opacity').fill('0.7')
    await expect(page.locator('#opacity-value')).toHaveText('0.70')
    await expect(page.locator('#panel-summary')).toContainText('Translucent faces · 70% opacity')
    await expect.poll(() => page.evaluate(() => ReferenceViewer.snapshot().opacity)).toBe(0.7)
    await page.locator('#opacity').fill('0')
    await expect(page.locator('#panel-summary')).toContainText('Edges only · 0% opacity')
    await page.locator('#opacity').fill('1')
    await expect(page.locator('#panel-summary')).toContainText('Full-opacity faces · 100% opacity')
    await page.locator('#opacity').fill('0.7')
    const distance = await page.evaluate(() => ReferenceViewer.snapshot().distance)
    await page.locator('#zoom-in').click()
    assert.ok(await page.evaluate(() => ReferenceViewer.snapshot().distance) < distance)
    await page.locator('#reset').click()
    assert.equal(await page.evaluate(() => ReferenceViewer.snapshot().rotation), 0)
    await page.locator('#spin').click()
    await expect(page.locator('#panel-summary')).toContainText('Automatic motion is on.')
    await expect.poll(() => page.evaluate(() => ReferenceViewer.snapshot().rotation)).toBeGreaterThan(0)
    await page.emulateMedia({ reducedMotion: 'reduce' })
    await expect(page.locator('#spin')).toHaveAttribute('aria-pressed', 'false')
    await expect(page.locator('#panel-summary')).toContainText('Automatic motion is off.')
    await expect.poll(() => page.evaluate(() => ReferenceViewer.snapshot().scheduled)).toBe(false)
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false)
    await page.setViewportSize({ width: 700, height: 600 })
    await expect.poll(() => page.evaluate(() => {
      const canvas = document.querySelector('canvas');
      return Math.abs(canvas.width / canvas.height - canvas.clientWidth / canvas.clientHeight)
    })).toBeLessThan(0.02)
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false)
    assert.deepEqual(external, []); assert.deepEqual(errors, [])
    await page.evaluate(() => ReferenceViewer.dispose())
    await expect(page.locator('#spin')).toHaveAttribute('aria-pressed', 'false')
    await expect(page.locator('canvas')).toHaveCount(0)
    await expect(page.locator('#fallback')).toBeVisible()
    assert.equal(await page.evaluate(() => ReferenceViewer.snapshot().scheduled), false)
    await page.close()
  }
  for (const mode of ['no-webgl', 'missing-three', 'missing-controls', 'context-loss']) {
    const page = await browser.newPage()
    const errors = []; page.on('pageerror', error => errors.push(error.message))
    if (mode === 'missing-three') await page.route('**/vendor/three.min.js', route => route.abort())
    if (mode === 'missing-controls') await page.route('**/vendor/OrbitControls.js', route => route.abort())
    if (mode === 'no-webgl') await page.addInitScript(() => {
      const get = HTMLCanvasElement.prototype.getContext
      HTMLCanvasElement.prototype.getContext = function (type, ...args) {
        return /webgl/.test(type) ? null : get.call(this, type, ...args)
      }
    })
    await page.goto(url)
    if (mode === 'context-loss') {
      await expect(page.locator('html')).toHaveAttribute('data-view', 'webgl')
      await page.evaluate(() => document.querySelector('canvas').dispatchEvent(new Event('webglcontextlost', { cancelable: true })))
    }
    await expect(page.locator('html')).toHaveAttribute('data-view', 'fallback')
    await expect(page.locator('#fallback')).toBeVisible()
    await expect(page.locator('#reset')).toBeDisabled()
    await expect(page.locator('#status')).toContainText('Static diagram shown')
    assert.deepEqual(errors, [])
    await page.close()
  }
  // Teardown while the first dependency is pending must not create a late renderer.
  const pending = await browser.newPage()
  let release, signalRequest
  const gate = new Promise(resolve => { release = resolve })
  const requested = new Promise(resolve => { signalRequest = resolve })
  const lateErrors = []; pending.on('pageerror', error => lateErrors.push(error.message))
  await pending.route('**/vendor/three.min.js', async route => {
    signalRequest(); await gate; await route.continue()
  })
  await pending.goto(url, { waitUntil: 'domcontentloaded' })
  await requested
  await pending.evaluate(() => ReferenceViewer.dispose())
  release()
  await pending.waitForLoadState('networkidle')
  await expect(pending.locator('html')).toHaveAttribute('data-view', 'fallback')
  await expect(pending.locator('canvas')).toHaveCount(0)
  await expect(pending.locator('#fallback')).toBeVisible()
  assert.deepEqual(lateErrors, [])
  await pending.close()
  // Vue/module failure must not erase the authored HTML/SVG fallback.
  const noScript = await browser.newContext({ javaScriptEnabled: false })
  const staticPage = await noScript.newPage()
  await staticPage.goto(url)
  await expect(staticPage.locator('#fallback')).toBeVisible()
  await expect(staticPage.locator('#status')).toContainText('Static diagram shown')
  await noScript.close()
  const missingApp = await browser.newPage()
  await missingApp.route('**/assets/*.js', route => route.abort())
  await missingApp.goto(url)
  await expect(missingApp.locator('#fallback')).toBeVisible()
  await expect(missingApp.locator('#status')).toContainText('Static diagram shown')
  await missingApp.close()
  console.log('PASS: Vue computed panels, desktop/mobile WebGL, local-only bundles, keyboard camera controls, reduced-motion change, resize, idle scheduling, disposal, four renderer fallback paths, no-JS and missing-app fallback. No uncaught errors in interactive checks.')
} finally {
  await browser?.close()
  await new Promise(resolve => server.close(resolve))
}
