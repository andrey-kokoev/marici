import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','cellulation');await page.waitForFunction(()=>Math.abs(Math.hypot(...(window.normalRayAudit?.cellulationAudit?.translation??[]))-8)<1e-8);
 for(let step=2;step<=10;step++){
  await page.locator('#cellulation-next').click();await page.waitForFunction(s=>normalRayAudit.cellulationAudit.step===s,step);
  const dots=await page.evaluate(()=>normalRayViewAudit.cellulationDots);assert(dots.length>0);
  for(const dot of dots){
   const title=await page.locator(`[data-dot-lock="${dot.id}"]`).getAttribute('title');assert(title.startsWith(`ID: ${dot.id}\n`));assert(title.includes(`Lattice (x, y, z): (${dot.latticePoint.join(', ')})`));assert(title.includes('World (x, y, z):'));
   assert(dot.latticePoint.every(Number.isInteger));assert.equal(dot.latticePoint.reduce((a,b)=>a+b,0)%2,0);
  }
 }
 await page.locator('#viewport-recenter').click();await page.waitForTimeout(100);
 const seed=page.locator('[data-dot-lock="seed"]');await seed.hover();assert.match(await seed.getAttribute('title'),/ID: seed\nLattice \(x, y, z\): \(0, 0, 0\)/);
 await seed.click();await page.waitForFunction(()=>normalRayViewAudit.cellulationLock?.id==='seed');assert.match(await seed.getAttribute('title'),/Click to release/);
 assert.deepEqual(errors,[]);console.log('PASS: every dot exposes its stable ID, lattice coordinates and translated world position; hover and pin behavior remain intact.');
}finally{await browser.close();}
