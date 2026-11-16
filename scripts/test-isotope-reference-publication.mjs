import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import path from 'node:path'
import http from 'node:http'
import { fileURLToPath, pathToFileURL } from 'node:url'
import { chromium, expect } from '@playwright/test'

const root = fileURLToPath(new URL('../', import.meta.url))
const dist = path.join(root, 'website/.vitepress/dist')
const tablePath = '/experiments/isotope-electron-shells.html'
const table = await fs.readFile(path.join(dist, tablePath))
const published = await fs.readFile(path.join(root, 'website/public', tablePath))
assert(table.equals(published), 'Built table is not the exact generated public copy')
const server = http.createServer(async (req, res) => {
  try {
    const route = new URL(req.url, 'http://local').pathname
    if (route === tablePath) { res.setHeader('Content-Type', 'text/html'); res.end(table); return }
    if (route === '/experiments/isotope-reference') {
      res.setHeader('Content-Type', 'text/html')
      res.end(await fs.readFile(path.join(dist, 'experiments/isotope-reference.html'))); return
    }
    res.writeHead(404); res.end('Not found')
  } catch { res.writeHead(500); res.end('Publication read failed') }
})
await new Promise(resolve => server.listen(0, '127.0.0.1', resolve))
const base = `http://127.0.0.1:${server.address().port}`
let browser
try {
  browser = await chromium.launch()
  for (const viewport of [{ width: 1440, height: 1000 }, { width: 390, height: 844 }]) {
    for (const url of [base + tablePath, pathToFileURL(path.join(dist, tablePath)).href]) {
      const page = await browser.newPage({ viewport })
      const errors = [], external = []
      page.on('pageerror', error => errors.push(error.message))
      await page.route('**/*', route => {
        const request = new URL(route.request().url())
        if (['http:', 'https:'].includes(request.protocol) && request.origin !== base) {
          external.push(request.href); return route.abort()
        }
        return route.continue()
      })
      await page.goto(url)
      await expect(page.locator('#row-count')).toHaveText('96 isotopes · 80 elements')
      await expect(page.locator('#isotope-body tr')).toHaveCount(96)
      await expect(page.locator('thead th')).toHaveCount(11)
      assert.equal(await page.locator('td.abundance').filter({ hasText: 'Not available' }).count(), 0)
      assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth))
      const region = await page.locator('.table-wrap').evaluate(element => ({ height: element.getBoundingClientRect().height, width: element.clientWidth, scroll: element.scrollWidth, viewport: innerHeight }))
      assert(Math.abs(region.height / region.viewport - 0.9) < 0.01)
      if (viewport.width === 390) assert(region.scroll > region.width, 'Mobile table should scroll internally')
      await page.locator('#isotope-search').fill('Lead-204')
      await expect(page.locator('#isotope-body tr:visible')).toHaveCount(1)
      await expect(page.locator('#isotope-body tr:visible td.stability')).toContainText('≥')
      await expect(page.locator('#isotope-body tr:visible td.abundance')).toHaveText('1.4')
      await page.locator('#isotope-search').fill('NoSuchIsotope')
      await expect(page.locator('#empty-state')).toBeVisible()
      await expect(page.locator('#row-count')).toHaveText('0 of 96 isotopes')
      await page.locator('#isotope-search').fill('')
      await expect(page.locator('#isotope-body tr:visible')).toHaveCount(96)
      await expect(page.locator('.notes').first()).toContainText('not its share of all matter')
      await expect(page.locator('.notes').last()).toContainText('not a measured decay lifetime')
      assert.deepEqual(errors, [])
      assert.deepEqual(external, [])
      console.log(`PASS: ${viewport.width}px ${url.startsWith('file:') ? 'file' : 'HTTP'} table, scrolling, filtering, provenance qualifications and no external runtime requests`)
      await page.close()
    }
  }
} finally {
  await browser?.close()
  await new Promise(resolve => server.close(resolve))
}
