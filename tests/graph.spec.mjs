import { expect, test } from '@playwright/test'

test('graph selection, comparison, isolation, history, and time state are shareable', async ({ page }) => {
  await page.goto('/explore/graph/')
  const nodes = page.locator('.graph-node')
  await expect(nodes.first()).toBeVisible({ timeout: 30000 })
  const firstId = await nodes.nth(0).getAttribute('data-id')
  const secondId = await nodes.nth(1).getAttribute('data-id')

  await nodes.nth(0).click()
  await expect(page).toHaveURL(new RegExp(`entity=${encodeURIComponent(firstId)}`))
  await expect(page.locator('.entity-summary h2')).toBeVisible()
  await nodes.nth(1).hover()
  await expect(page.locator('[role="tooltip"]')).toBeVisible()
  await page.locator(`.graph-node[data-id="${secondId}"]`).click({ button: 'right' })
  await expect(page).toHaveURL(new RegExp(`compare=${encodeURIComponent(secondId)}`))

  const before = await nodes.count()
  await page.getByRole('button', { name: 'Isolate neighborhood' }).click()
  await expect(page.getByRole('button', { name: 'Show full graph' })).toBeVisible()
  expect(await nodes.count()).toBeLessThan(before)
  await page.getByRole('button', { name: 'Show full graph' }).click()
  await page.goBack()
  await expect(page).toHaveURL(new RegExp(`entity=${encodeURIComponent(firstId)}`))

  await page.getByRole('button', { name: 'At entry' }).click()
  await page.locator('input[type="range"]').first().fill('1')
  await page.locator('input[type="range"]').first().dispatchEvent('change')
  await expect(page).toHaveURL(/time=at/)
  await expect(page).toHaveURL(/to=1/)
})

test('deep-linked graph opens the inspector as a mobile sheet', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 })
  await page.goto('/explore/graph/')
  const first = page.locator('.graph-node').first()
  await expect(first).toBeVisible({ timeout: 30000 })
  const id = await first.getAttribute('data-id')
  await page.goto(`/explore/graph/?entity=${encodeURIComponent(id)}`)
  await expect(page.locator('.entity-summary h2')).toBeVisible()
  await expect(page.locator('.graph-app')).toHaveClass(/sheet-open/)
  await page.getByRole('button', { name: 'Close details' }).click()
  await expect(page.locator('.graph-app')).not.toHaveClass(/sheet-open/)
})
