import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import {chromium} from '@playwright/test';
const url=new URL('../public/experiments/hex-edge-grid.html',import.meta.url),html=readFileSync(url,'utf8');
const helpers=readFileSync(new URL('../public/experiments/hex-edge-strands.js',import.meta.url),'utf8');
const source=html.slice(html.indexOf('function buildHexGrid'),html.indexOf('const svg=document'));
const api=vm.runInNewContext(`${helpers}\n${source}\n({growSimplex,simplexScene,applyProcess1,auditStrands,calculateSeedStrands})`);
test('strand count follows depth, with all actual choices retained through merges',()=>{
 for(let depth=1;depth<=6;depth++)for(let direction=0;direction<3;direction++){
  const seed=api.growSimplex(-14,-14,depth,direction),strands=api.calculateSeedStrands(seed);
  assert.equal(strands.length,2**depth);assert.equal(new Set(strands.map(s=>s.id)).size,strands.length);
  for(const s of strands){assert.equal(s.choices.length,depth);assert.equal(s.seedEdges.length,2*depth);assert(s.seedEdges.every(id=>seed.edges.has(id)));}
 }
 const seed=api.simplexScene(api.growSimplex(-14,-14,4,2)),audit=api.auditStrands(seed);
 assert.equal(audit.strands,16);assert.equal(audit.seedTerminals,5);assert.equal(audit.unassignedEdges.length,0);
 const counts=new Map();for(const s of seed.strands){const id=s.seedVertices.at(-1).id;counts.set(id,(counts.get(id)||0)+1);}
 assert.deepEqual([...counts.values()].sort((a,b)=>a-b),[1,1,4,4,6]);
});
test('existing transformations carry paths exactly, without invented seam continuations',()=>{
 const p=api.applyProcess1(api.growSimplex(-14,-14,4,2));
 for(const [i,scene] of [p.whiteStep,p.redStep,p.step3,p.step4,p.step5,p.step6,p].entries()){
  const audit=api.auditStrands(scene);assert.equal(audit.strands,16);assert.equal(audit.traceCopies,16*2**(i+1));
  for(const s of scene.strands){
   assert.equal(s.traces.length,2**(i+1));
   assert(s.traces.every(t=>t.edges.length===8&&t.vertices.length===9));
   assert.equal(new Set(s.traces.map(t=>t.history.join('|'))).size,s.traces.length);
  }
 }
 const transform=p.whiteStep.reflect;
 for(const s of p.whiteStep.strands)assert.deepEqual(s.traces[1].vertices,s.traces[0].vertices.map(transform));
});
test('file URL shows sixteen table rows, selectable overlays and all stages without page errors',async()=>{
 const browser=await chromium.launch();try{
  const page=await browser.newPage({viewport:{width:1500,height:1100}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.goto(url.href);
  assert.equal(await page.locator('#strand-table tr').count(),16);
  assert.equal(await page.evaluate(()=>hexStrandAudit.strands),16);
  assert.equal(await page.evaluate(()=>hexStrandAudit.traceCopies),2048);
  await page.selectOption('#process','original');
  assert.equal(await page.evaluate(()=>hexStrandAudit.traceCopies),16);
  assert.equal(await page.evaluate(()=>hexStrandAudit.unassignedEdges.length),0);
  await page.locator('#strand-table button').first().click();
  const ids=await page.locator('.strand-line').evaluateAll(es=>[...new Set(es.map(e=>e.dataset.strand))]);
  assert.equal(ids.length,1);assert.equal(ids[0],'SLLLL');
  assert.match(await page.locator('#strand-path').textContent(),/SLLLL:.*→/);
  await page.locator('#show-strands').uncheck();assert.equal(await page.locator('.strand-line').count(),0);
  await page.locator('#show-strands').check();await page.selectOption('#strand-select','all');
  assert.equal(await page.locator('.strand-line').evaluateAll(es=>new Set(es.map(e=>e.dataset.strand)).size),16);
  await page.selectOption('#process','process1');
  for(let stage=1;stage<=7;stage++){
   await page.click(`[data-stage="${stage}"]`);assert.equal(await page.evaluate(()=>hexStrandAudit.traceCopies),16*2**stage);
  }
  await page.selectOption('#process','reference');assert(await page.locator('#reference-workspace').isVisible());
  assert.deepEqual(errors,[]);
 }finally{await browser.close();}
});
