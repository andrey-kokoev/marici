import assert from 'node:assert/strict';
import {mkdir} from 'node:fs/promises';
import {expect} from '@playwright/test';
import {launchBrowser,newBrowserPage} from './isotope-browser.mjs';
const browser=await launchBrowser();
try{
 const page=await newBrowserPage(browser,{offline:true,viewport:{width:1280,height:900}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(new URL('../examples/isotope-wiring/index.html',import.meta.url).href);
 await expect(page.locator('#view-kind')).toBeVisible();
 const choose=async id=>{if(await page.locator('#catalog').isHidden())await page.locator('#catalog-toggle').click();await page.locator('#catalog-search').fill(id);await page.locator(`#isotopes button[data-id="${id}"]`).click();};
 const captions=[];
 for(const id of ['He3','Mg25','Si28']){
  await choose(id);const caption=await page.locator(`#isotopes button[data-id="${id}"] .isotope-id`).innerText();captions.unshift(caption);
  await expect(page.locator('#view-kind .diagram-caption')).toHaveText(caption);await page.locator('#pin-reference').click();
 }
 await choose('Na23');await expect(page.locator('#view-kind .diagram-caption')).toHaveText('11 P / 12 N / 11 E · shells 2 · 8 · 1');
 await page.locator('#catalog-close').click();await expect(page.locator('.reference-head .diagram-caption')).toHaveText(captions);
 await mkdir('temp/isotope-captions',{recursive:true});
 for(const width of [1280,390]){
  await page.setViewportSize({width,height:900});
  const layout=await page.evaluate(()=>{
   const active=document.querySelector('#view-kind'),canvas=document.querySelector('#canvas svg');
   return [[active,canvas],...Array.from(document.querySelectorAll('.reference-card'),card=>[card.querySelector('.reference-head'),card.querySelector('svg.diagram')])].map(([head,svg])=>({headerBottom:head.getBoundingClientRect().bottom,graphTop:svg.getBoundingClientRect().top,captionClipped:Array.from(head.querySelectorAll('.diagram-caption')).some(c=>c.scrollWidth>c.clientWidth+1)}));
  });
  for(const item of layout){assert(item.headerBottom<=item.graphTop+1,JSON.stringify({width,...item}));assert.equal(item.captionClipped,false);}
  await page.screenshot({path:`temp/isotope-captions/${width}.png`});
 }
 await page.reload();await expect(page.locator('.reference-head .diagram-caption')).toHaveText(captions);
 await expect(page.locator('#view-kind .diagram-caption')).toHaveText('11 P / 12 N / 11 E · shells 2 · 8 · 1');
 assert.deepEqual(errors,[]);console.log('PASS: active and pinned captions match catalog inventories, wrap without overlap, and persist across reload.');
}finally{await browser.close();}
