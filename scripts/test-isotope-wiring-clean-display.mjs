import assert from 'node:assert/strict';
import {expect} from '@playwright/test';
import {launchBrowser,newBrowserPage} from './isotope-browser.mjs';
const browser=await launchBrowser();
try{
 const page=await newBrowserPage(browser,{offline:true}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(new URL('../examples/isotope-wiring/index.html',import.meta.url).href);await expect(page.locator('#core-state')).toHaveText('Passed');
 const ids=await page.evaluate(()=>Object.keys(IsotopeWiring.fixtures()));
 for(const id of ids){
  if(await page.locator('#catalog').isHidden())await page.locator('#catalog-toggle').click();await page.locator('#catalog-search').fill(id);await page.locator(`#isotopes button[data-id="${id}"]`).click();
  await expect(page.locator('[data-workflow-id]')).toHaveCount(0);
  await expect(page.locator('#canvas .placement-question, #canvas .question-badge')).toHaveCount(0);await expect(page.locator('#placement-banner')).toBeHidden();await expect(page.locator('#uncertainty-legend')).toBeHidden();
  await expect(page.locator('#core-state')).toHaveText(id==='V51-conflict'?'Failed':'Passed');
  if(id==='V51-conflict')await expect(page.locator('#status-counts')).toContainText('errors');
  else if(id==='H1')await expect(page.locator('#status-counts')).toHaveText('1 EP · 0 N');
 }
 const result=await page.evaluate(()=>Object.values(IsotopeWiring.fixtures()).flatMap(d=>[false,true].map(neutronVs=>({id:d.id,svg:IsotopeWiring.renderSVG(d,{neutronVs,standalone:true})}))));
 for(const {id,svg} of result)assert.doesNotMatch(svg,/question-badge|data-question-cell|Placement unresolved|visual prototype|legacy checks only/,id);
 // Historical workflow metadata must not bring the removed controls back.
 const legacy=await page.evaluate(()=>({...IsotopeWiring.fixtures().H1,workflowStatus:'ready'}));await page.locator('#file-input').setInputFiles({name:'old.json',mimeType:'application/json',buffer:Buffer.from(JSON.stringify(legacy))});
 await expect(page.locator('[data-workflow-id]')).toHaveCount(0);await expect(page.locator('#core-state')).toHaveText('Passed');assert.deepEqual(errors,[]);
 console.log('PASS: all built-in isotope displays and SVGs omit workflow controls/question overlays/caveat labels; structural failures remain visible.');
}finally{await browser.close();}
