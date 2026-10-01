import assert from 'node:assert/strict';
import { fileURLToPath } from 'node:url';
import { chromium } from '@playwright/test';

// Independent Rodrigues rotation, separate from the page's quaternions.
function rotate(v,n,t){
  const c=Math.cos(t),s=Math.sin(t),dot=v.reduce((a,x,i)=>a+x*n[i],0);
  const cross=[n[1]*v[2]-n[2]*v[1],n[2]*v[0]-n[0]*v[2],n[0]*v[1]-n[1]*v[0]];
  return v.map((x,i)=>c*x+s*cross[i]+(1-c)*dot*n[i]);
}
const C=[.5,Math.sqrt(3)/2,0],D=[-.5,Math.sqrt(3)/2,0];
const browser = await chromium.launch({headless:true,args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});
try {
  const page=await browser.newPage({viewport:{width:1280,height:900}});
  const errors=[];const network=[];
  page.on('pageerror',error=>errors.push(error.message));
  page.on('request',request=>{if(/^https?:/.test(request.url()))network.push(request.url());});
  await page.route(/^https?:/,route=>route.abort());
  await page.goto(new URL('./index.html',import.meta.url).href);
  await page.waitForFunction(()=>Boolean(window.pawCycle));
  assert.equal(await page.locator('#error').isVisible(),false);
  for(let i=0;i<=200;i++){
    const s=await page.evaluate(t=>{window.pawCycle.setProgress(t);return window.pawCycle.snapshot();},i/200);
    const expectedD=rotate(rotate(D,C,s.theta),D,s.phi);
    const expectedC=rotate(C,D,s.phi);
    for(let j=0;j<3;j++){
      assert.ok(Math.abs(s.points.D[j]-expectedD[j])<1e-10);
      assert.ok(Math.abs(s.points.C[j]-expectedC[j])<1e-10);
    }
    assert.ok(Math.abs(s.geometricVolume-Math.sin(s.theta)/8)<1e-10);
    for(const [edge,renderedLength] of Object.entries(s.visibleEdges)){
      const [a,b]=[s.points[edge[0]],s.points[edge[1]]];
      const length=Math.hypot(...a.map((x,i)=>x-b[i]));
      assert.ok(Math.abs(length-1)<1e-10,`Endpoint length ${edge} at ${s.progress}: ${length}`);
      assert.ok(Math.abs(renderedLength-1)<1e-10,`Rendered length ${edge}: ${renderedLength}`);
    }
  }
  await page.locator('[data-stage="3"]').click();
  assert.equal(await page.locator('#packets').textContent(),'12');
  assert.equal(await page.locator('#edges').textContent(),'6');
  assert.equal(await page.locator('#volume').textContent(),'0.1179');
  const finalState=await page.evaluate(()=>window.pawCycle.snapshot());
  assert.equal(Object.keys(finalState.visibleEdges).length,6);
  assert.ok(Math.abs(finalState.geometricVolume-Math.sqrt(2)/12)<1e-10);
  assert.equal(await page.locator('[data-stage="3"]').getAttribute('aria-pressed'),'true');
  await page.locator('#traces').uncheck();
  await page.screenshot({path:fileURLToPath(new URL('./preview.png',import.meta.url)),fullPage:true});
  await page.locator('#faces').uncheck();
  await page.locator('#faces').check();
  await page.locator('#reset').click();
  assert.equal(await page.locator('#packets').textContent(),'8');
  await page.locator('#play').click();
  await page.waitForFunction(()=>window.pawCycle.snapshot().progress>0.005);
  await page.locator('#play').click();
  const paused=await page.evaluate(()=>window.pawCycle.snapshot().progress);
  await page.waitForTimeout(100);
  assert.equal(await page.evaluate(()=>window.pawCycle.snapshot().progress),paused);
  await page.setViewportSize({width:390,height:844});
  await page.locator('[data-stage="3"]').click();
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  await page.screenshot({path:fileURLToPath(new URL('./preview-mobile.png',import.meta.url)),fullPage:true});
  assert.deepEqual(network,[],'The page must work offline.');
  assert.deepEqual(errors,[]);
  console.log('PASS: offline loading,201 coordinate/volume samples, every visible edge unit length, regular tetrahedron, controls and mobile layout.');
} finally { await browser.close(); }
