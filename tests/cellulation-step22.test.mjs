import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep,cellulationSteps} from '../research/realization-tower/cellulation-steps.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
import {renderedCellulationArrows} from '../examples/normal-ray/cellulation-loop-validation.js';
import {validateCellulationLoop} from '../research/realization-tower/cellulation-loop-validation.mjs';
test('Step 22 joins the remaining corners with a full six-unit white bar, without duplicate cells',()=>{
 assert(cellulationSteps.some(s=>s.step===22));
 for(const size of [.5,1,2]){
  const m=buildCellulationStep(22,size),c=m.crossEdge;
  assert.deepEqual(c.latticePoints,[[1,1,0],[2,2,0],[3,3,0],[4,4,0],[5,5,0],[6,6,0],[7,7,0]]);
  assert.equal(m.cells.length,64);assert.deepEqual(m.cells.slice(0,53),m.previous.cells);
  assert.equal(c.newCells.filter(c=>c.kind==='tetrahedron').length,6);assert.equal(c.newCells.filter(c=>c.kind==='octahedron').length,5);
  assert(m.faces.filter(f=>f.owners.length===2&&f.owners.some(id=>id.startsWith('remaining-complex:'))).length>=12);
  for(const a of c.arrows)assert(Math.abs(Math.hypot(...a.from.map((x,i)=>x-a.to[i]))-size)<1e-9);
 }
});
test('new bar preserves Step 21, endpoint IDs and colors; animation and replay affect only Step 22',()=>{
 const m=buildCellulationStep(22),g=createCellulation(m),prior=structuredClone(g.children[0].userData.cellulationAnchors),key=p=>p.map(x=>Math.round(x*Math.SQRT2)).join(',');
 for(const [elapsed,cells] of [[0,53],[1000,54],[3000,58],[6000,64]]){
  g.userData.animate(elapsed,{});assert.equal(g.userData.cellulationCells.length,cells);assert.deepEqual(g.children[0].userData.cellulationAnchors,prior);assert.equal(g.children[0].userData.audit.animation.phase,'complete');
 }
 const anchors=g.userData.cellulationAnchors;assert.equal(new Set(anchors.map(a=>key(a.point))).size,anchors.length);assert.equal(anchors.length,prior.length+16);
 for(const p of ['1,1,0','7,7,0'])assert.deepEqual(anchors.find(a=>key(a.point)===p),prior.find(a=>key(a.point)===p));
 for(const p of m.crossEdge.points.slice(1,-1))assert(anchors.some(a=>a.id===`remaining-edge:${key(p)}`));
 g.children[1].traverse(o=>{if(o.material?.color)assert.equal(o.material.color.getHex(),0xffffff);});
 const audit=validateCellulationLoop(m,renderedCellulationArrows(g),anchors);assert.equal(audit.invalidCells,0);assert.equal(audit.duplicateCells,0);assert.equal(audit.issues.length,2);assert.equal(audit.checks.find(c=>c.name==='Arrow geometry').status,'pass');
 g.userData.animate(0,{});assert.deepEqual(g.userData.cellulationAnchors,prior);assert.equal(g.userData.cellulationCells.length,53);
});
