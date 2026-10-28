import {createServer} from 'vite';
import {chromium} from '@playwright/test';
import fs from 'node:fs/promises';
const server=await createServer({configFile:false,root:'examples/realization-lattice',server:{host:'127.0.0.1',port:0},logLevel:'error'});
let browser;
try{
 await server.listen();browser=await chromium.launch({headless:true,args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});
 const page=await browser.newPage({viewport:{width:1100,height:760},deviceScaleFactor:2});
 await page.addInitScript(()=>{
  window.profile={callbacks:[],draws:0};
  const raf=window.requestAnimationFrame.bind(window);
  window.requestAnimationFrame=cb=>raf(t=>{const start=performance.now();cb(t);window.profile.callbacks.push(performance.now()-start);});
  for(const proto of [WebGLRenderingContext.prototype,WebGL2RenderingContext.prototype])for(const name of ['drawArrays','drawElements','drawArraysInstanced','drawElementsInstanced'])if(Object.hasOwn(proto,name)){
   const original=proto[name];proto[name]=function(...args){window.profile.draws++;return original.apply(this,args);};
  }
 });
 await page.goto(`http://127.0.0.1:${server.httpServer.address().port}/`);await page.waitForFunction(()=>document.querySelector('#fallback').hidden);
 const results=[];
 for(const mode of ['default','extent6','helium']){
  if(mode==='extent6'){await page.locator('#extent').evaluate(el=>{el.value='6';el.dispatchEvent(new Event('input'));});}
  if(mode==='helium')await page.locator('#helium-preset').click();
  await page.waitForTimeout(400);
  await page.evaluate(()=>window.profile={callbacks:[],draws:0});await page.waitForTimeout(300);
  const idle=await page.evaluate(()=>({callbacks:window.profile.callbacks.length,draws:window.profile.draws}));
  await page.evaluate(()=>window.profile={callbacks:[],draws:0});
  const b=await page.locator('canvas').boundingBox();
  await page.mouse.move(b.x+b.width*.4,b.y+b.height*.4);await page.mouse.down();
  for(let i=0;i<35;i++){await page.mouse.move(b.x+b.width*.4+i*3,b.y+b.height*.4+i);await page.waitForTimeout(16);}
  await page.mouse.up();await page.waitForTimeout(100);
  const data=await page.evaluate(()=>{const a=window.profile.callbacks.toSorted((a,b)=>a-b);return {callbacks:a.length,draws:window.profile.draws,callbackMedianMs:a[Math.floor(a.length*.5)],callbackP95Ms:a[Math.floor(a.length*.95)],canvasPixels:document.querySelector('canvas').width*document.querySelector('canvas').height};});
  results.push({mode,idle,...data});
 }
 const output={environment:'Headless Chromium, SwiftShader software GL, 1100x760, DPR2. CPU callback durations are not physical GPU frame timings.',results};
 const file=process.argv[2]||'research/realization-tower/results/lattice-ui/profile.json';await fs.mkdir(new URL('../research/realization-tower/results/lattice-ui/',import.meta.url),{recursive:true});await fs.writeFile(file,JSON.stringify(output,null,2)+'\n');console.log(JSON.stringify(output));
}finally{await browser?.close();await server.close();}
