import { chromium } from '@playwright/test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import http from 'node:http';
import { prepareConjectureNets } from './prepare-conjecture-nets.mjs';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
await prepareConjectureNets(root,{check:true});
const html=await fs.readFile(path.join(root,'website/public/experiments/conjecture-nets.html'));
const server=http.createServer((req,res)=>{if(req.url.split('?')[0]==='/experiments/conjecture-nets.html'){res.setHeader('Content-Type','text/html; charset=utf-8');res.end(html);}else{res.statusCode=404;res.end();}});
await new Promise(r=>server.listen(0,'127.0.0.1',r));
let browser;
try {
  browser=await chromium.launch({headless:true});
  for (const [mode,url] of [['file',pathToFileURL(path.join(root,'website/public/experiments/conjecture-nets.html')).href],['http',`http://127.0.0.1:${server.address().port}/experiments/conjecture-nets.html`]]) {
    const page=await browser.newPage({viewport:{width:1440,height:960},reducedMotion:'reduce'}),errors=[];
    page.on('pageerror',e=>errors.push(e.message));
    await page.goto(url);await page.locator('#graph .graph-node').first().waitFor();
    assert.equal(await page.locator('#net-select option').count(),5);
    assert.equal(await page.locator('#graph .graph-node').count(),7);
    assert.equal(await page.locator('#results').isVisible(),false);
    assert.equal(await page.locator('#drawer').getAttribute('aria-hidden'),'true');
    const size=await page.locator('#graph-scroll').boundingBox();assert.equal(size.height,864);assert.equal(size.width,1440);
    await page.locator('#search').fill('nonexistent-needle');assert.equal(await page.locator('.node-item').count(),0);assert.equal(await page.locator('#graph .graph-node').count(),7);
    await page.locator('#search').fill('');await page.locator('#filter').selectOption('frontier');assert.equal(await page.locator('.node-item').count(),2);
    await page.locator('#filter').selectOption('all');
    await page.locator('.graph-node[data-id="three-vertex-overlap-candidate"]').focus();await page.keyboard.press('Enter');
    assert.equal(await page.locator('#drawer').getAttribute('aria-hidden'),'false');
    assert.match(await page.locator('#details').innerText(),/Formal outcome: none recorded/);
    assert.match(await page.locator('#details').innerText(),/eighteen primitive usages/);
    // Overlay never consumes graph width; closing deselects and Escape restores focus.
    assert.equal((await page.locator('#graph-scroll').boundingBox()).width,1440);
    await page.keyboard.press('Escape');assert.equal(await page.locator('#drawer').getAttribute('aria-hidden'),'true');assert.equal(await page.locator('.graph-node.selected').count(),0);
    await page.locator('#net-select').selectOption('scattering.low-energy.research.v3');
    await page.locator('.graph-node[data-id="seed-composition-external-obligation"]').click();
    await page.getByRole('button',{name:/Open Arrow seeds & isotope atlas:/}).click();
    assert.equal(await page.locator('#net-select').inputValue(),'scattering.seed-composition.research.v1');
    await page.reload();assert.match(await page.locator('#details h2').innerText(),/admissible composition/);
    await page.locator('#close-details').click();await page.locator('.graph-node[data-id="isotope-atlas-evidence"]').click();
    const sourceHref=await page.locator('#details a').first().getAttribute('href');assert.ok(sourceHref.startsWith(mode==='file'?'../../../research/':'https://github.com/'));
    await page.locator('#close-details').click();
    const downloadPromise=page.waitForEvent('download');await page.locator('#download').click();const download=await downloadPromise;const saved=JSON.parse(await fs.readFile(await download.path(),'utf8'));assert.equal(saved.id,'scattering.seed-composition.research.v1');
    const dependencyCount=await page.locator('#graph .edge').count();
    await page.locator('#tab-ports').click();assert.equal(await page.locator('.port').count(),28);
    assert.ok(dependencyCount>0);assert.equal(await page.locator('.dependency-edge').count(),dependencyCount);
    assert.equal(await page.locator('.implication-edge:not(.dependency-edge)').count(),0);
    assert.match(await page.locator('#port-notice').innerText(),/No explicit outcome implications/);
    assert.equal(await page.locator('.dependency-edge .ink').first().getAttribute('stroke-dasharray'),'7 5');
    await page.locator('.dependency-edge').first().focus();await page.keyboard.press('Enter');
    assert.match(await page.locator('#details').innerText(),/Research dependency \(dashed\), not an outcome implication/);
    assert.equal(await page.locator('.dependency-edge.selected').count(),1);
    await page.locator('#close-details').click();
    // Existing scientific proof relations, not inferred scattering implications.
    await page.locator('#net-select').selectOption({label:'Proof-outcome net · local core'});
    assert.equal(await page.locator('.port').count(),72);assert.equal(await page.locator('.implication-edge').count(),7);assert.equal(await page.locator('.and-gate').count(),1);
    assert.match(await page.locator('#port-notice').innerText(),/5 declared implications. 2 non-outcome relations omitted/);
    const fixture={id:'port-fixture',conjectures:['a','b','c','d','e'].map(id=>({id,title:'Conjecture '+id,depends_on:id==='d'?['a']:[]})),port_implications:[
      {id:'ab',from:{node:'a',port:'++'},to:{node:'b',port:'++'},weight:4},
      {id:'bc',from:{node:'b',port:'++'},to:{node:'c',port:'-+'},weight:1},
      {id:'and',premises:[{node:'b',port:'++'},{node:'d',port:'++'}],to:{node:'e',port:'++'},weight:2}
    ]};
    await page.locator('#import-file').setInputFiles({name:'ports.json',mimeType:'application/json',buffer:Buffer.from(JSON.stringify(fixture))});
    await page.waitForFunction(()=>document.querySelector('#net-select').value==='port-fixture');
    assert.equal(await page.evaluate(()=>d3.version),'7.9.0');assert.equal(await page.locator('.port').count(),20);
    const port=page.locator('.port[data-node="a"][data-port="++"]');await port.focus();await page.keyboard.press('Enter');
    assert.equal(await page.locator('.force-node[data-id="a"]').evaluate(x=>x.classList.contains('dim')),false);
    assert.equal(await page.locator('.force-node[data-id="c"]').evaluate(x=>x.classList.contains('dim')),false);
    assert.equal(await page.locator('.force-node[data-id="d"]').evaluate(x=>x.classList.contains('dim')),true);
    assert.equal(await page.locator('.dependency-edge').evaluate(x=>x.classList.contains('dim')),true);
    assert.equal(await page.locator('.force-node[data-id="e"]').evaluate(x=>x.classList.contains('dim')),true);
    assert.equal(await page.locator('.port[data-node="a"][data-port="--"]').evaluate(x=>x.classList.contains('dim')),true);
    assert.equal(await page.locator('.implication-edge[data-rule="and"]').first().evaluate(x=>x.classList.contains('dim')),true);
    await page.locator('#close-details').click();assert.equal(await page.locator('#port-graph .dim').count(),0);
    await port.click();assert.match(await page.locator('#details h2').first().innerText(),/prove: proved/);
    await page.locator('#close-details').click();
    const edgePoint=await page.locator('.implication-edge[data-rule="bc"] .hit').evaluate(p=>{
      const length=p.getTotalLength(),matrix=p.getScreenCTM();
      for(let i=2;i<48;i++){const point=p.getPointAtLength(length*i/50).matrixTransform(matrix);const hit=document.elementFromPoint(point.x,point.y);if(hit?.closest('.implication-edge')===p.parentElement)return {x:point.x,y:point.y};}
      return null;
    });
    assert.ok(edgePoint,'implication must have a visible pointer-clickable segment');
    await page.mouse.click(edgePoint.x,edgePoint.y);assert.equal(await page.locator('#details h2').innerText(),'bc');
    await page.locator('#close-details').click();
    const edge=page.locator('.implication-edge[data-rule="and"]').last();await edge.focus();await page.keyboard.press('Enter');
    assert.match(await page.locator('#details').innerText(),/ALL premises required/);
    assert.equal(await page.locator('.force-node[data-id="e"]').evaluate(x=>x.classList.contains('dim')),false);
    assert.equal(await page.locator('.force-node[data-id="a"]').evaluate(x=>x.classList.contains('dim')),true);
    await page.locator('#close-details').click();
    const widths=await page.locator('.implication-edge').evaluateAll(gs=>Object.fromEntries(gs.map(g=>[g.dataset.rule,Number(g.querySelector('.ink').getAttribute('stroke-width'))])));assert.ok(widths.ab>widths.bc);
    assert.equal(await page.locator('.implication-edge[data-rule="ab"] .edge-weight').textContent(),'4');
    assert.equal(await page.locator('.implication-edge[data-rule="bc"] .edge-weight').textContent(),'1');
    const beforeGravity=await page.locator('.force-node').evaluateAll(ns=>ns.map(n=>n.getAttribute('transform')));
    await page.locator('#port-gravity').fill('0.18');
    assert.equal(await page.locator('#port-gravity-value').textContent(),'0.18');
    const afterGravity=await page.locator('.force-node').evaluateAll(ns=>ns.map(n=>n.getAttribute('transform')));
    assert.notDeepEqual(afterGravity,beforeGravity);
    await page.waitForTimeout(100);
    assert.deepEqual(await page.locator('.force-node').evaluateAll(ns=>ns.map(n=>n.getAttribute('transform'))),afterGravity);
    assert.equal(await page.locator('#port-pause').textContent(),'Resume layout');
    await page.locator('#tab-dependencies').click();assert.equal(await page.locator('#tab-dependencies').getAttribute('aria-selected'),'true');
    const malicious={id:'hostile-local',conjectures:[{id:'x',statement:'<img src=x onerror="globalThis.pwned=1">',status:'open',depends_on:[],evidence:['javascript:alert(1)']}],frontier:['x']};
    await page.locator('#import-file').setInputFiles({name:'hostile.json',mimeType:'application/json',buffer:Buffer.from(JSON.stringify(malicious))});
    await page.waitForFunction(()=>document.querySelector('#net-select').value==='hostile-local');await page.locator('.graph-node').click();
    assert.equal(await page.locator('#details img').count(),0);assert.equal(await page.evaluate(()=>globalThis.pwned),undefined);assert.equal(await page.locator('#details a').count(),0);
    await page.locator('#close-details').click();await page.locator('#import-file').setInputFiles({name:'bad.json',mimeType:'application/json',buffer:Buffer.from('{')});await page.waitForFunction(()=>document.querySelector('#error').textContent.includes('Cannot import'));
    await page.setViewportSize({width:390,height:844});await page.locator('#net-select').selectOption('scattering.low-energy.research.v3');
    assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
    assert.ok(Math.abs((await page.locator('#graph-scroll').boundingBox()).height-844*.9)<1);
    await page.locator('.graph-node').first().click();assert.ok((await page.locator('#drawer').boundingBox()).width<=390);
    await page.locator('#close-details').click();await page.locator('#zoom-in').click();await page.locator('#fit').click();
    const clipped=await page.locator('.graph-node').evaluateAll(groups=>groups.some(g=>{const box=g.querySelector('rect'),w=Number(box.getAttribute('width')),h=Number(box.getAttribute('height'));return [...g.querySelectorAll('text')].some(t=>{const b=t.getBBox();return b.x<0||b.y<0||b.x+b.width>w||b.y+b.height>h;});}));assert.equal(clipped,false);
    assert.deepEqual(errors,[]);await page.close();console.log(mode+': full-width 90vh, closable drawer, tabs, D3 weights, port/AND reachability, safe import, mobile passed');
  }
} finally {if(browser)await browser.close();await new Promise(r=>server.close(r));}
