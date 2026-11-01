import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep,cellulationSteps} from '../research/realization-tower/cellulation-steps.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
import {renderedCellulationArrows} from '../examples/normal-ray/cellulation-loop-validation.js';
import {validateCellulationLoop} from '../research/realization-tower/cellulation-loop-validation.mjs';
test('Step 21 builds six whole tetrahedra and five whole octahedra along 718→178',()=>{
 assert(cellulationSteps.some(s=>s.step===21));
 for(const size of [.5,1,2]){
  const m=buildCellulationStep(21,size),c=m.crossEdge;
  assert.deepEqual(c.latticePoints,[[7,1,8],[6,2,8],[5,3,8],[4,4,8],[3,5,8],[2,6,8],[1,7,8]]);
  assert.equal(m.cells.length,53);assert.equal(c.newCells.filter(c=>c.kind==='tetrahedron').length,6);assert.equal(c.newCells.filter(c=>c.kind==='octahedron').length,5);
  assert.deepEqual(m.cells.slice(0,42),m.previous.cells);
  for(const a of c.arrows){assert.equal(a.colour,0xffffff);assert(Math.abs(Math.hypot(...a.from.map((x,i)=>x-a.to[i]))-size)<1e-9);}
  // Each neighboring pair is connected through a complete octahedron face.
  const shared=m.faces.filter(f=>f.owners.length===2&&f.owners.some(id=>id.startsWith('cross-complex:')));
  assert(shared.length>=12);
 }
});
test('full white complex builds sequentially, preserves old joins and IDs, and replays only the additions',()=>{
 const m=buildCellulationStep(21),g=createCellulation(m),previous=g.children[0],prior=structuredClone(previous.userData.cellulationAnchors);
 for(const [elapsed,complete,cells] of [[0,0,0],[500,0,0],[1000,1,1],[2500,2,3],[5000,5,9],[6000,6,11]]){
  g.userData.animate(elapsed,{});assert.equal(g.userData.audit.animation.completedArrows,complete);assert.equal(g.userData.audit.animation.completedCells,cells);
  assert.deepEqual(previous.userData.cellulationAnchors,prior);assert.equal(previous.userData.audit.animation.phase,'complete');assert.equal(g.userData.cellulationCells.length,42+cells);
 }
 const anchors=g.userData.cellulationAnchors,key=p=>p.map(x=>Math.round(x*Math.SQRT2)).join(',');assert.equal(new Set(anchors.map(a=>key(a.point))).size,anchors.length);
 assert.equal(anchors.find(a=>key(a.point)==='7,1,8').id,'extension:4:cycle:turn-first');assert.equal(anchors.find(a=>key(a.point)==='1,7,8').id,'blue:extension:4:cycle:turn-second');
 for(const p of m.crossEdge.points.slice(1,-1))assert(anchors.some(a=>a.id===`cross-edge:${key(p)}`));
 const copy=g.children[1];copy.traverse(o=>{if(o.material?.color)assert.equal(o.material.color.getHex(),0xffffff);});
 assert(copy.children.length>0);const audit=validateCellulationLoop(m,renderedCellulationArrows(g),anchors);assert.equal(audit.issues.length,2);assert.equal(audit.invalidCells,0);assert.equal(audit.duplicateCells,0);assert.equal(audit.checks.find(c=>c.name==='Arrow geometry').status,'pass');
 g.userData.animate(Infinity,{edgesOnly:true});copy.traverse(o=>{if(o.isMesh&&o.geometry.type==='BufferGeometry'&&!o.geometry.index)assert.equal(o.visible,false);});
 g.userData.animate(0,{});assert.deepEqual(g.userData.cellulationAnchors,prior);assert.equal(g.userData.cellulationCells.length,42);assert.equal(g.userData.cellulationGridSeeds.length,0);assert(g.children.slice(2).every(a=>!a.children[0].visible));
});
