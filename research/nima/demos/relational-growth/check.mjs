import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {chromium} from '@playwright/test';
const browser=await chromium.launch({headless:true,args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});
try{
 const page=await browser.newPage({viewport:{width:1280,height:950}}),errors=[],network=[];
 page.on('pageerror',e=>errors.push(e.message));page.on('request',r=>{if(/^https?:/.test(r.url()))network.push(r.url());});await page.route(/^https?:/,r=>r.abort());
 await page.goto(new URL('./index.html',import.meta.url).href);await page.waitForFunction(()=>Boolean(window.relationalGrowth));
 for(let level=0;level<=2;level++){
  await page.locator(`[data-level="${level}"]`).click();const s=await page.evaluate(()=>window.relationalGrowth.snapshot());
  const arity=2**level;assert.equal(s.recordCount,4**arity);assert.equal(s.arrowCount,12**arity);assert.equal(s.modelDimension,2*arity);
  assert.equal(new Set(s.tuples.map(t=>JSON.stringify(t))).size,s.recordCount);
  const edges=new Set(s.pairs.map(([a,b])=>`${a},${b}`));assert.equal(edges.size,s.edgeCount);
  for(let a=0;a<s.recordCount;a++)for(let b=a+1;b<s.recordCount;b++)assert.equal(edges.has(`${a},${b}`),s.tuples[a].every((v,i)=>v!==s.tuples[b][i]));
  for(let i=0;i<s.recordCount;i++){
   assert.ok(s.positions[i].every(Number.isFinite));
   if(level)assert.deepEqual(s.parents[i].flat(),s.tuples[i]);
  }
  // Display projection must not accidentally merge distinct endpoint records.
  for(let a=0;a<s.recordCount;a++)for(let b=a+1;b<s.recordCount;b++)assert.ok(Math.hypot(...s.positions[a].map((v,i)=>v-s.positions[b][i]))>1e-6);
 }
 // As the square starts, children must start continuously at their left parent.
 for(let level=0;level<2;level++){
  const [before,after]=await page.evaluate(l=>{window.relationalGrowth.setProgress(l);const a=window.relationalGrowth.snapshot();window.relationalGrowth.setProgress(l+1e-6);return [a,window.relationalGrowth.snapshot()];},level);
  after.positions.forEach((p,i)=>{const parent=before.tuples.findIndex(t=>JSON.stringify(t)===JSON.stringify(after.parents[i][0]));p.forEach((v,j)=>assert.ok(Math.abs(v-before.positions[parent][j])<1e-9));});
 }
 await page.locator('[data-level="2"]').click();await page.screenshot({path:fileURLToPath(new URL('./preview.png',import.meta.url)),fullPage:true});
 await page.locator('#edges').uncheck();await page.locator('#parents').uncheck();await page.locator('#reset').click();assert.equal((await page.evaluate(()=>window.relationalGrowth.snapshot())).recordCount,4);
 await page.locator('#play').click();await page.waitForFunction(()=>window.relationalGrowth.snapshot().progress>.005);await page.locator('#play').click();const paused=await page.evaluate(()=>window.relationalGrowth.snapshot().progress);await page.waitForTimeout(100);assert.equal(await page.evaluate(()=>window.relationalGrowth.snapshot().progress),paused);
 await page.setViewportSize({width:390,height:844});assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
 assert.deepEqual(errors,[]);assert.deepEqual(network,[]);console.log('PASS: exact product relations at all levels, counts, parent provenance, continuous unfolding, distinct projected records, offline load, controls, mobile.');
}finally{await browser.close();}
