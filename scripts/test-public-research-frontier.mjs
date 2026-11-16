import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import http from 'node:http'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { chromium, expect } from '@playwright/test'

const root = fileURLToPath(new URL('../', import.meta.url))
const dist = path.join(root, 'website/.vitepress/dist')
const contract = JSON.parse(await fs.readFile(path.join(root, 'config/public-research-coverage.v1.json'), 'utf8'))
const mime = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml', '.woff2': 'font/woff2' }
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
try {
  browser = await chromium.launch()
  for (const viewport of [{ width: 1440, height: 1000 }, { width: 390, height: 844 }]) {
    const page = await browser.newPage({ viewport })
    const errors = [], failed = [], external = []
    page.on('pageerror', error => errors.push(error.message))
    page.on('response', response => { if (response.status() >= 400) failed.push(response.url()) })
    await page.route('**/*', route => {
      const url = new URL(route.request().url())
      if (['http:', 'https:'].includes(url.protocol) && url.origin !== base) { external.push(url.href); return route.abort() }
      return route.continue()
    })
    await page.goto(base + '/research/results/#next-discriminating-tests')
    await page.getByRole('link', { name: 'versioned current-frontier map', exact: true }).click()
    await expect(page.getByRole('heading', { level: 1, name: 'Current frontier: missing source objects and acceptance tests' })).toBeVisible()
    await expect(page.locator('main tbody tr')).toHaveCount(contract.frontier.length)
    assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), 'Frontier overflows the viewport')
    await page.getByRole('link', { name: 'publication provenance guide', exact: true }).click()
    const download = page.getByRole('link', { name: 'Download the compact v1 provenance manifest', exact: true })
    await expect(download).toBeVisible()
    const response = await page.request.get(base + await download.getAttribute('href'))
    assert.equal(response.status(), 200)
    const metadata = await response.json()
    assert.equal(metadata.entries.length, contract.required_result_slugs.length)
    assert.equal(metadata.scientific_replay_performed, false)
    assert((await response.body()).length < 65536)
    await page.goto(base + '/research/frontier/current')
    await page.getByRole('link', { name: contract.frontier[0].label, exact: true }).click()
    await expect(page.getByText('Metadata validation is not scientific replay.', { exact: false })).toBeVisible()
    assert.deepEqual(errors, [])
    assert.deepEqual(failed, [])
    assert.deepEqual(external, [])
    await page.close()
    console.log(`PASS frontier navigation, ${contract.frontier.length} acceptance rows, provenance download and result binding at ${viewport.width}px`)
  }
} finally {
  if (browser) await browser.close()
  await new Promise(resolve => server.close(resolve))
}
