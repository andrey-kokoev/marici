import { expect, test } from '@playwright/test'

const SITE = 'https://marici.andrei-kokoev.workers.dev'
const OUT = '.ai/tmp/verify-snapshots'

test.beforeAll(async ({ request }) => {
  const resp = await request.get(SITE)
  expect(resp.ok()).toBe(true)
})

// ── Landing page ────────────────────────────────────────────────

test('landing: hero removed, header clean', async ({ page }) => {
  await page.goto(SITE + '/')
  await page.screenshot({ path: `${OUT}/landing-top.png`, fullPage: false })

  // No hero section
  await expect(page.locator('.hero')).toHaveCount(0)
  // No branches section
  await expect(page.locator('#branches-title')).toHaveCount(0)
  // No ledger section on landing
  await expect(page.locator('#ledger-title')).toHaveCount(0)

  // Eyebrow on relational carrier section present
  await expect(page.locator('.eyebrow:has-text("Marici relational carrier")')).toBeVisible()
  // Carrier heading is the simpler version
  await expect(page.locator('#carrier-title')).toContainText('Relational carrier: physics from one object')

  // Predictions heading is "Predictions" (not the cute "7 testable consequences...")
  await expect(page.locator('#predictions-title')).toContainText('Predictions')

  // Postnikov heading is just "Postnikov descent" (not the cute version)
  await expect(page.locator('#bridges-title')).toContainText('Postnikov descent')
})

test('landing: carrier cards single column centered', async ({ page }) => {
  await page.goto(SITE + '/')
  const grid = page.locator('.dimension-grid').first()
  const box = await grid.boundingBox()
  // Max-width 620px centered — box width should be ≤ 620
  expect(box.width).toBeLessThanOrEqual(626) // allow 6px rounding
})

test('landing: header has no dead label', async ({ page }) => {
  await page.goto(SITE + '/')
  await expect(page.locator('nav a:has-text("research map")')).toHaveCount(0)
  await expect(page.locator('nav a:has-text("Ledger")')).toBeVisible()
})

test('landing: section descriptions stacked below heading', async ({ page }) => {
  await page.goto(SITE + '/')
  const headingBox = await page.locator('#carrier-title').boundingBox()
  const descBox = await page.locator('.section-heading > p').first().boundingBox()
  // Description should be below the heading (larger y)
  expect(descBox.y).toBeGreaterThan(headingBox.y + headingBox.height - 5)
})

// ── Ledger page ──────────────────────────────────────────────────

test('ledger: heading is Research ledger, no One objective', async ({ page }) => {
  await page.goto(SITE + '/ledger/')
  await page.waitForLoadState('networkidle')
  await page.screenshot({ path: `${OUT}/ledger-top.png`, fullPage: false })

  await expect(page.locator('#ledger-title')).toContainText('Research ledger')
  await expect(page.locator('#ledger-title')).not.toContainText('One objective')
})

test('ledger: no Boundary badge on entries', async ({ page }) => {
  await page.goto(SITE + '/ledger/')
  await expect(page.locator('.tag')).toHaveCount(0)
})

test('ledger: pagefind search bar visible', async ({ page }) => {
  await page.goto(SITE + '/ledger/')
  await page.waitForLoadState('networkidle')

  const search = page.locator('#search')
  await expect(search).toBeVisible()
  // Ideally the pagefind input is rendered inside the search div
  // We wait for pagefind JS to initialize
  const input = search.locator('input').first()
  await expect(input).toBeVisible({ timeout: 5000 })
})

test('ledger: ledger count shown', async ({ page }) => {
  await page.goto(SITE + '/ledger/')
  await expect(page.locator('.ledger-count')).toBeVisible()
  await expect(page.locator('.ledger-count')).toContainText('published entries')
})

// ── Results page ─────────────────────────────────────────────────

test('results: page loads', async ({ page }) => {
  await page.goto(SITE + '/results/')
  await page.screenshot({ path: `${OUT}/results-top.png`, fullPage: false })
  await expect(page.locator('#main-content')).toBeVisible()
})

// ── Theory page ──────────────────────────────────────────────────

test('theory: page loads', async ({ page }) => {
  await page.goto(SITE + '/theory/')
  await page.screenshot({ path: `${OUT}/theory-top.png`, fullPage: false })
  await expect(page.locator('h1')).toBeVisible()
})

// ── Team page ────────────────────────────────────────────────────

test('team: page loads', async ({ page }) => {
  await page.goto(SITE + '/team/')
  await page.screenshot({ path: `${OUT}/team-top.png`, fullPage: false })
  await expect(page.locator('h1')).toBeVisible()
})

// ── Ledger entry page (first entry) ─────────────────────────────

test('ledger entry: renders with math and attribution', async ({ page }) => {
  await page.goto(SITE + '/ledger/')
  await page.waitForLoadState('networkidle')
  // Click the first entry card
  const firstCard = page.locator('.article-card').first()
  await expect(firstCard).toBeVisible()
  await firstCard.click()
  await page.waitForLoadState('networkidle')
  await page.screenshot({ path: `${OUT}/ledger-entry.png`, fullPage: true })

  // Should have an h1
  await expect(page.locator('h1').first()).toBeVisible()
  // Author attribution from plain-HTML build is entry number + date
  await expect(page.locator('.byline')).toBeVisible()
})