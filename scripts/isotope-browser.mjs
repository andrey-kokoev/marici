import assert from 'node:assert/strict';
import { chromium, firefox, webkit } from '@playwright/test';

export async function launchBrowser(name = process.env.ISOTOPE_BROWSER || 'chromium') {
  const engines = { chromium, firefox, webkit };
  assert(Object.hasOwn(engines, name), `Unsupported ISOTOPE_BROWSER: ${name}`);
  console.log(`Browser engine: ${name}`);
  if (name === 'webkit') console.log('WebKit file-mode tests block HTTP(S) via routing: its native offline flag rejects file:// navigation on Windows.');
  return engines[name].launch();
}

export async function disableNetworking(page) {
  await page.route(/^https?:\/\//, route => route.abort('internetdisconnected'));
  if (page.context().browser().browserType().name() !== 'webkit') await page.context().setOffline(true);
}

export async function newBrowserPage(browser, options = {}) {
  const { offline = false, ...rest } = options;
  const page = await browser.newPage(rest);
  if (offline) await disableNetworking(page);
  return page;
}
