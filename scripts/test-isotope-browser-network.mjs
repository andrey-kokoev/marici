import assert from 'node:assert/strict';
import { createServer } from 'node:http';
import { expect } from '@playwright/test';
import { launchBrowser, newBrowserPage } from './isotope-browser.mjs';

let requests = 0;
const server = createServer((req, res) => { requests++; res.end('Unexpected network access'); });
await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
let browser;
try {
  browser = await launchBrowser();
  const page = await newBrowserPage(browser, { offline: true });
  // A reachable local endpoint distinguishes actual blocking from a DNS/server failure.
  await assert.rejects(() => page.goto(`http://127.0.0.1:${server.address().port}/must-not-load`));
  assert.equal(requests, 0, 'Disabled networking must prevent the server receiving any request');
  await page.close(); // Do not race a browser's asynchronous network-error page navigation.
  const file = await newBrowserPage(browser, { offline: true });
  await file.goto(new URL('../examples/isotope-wiring/index.html', import.meta.url).href);
  await expect(file.locator('#core-state')).toHaveText('Passed');
  assert.equal(requests, 0);
  console.log('PASS: network-disabled test pages block a reachable HTTP endpoint while the self-contained file loads.');
} finally {
  if (browser) await browser.close();
  await new Promise(resolve => server.close(resolve));
}
