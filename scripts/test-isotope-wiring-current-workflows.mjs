import assert from 'node:assert/strict';
import {expect} from '@playwright/test';
import {launchBrowser,newBrowserPage} from './isotope-browser.mjs';

const browser=await launchBrowser();
try{
 const page=await newBrowserPage(browser,{offline:true,viewport:{width:1280,height:900}}),errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 const url=new URL('../examples/isotope-wiring/index.html',import.meta.url).href;
 await page.goto(url);await expect(page.locator('#core-state')).toHaveText('Passed');
 // Exercise the delivered JSON/data bridge without claiming a retired placement dialog exists.
 const bridge=await page.evaluate(()=>{
  const source=IsotopeWiring.fixtures().V51,text=JSON.stringify(source),core=IsotopeWiringResearch;
  const trial=core.trialPlacement(text,'s3-10-upper','s3-01');
  const survey=core.surveyPlacements(text,'pairs','s3-10-upper',0);
  const witness=core.trialWitnessPlacement(JSON.stringify(IsotopeWiring.fixtures().O16),'s2-01-H','s2-00');
  return {unchanged:JSON.stringify(source)===text,source:source.graph.pairs.find(p=>p.id==='s3-10-upper').cell,
   trial:trial.definition.graph.pairs.find(p=>p.id==='s3-10-upper').cell,status:trial.report.status,
   scope:survey.scope,total:survey.total,rows:survey.rows.length,witnessStatus:witness.report.status};
 });
 assert(bridge.unchanged);assert.equal(bridge.source,'s3-10');assert.equal(bridge.trial,'s3-01');assert.equal(bridge.status,'verified');assert(bridge.scope.includes('not a physical uniqueness test'));assert.equal(bridge.total,8);assert.equal(bridge.rows,8);assert.equal(bridge.witnessStatus,'verified');
 await expect(page.locator('#trial-open,#canvas .difference-mark')).toHaveCount(0);
 await page.locator('#definition-view').click();
 const fixture=JSON.parse(await page.locator('#source').inputValue());
 const apply=async value=>{await page.locator('#source').fill(JSON.stringify(value));await page.locator('#apply').click();await expect(page.locator('#source-status.error')).toHaveCount(0);};
 const download=async selector=>{await page.locator('#file-menu > summary').click();const pending=page.waitForEvent('download');await page.locator(selector).click();const chunks=[];for await(const chunk of await(await pending).createReadStream())chunks.push(chunk);return Buffer.concat(chunks).toString('utf8');};
 const base={...fixture,id:'MatrixBase',name:'Matrix base',obsolete:{remove:true}};
 const target={...fixture,id:'MatrixTarget',name:'Matrix target',provenance:{verified:false}};delete target.notes;
 await apply(base);await apply({kind:'delta',id:base.id,base:base.id,ops:[]});
 assert.deepEqual(JSON.parse(await page.locator('#source').inputValue()),base);
 assert.deepEqual(JSON.parse(await download('#export-json')),base);
 await apply(target);await page.locator('#format').selectOption('delta');await page.locator('#base-search').fill(base.id);await page.locator(`#base-results button[data-base="${base.id}"]`).click();
 const delta=JSON.parse(await download('#export-json'));assert(delta.ops.some(op=>op.op==='remove-metadata'&&op.key==='obsolete'));
 await apply(delta);await page.locator('#format').selectOption('absolute');
 assert.deepEqual(JSON.parse(await page.locator('#source').inputValue()),target);
 const project=JSON.parse(await download('#export-project'));
 const fresh=await newBrowserPage(browser,{offline:true});fresh.on('pageerror',e=>errors.push(e.message));await fresh.goto(url);await expect(fresh.locator('#core-state')).toHaveText('Passed');
 await fresh.locator('#file-input').setInputFiles({name:'matrix-project.json',mimeType:'application/json',buffer:Buffer.from(JSON.stringify(project))});
 await expect(fresh.locator('#toast')).toContainText('Project imported');
 if(await fresh.locator('#catalog').isHidden())await fresh.locator('#catalog-toggle').click();
 await fresh.locator('#catalog-search').fill(target.id);await fresh.locator(`#isotopes button[data-id="${target.id}"]`).click();await fresh.locator('#catalog-close').click();await fresh.locator('#definition-view').click();
 await fresh.locator('#format').selectOption('absolute');assert.deepEqual(JSON.parse(await fresh.locator('#source').inputValue()),target);
 await expect(fresh.locator('#storage-state')).toHaveText('Definitions saved in this browser');
 await fresh.reload();await expect(fresh.locator('#title')).toHaveText(target.name);assert.deepEqual(JSON.parse(await fresh.locator('#source').inputValue()),target);
 await fresh.close();
 // Invalid text stays separate from applied definitions and survives reload.
 const draft='unapplied matrix draft: not JSON';await page.locator('#source').fill(draft);await expect(page.locator('#source-status')).toContainText('Text draft saved');
 await page.reload();await expect(page.locator('#source')).toHaveValue(draft);
 const draftDownload=page.waitForEvent('download');await page.locator('#export-text').click();const chunks=[];for await(const chunk of await(await draftDownload).createReadStream())chunks.push(chunk);assert.equal(Buffer.concat(chunks).toString('utf8'),draft);
 page.once('dialog',dialog=>dialog.dismiss());await page.locator('#reload-source').click();await expect(page.locator('#source')).toHaveValue(draft);
 page.once('dialog',dialog=>dialog.accept());await page.locator('#reload-source').click();assert.deepEqual(JSON.parse(await page.locator('#source').inputValue()),target);
 await apply({...fixture,id:'MatrixCycleA',name:'Cycle A'});await apply({kind:'delta',id:'MatrixCycleB',base:'MatrixCycleA',ops:[]});
 await page.locator('#source').fill(JSON.stringify({kind:'delta',id:'MatrixCycleA',base:'MatrixCycleB',ops:[]}));await page.locator('#apply').click();await expect(page.locator('#source-status.error')).toContainText('Cyclic delta');
 assert.deepEqual(errors,[]);
 console.log('PASS: isolated placement/survey data bridge, same-ID replay, metadata deletion, exact export/fresh import/reload, retained drafts/discard and cyclic-update refusal; no placement-dialog claim.');
}finally{await browser.close();}
