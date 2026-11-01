import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
import {renderedCellulationArrows} from '../examples/normal-ray/cellulation-loop-validation.js';
import {validateCellulationLoop} from '../research/realization-tower/cellulation-loop-validation.mjs';
test('four unit-triangulated faces form a closed shell, with inward whole-cell support and no deep interior fill',()=>{
 for(const size of [.5,1,2]){
  const model=buildCellulationStep(26,size),triangles=[];let m=model;
  while(m.shellFace){
   const f=m.shellFace;assert.equal(f.triangles.length,64);assert.equal(f.interiorCellsExcluded,86);assert(Math.abs(Math.hypot(...f.normal)-1)<1e-9);
   const origin=f.corners[0].map(x=>x*size/Math.SQRT2),signed=p=>p.reduce((sum,x,i)=>sum+(x-origin[i])*f.normal[i],0);
   assert(f.newCells.every(c=>c.vertices.every(p=>signed(p)<1e-7)));assert(f.triangles.flat().every(p=>Math.abs(signed(p))<1e-7));
   assert.deepEqual(m.cells.slice(0,m.previous.cells.length),m.previous.cells);triangles.push(...f.triangles);m=m.previous;
  }
  assert.equal(model.cells.length,174);const key=p=>p.map(x=>Math.round(x*Math.SQRT2/size)).join(','),vertices=new Set(),edges=new Map(),faces=new Set();
  for(const f of triangles){faces.add(f.map(key).sort().join('|'));for(let i=0;i<3;i++){vertices.add(key(f[i]));const next=f[(i+1)%3];assert(Math.abs(Math.hypot(...f[i].map((x,j)=>x-next[j]))-size)<1e-8);const e=[key(f[i]),key(next)].sort().join('|');edges.set(e,(edges.get(e)??0)+1);}}
  assert.equal(faces.size,256);assert([...edges.values()].every(n=>n===2));assert.equal(vertices.size-edges.size+faces.size,2);
  // No selected whole cell lies strictly away from all four shell planes.
  const planes=[p=>p[0]+p[1]-p[2],p=>p[0]+p[2]-p[1],p=>p[1]+p[2]-p[0],p=>16-p[0]-p[1]-p[2]];
  assert(model.cells.every(c=>c.faces.some(f=>planes.some(plane=>f.every(p=>Math.abs(plane(p.map(x=>x*Math.SQRT2/size)))<1e-7)))));
 }
});
test('face animation preserves earlier construction and dot IDs; completed shell validates and replay removes only the last patch',()=>{
 const m=buildCellulationStep(26),g=createCellulation(m),previous=g.children[0],anchors=structuredClone(previous.userData.cellulationAnchors);
 assert.equal(g.userData.cellulationCells.length,149);g.userData.animate(1200,{});assert.equal(g.userData.audit.animation.progress,1200/g.userData.witnessPlan.duration);assert.deepEqual(g.userData.cellulationAnchors.slice(0,anchors.length),anchors);assert.equal(previous.userData.audit.animation.phase,'complete');
 g.userData.animate(Infinity,{});assert.equal(g.userData.cellulationCells.length,174);for(const a of anchors)assert.deepEqual(g.userData.cellulationAnchors.find(b=>b.id===a.id),a);
 const key=p=>p.map(x=>Math.round(x*Math.SQRT2)).join(',');assert.equal(new Set(g.userData.cellulationAnchors.map(a=>key(a.point))).size,g.userData.cellulationAnchors.length);
 const report=validateCellulationLoop(m,renderedCellulationArrows(g),g.userData.cellulationAnchors);assert.equal(report.invalidCells,0);assert.equal(report.duplicateCells,0);assert.equal(report.issues.length,2);
 g.userData.animate(Infinity,{edgesOnly:true});assert(g.children.filter(o=>o.userData.cellulationFaces).every(o=>!o.visible));
 g.userData.animate(0,{});assert.equal(g.userData.cellulationCells.length,149);assert.deepEqual(g.userData.cellulationAnchors.slice(0,anchors.length),anchors);
});
