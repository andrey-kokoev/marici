import http from 'node:http';
import fs from 'node:fs/promises';
import path from 'node:path';
import {chromium} from '@playwright/test';
import * as T from 'three';
import {worldPoint} from '../research/realization-tower/normal-ray-model.mjs';
import {fibrationDisplayEnvelope as env} from '../research/realization-tower/fibration12-process.mjs';
const root=process.cwd(),out='research/strominger/results/fibration12-viewer';
const server=http.createServer(async(req,res)=>{try{const p=path.resolve(root,'.'+new URL(req.url,'http://localhost').pathname);if(!p.startsWith(root+path.sep))throw Error('path');res.setHeader('Content-Type',({'.html':'text/html','.js':'text/javascript','.css':'text/css'})[path.extname(p)]??'text/plain');res.end(await fs.readFile(p));}catch{res.statusCode=404;res.end();}});
await new Promise(r=>server.listen(0,'127.0.0.1',r));let browser;
try{
 browser=await chromium.launch();const page=await browser.newPage({viewport:{width:1500,height:1100}});
 await page.goto(`http://127.0.0.1:${server.address().port}/research/realization-tower/normal-ray.html`);
 await page.waitForFunction(()=>globalThis.NormalRayViewer?.snapshot().draws>0);
 await page.selectOption('#process-select','fibration-12x12');await page.waitForFunction(()=>normalRayAudit.processId==='fibration-12x12');
 for(let s=1;s<=5;s++){await page.click('#next');await page.waitForFunction(s=>normalRayAudit.proceduralStep===s,s);}
 await page.click('#reset-view');await page.click('#role-label-toggles');await page.uncheck('#grid');
 const verts=[...env.slice(0,4),env[5]].map(p=>new T.Vector3(...worldPoint(p)));
 for(const [name,ids,inside] of [['F423',[3,1,2],0],['F453',[3,4,2],0],['F154',[0,4,3],2],['F124',[0,1,3],2],['F351',[2,4,0],3],['F321',[2,1,0],3]]){
  await page.click('#reset-view');await page.waitForTimeout(250);
  const [a,b,c]=ids.map(i=>verts[i]);const normal=b.clone().sub(a).cross(c.clone().sub(a)).normalize();
  if(normal.dot(verts[inside].clone().sub(a))>0)normal.negate();
  const spherical=new T.Spherical().setFromVector3(normal),azimuth=T.MathUtils.radToDeg(spherical.theta),elevation=90-T.MathUtils.radToDeg(spherical.phi);
  await page.locator('#azimuth').evaluate((e,v)=>{e.value=String(v);e.dispatchEvent(new Event('input',{bubbles:true}));},azimuth);
  await page.waitForTimeout(250);
  await page.locator('#elevation').evaluate((e,v)=>{e.value=String(v);e.dispatchEvent(new Event('input',{bubbles:true}));},elevation);
  await page.waitForTimeout(250);
  await page.screenshot({path:`${out}/inspect-${name}.png`});
  console.log(name,JSON.stringify(await page.evaluate(()=>({view:normalRayViewAudit.azimuth,elevation:normalRayViewAudit.elevation,step:normalRayAudit.proceduralStep}))));
 }
}finally{await browser?.close();await new Promise(r=>server.close(r));}
