import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';
import { chromium } from '@playwright/test';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const data=JSON.parse(await readFile(path.join(root,'research/matter/element-isotope-catalog.json'),'utf8'));
const asset=path.join(root,'website/public/experiments/matter-catalog.html');
assert.deepEqual(JSON.parse(await readFile(path.join(root,'website/public/experiments/matter-catalog.json'),'utf8')),data);
const browser=await chromium.launch();
try {
 const page=await browser.newPage({viewport:{width:1360,height:900}}),errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 await page.goto(pathToFileURL(asset).href);
 assert.deepEqual(await page.locator('#catalog-data').evaluate(e=>JSON.parse(e.textContent)),data);
 const total=data.mechanisms.length+data.constituents.length+data.elements.flatMap(e=>e.isotopes).length;
 assert.equal(await page.locator('.card').count(),total);
 await page.locator('#kind').selectOption('mechanism');
 assert.equal(await page.locator('.card').count(),data.mechanisms.length);
 await page.locator('#status').selectOption('refuted');
 assert.equal(await page.locator('.card').count(),1);
 assert.equal(await page.locator('.card').getAttribute('id'),'gram-energy-test');
 await page.locator('#reset').click();
 await page.locator('#search').fill('recoil');
 assert((await page.locator('.card').count())>0);
 await page.locator('#search').fill('no-such-record-xyz');
 assert.equal(await page.locator('.card').count(),0);
 assert.equal(await page.locator('#empty').isVisible(),true);
 await page.locator('#reset').click();
 await page.locator('#H-1 > summary').click();
 await page.locator('#H-1').getByRole('button',{name:'Hydrogen atom plus photon mass accounting',exact:true}).click();
 assert.equal(await page.locator('#hydrogen-accounting').getAttribute('open'),'');
 assert.equal(new URL(page.url()).hash,'#hydrogen-accounting');
 assert((await page.locator('#hydrogen-accounting').innerText()).includes('E_gamma'));
 await page.locator('#compare').click();
 assert.equal(await page.locator('#comparison').isVisible(),true);
 assert.equal(await page.locator('#compare-body tr').count(),2);
 assert.equal(await page.locator('#compare').getAttribute('aria-expanded'),'true');
 await page.locator('#compare').click();
 assert.equal(await page.locator('#comparison').isVisible(),false);
 const links=await page.locator('.sources a').evaluateAll(es=>es.map(e=>e.href));
 assert(links.length>0&&links.every(x=>x.startsWith('https://')));
 assert(links.some(x=>x.endsWith('research/nima/hydrogen-mass-readout.md')));
 await page.goto(pathToFileURL(asset).href+'#core-dressing');
 assert.equal(await page.locator('#core-dressing').getAttribute('open'),'');
 await page.goto(pathToFileURL(asset).href+'#neutron-candidate');
 await page.locator('#neutron-candidate').getByRole('button',{name:'Common geometric assembly with retained interfaces',exact:true}).click();
 assert.equal(new URL(page.url()).hash,'#common-geometric-assembly');
 assert.equal(await page.locator('#common-geometric-assembly').getAttribute('open'),'');
 const commonText=await page.locator('#common-geometric-assembly').innerText();
 assert(commonText.includes('maximal')&&commonText.includes('twenty-four')&&commonText.includes('not invariant'));
 assert((await page.locator('#common-geometric-assembly .sources a').evaluateAll(es=>es.map(e=>e.href))).some(x=>x.includes('20261010-4319')));
 for(const id of ['proton-candidate','neutron-candidate','electron-candidate']) {
  assert(data.constituents.find(x=>x.id===id).mechanism_ids.includes('common-geometric-assembly'));
 }
 for(const isotope of data.elements.flatMap(e=>e.isotopes)) {
  assert(isotope.model.mechanism_ids.includes('common-geometric-assembly'));
  assert.equal(isotope.model.binding.status,'unconstructed');
  assert.equal(isotope.model.stability_explanation.status,'unconstructed');
 }
 await page.setViewportSize({width:390,height:844});
 await page.locator('#compare').click();
 assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
 await page.locator('#search').fill('electron');
 assert((await page.locator('.card').count())>0);
 assert.deepEqual(errors,[]);
 console.log(JSON.stringify({verification_passed:true,records:total,embedded_registry_matches:true,filters:true,isotope_comparison:true,related_records_and_deep_links:true,source_links:true,common_geometry_research_and_counterexample:true,mobile:true,page_errors:errors},null,2));
} finally {await browser.close();}
