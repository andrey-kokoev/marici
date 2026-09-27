import { expect, test } from '@playwright/test'

const SITE = 'https://marici.andrei-kokoev.workers.dev'
const OUT = '.ai/tmp/verify-snapshots'

test.beforeAll(async ({ request }) => {
  expect((await request.get(SITE)).ok()).toBe(true)
})

test('landing uses the authored carrier page and links the main sections', async ({ page }) => {
  await page.goto(SITE + '/')
  await expect(page.locator('h1')).toContainText('Physics from one object')
  await expect(page.getByRole('link', { name: 'Theory' })).toHaveAttribute('href', '/research/theory/')
  await expect(page.getByRole('link', { name: 'Results' })).toHaveAttribute('href', '/research/results/')
  await expect(page.locator('#predictions')).toBeVisible()
  await page.screenshot({ path: `${OUT}/landing-top.png` })
})

test('authored theory and results Markdown are published', async ({ page }) => {
  await page.goto(SITE + '/research/theory/')
  await expect(page.locator('h1')).toContainText('Full derivation')
  await page.screenshot({ path: `${OUT}/theory-top.png` })
  await page.goto(SITE + '/research/results/')
  await expect(page.locator('h1')).toContainText('Results & predictions')
  await expect(page.locator('h2', { hasText: 'Physics domains' })).toBeVisible()
  await page.screenshot({ path: `${OUT}/results-top.png` })
})

test('ledger search and full text entries are published', async ({ page }) => {
  await page.goto(SITE + '/research/ledger/')
  await expect(page.getByRole('heading', { name: 'Research ledger' })).toBeVisible()
  await expect(page.getByLabel('Search all public entries')).toBeVisible()
  await expect(page.locator('.ledger-list article').first()).toBeVisible({ timeout: 20000 })
  const entryLink = page.locator('.ledger-list article h2 a').first()
  const entryUrl = await entryLink.getAttribute('href')
  await entryLink.click()
  await expect(page.locator('h1')).toBeVisible()
  await expect(page.locator('.meta').first()).toContainText('Entry')
  await page.screenshot({ path: `${OUT}/ledger-entry.png`, fullPage: true })
  expect(entryUrl).toMatch(/^\/research\/ledger\/.+\/$/)
})

test('team and graph routes are live; graph selection is shareable', async ({ page }) => {
  await page.goto(SITE + '/about/team/')
  await expect(page.locator('h1')).toContainText('Research team')
  await page.goto(SITE + '/explore/graph/')
  await expect(page.locator('.graph-node').first()).toBeVisible({ timeout: 30000 })
  await page.locator('.graph-node').first().click()
  await expect(page).toHaveURL(/entity=/)
  await page.screenshot({ path: `${OUT}/graph-selected.png`, fullPage: true })
})
