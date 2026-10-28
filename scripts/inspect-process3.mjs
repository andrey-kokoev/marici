// Reproducible visual + geometric inspection. No external servers/assets.
// node scripts/inspect-process3.mjs --k 5,7 --step 6 [--out DIRECTORY]
import http from 'node:http';
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import {fileURLToPath} from 'node:url';
import {chromium} from '@playwright/test';
import {prepareNormalRay} from './prepare-normal-ray.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const option=(name,fallback)=>{const i=process.argv.indexOf(name);return i<0?fallback:process.argv[i+1];};
const ks=option('--k','5,7').split(',').map(Number),step=Number(option('--step','6'));
if(ks.some(k=>!Number.isInteger(k)||k<1||k>7)||!Number.isInteger(step)||step<0||step>7)throw Error('Use k=1..7 and step=0..7');
const out=path.resolve(option('--out',await fs.mkdtemp(path.join(os.tmpdir(),'process3-visual-'))));await fs.mkdir(out,{recursive:true});
await prepareNormalRay(root);
const server=http.createServer(async(req,res)=>{
 try{
  const file=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));
  if(!file.startsWith(root+path.sep))throw Error('Outside root');
  const data=await fs.readFile(file);res.setHeader('Content-Type',({'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json'})[path.extname(file)]??'application/octet-stream');res.end(data);
 }catch{res.statusCode=404;res.end('Not found');}
});
await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
let browser;
try{
 browser=await chromium.launch();
 for(const k of ks){
  const page=await browser.newPage({viewport:{width:1200,height:900}}),errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  await page.route('**/*',r=>new URL(r.request().url()).hostname==='127.0.0.1'?r.continue():r.abort());
  await page.addInitScript(k=>localStorage.setItem('marici:isotope-constructor:v1:scene-settings',JSON.stringify({version:1,process:{id:'diamond-construction',k,step:0,branch:1},appearance:{grid:false,bodies:false,faceOpacity:.65,labels:true}})),k);
  await page.goto(`http://127.0.0.1:${server.address().port}/research/realization-tower/normal-ray.html`);
  await page.waitForFunction(()=>globalThis.normalRayAudit?.processId==='diamond-construction');
  for(let i=0;i<step&&await page.locator('#next').isEnabled();i++){
   await page.locator('#next').click();await page.waitForFunction(n=>normalRayAudit.proceduralStep===n,i+1);
  }
  const audit=await page.evaluate(()=>({construction:normalRayAudit,view:normalRayViewAudit,summary:document.querySelector('#procedure').textContent,counts:[...document.querySelectorAll('#particle-counts tbody tr')].map(r=>r.textContent)}));
  await fs.writeFile(path.join(out,`k${k}-audit.json`),JSON.stringify(audit,null,2));
  await page.locator('#close-process').click();await page.locator('#close-scene').click();
  await page.evaluate(({k,step,core,orientations})=>{
   const label=document.createElement('div');label.id='visual-audit-caption';label.style.cssText='position:absolute;left:12px;top:12px;z-index:10;background:#101827dd;color:white;padding:10px;font:14px monospace;pointer-events:none';
   label.textContent=`Visual audit: k=${k}, step=${step}, core=${core}, branch orientations=${orientations}`;document.querySelector('#scene').append(label);
  },{k,step:audit.construction.proceduralStep,core:audit.construction.radial.centralCell,orientations:audit.construction.radial.orientationCount});
  await page.waitForTimeout(150);await page.locator('#scene').screenshot({path:path.join(out,`k${k}-overview.png`)});
  const focus=audit.construction.radial.centralCell??audit.construction.radial.centerCandidates[0];
  await page.evaluate(cell=>NormalRayViewer.inspectView({cell,zoom:3}),focus);
  await page.waitForFunction(cell=>normalRayViewAudit.inspection?.cell===cell&&Math.abs(normalRayViewAudit.inspection.ndc[0])<1e-6&&Math.abs(normalRayViewAudit.inspection.ndc[1])<1e-6,focus);
  await page.locator('#scene').screenshot({path:path.join(out,`k${k}-core.png`)});
  for(const axis of ['x','y','z']){
   await page.evaluate(({cell,axis})=>NormalRayViewer.inspectView({cell,zoom:3,axis}),{cell:focus,axis});await page.waitForTimeout(100);
   if(!await page.evaluate(()=>normalRayViewAudit.inspection.ndc.slice(0,2).every(x=>Math.abs(x)<1e-6)))throw Error('Core is not centered in inspection view');
   await page.locator('#scene').screenshot({path:path.join(out,`k${k}-${axis}.png`)});
  }
  if(JSON.stringify(await page.evaluate(()=>normalRayAudit.assignments))!==JSON.stringify(audit.construction.assignments))throw Error('Inspection changed construction');
  if(errors.length)throw Error(errors.join('\n'));
  console.log(JSON.stringify({k,step:audit.construction.proceduralStep,center:audit.construction.radial.centralCell,orientationCount:audit.construction.radial.orientationCount,assignments:audit.construction.assignments.map(a=>[a.cell,a.role]),out}));
  await page.close();
 }
}finally{await browser?.close();await new Promise(resolve=>server.close(resolve));}
