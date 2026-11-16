import { test } from 'node:test';
import assert from 'node:assert/strict';
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { chromium } from '@playwright/test';
import { defaults, fieldAt, sampleField, stepParticle, stepShuttle, initialTarget } from '../examples/two-attractor-field/model.js';

test('softened vector superposition, symmetry, zero weights and finite samples',()=>{
  assert.deepEqual(fieldAt(0,0,defaults()),{x:0,y:0,magnitude:0});
  assert.ok(fieldAt(0,0,{weightA:2,weightB:1}).x<0);
  assert.ok(fieldAt(0,0,{weightA:1,weightB:2}).x>0);
  for(const p of sampleField({weightA:0,weightB:0}))assert.equal(p.magnitude,0);
  const a=fieldAt(2,1,defaults()),b=fieldAt(-2,-1,defaults());
  assert.equal(a.x,-b.x);assert.equal(a.y,-b.y);
  for(const p of sampleField({weightA:5,weightB:5}))assert.ok(Number.isFinite(p.magnitude));
  assert.throws(()=>fieldAt(0,0,{weightA:-1,weightB:1}));
  assert.equal(fieldAt(-3,0,{weightA:1,weightB:0}).magnitude,0);
});

test('momentum persists, drag decays velocity, and force accelerates particles',()=>{
  const off={weightA:0,weightB:0},p={x:0,y:0,vx:2,vy:-1};
  const free=stepParticle(p,off,0,0.01);
  assert.deepEqual(free,{x:0.02,y:-0.01,vx:2,vy:-1});
  const damped=stepParticle(p,off,0.5,0.01);
  assert.ok(Math.abs(damped.vx-2*Math.exp(-0.005))<1e-12);
  assert.ok(stepParticle({x:0,y:1,vx:0,vy:0},defaults(),0,0.01).vy<0);
  let cloud=Array.from({length:100},(_,i)=>({x:-8+16*i/100,y:-5+10*i/100,vx:0,vy:0}));
  for(let i=0;i<1200;i++)cloud=cloud.map(p=>stepParticle(p,{weightA:5,weightB:5},0,1/120));
  assert.ok(cloud.every(p=>Object.values(p).every(Number.isFinite)));
  assert.throws(()=>stepParticle(p,off,-1,0.01));
});

test('pole passes alternate attraction and preserve velocity',()=>{
  assert.equal(initialTarget(-2,1),0);assert.equal(initialTarget(3,0),0);
  const p={x:-3.01,y:0,vx:2,vy:0};
  const result=stepShuttle(p,defaults(),0,0.01,0);
  assert.equal(result.target,1);assert.equal(result.switched,true);
  assert.deepEqual(result.particle,stepParticle(p,{weightA:1,weightB:0},0,0.01));
  assert.equal(stepShuttle({x:-3.01,y:2,vx:2,vy:0},defaults(),0,0.01,0).switched,false);
  let particle={x:-1,y:1,vx:0,vy:0},target=0,passes=[];
  for(let i=0;i<120*120;i++){
    const next=stepShuttle(particle,defaults(),0.3,1/120,target);
    particle=next.particle;target=next.target;if(next.switched)passes.push(target);
  }
  assert.ok(passes.length>=2);assert.deepEqual(passes.slice(0,2),[1,0]);
});

test('local-only browser draw, weights, idle rendering, mobile and WebGL fallback',async()=>{
  const root=new URL('../website/public/experiments/two-attractor-field/',import.meta.url);
  const server=createServer(async(req,res)=>{
    try {
      const pathname=new URL(req.url,'http://localhost').pathname;
      const file=new URL('.'+(pathname==='/'?'/index.html':pathname),root);
      if(!file.href.startsWith(root.href))throw Error('Invalid path');
      const body=await readFile(file);
      res.setHeader('Content-Type',file.pathname.endsWith('.js')?'text/javascript':file.pathname.endsWith('.css')?'text/css':'text/html');res.end(body);
    }catch{res.statusCode=404;res.end();}
  });
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  const browser=await chromium.launch({headless:true});
  try {
    const url=`http://127.0.0.1:${server.address().port}/`;
    const page=await browser.newPage(),errors=[];page.on('pageerror',e=>errors.push(e.message));
    await page.route('**/*',route=>route.request().url().startsWith(url)?route.continue():route.abort());
    await page.goto(url);await page.waitForFunction(()=>window.ReferenceViewer?.snapshot().draws>0);
    assert.equal(await page.evaluate(()=>THREE.REVISION),'128');
    assert.equal(await page.locator('#fallback').isVisible(),false,await page.locator('#status').innerText());
    const camera=await page.evaluate(()=>ReferenceViewer.snapshot());
    await page.locator('#right').click();
    assert.notEqual(await page.evaluate(()=>ReferenceViewer.snapshot().azimuth),camera.azimuth);
    await page.locator('#zoom-in').click();
    assert.ok(await page.evaluate(()=>ReferenceViewer.snapshot().distance)<camera.distance);
    await page.locator('#reset').click();
    assert.ok(Math.abs(await page.evaluate(()=>ReferenceViewer.snapshot().distance)-camera.distance)<1e-8);
    await page.locator('#weight-a').focus();await page.keyboard.press('ArrowRight');
    await page.waitForFunction(()=>ReferenceViewer.snapshot().panel.weightA>1);
    assert.match(await page.locator('aside').innerText(),/A weight 1.05/);
    await page.locator('#reset-settings').click();await page.waitForTimeout(100);
    const draws=await page.evaluate(()=>ReferenceViewer.snapshot().draws);
    await page.waitForTimeout(100);assert.equal(await page.evaluate(()=>ReferenceViewer.snapshot().draws),draws);
    assert.equal(await page.evaluate(()=>ReferenceViewer.snapshot().particles.length),0);
    await page.locator('#damping').fill('0.1');
    const canvas=page.locator('canvas'),box=await canvas.boundingBox();
    await canvas.click({position:{x:box.width*.4,y:box.height*.4}});
    await page.waitForFunction(()=>ReferenceViewer.snapshot().steps>10);
    assert.equal(await page.locator('#run').getAttribute('aria-pressed'),'true');
    await page.locator('#run').click();
    const first=await page.evaluate(()=>ReferenceViewer.snapshot().particles);
    assert.equal(first.length,1);
    assert.ok(Math.hypot(first[0].vx,first[0].vy)>0);
    await canvas.click({position:{x:box.width*.65,y:box.height*.6}});
    await page.waitForFunction(()=>ReferenceViewer.snapshot().running);
    await page.locator('#run').click();
    const second=await page.evaluate(()=>ReferenceViewer.snapshot().particles);
    assert.equal(second.length,1);assert.notDeepEqual(first,second);
    await page.mouse.move(box.x+box.width/2,box.y+box.height/2);
    await page.mouse.down();await page.mouse.move(box.x+box.width/2+40,box.y+box.height/2,{steps:5});await page.mouse.up();
    assert.deepEqual(await page.evaluate(()=>ReferenceViewer.snapshot().particles),second);
    await page.locator('#run').click();
    await canvas.scrollIntoViewIfNeeded();
    await page.waitForFunction(()=>ReferenceViewer.snapshot().steps>20);
    assert.equal(await page.evaluate(()=>ReferenceViewer.snapshot().particles.length),1);
    assert.ok(await page.evaluate(()=>ReferenceViewer.snapshot().particles.some(p=>Math.hypot(p.vx,p.vy)>0)));
    await page.locator('#run').click();await page.waitForTimeout(100);
    const paused=await page.evaluate(()=>ReferenceViewer.snapshot().steps);
    await page.waitForTimeout(100);assert.equal(await page.evaluate(()=>ReferenceViewer.snapshot().steps),paused);
    await page.locator('#reset-particles').click();
    assert.equal(await page.evaluate(()=>ReferenceViewer.snapshot().particles.length),0);
    assert.equal(await page.evaluate(()=>ReferenceViewer.snapshot().steps),0);
    await page.setViewportSize({width:390,height:844});await page.waitForTimeout(100);
    assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    assert.ok(await page.locator('canvas').evaluate(c=>c.width>0&&c.height>0));
    await page.evaluate(()=>document.querySelector('canvas').dispatchEvent(new Event('webglcontextlost',{cancelable:true})));
    assert.equal(await page.locator('#fallback').isVisible(),true);
    assert.match(await page.locator('[role=status]').innerText(),/context lost/i);
    assert.deepEqual(errors,[]);
    const failed=await browser.newPage();
    await failed.addInitScript(()=>{HTMLCanvasElement.prototype.getContext=()=>null;});
    await failed.goto(url);await failed.waitForTimeout(300);
    assert.equal(await failed.locator('#fallback').isVisible(),true);
    const noJS=await browser.newPage({javaScriptEnabled:false});await noJS.goto(url);
    assert.equal(await noJS.locator('#fallback').isVisible(),true);
  }finally{await browser.close();await new Promise(resolve=>server.close(resolve));}
});
