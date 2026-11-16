import assert from 'node:assert/strict';
import {expect} from '@playwright/test';
import {launchBrowser,newBrowserPage} from './isotope-browser.mjs';
const browser=await launchBrowser();
try{
 const page=await newBrowserPage(browser,{offline:true,hasTouch:true,viewport:{width:1200,height:900}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(new URL('../examples/isotope-wiring/index.html',import.meta.url).href);await expect(page.locator('#core-state')).toHaveText('Passed');
 const back=page.locator('#isotope-back'),forward=page.locator('#isotope-forward');await expect(back).toBeEnabled();await expect(forward).toBeEnabled();
 await forward.click();await expect(page.locator('#title')).toHaveText('Oxygen-17');await back.click();await expect(page.locator('#title')).toHaveText('Oxygen-16');await back.click();await expect(page.locator('#title')).toHaveText('Nitrogen-15');
 const choose=async id=>{if(await page.locator('#catalog').isHidden())await page.locator('#catalog-toggle').click();await page.locator('#catalog-search').fill(id);await page.locator(`#isotopes button[data-id="${id}"]`).click();};
 await choose('H1');await expect(back).toBeDisabled();await page.locator('#definition-view').click();const pending='{"unfinished":"keep while navigating"}';await page.locator('#source').fill(pending);
 // An exact search match must not trap the arrows at a single result.
 await forward.click();await expect(page.locator('#title')).toHaveText('Hydrogen-2');await expect(page.locator('#catalog-search')).toHaveValue('H1');await forward.click();await expect(page.locator('#title')).toHaveText('Helium-3');
 await back.click();await back.click();await expect(page.locator('#title')).toHaveText('Hydrogen-1');assert.equal(await page.locator('#source').inputValue(),pending);
 await forward.click();await page.reload();await expect(page.locator('#title')).toHaveText('Hydrogen-2');await forward.click();await expect(page.locator('#title')).toHaveText('Helium-3');
 const last=await page.evaluate(()=>IsotopeWiring.catalogIndex(IsotopeWiring.fixtures()).at(-1).id);await choose(last);await expect(forward).toBeDisabled();await expect(back).toBeEnabled();
 await page.setViewportSize({width:320,height:700});
 const picker=await page.locator('#catalog-toggle').boundingBox(),navigation=await page.locator('.isotope-history').boundingBox();assert(navigation.x>=picker.x+picker.width-1);assert(navigation.x+navigation.width<=320);assert(Math.abs(navigation.y-picker.y)<8);
 for(const control of [back,forward]){const box=await control.boundingBox();assert(box.width>=44&&box.height>=44);}
 assert.deepEqual(errors,[]);console.log('PASS: immediate catalog navigation, exact-search independence, boundaries, reload recovery, retained text and mobile layout.');
}finally{await browser.close();}
