import { test } from '@playwright/test'

test('inspect clear button styles', async ({ page }) => {
  await page.goto('http://localhost:4321/ledger/')
  await page.waitForLoadState('networkidle')
  const input = page.locator('#search input')
  await input.waitFor({ timeout: 10000 })
  await input.fill('curvature')
  await page.waitForTimeout(800)
  await page.screenshot({ path: '.ai/tmp/clear-button-local.png', fullPage: false })

  const clear = page.locator('.pagefind-ui__search-clear')
  const styles = await clear.evaluate(el => {
    const cs = getComputedStyle(el)
    return {
      paddingLeft: cs.paddingLeft,
      paddingRight: cs.paddingRight,
      right: cs.right,
      left: cs.left,
      top: cs.top,
      height: cs.height,
      background: cs.background,
      border: cs.border,
      borderLeftWidth: cs.borderLeftWidth,
      opacity: cs.opacity,
      fontSize: cs.fontSize,
      fontWeight: cs.fontWeight,
      color: cs.color,
      text: el.textContent,
      isVisible: el.offsetParent !== null,
      overflow: cs.overflow,
    }
  })

  console.log(JSON.stringify(styles, null, 2))
})