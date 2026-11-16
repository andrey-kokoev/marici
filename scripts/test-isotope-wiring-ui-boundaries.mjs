import assert from 'node:assert/strict';
import {expect} from '@playwright/test';
import {launchBrowser,newBrowserPage} from './isotope-browser.mjs';
const browser=await launchBrowser();
try{
 const page=await newBrowserPage(browser,{offline:true,viewport:{width:1280,height:900}}),errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 const url=new URL('../examples/isotope-wiring/index.html',import.meta.url).href;
 await page.goto(url);await expect(page.locator('#core-state')).toHaveText('Passed');
 await expect(page.locator('footer #inventory,footer #status-counts')).toHaveCount(0);await expect(page.locator('footer')).not.toContainText('Graph ready');
 await expect(page.locator('#file-menu #reset,#file-menu #local-theme')).toHaveCount(0);
 await expect(page.locator('#definition-view')).toHaveText('Definition');await expect(page.locator('#counts-toggle')).toHaveText('Validation');
 await page.locator('#changes-overlay').check();await expect(page.locator('#toolstrip #comparison-controls')).toBeVisible();
 await page.locator('#visualization-view').selectOption('neutron-only');await expect(page.locator('#changes-overlay')).not.toBeChecked();await expect(page.locator('#comparison-controls')).toBeHidden();await expect(page.locator('#view-kind')).toBeHidden();await expect(page.locator('#diagram-legend')).toBeHidden();
 await page.locator('#zoom-in').click();await expect(page.locator('#zoom-fit')).toHaveText('Fit');await expect(page.locator('#zoom-level')).toHaveText('1.25× fit');await page.locator('#zoom-fit').click();
 await page.locator('#catalog-toggle').click();await page.locator('#catalog-search').fill('O16');await page.locator('#pin-reference').click();await expect(page.locator('#pin-reference')).toBeFocused();await expect(page.locator('#pin-reference')).toHaveAttribute('aria-pressed','true');
 await page.locator('#visualization-view').selectOption('ep-wiring');await expect(page.locator('#pin-reference')).toHaveAttribute('aria-pressed','true');await expect(page.locator('.reference-card')).toHaveCount(1);
 await page.locator('#pin-reference').click();await expect(page.locator('.reference-card')).toHaveCount(0);await page.locator('#pin-reference').click();
 await page.locator('#catalog-search').fill('B11');await page.locator('#isotopes button[data-id="B11"]').click();await page.locator('#visualization-view').selectOption('neutron-only');await page.locator('#pin-reference').click();await page.locator('#catalog-close').click();
 await expect(page.locator('#view-kind')).toHaveText('Boron-11');await page.locator('#canvas .cell-hit[data-cell="s2-00"]').click();await expect(page.locator('#cell-actions')).toBeHidden();await expect(page.locator('#placement-actions')).toBeHidden();await expect(page.locator('#sketch-edit-help')).toBeVisible();await page.locator('#edit-wiring').click();await expect(page.locator('#cell-actions')).toBeVisible();await expect(page.locator('#visualization-view')).toHaveValue('ep-wiring');await page.locator('#inspector-close').click();await page.locator('#visualization-view').selectOption('neutron-only');
 const download=async selector=>{await page.locator('#file-menu summary').click();const pending=page.waitForEvent('download');await page.locator(selector).click();const chunks=[];for await(const chunk of await(await pending).createReadStream())chunks.push(chunk);return Buffer.concat(chunks).toString('utf8');};
 const canvas=await download('#export-canvas');assert.match(canvas,/Oxygen-16/);assert.match(canvas,/Boron-11/);const views=[...canvas.matchAll(/data-definition="[^"]+" viewBox="([^"]+)"/g)].map(match=>match[1]);assert.equal(views.length,3);assert.equal(new Set(views).size,1);
 const active=await download('#export-svg');assert.doesNotMatch(active,/Oxygen-16/);assert.match(active,/boron-slot-square/);
 const project=await download('#export-project'),saved=JSON.parse(project);assert.equal(saved.workspace.references.length,2);assert.equal(saved.workspace.id,'B11');
 const restored=await newBrowserPage(browser,{offline:true,viewport:{width:1280,height:900}});restored.on('pageerror',e=>errors.push(e.message));await restored.goto(url);await expect(restored.locator('#core-state')).toHaveText('Passed');await restored.locator('#file-input').setInputFiles({name:'project.json',mimeType:'application/json',buffer:Buffer.from(project)});await expect(restored.locator('#title')).toHaveText('Boron-11');await expect(restored.locator('.reference-card')).toHaveCount(2);await expect(restored.locator('#visualization-view')).toHaveValue('neutron-only');await restored.reload();await expect(restored.locator('.reference-card')).toHaveCount(2);await expect(restored.locator('#title')).toHaveText('Boron-11');
 await restored.locator('#catalog-toggle').click();await restored.locator('#catalog-search').fill('C12');await restored.locator('#isotopes button[data-id="C12"]').click();await expect(restored.locator('#visualization-view')).toHaveValue('ep-wiring');assert.equal(await restored.locator('#visualization-view option[value="neutron-only"]').evaluate(option=>option.disabled),true);assert(await restored.locator('#canvas .ep').count()>0);
 assert.deepEqual(errors,[]);console.log('PASS: item/app status separation, per-isotope pin toggle and focus, sketch editing boundary, actual-view selector, comparison controls, stable Fit action, explicit SVG scopes and project workspace/reference roundtrip.');
}finally{await browser.close();}
