import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {chromium} from '@playwright/test';
const reference=JSON.parse(readFileSync(new URL('../../results/two-paws.json',import.meta.url),'utf8'));
const browser=await chromium.launch({headless:true,args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});
try {
 const page=await browser.newPage();const errors=[],network=[];
 page.on('pageerror',e=>errors.push(e.message));page.on('request',r=>{if(/^https?:/.test(r.url()))network.push(r.url());});
 await page.route(/^https?:/,r=>r.abort());await page.goto(new URL('./index.html',import.meta.url).href);
 await page.waitForFunction(()=>Boolean(window.twoPaws));
 for(let i=0;i<=100;i++){
  const s=await page.evaluate(t=>{window.twoPaws.setProgress(t);return window.twoPaws.snapshot();},i/100);
  for(const k of reference.seed_edges)assert.ok(Math.abs(s.visibleEdges[k]-1)<1e-10);
  assert.deepEqual(s.points.A,[0,0,0]);assert.deepEqual(s.points.D,[-.5,Math.sqrt(3)/2,0]);
 }
 const s=await page.evaluate(()=>window.twoPaws.snapshot());assert.equal(s.edgeCount,15);assert.equal(Object.keys(s.visibleEdges).length,15);
 for(const k of 'ABCDEF')s.points[k].forEach((v,i)=>assert.ok(Math.abs(v-reference.final_points[k][i])<1e-10));
 s.volumes.forEach(v=>assert.ok(Math.abs(v-Math.sqrt(2)/12)<1e-10));
 await page.selectOption('#scope','local');const local=await page.evaluate(()=>window.twoPaws.snapshot());assert.equal(local.edgeCount,11);assert.equal(Object.keys(local.visibleEdges).length,11);
 Object.values(local.visibleEdges).forEach(v=>assert.ok(Math.abs(v-1)<1e-10));
 await page.locator('#faces').uncheck();await page.locator('#reset').click();assert.equal((await page.evaluate(()=>window.twoPaws.snapshot())).edgeCount,7);
 await page.locator('#play').click();await page.waitForFunction(()=>window.twoPaws.snapshot().progress>.005);await page.locator('#play').click();
 const paused=await page.evaluate(()=>window.twoPaws.snapshot().progress);await page.waitForTimeout(100);assert.equal(await page.evaluate(()=>window.twoPaws.snapshot().progress),paused);
 await page.setViewportSize({width:390,height:844});assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
 assert.deepEqual(errors,[]);assert.deepEqual(network,[]);console.log('PASS: offline browser, 101 motion samples, Python endpoint agreement, both scopes, controls, mobile.');
} finally {await browser.close();}
