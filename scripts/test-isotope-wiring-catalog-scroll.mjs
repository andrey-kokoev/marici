import assert from 'node:assert/strict';
import {expect} from '@playwright/test';
import {launchBrowser,newBrowserPage} from './isotope-browser.mjs';
const browser=await launchBrowser();
try{
 const page=await newBrowserPage(browser,{offline:true,viewport:{width:1200,height:700}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.addInitScript(()=>{if(!localStorage.getItem('isotope-wiring-ui-v1'))localStorage.setItem('isotope-wiring-ui-v1',JSON.stringify({version:1,id:'V51',catalogOpen:true}));});
 await page.goto(new URL('../examples/isotope-wiring/index.html',import.meta.url).href);await expect(page.locator('#title')).toHaveText('Vanadium-51');await expect(page.locator('#catalog-search')).toBeFocused();
 const list=page.locator('#isotopes'),selected=page.locator('#isotopes button[data-id="V51"]');
 const box=await list.boundingBox(),row=await selected.boundingBox();assert(row.y>=box.y-1&&row.y+row.height<=box.y+box.height+1,'Selected isotope is visible when no scroll state exists');assert(await list.evaluate(e=>e.scrollTop)>0);
 await list.evaluate(e=>{e.scrollTop=170;});await expect.poll(()=>page.evaluate(()=>JSON.parse(localStorage.getItem('isotope-wiring-ui-v1')).catalogScrollTop)).toBe(170);
 await page.locator('#grid').check();assert.equal(await list.evaluate(e=>e.scrollTop),170,'Redrawing must not jump the list');
 await page.reload();await expect(page.locator('#title')).toHaveText('Vanadium-51');await expect(page.locator('#catalog-search')).toBeFocused();await expect.poll(()=>list.evaluate(e=>e.scrollTop)).toBe(170);
 await page.locator('#catalog-close').click();await page.reload();await expect(page.locator('#catalog')).toBeHidden();await page.locator('#catalog-toggle').click();await expect.poll(()=>list.evaluate(e=>e.scrollTop)).toBe(170);
 for(const edge of ['first','last']){
  const targetId=await list.evaluate((list,edge)=>{const box=list.getBoundingClientRect(),visible=[...list.querySelectorAll('button[data-id]')].filter(button=>{const row=button.getBoundingClientRect();return row.top>=box.top+1&&row.bottom<=box.bottom-1;});return (edge==='first'?visible[0]:visible.at(-1)).dataset.id;},edge);
  const target=page.locator(`#isotopes button[data-id="${targetId}"]`),before=await target.boundingBox();
  if(edge==='first')await target.click();else{await target.evaluate(button=>button.focus({preventScroll:true}));await target.press('Enter');}
  await expect(target).toHaveAttribute('aria-current','true');assert.equal(await list.evaluate(e=>e.scrollTop),170,'Selecting a visible row must not recenter the list');assert.equal((await target.boundingBox()).y,before.y,'The clicked row stays in place');
 }
 await page.locator('#isotope-forward').click();assert.equal(await list.evaluate(e=>e.scrollTop),170,'Arrow navigation must not move the open list');
 await page.reload();await expect(page.locator('#catalog-search')).toBeFocused();await expect.poll(()=>list.evaluate(e=>e.scrollTop)).toBe(170);
 await page.locator('#catalog-search').fill('Li');await expect.poll(()=>list.evaluate(e=>e.scrollTop)).toBe(0);
 assert.deepEqual(errors,[]);console.log('PASS: selected-item fallback, remembered catalog scroll, reload/close/reopen recovery, redraw stability, stationary mouse/keyboard selection and navigation, and filter reset.');
}finally{await browser.close();}
