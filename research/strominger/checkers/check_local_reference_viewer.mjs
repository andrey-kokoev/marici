import assert from 'node:assert/strict';
import {createServer} from 'node:http';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import path from 'node:path';
import {chromium} from '@playwright/test';
import {createLocalReferenceDisplay} from '../demos/particle-overlap-tetrahedron/local-reference-display.mjs';
const root=process.cwd(),out='research/strominger/results/local-reference-viewer',targets={'nitrogen15-local':{proton:7,neutron:8,electron:7},'oxygen16-local':{proton:8,neutron:8,electron:8},'oxygen17-local':{proton:8,neutron:9,electron:8},'oxygen18-local':{proton:8,neutron:10,electron:8},'fluorine19-local':{proton:9,neutron:10,electron:9},'neon20-local':{proton:10,neutron:10,electron:10},'neon22-local':{proton:10,neutron:12,electron:10}};
for(const [id,target] of Object.entries(targets)){const m=createLocalReferenceDisplay(id);assert.deepEqual(m.snapshot().counts,target);for(let n=1;n<=m.fullItems().length;n++){m.setShown(n);assert.equal(m.snapshot().items.length,n);}m.next();assert.equal(m.snapshot().items.length,1);m.previous();assert.equal(m.snapshot().items.length,m.fullItems().length);assert.throws(()=>m.setShown(0));}
await mkdir(out,{recursive:true});const server=createServer(async(req,res)=>{try{const file=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));if(!file.startsWith(root+path.sep))throw Error('Invalid path');const data=await readFile(file);res.setHeader('Content-Type',file.endsWith('.html')?'text/html':/\.(mjs|js)$/.test(file)?'text/javascript':file.endsWith('.css')?'text/css':'application/octet-stream');res.end(data);}catch{res.statusCode=404;res.end();}});await new Promise(r=>server.listen(0,'127.0.0.1',r));let browser;
try{
 browser=await chromium.launch({headless:true,args:['--no-sandbox','--enable-webgl','--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});const page=await browser.newPage({viewport:{width:1400,height:1000}}),errors=[];page.on('pageerror',e=>{errors.push(e.message);console.error(e.message);});page.on('console',m=>{if(m.type()==='error')console.error(m.text());});
 await page.goto(`http://127.0.0.1:${server.address().port}/public/experiments/particle-overlap-tetrahedron/vacuum.html`);await page.waitForFunction(()=>!!globalThis.FiberSpaceViewer);const results=[];
 for(const [id,target] of Object.entries(targets)){
  await page.selectOption('#comparison-atom','none');await page.selectOption('#atom',id);const s=await page.evaluate(()=>FiberSpaceViewer.snapshot());assert.deepEqual(s.atomCounts,target);assert.equal(s.assemblyDisplay.mode,'local-reference');assert.equal(s.visibleComponentCount,Object.values(target).reduce((a,b)=>a+b,0));assert.equal(s.phaseAudit.globalSewingAsserted,false);assert.match(await page.locator('#loadout-readout').textContent(),/no global sewing/);
  await page.evaluate(()=>FiberSpaceViewer.previousItem());assert.equal((await page.evaluate(()=>FiberSpaceViewer.snapshot())).assemblyDisplay.shown,s.assemblyDisplay.total-1);await page.evaluate(()=>FiberSpaceViewer.nextItem());
  await page.screenshot({path:out+'/'+id+'.png'});results.push({id,counts:s.atomCounts,visibleComponents:s.visibleComponentCount});
 }
 await page.selectOption('#atom','nitrogen15-local');await page.selectOption('#comparison-atom','oxygen16-local');let pair=await page.evaluate(()=>({a:FiberSpaceViewer.sequentialSnapshot(),b:FiberSpaceViewer.comparisonSnapshot(),s:FiberSpaceViewer.snapshot()}));assert.deepEqual(pair.a.counts,targets['nitrogen15-local']);assert.deepEqual(pair.b.counts,targets['oxygen16-local']);assert.equal(pair.s.comparison.visibleComponents,24);await page.screenshot({path:out+'/comparison.png'});
 // New reference as Shape 2 with the old default, on a fresh page, exercises
 // dynamic comparison geometry not already materialized by Shape 1.
 await page.reload();await page.waitForFunction(()=>!!globalThis.FiberSpaceViewer);for(const [id,target] of Object.entries(targets)){await page.selectOption('#comparison-atom',id);assert.deepEqual(await page.evaluate(()=>FiberSpaceViewer.comparisonSnapshot().counts),target);}
 assert.equal(await page.locator('#atom option[value="nitrogen15"]').count(),1);assert.deepEqual(errors,[]);await writeFile(out+'/verification.json',JSON.stringify({status:'local-reference-viewer-passed',results,comparison:true,freshComparisonGeometry:true,displayPrefixes:true,originalNitrogen15OptionPreserved:true,pageErrors:errors},null,2)+'\n');console.log('Local references passed model and browser checks');
}finally{await browser?.close();await new Promise(r=>server.close(r));}
