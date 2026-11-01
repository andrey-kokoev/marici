import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
import {retainedExpansionViewportLabels,retainedExpansionAtoms} from '../examples/normal-ray/retained-expansion-renderer.js';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 async function checkLabel(step){
  const locator=page.locator('#retained-expansion-label');
  const atom=retainedExpansionAtoms[step];
  const expected=`${retainedExpansionViewportLabels[step]}\nnatural abundance: ${atom.abundancePercent}%\nstability: ${atom.stability}`;
  assert.equal((await locator.textContent()).replace(/\s+/g,''),expected.replace(/\s+/g,''));
  assert.equal(await locator.locator('[data-isotope-abundance]').textContent(),`${atom.abundancePercent}%`);
  assert.equal(await locator.locator('[data-isotope-stability]').textContent(),'Stable');
  assert.equal(await locator.evaluate(el=>getComputedStyle(el).fontSize),'12px');
  assert.equal(await locator.locator('strong').evaluate(el=>getComputedStyle(el).fontSize),'14px');
  const label=await locator.boundingBox(),scene=await page.locator('#scene').boundingBox();
  assert(label.x>=scene.x&&label.x<scene.x+50);assert(label.y>=scene.y&&label.y<scene.y+50);
 }
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','retained-expansion');
 for(let step=1;step<=20;step++){
  await page.waitForFunction(s=>window.normalRayAudit?.view==='retained-expansion'&&normalRayAudit.retainedExpansionAudit.step===s&&normalRayAudit.retainedExpansionAudit.progress===1,step);
  const a=await page.evaluate(()=>normalRayAudit.retainedExpansionAudit);assert.equal(a.arrowDirections,0);assert.equal(a.growingLines,step===8?3:step>=7?2:step>=5||step===2?1:0);assert.equal(a.triangles,step>=20?12:step>=19?11:step>=17?10:step>=15?9:step>=13?8:step>=11?7:step>=10?6:step>=8?5:step>=6?4:step>=3?2:0);assert.equal(a.colouredTriangles,step>=20?11:step>=19?10:step>=17?9:step>=15?8:step>=13?7:step>=11?6:step>=10?5:step===8?5:step>=6?4:step>=4?2:0);assert.equal(a.dots,step>=3?0:1);assert.equal(a.rectangle,step>=3&&step<=8);if(step>=3)assert.deepEqual(a.tipPositions,step===3?[[1.5,1.5,0],[1.5,-1.5,0]]:[[1.5,1.5,0]]);
  if(step>=3&&step<=5)assert.equal(a.horizontalSeparator,step===5);
  if(step===5){assert.deepEqual(a.faceSides,{front:{upper:'red',lower:'blue'},back:{upper:'blue',lower:'red'}});assert.equal(a.planar,true);assert.equal(a.square,true);assert.equal(a.droppedArrows,0);assert.deepEqual(a.dropSources,[]);assert.deepEqual(a.dropTargets,[]);assert.deepEqual(a.sharedEdge,[[0,0,0],[3,0,0]]);}
  if(step===6||step===7){
   assert.equal(a.square,true);assert.equal(a.colouredTriangles,4);assert.equal(a.insetTriangles,4);
   assert.equal(a.whiteningProgress,0);assert.equal(a.droppedArrows,0);
   assert.deepEqual(a.splitFields,['upper','lower']);assert.deepEqual(a.verticalSplit,[[1.5,-1.5,0],[1.5,1.5,0]]);
   assert.equal(a.whiteSeparator,step===7);
   assert.deepEqual(a.faceSides,{front:{upper:['red','blue'],lower:['blue','red']},back:{upper:['blue','red'],lower:['red','blue']}});
  }
  if(step===8){
   assert.equal(a.square,true);assert.equal(a.colouredTriangles,5);assert.equal(a.insetTriangles,5);
   assert.deepEqual(a.splitColoredFace,{face:'upper',slot:1});assert.deepEqual(a.diagonalSplit,[[1.5,0,0],[2.25,.75,0]]);
   assert.equal(a.whiteSeparator,true);assert.equal(a.newPairSeparator,true);
  }
  if(step>=9){assert.equal(a.whiteningProgress,step===6||step===8||step===11||step===13||step===15||step===17||step===19||step===20?0:1);assert.equal(a.insetProgress,1);assert.equal(a.insetTriangles,step>=20?10:step>=19?9:step>=17?8:step>=15?7:step>=13?6:step>=11?5:step>=10?3:2);assert.equal(a.insetPairsPerSide,1);assert.deepEqual(a.faceSides,step>=8?{front:{left:'white',right:{lower:'blue',upper:'red'}},back:{left:'white',right:{lower:'red',upper:'blue'}}}:step===6?{front:{left:'red',right:'blue'},back:{left:'blue',right:'red'}}:{front:{left:'white',right:'blue'},back:{left:'white',right:'red'}});assert.equal(a.whiteSeparator,step>=7);assert.equal(a.rightPairSeparator,step>=12);assert.equal(a.carbonSplit,step>=13);assert.equal(a.carbonPairSeparator,step>=14);assert.equal(a.nitrogenSplit,step>=15);assert.equal(a.nitrogenPairSeparator,step>=16);assert.equal(a.oxygenSplit,step>=17);assert.equal(a.oxygenPairSeparator,step>=18);assert.equal(a.fluorineSplit,step>=19);assert.equal(a.neonSplit,step>=20);assert.equal(a.fluorinePairSeparator,step>=19);assert.equal(a.unplacedAdditionalNeutrons,0);}
  if(step>=4)await checkLabel(step);
  await page.screenshot({path:`test-results/retained-expansion-step${step}.png`});if(step<20)await page.locator('#retained-expansion-next').click();
 }
 assert(await page.locator('#retained-expansion-next').isDisabled());assert.equal(await page.locator('#inventory-panel').isVisible(),false);assert.equal(await page.locator('#sulfur-32-fibrate').isVisible(),false);
 for(const reset of ['#reset-view','#viewport-reset']){
  await page.locator('[data-view-axis="x"]').click();
  await page.waitForFunction(()=>Math.abs(normalRayViewAudit.camera.offset[0])>1);
  await page.getByRole('button',{name:'Roll left',exact:true}).click();
  await page.locator(reset).click();
  await page.waitForFunction(()=>Math.abs(normalRayViewAudit.camera.offset[0])<1e-8&&Math.abs(normalRayViewAudit.camera.offset[1])<1e-8&&normalRayViewAudit.camera.offset[2]>0);
  const camera=await page.evaluate(()=>normalRayViewAudit.camera);
  camera.up.forEach((n,i)=>assert(Math.abs(n-[0,1,0][i])<1e-8));
  camera.targetOffset.forEach(n=>assert(Math.abs(n)<1e-8));assert.equal(camera.zoom,1);
  assert.equal(await page.evaluate(()=>normalRayAudit.retainedExpansionAudit.step),20);
 }
 await page.reload();await page.waitForFunction(()=>window.normalRayAudit?.view==='retained-expansion'&&normalRayAudit.retainedExpansionAudit.step===20);await checkLabel(20);
 for(let step=19;step>=3;step--){
  await page.locator('#retained-expansion-prev').click();await page.waitForFunction(s=>normalRayAudit.retainedExpansionAudit.step===s,step);
  if(step>=4)await checkLabel(step);
 }
 await page.waitForFunction(()=>normalRayAudit.retainedExpansionAudit.triangles===2&&normalRayAudit.retainedExpansionAudit.colouredTriangles===0);
 await page.selectOption('#sulfur-32-view','cellulation');await page.waitForFunction(()=>normalRayAudit?.view==='cellulation');
 await page.selectOption('#sulfur-32-view','retained-expansion');await page.waitForFunction(()=>normalRayAudit?.view==='retained-expansion'&&normalRayAudit.retainedExpansionAudit.step===3);
 assert.deepEqual(errors,[]);console.log('PASS: retained expansion steps, formatted labels, animation, both reset buttons, reload, reverse navigation and view switching.');
}finally{await browser.close();}
