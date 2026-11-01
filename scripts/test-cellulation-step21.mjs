import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const step=Number(process.env.CELLULATION_TEST_STEP??21),baseCells=step===22?53:42;
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000},permissions:['clipboard-read','clipboard-write']}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','cellulation');await page.waitForFunction(()=>Math.abs(Math.hypot(...(window.normalRayAudit?.cellulationAudit?.translation??[]))-8)<1e-8);
 for(let s=2;s<step;s++){await page.locator('#cellulation-next').click();await page.waitForFunction(n=>normalRayAudit.cellulationAudit.step===n,s);}
 await page.locator('#viewport-recenter').click();await page.waitForTimeout(100);const camera=await page.evaluate(()=>normalRayViewAudit.camera),ids=await page.evaluate(()=>normalRayViewAudit.cellulationDots.map(a=>a.id));
 await page.locator('#cellulation-next').click();await page.waitForFunction(s=>normalRayAudit.cellulationAudit.step===s&&normalRayAudit.cellulationAudit.animation.phase==='complete',step);
 assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),camera);assert.equal(await page.locator('#cellulation-next').isDisabled(),false);
 const audit=await page.evaluate(()=>normalRayAudit.cellulationAudit);assert.equal(audit.cells,baseCells+11);assert(audit.faces>audit.previous.faces);assert.equal(audit.newTetrahedra,6);assert.equal(audit.newOctahedra,5);assert.equal(audit.arrows.length,6);assert.equal(audit.grid.placedCells,baseCells+11);assert.equal(audit.grid.edgeContextCells,24);assert.equal(audit.animation.completedCells,11);
 const dots=await page.evaluate(()=>normalRayViewAudit.cellulationDots);assert.equal(dots.length,ids.length+16);for(const id of ids)assert(dots.some(a=>a.id===id));assert.equal(new Set(dots.map(a=>a.latticePoint.join(','))).size,dots.length);
 await page.locator('#cellulation-animate').check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='growing-cross-complex');assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.previous.animation.phase),'complete');await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.completedArrows===6,{},{timeout:15000});assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),camera);
 await page.locator('#cellulation-validate-loop').check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.loopValidation?.issues?.length===2);await page.locator('#cellulation-validate-loop').uncheck();
 await page.reload();await page.waitForFunction(s=>window.normalRayAudit?.cellulationAudit?.step===s,step);assert.equal(await page.locator('#cellulation-animate').isChecked(),false);
 await page.locator('[data-view-axis="z"]').click();await page.locator('#viewport-recenter').click();await page.waitForTimeout(100);await page.screenshot({path:`test-results/cellulation-step${step}.png`});
 const candidate=await page.evaluate(prefix=>normalRayViewAudit.cellulationDots.find(a=>a.id.startsWith(prefix)&&a.visible),step===22?'remaining-edge:':'cross-edge:');assert(candidate);
 await page.locator(`[data-dot-lock="${candidate.id}"]`).dblclick();await page.waitForFunction(id=>document.querySelector('#cellulation-copy-status')?.textContent===`Copied ID: ${id}`,candidate.id);assert.equal(await page.evaluate(()=>navigator.clipboard.readText()),candidate.id);
 assert.deepEqual(errors,[]);console.log(`PASS: Step ${step} builds a full white bar with six tetrahedra, five octahedra, faces and arrows; preserves old joins/IDs/camera; supports animation, validation, reload and copy.`);
}finally{await browser.close();}
