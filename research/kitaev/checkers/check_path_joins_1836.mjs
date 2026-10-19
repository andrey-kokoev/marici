import {readFile,mkdir,writeFile} from 'node:fs/promises';
import {resolve} from 'node:path';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const root=resolve(import.meta.dirname,'../../..'),html=await readFile(resolve(root,'public/experiments/path-joins-1836.html'),'utf8');
const ctx=vm.createContext({});vm.runInContext(html.match(/<script id="path-model">([\s\S]*?)<\/script>/)[1],ctx);const m=ctx.PathJoins;
assert.deepEqual(Array.from(m.levels,p=>p.length),[3,6,12]);assert.equal(m.out.length,21);assert.equal(m.incoming.length,21);
for(const p of [...m.out,...m.incoming]){assert.equal(p.vertices.length,p.length+1);for(let i=1;i<p.vertices.length;i++){assert.notEqual(p.vertices[i],p.vertices[i-1]);if(i>1)assert.notEqual(p.vertices[i],p.vertices[i-2]);}}
assert.deepEqual(Array.from(m.counts,c=>c.out),[6,5,5,5]);assert.deepEqual(Array.from(m.counts,c=>c.incoming),[6,5,5,5]);
assert.equal(m.matches.length,111);assert.equal(m.allowed.length,72);assert.equal(m.rejected.length,39);assert.equal(new Set(m.matches.map(p=>p.id)).size,111);
for(const p of m.matches){assert.equal(p.out.end,p.incoming.origin);assert.equal(p.vertices[0],0);assert.equal(p.vertices.at(-1),0);const backtracks=p.vertices.some((v,i)=>i>=2&&v===p.vertices[i-2]);assert.equal(backtracks,!p.allowed);}
// Hostile: the full Cartesian product invents 330 unmatched joins.
assert.equal(m.out.length*m.incoming.length-m.matches.length,330);
const result={model:'passed',source:'complete directed tetrahedron, nonbacktracking, each leg length 1..3',outgoing:21,incoming:21,endpointMatches:111,rejectedSeams:39,retainedPairs:72,notDerived:1836,browser:null};
const dir=resolve(root,'research/kitaev/results/path-joins-1836');await mkdir(dir,{recursive:true});
const browser=await chromium.launch({headless:true});try{
 const page=await browser.newPage({viewport:{width:1440,height:1000},reducedMotion:'reduce'}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.route('http://path-joins.test/',r=>r.fulfill({contentType:'text/html',body:html}));await page.goto('http://path-joins.test/',{waitUntil:'networkidle',timeout:60000});await page.waitForFunction(()=>globalThis.PathJoinScene);
 const counts=[3,6,12,21,21,111,72,72];
 for(let i=0;i<8;i++){await page.locator('#steps button').nth(i).click();assert.equal(await page.locator('#count').textContent(),String(counts[i]));const stats=await page.evaluate(()=>PathJoinScene.stats());assert(stats.depth>4);if(i>=5)assert.equal(stats.matched,111);if(i===0||i===4||i===7)await page.screenshot({path:resolve(dir,['bidirectional-seed.png','','','','incoming-paths.png','','','matched-returns.png'][i]),fullPage:true});}
 await page.locator('#pair').selectOption('20');assert.match(await page.locator('#inspect').textContent(),/Joined:/);assert.match(await page.locator('#inspect').textContent(),/allowed/);
 await page.locator('#steps button').nth(5).click();const point=await page.evaluate(()=>PathJoinScene.projectMatch(30));await page.mouse.click(point.x,point.y);assert.match(await page.locator('#inspect').textContent(),/Joined:|Rejected seam/);
 await page.locator('#reset').click();assert.equal(await page.locator('#count').textContent(),'3');await page.locator('#play').click();await page.waitForTimeout(3500);assert.equal(await page.locator('#count').textContent(),'6');await page.locator('#play').click();
 await page.setViewportSize({width:390,height:844});await page.locator('#steps button').nth(7).click();assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));await page.screenshot({path:resolve(dir,'bidirectional-mobile.png'),fullPage:true});assert.equal(errors.length,0);assert.equal(await page.locator('#view canvas').count(),1);result.browser={controls:'passed',selection:'passed',leftToRight3D:'passed',mobile:'passed',errors};
}finally{await browser.close()}
await writeFile(resolve(root,'research/kitaev/results/path-joins-1836.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result,null,2));
