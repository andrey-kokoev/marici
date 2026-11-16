import assert from 'node:assert/strict';
import {expect} from '@playwright/test';
import {launchBrowser,newBrowserPage} from './isotope-browser.mjs';
const browser=await launchBrowser();
try{
 const page=await newBrowserPage(browser,{offline:true}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.addInitScript(()=>{if(!localStorage.getItem('isotope-wiring-ui-v1'))localStorage.setItem('isotope-wiring-ui-v1',JSON.stringify({version:1,id:'O16',catalogOpen:true,catalogPage:99,element:'1',mass:'1',query:''}));});
 await page.goto(new URL('../examples/isotope-wiring/index.html',import.meta.url).href);await expect(page.locator('#core-state')).toHaveText('Passed');
 await expect(page.locator('#catalog-pagination,#catalog-prev,#catalog-next,#catalog-page')).toHaveCount(0);
 const help=await page.locator('#graph-keyboard-help').evaluate(element=>({width:element.getBoundingClientRect().width,height:element.getBoundingClientRect().height,clip:getComputedStyle(element).clipPath}));assert(help.width<=1&&help.height<=1&&help.clip==='inset(50%)','Keyboard help remains visually hidden');
 await expect(page.locator('#isotopes button[data-id]')).toHaveCount(1);await expect(page.locator('#isotopes button[data-id="H1"]')).toBeVisible();await expect(page.locator('#catalog-count')).toContainText('A=1');
 await page.locator('#catalog-reset-filters').click();const total=await page.evaluate(()=>Object.keys(IsotopeWiring.fixtures()).length);assert(total>30,'Exercise a catalog larger than the removed page size');await expect(page.locator('#isotopes button[data-id]')).toHaveCount(total);await expect(page.locator('#catalog-count')).toHaveText(`${total} definitions`);await expect(page.locator('#isotopes button[data-id="V51"]')).toHaveCount(1);await expect(page.locator('#catalog-search')).toBeFocused();
 await expect(page.locator('#isotopes button[data-id="C12"] .isotope-label')).toHaveText('Carbon-12');
 await expect(page.locator('#isotopes button[data-id="C12"] .isotope-id')).toHaveText('6 P / 6 N / 6 E · shells 2 · 4');
 await expect(page.locator('#isotopes button[data-id="H1"] .isotope-id')).toHaveText('1 P / 0 N / 1 E · shells 1');
 await expect(page.locator('#isotopes button[data-id="O18"] .isotope-id')).toHaveText('8 P / 10 N / 8 E · shells 2 · 6');
 await page.reload();await expect(page.locator('#isotopes button[data-id]')).toHaveCount(total);
 await expect(page.locator('#isotopes button[data-id="C12"] .isotope-id')).toHaveText('6 P / 6 N / 6 E · shells 2 · 4');
 await page.locator('#catalog-search').fill('O16');await expect(page.locator('#isotopes button[data-id="O16"]')).toBeVisible();await expect(page.locator('#isotopes button[data-id]')).toHaveCount(1);
 await page.locator('#mass-filter').fill('1');await page.locator('#catalog-clear').click();await expect(page.locator('#mass-filter')).toHaveValue('1');await page.locator('#catalog-search').fill('O16');await expect(page.locator('#isotopes button[data-id]')).toHaveCount(0);await page.locator('[data-clear-catalog]').click();await expect(page.locator('#isotopes button[data-id]')).toHaveCount(total);
 await expect(page.locator('#element-filter')).toHaveValue('');await expect(page.locator('#mass-filter')).toHaveValue('');await expect(page.locator('#catalog-search')).toHaveValue('');assert.deepEqual(errors,[]);
 for(const viewport of [{width:1200,height:800},{width:320,height:700}]){await page.setViewportSize(viewport);const clipped=await page.locator('#isotopes button[data-id]').evaluateAll(buttons=>buttons.filter(button=>{const caption=button.querySelector('.isotope-id'),row=button.getBoundingClientRect(),box=caption.getBoundingClientRect();return caption.scrollWidth>caption.clientWidth+1||box.right>row.right+1||box.bottom>row.bottom+1;}).map(button=>button.dataset.id));assert.deepEqual(clipped,[],`Full captions fit at ${viewport.width}px`);}
 console.log('PASS: catalog filters, inventory captions, reload persistence, search, empty-result recovery and unclipped desktop/mobile captions.');
}finally{await browser.close();}
