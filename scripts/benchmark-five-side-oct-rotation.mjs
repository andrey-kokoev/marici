import http from 'node:http';
import fs from 'node:fs/promises';
import path from 'node:path';
import {chromium} from '@playwright/test';
const option=(name,fallback)=>Number(process.argv.find(a=>a.startsWith(`--${name}=`))?.split('=')[1]??fallback);
const width=option('width',1280),height=option('height',720),faceOpacity=option('face-opacity',1);
const root=process.cwd(),server=http.createServer(async(req,res)=>{
 try{const p=path.resolve(root,'.'+new URL(req.url,'http://localhost').pathname);if(!p.startsWith(root+path.sep))throw Error('path');res.setHeader('Content-Type',({'.html':'text/html','.js':'text/javascript','.css':'text/css'})[path.extname(p)]??'text/plain');res.end(await fs.readFile(p));}catch{res.statusCode=404;res.end();}
});
await new Promise(r=>server.listen(0,'127.0.0.1',r));let browser;
try{
 browser=await chromium.launch({headless:!process.argv.includes('--headed')});const page=await browser.newPage({viewport:{width,height}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(`http://127.0.0.1:${server.address().port}/website/public/experiments/native-belt/index.html`);
 await page.waitForFunction(()=>globalThis.normalRayAudit);
 await page.selectOption('#process-select','ruthenium-98');await page.selectOption('#ruthenium-98-view','wiring');
 await page.waitForFunction(()=>globalThis.normalRayAudit?.rutheniumWiringAudit?.status==='coherent-port-routing');
 await page.locator('#face-opacity').evaluate((el,value)=>{el.value=String(value);el.dispatchEvent(new Event('input',{bubbles:true}));},faceOpacity);
 const result=await page.evaluate(async()=>{
  const gl=[...document.querySelectorAll('canvas')].map(c=>c.getContext('webgl2')).find(Boolean),ext=gl?.getExtension('WEBGL_debug_renderer_info');
  const gpu=ext?gl.getParameter(ext.UNMASKED_RENDERER_WEBGL):gl?.getParameter(gl.RENDERER);
  const speed=document.querySelector('#rotation-speed');speed.value='1';speed.dispatchEvent(new Event('input',{bubbles:true}));
  await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
  const start=performance.now(),intervals=[];let lastTime=start,lastView=globalThis.normalRayViewAudit,lastAngle=lastView.azimuth,totalDegrees=0;
  document.querySelector('#auto-rotate').click();
  return await new Promise(resolve=>{
   function sample(){
    const now=performance.now(),view=globalThis.normalRayViewAudit;
    if(view!==lastView){
     const delta=((view.azimuth-lastAngle+540)%360)-180;
     if(Math.abs(delta)>1e-7){totalDegrees+=Math.abs(delta);intervals.push(now-lastTime);lastTime=now;}
     lastAngle=view.azimuth;lastView=view;
    }
    if(totalDegrees>=360||now-start>240000){
     document.querySelector('#auto-rotate').click();
     const sorted=[...intervals].sort((a,b)=>a-b),percentile=p=>sorted[Math.min(sorted.length-1,Math.floor(sorted.length*p))];
     resolve({gpu,viewport:[innerWidth,innerHeight],speed:1,faceOpacity:document.querySelector('#face-opacity').value,completed:totalDegrees>=360,degrees:totalDegrees,seconds:(now-start)/1000,frames:intervals.length,averageFps:intervals.length/((now-start)/1000),frameMs:{median:percentile(.5),p95:percentile(.95),max:Math.max(...intervals)},idealSeconds:2*Math.PI/.3,audit:globalThis.normalRayAudit.rutheniumWiringAudit.rendered});return;
    }
    requestAnimationFrame(sample);
   }
   requestAnimationFrame(sample);
  });
 });
 console.log(JSON.stringify({...result,errors},null,2));
 if(!result.completed||errors.length)process.exitCode=1;
}finally{await browser?.close();await new Promise(r=>server.close(r));}
