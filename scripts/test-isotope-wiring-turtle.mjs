import assert from 'node:assert/strict';
import {readFile,mkdtemp,writeFile,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {pathToFileURL} from 'node:url';
import {expect} from '@playwright/test';
import {launchBrowser,newBrowserPage} from './isotope-browser.mjs';
import {prepareEmbeddedTurtle} from './prepare-isotope-wiring-turtle.mjs';

await prepareEmbeddedTurtle({check:true});
const source=new URL('../examples/isotope-wiring/index.html',import.meta.url);
const html=await readFile(source,'utf8');
const raw=await readFile(new URL('../research/strominger/isotope-schema/results/neon-20-inventory.ttl',import.meta.url));
const snapshot=JSON.parse(await readFile(new URL('../examples/isotope-wiring/core/ne20-inventory.json',import.meta.url),'utf8'));
const temporary=await mkdtemp(join(tmpdir(),'marici-turtle-ui-'));
const browser=await launchBrowser();
try{
 const altered=structuredClone(snapshot);
 altered.inputs['research/strominger/isotope-schema/check.py']='0'.repeat(64);
 const stale=join(temporary,'stale.json');await writeFile(stale,JSON.stringify(altered));
 await assert.rejects(prepareEmbeddedTurtle({check:true,snapshotFile:pathToFileURL(stale)}),/Stale validated Turtle snapshot/);
 altered.inputs=snapshot.inputs;altered.turtle+='\n# modified';await writeFile(stale,JSON.stringify(altered));
 await assert.rejects(prepareEmbeddedTurtle({check:true,snapshotFile:pathToFileURL(stale)}));
 const errors=[],page=await newBrowserPage(browser,{offline:true,viewport:{width:1100,height:850}});
 page.on('pageerror',e=>errors.push(e.message));
 const choose=async(page,id)=>{
  if(!await page.locator('#catalog').isVisible())await page.locator('#catalog-toggle').click();
  await page.locator('#catalog-search').fill(id);
  await page.locator(`#isotopes button[data-id="${id}"]`).click();
  await page.locator('#catalog-close').click();
 };
 await page.goto(source.href);await choose(page,'Ne20');
 await page.locator('#catalog-toggle').click();
 await expect(page.locator('[data-id="Ne20"] [data-turtle-inventory]')).toHaveAttribute('data-turtle-inventory','matched');
 await page.locator('#catalog-close').click();await page.locator('#counts-toggle').click();
 await expect(page.locator('#turtle-inventory-panel')).toBeVisible();
 await expect(page.locator('#turtle-inventory-panel')).toHaveAttribute('data-inventory-state','matched');
 await expect(page.locator('#turtle-inventory-readouts')).toContainText('Z=10 · N=10 · A=20');
 await expect(page.locator('#turtle-inventory-readouts')).toContainText('Electron count and charge: unspecified');
 await expect(page.locator('#turtle-inventory-status')).toContainText('does not validate the drawing');
 const pending=page.waitForEvent('download');await page.locator('#download-turtle-inventory').click();
 const download=await pending;assert.equal(download.suggestedFilename(),'neon-20-inventory.ttl');
 assert.deepEqual(await readFile(await download.path()),raw);
 await page.locator('#counts-close').click();await page.locator('#definition-view').click();
 const definition=JSON.parse(await page.locator('#source').inputValue());
 const expected=await page.evaluate(()=>IsotopeWiring.compile(IsotopeWiring.fixtures().Ne20,IsotopeWiring.fixtures()).graph);
 assert.deepEqual(definition.graph,expected,'Attaching the inventory must not change drawing records');
 definition.N=11;await page.locator('#source').fill(JSON.stringify(definition));await page.locator('#apply').click();
 await page.locator('#counts-toggle').click();
 await expect(page.locator('#turtle-inventory-panel')).toHaveAttribute('data-inventory-state','mismatch');
 await expect(page.locator('#turtle-inventory-status')).toContainText('Edits are not certified');
 await expect(page.locator('#turtle-inventory-readouts')).toContainText('N=10');
 await page.setViewportSize({width:390,height:844});
 assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
 await choose(page,'O16');await page.locator('#counts-toggle').click();
 await expect(page.locator('#turtle-inventory-panel')).toBeHidden();
 // Malformed/missing or digest-corrupted snapshot never produces a success badge.
 for(const payload of [null,{...snapshot,turtle:snapshot.turtle+'\n# corruption'}]){
  const broken=join(temporary,`unavailable-${payload===null?'missing':'digest'}.html`);
  await writeFile(broken,html.replace(/<script type="application\/json" id="isotope-turtle-inventory">[\s\S]*?<\/script>/,
   ()=>`<script type="application/json" id="isotope-turtle-inventory">${JSON.stringify(payload).replaceAll('<','\\u003c')}</script>`));
  const unavailable=await newBrowserPage(browser,{offline:true,viewport:{width:1100,height:850}});
  unavailable.on('pageerror',e=>errors.push(e.message));await unavailable.goto(pathToFileURL(broken).href);
  await choose(unavailable,'Ne20');await unavailable.locator('#counts-toggle').click();
  await expect(unavailable.locator('#turtle-inventory-panel')).toHaveAttribute('data-inventory-state','unavailable');
  await expect(unavailable.locator('#download-turtle-inventory')).toBeDisabled();
  await expect(unavailable.locator('#turtle-inventory-status')).toContainText('no inventory validation is claimed');
  await unavailable.close();
 }
 assert.deepEqual(errors,[]);
 console.log('PASS: Ne-20 offline inventory attachment, exact Turtle download, unchanged drawing, edit mismatch, mobile layout, non-Ne20 isolation, unavailable/corrupt data and publication freshness gates.');
}finally{await browser.close();await rm(temporary,{recursive:true,force:true});}
