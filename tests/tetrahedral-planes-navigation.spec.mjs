import { test, expect } from '@playwright/test';

test.use({ launchOptions: { args: ['--enable-unsafe-swiftshader'] } });

test('site navigation opens the Vue planes viewer and returns to the gallery', async ({ page }) => {
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  await page.goto('/');
  await expect(page.locator('.VPNavBarMenu')).toBeVisible();
  await page.locator('.VPNavBarMenu').getByRole('link', { name: 'Constructions', exact: true }).click();
  await expect(page.getByRole('heading', { name: 'Explore the constructions' })).toBeVisible();
  const card = page.locator('a.construction-preview[href="/experiments/tetrahedral-planes/index.html"]');
  await expect(card).toHaveAttribute('target', '_self');
  await card.scrollIntoViewIfNeeded();
  await expect.poll(() => card.locator('img').evaluate(image => image.complete && image.naturalWidth > 0)).toBe(true);
  await card.click();
  await expect(page).toHaveURL(/\/experiments\/tetrahedral-planes\/index\.html$/);
  await expect(page.locator('html')).toHaveAttribute('data-view', 'webgl');
  await expect(page.locator('#status')).toContainText('4 vertices · 4 faces · 4 disks');
  await page.getByRole('link', { name: '← Construction gallery' }).click();
  await expect(page.getByRole('heading', { name: 'Explore the constructions' })).toBeVisible();
  expect(errors).toEqual([]);
});
