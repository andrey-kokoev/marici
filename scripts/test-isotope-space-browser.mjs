import assert from 'node:assert/strict';
import {createServer} from 'node:http';
import {readFile} from 'node:fs/promises';
import path from 'node:path';
import {chromium} from '@playwright/test';

const root=path.resolve(process.argv[2]||'website/public');
const server=createServer(async(req,res)=>{
  try{
    const file=path.resolve(root,'.'+new URL(req.url,'http://localhost').pathname);
    if(!file.startsWith(root+path.sep))throw Error('outside root');
    const bytes=await readFile(file);
    res.setHeader('Content-Type',/\.(m?js)$/.test(file)?'text/javascript':file.endsWith('.html')?'text/html':'application/octet-stream');res.end(bytes);
  }catch{res.writeHead(404);res.end();}
});
await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
const browser=await chromium.launch();
try{
  const page=await browser.newPage();const errors=[],requests=[];
  page.on('request',request=>requests.push(request.url()));
  page.on('pageerror',error=>errors.push(error.message));
  const base=`http://127.0.0.1:${server.address().port}/experiments/particle-overlap-tetrahedron/tessellated-space.html`;
  const start=Date.now();await page.goto(base);await page.waitForSelector('#loading',{state:'detached'});
  assert.match(await page.locator('#summary').innerText(),/PNE triples/);
  const shellMs=Date.now()-start;
  assert.equal(await page.evaluate(()=>performance.getEntriesByType('resource').some(r=>r.name.includes('phase-assembly-model'))),false);
  await page.click('[data-view=isotope]');
  await page.click('[data-view=space]');
  assert.match(await page.locator('#summary').innerText(),/PNE triples/);
  // A new selection supersedes any unfinished asset load.
  await page.selectOption('#isotope','hydrogen');
  const ready=()=>page.waitForFunction(()=>document.querySelector('#summary').textContent.includes('native tetrahedral grid'),null,{timeout:60000});
  await ready();assert.match(await page.locator('#summary').innerText(),/1P \/ 0N \/ 1e/);
  await page.locator('#grid-extent').fill('2');await page.locator('#grid-extent').dispatchEvent('input');
  assert.match(await page.locator('#summary').innerText(),/extent 2/);
  const isotopeStart=Date.now();
  await page.goto(base+'?isotope=nitrogen15&view=isotope');await ready();
  const nitrogen15Ms=Date.now()-isotopeStart;
  assert.match(await page.locator('#summary').innerText(),/7P \/ 8N \/ 7e/);
  assert.equal(await page.locator('#error').isVisible(),false);
  await page.setViewportSize({width:390,height:844});
  await page.waitForFunction(()=>document.documentElement.scrollWidth<=innerWidth);
  // Every published isotope must render without a research model import.
  for(const id of await page.locator('#isotope option').evaluateAll(options=>options.map(o=>o.value))){
    await page.selectOption('#isotope',id);await ready();
    assert.equal(await page.locator('#error').isVisible(),false,id);
  }
  assert.equal(requests.some(url=>/phase-assembly-model|simplex-model|local-reference-display|atom-model|isotope-structure-worker/.test(url)),false);
  // Network failure must surface and be recoverable.
  await page.route('**/isotope-geometry/hydrogen.json*',route=>route.abort());
  await page.goto(base+'?view=isotope&isotope=hydrogen');
  await page.waitForSelector('#retry',{state:'visible'});
  await page.unroute('**/isotope-geometry/hydrogen.json*');await page.click('#retry');await ready();
  assert.equal(await page.locator('#error').isVisible(),false);
  // Reject mismatched bytes rather than silently showing stale geometry.
  await page.route('**/isotope-geometry/hydrogen.json*',route=>route.fulfill({contentType:'application/json',body:'{}'}));
  await page.goto(base+'?view=isotope&isotope=hydrogen');
  await page.waitForSelector('#retry',{state:'visible'});
  assert.match(await page.locator('#error').innerText(),/digest mismatch/);
  await page.unroute('**/isotope-geometry/hydrogen.json*');await page.click('#retry');await ready();
  assert.deepEqual(errors,[]);
  console.log(JSON.stringify({status:'pass',root,shellMs,nitrogen15Ms,checks:['lazy startup','responsive mode switch','supersede obsolete load','hydrogen counts','grid extent','nitrogen15 deep link and counts','mobile width','all isotope assets','no research imports','asset failure and retry','digest mismatch rejection','no uncaught errors']}));
}finally{await browser.close();await new Promise(resolve=>server.close(resolve));}
