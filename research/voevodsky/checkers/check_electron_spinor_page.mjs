import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {chromium} from '@playwright/test';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const asset=path.join(root,'website/.vitepress/dist/experiments/electron-spinor-construction.html');
const source=JSON.parse(await fs.readFile(path.join(root,'research/voevodsky/results/electron_tetrahedral_spinor_store.json'),'utf8'));
const frac=s=>{const p=s.split('/').map(Number);return p.length===1?p[0]:p[0]/p[1];};
const real=p=>frac(p[0])+Math.sqrt(3)*frac(p[1]);
const decode=z=>z.map(real);
const error=(a,b)=>Math.max(...a.map((x,i)=>Math.abs(x-b[i])));
const browser=await chromium.launch({headless:true,args:['--enable-unsafe-swiftshader']});
const errors=[];let tested=0;
try{
 const page=await browser.newPage({viewport:{width:1500,height:1000}});page.on('pageerror',e=>errors.push(e.message));
 await page.goto(pathToFileURL(asset).href);
 await page.waitForFunction(()=>window.electronAssemblyAudit||!document.querySelector('#error').hidden,null,{timeout:30000});
 async function audit(){assert.equal(await page.locator('#error').isVisible(),false,await page.locator('#error').textContent());const a=await page.evaluate(()=>window.electronAssemblyAudit);assert(a);assert(Math.abs(a.totalWeight-1)<1e-10);assert(Math.abs(a.polarization+1)<1e-10);assert(a.reconstructionError<1e-10&&a.covarianceError<1e-10);tested++;return a;}
 for(let i=0;i<6;i++){await page.locator(`[data-step="${i}"]`).click();await page.waitForTimeout(850);await audit();}
 let a=await audit();
 source.normals.forEach((n,i)=>assert(error(a.normals[i],n.map(real))<1e-12));
 source.face_projectors.forEach((P,i)=>{for(let k=0;k<2;k++)assert(error(a.faceStates[i][k],decode(P[k][0]).map(v=>v/Math.sqrt(2)))<1e-12);});
 for(const [t,p]of [[0,0],[180,0],[45,30],[90,90],[120,-60]]){await page.locator('#theta').fill(String(t));await page.locator('#theta').dispatchEvent('input');await page.locator('#phi').fill(String(p));await page.locator('#phi').dispatchEvent('input');await audit();}
 await page.locator('#zero-face').click();a=await audit();assert(a.weights[0]<1e-12);
 for(const [angle,sign]of [[360,-1],[720,1],[0,1]]){await page.locator('#turn'+angle).click();await page.waitForTimeout(1450);a=await audit();assert(Math.abs(a.angleDegrees-angle)<1e-10);assert(error(a.referenceOverlap,[sign,0])<1e-10);for(let k=0;k<2;k++)assert(error(a.spinor[k],a.reference[k].map(x=>sign*x))<1e-10);}
 assert.equal(await page.locator('canvas').count(),1);
 await page.setViewportSize({width:600,height:900});await page.waitForTimeout(150);await audit();
 assert.deepEqual(errors,[]);
 const old=await fs.readFile(path.join(root,'website/.vitepress/dist/experiments/proton-neutron-assembly.html'),'utf8');assert(old.includes('href="electron-spinor-construction.html"'));
 const ledger=await fs.readFile(path.join(root,'website/.vitepress/dist/research/ledger/20261009-4316-electron-coupling-from-retained-phase-and-spinor-pairing/index.html'),'utf8');assert(ledger.includes('href="/experiments/electron-spinor-construction.html"'));
 const result={verification_passed:true,stage_count:6,audited_states:tested,exact_store_normals_and_seed_projection_match:true,zero_face_preserves_full_state:true,rotation_360_opposite_sign:true,rotation_720_original_sign:true,mobile_resize:true,existing_page_and_ledger_links:true,page_errors:errors};
 await fs.writeFile(path.join(root,'research/voevodsky/results/electron_spinor_browser.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result,null,2));
}finally{await browser.close();}
