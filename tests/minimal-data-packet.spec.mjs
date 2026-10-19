import { test, expect } from '@playwright/test';

test.use({ launchOptions: { args: ['--use-angle=swiftshader', '--enable-webgl', '--enable-unsafe-swiftshader'] } });
const url = '/experiments/minimal-data-packet/';

for (const [name, viewport] of [['desktop', { width: 1440, height: 1000 }], ['mobile', { width: 390, height: 844 }]]) {
  test(`${name}: local 3D packet, controls, counts and layout`, async ({ page }) => {
    await page.setViewportSize(viewport);
    const errors = []; page.on('pageerror', e => errors.push(e.message));
    const external = [];
    await page.route('**/*', route => {
      const target = new URL(route.request().url());
      if (target.protocol.startsWith('http') && !['localhost', '127.0.0.1'].includes(target.hostname)) {
        external.push(target.href); return route.abort();
      }
      return route.continue();
    });
    await page.goto(url);
    await expect(page.locator('html')).toHaveAttribute('data-view', 'webgl');
    await expect(page.locator('#scene canvas')).toBeVisible();
    await expect(page.locator('html')).toHaveAttribute('data-tetra-view', 'webgl');
    await expect(page.locator('#tetra-scene canvas')).toBeVisible();
    await expect(page.locator('#tetra-sector option')).toHaveCount(12);
    await expect(page.locator('#sector option')).toHaveCount(12);
    await expect(page.locator('#sector-summary')).toContainText('Omit c');
    await expect(page.locator('#count-products')).toContainText('108 + 432 + 1,296 = 1,836');
    await page.selectOption('#sector', '0:-1:1');
    await expect(page.locator('#sector-summary')).toContainText('Omit a; retain −b and +c');
    await expect(page.locator('#tetra-sector')).toHaveValue('0:-1:1');
    await expect(page.locator('#tetra-sector-summary')).toContainText('Omit a; retain −b and +c');
    await page.check('#only-selected');
    await page.uncheck('#fills');
    await page.uncheck('#signed');
    await page.selectOption('#path-mode', 'return');
    await expect(page.locator('#route-detail')).toContainText('→ +c → l');
    await page.locator('#progress').fill('1');
    await expect(page.locator('#progress-value')).toHaveText('100%');
    await page.getByRole('button', { name: 'Play paths' }).click();
    await expect(page.getByRole('button', { name: 'Pause paths' })).toHaveAttribute('aria-pressed', 'true');
    await expect.poll(() => page.evaluate(() => PacketView.snapshot().progress)).toBeGreaterThan(0);
    await page.getByRole('button', { name: 'Pause paths' }).click();
    await page.getByRole('button', { name: 'Reset camera' }).click();
    await page.locator('#dimension').fill('4');
    await expect(page.locator('#dimension-summary')).toContainText('32 dependency sectors of dimension 3');
    await expect(page.locator('#count-products')).toContainText('20,992');
    await page.locator('#dimension').fill('3');
    await page.check('#fills'); await page.uncheck('#only-selected'); await page.check('#signed');
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1);
    expect(overflow).toBe(false);
    expect(external).toEqual([]); expect(errors).toEqual([]);
    await page.locator('.workbench').first().screenshot({ path: test.info().outputPath(`${name}-packet.png`) });
    await page.locator('#tetrahedral .workbench').screenshot({ path: test.info().outputPath(`${name}-tetrahedral.png`) });
  });
}

test('WebGL failure retains an interactive SVG and readable discussion', async ({ page }) => {
  await page.addInitScript(() => {
    const get = HTMLCanvasElement.prototype.getContext;
    HTMLCanvasElement.prototype.getContext = function (type, ...args) {
      if (/webgl|experimental-webgl/.test(type)) return null;
      return get.call(this, type, ...args);
    };
  });
  const errors = []; page.on('pageerror', e => errors.push(e.message));
  await page.goto(url);
  await expect(page.locator('html')).toHaveAttribute('data-view', 'svg');
  await expect(page.locator('#fallback')).toBeVisible();
  await expect(page.locator('html')).toHaveAttribute('data-tetra-view', 'svg');
  await expect(page.locator('#tetra-fallback')).toBeVisible();
  await expect(page.locator('#scene-status')).toContainText('interactive SVG');
  await page.selectOption('#sector', '1:1:-1');
  await expect(page.locator('#sector-summary')).toContainText('Omit b');
  const before = await page.locator('#fallback').getAttribute('src');
  await page.check('#only-selected');
  expect(await page.locator('#fallback').getAttribute('src')).not.toBe(before);
  await page.locator('#dimension').fill('4');
  await expect(page.locator('#dimension-summary')).toContainText('32 dependency sectors');
  await expect(page.getByRole('heading', { name: 'What the packet proposes' })).toBeVisible();
  await page.selectOption('#tetra-sector', '2:1:1');
  await expect(page.locator('#sector')).toHaveValue('2:1:1');
  const tetraBefore = await page.locator('#tetra-fallback').getAttribute('src');
  await page.uncheck('#tetra-guide');
  expect(await page.locator('#tetra-fallback').getAttribute('src')).not.toBe(tetraBefore);
  expect(errors).toEqual([]);
});

test('tetrahedral controls synchronize the same paths in both coordinate frames', async ({ page }) => {
  await page.goto(url + '#tetrahedral');
  await expect(page.locator('html')).toHaveAttribute('data-tetra-view', 'webgl');
  await page.selectOption('#tetra-sector', '2:1:1');
  await page.selectOption('#tetra-path-mode', 'compare');
  await page.locator('#tetra-progress').fill('1');
  await expect(page.locator('#progress-value')).toHaveText('100%');
  const complete = await page.evaluate(() => PacketView.snapshot());
  expect(complete.frames.lattice.markerPositions).toEqual([[1, 1, 0], [1, 1, 0]]);
  for (const marker of complete.frames.tetrahedral.markerPositions) {
    expect(marker[0]).toBeCloseTo(2 / Math.sqrt(3), 10);
    expect(marker[1]).toBeCloseTo(0, 10); expect(marker[2]).toBeCloseTo(0, 10);
  }
  await page.check('#tetra-only-selected');
  await expect(page.locator('#only-selected')).toBeChecked();
  const isolated = await page.evaluate(() => PacketView.snapshot());
  expect(isolated.frames.tetrahedral.visibleSectors).toBe(1);
  expect(isolated.frames.lattice.visibleSectors).toBe(1);
  await page.uncheck('#tetra-guide');
  expect((await page.evaluate(() => PacketView.snapshot())).frames.tetrahedral.guideVisible).toBe(false);
  await page.selectOption('#tetra-path-mode', 'return');
  await expect(page.locator('#path-mode')).toHaveValue('return');
  await page.locator('#tetra-progress').fill('1');
  const returned = await page.evaluate(() => PacketView.snapshot());
  expect(returned.frames.lattice.markerPositions).toEqual([[0, 0, 0]]);
  expect(returned.frames.tetrahedral.markerPositions).toEqual([[0, 0, 0]]);
  await page.getByRole('button', { name: 'Reset tetrahedral camera' }).click();
});

for (const [name, viewport] of [['desktop', { width: 1440, height: 1000 }], ['mobile', { width: 390, height: 844 }]]) {
  test(`${name}: electron-like base and retained phase use the actual source loop`, async ({ page }) => {
    await page.setViewportSize(viewport);
    const errors = []; page.on('pageerror', error => errors.push(error.message));
    await page.goto(url + '#electron');
    await expect(page.locator('html')).toHaveAttribute('data-electron-view', 'webgl');
    await expect(page.locator('#electron-scene canvas')).toBeVisible();
    await expect(page.locator('#electron-play')).toBeEnabled();
    const initial = await page.evaluate(() => ElectronPacket.snapshot());
    await page.locator('#electron-progress').fill('4');
    await expect(page.locator('#electron-sign')).toHaveText('Same ray; opposite retained spinor sign.');
    const end = await page.evaluate(() => ElectronPacket.snapshot());
    initial.spinor.forEach((component, i) => component.forEach((x, j) => expect(end.spinor[i][j]).toBeCloseTo(-x, 10)));
    initial.ray.forEach((x, i) => expect(end.ray[i]).toBeCloseTo(x, 10));
    expect(Math.abs(end.relativePhase)).toBeCloseTo(Math.PI, 10);
    expect(end.decoderError).toBeLessThan(1e-12);
    await page.check('#electron-erase');
    await expect(page.locator('#electron-erased-readout')).toBeVisible();
    await expect(page.locator('#electron-pairing')).toContainText('0 − 0.8i');
    await page.getByText('Prepare another normalized spinor', { exact: true }).click();
    await page.locator('#electron-theta').fill('0');
    const north = await page.evaluate(() => ElectronPacket.snapshot());
    await page.locator('#electron-initial-phase').fill('90');
    const rephased = await page.evaluate(() => ElectronPacket.snapshot());
    north.ray.forEach((x, i) => expect(rephased.ray[i]).toBeCloseTo(x, 10));
    expect(rephased.spinor[0][1]).toBeCloseTo(1, 10);
    await page.getByRole('button', { name: 'Restore exact source preparation' }).click();
    await page.getByText('Prepare another normalized spinor', { exact: true }).click();
    for (let i = 0; i < 4; i++) await page.getByRole('button', { name: 'Next source step' }).click();
    await expect(page.getByRole('button', { name: 'Next source step' })).toBeDisabled();
    await page.getByRole('button', { name: 'Play spinor loop', exact: true }).click();
    await expect.poll(() => page.evaluate(() => ElectronPacket.snapshot().progress)).toBeGreaterThan(0);
    await page.getByRole('button', { name: 'Pause spinor loop', exact: true }).click();
    await page.getByRole('button', { name: 'Reset spinor camera' }).click();
    await page.locator('#electron-progress').fill('4');
    expect(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1)).toBe(false);
    expect(errors).toEqual([]);
    await page.locator('#electron .workbench').screenshot({ path: test.info().outputPath(`${name}-electron.png`) });
  });
}

test('electron trial retains interactive source readouts when WebGL is unavailable', async ({ page }) => {
  await page.addInitScript(() => {
    const get = HTMLCanvasElement.prototype.getContext;
    HTMLCanvasElement.prototype.getContext = function (type, ...args) {
      return /webgl|experimental-webgl/.test(type) ? null : get.call(this, type, ...args);
    };
  });
  await page.goto(url + '#electron');
  await expect(page.locator('html')).toHaveAttribute('data-electron-view', 'svg');
  await expect(page.locator('#electron-fallback')).toBeVisible();
  await page.locator('#electron-progress').fill('4');
  await expect(page.locator('#electron-sign')).toContainText('opposite retained spinor sign');
  const before = await page.locator('#electron-fallback').getAttribute('src');
  await page.check('#electron-erase');
  expect(await page.locator('#electron-fallback').getAttribute('src')).not.toBe(before);
  await expect(page.locator('#electron-evidence')).toContainText('16 passing checks');
});

test('electron source mismatch is isolated from the two existing 3D frames', async ({ page }) => {
  await page.route('**/electron-trial.json', async route => {
    const response = await route.fetch();
    const trial = await response.json();
    trial.display_fixture.steps[0].matrix[0][0] = ['2', '0'];
    await route.fulfill({ response, json: trial });
  });
  await page.goto(url + '#electron');
  await expect(page.locator('html')).toHaveAttribute('data-electron-view', 'error');
  await expect(page.locator('#electron-status')).toContainText('Source prefix mismatch');
  await expect(page.locator('#electron-controls')).toHaveAttribute('disabled', '');
  await expect(page.locator('#electron-play')).toBeDisabled();
  await expect(page.locator('html')).toHaveAttribute('data-view', 'webgl');
  await expect(page.locator('html')).toHaveAttribute('data-tetra-view', 'webgl');
});

test('atlas and gallery link to the packet, which links to the ledger', async ({ page }) => {
  await page.goto('/experiments/matter-catalog.html');
  await expect(page.getByRole('link', { name: 'Proposed packet primitive', exact: true })).toBeVisible();
  await page.getByRole('link', { name: 'Proposed packet primitive', exact: true }).click();
  await expect(page).toHaveURL(/minimal-data-packet\//);
  await page.getByRole('link', { name: 'Ledger 4322', exact: true }).click();
  await expect(page.getByRole('heading', { name: /4322.*Configuration Coherence/ })).toBeVisible();
  await page.goto('/experiments/');
  await expect(page.locator('a.construction-preview[href="/experiments/minimal-data-packet/"]')).toBeVisible();
});
