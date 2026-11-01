import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {cycleTiming} from '../research/realization-tower/cellulation-cycle.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
const key=p=>p.map(x=>x.toFixed(8)).join(',');
const faceKey=f=>f.map(key).sort().join('|');
test('step 9 adds exactly one red arrow and bridges the previous tetrahedron to the new one',()=>{
 for(const size of [.5,1,2]){
  const m=buildCellulationStep(9,size),{origin,closed,first}=m.cycle,last=m.previous.previous.repeat.stages.at(-1),fresh=first.at(-1);
  assert.deepEqual(origin,last.proposedVertex);assert.notDeepEqual(origin,m.previous.bridge.opposite);assert.deepEqual(first[0].markedVertex,origin);
  const red=[m.previous.previous.previous,last,fresh].map(t=>t.arrows[0]);
  const direction=red[0].to.map((x,i)=>x-red[0].from[i]);
  for(let i=0;i<red.length;i++){
   if(i)assert.equal(key(red[i].from),key(red[i-1].to));
   red[i].to.forEach((x,j)=>assert(Math.abs(x-red[i].from[j]-direction[j])<1e-12));
  }
  assert.equal(closed.cells.filter(c=>c.kind==='tetrahedron').length,1);assert.equal(closed.previous.arrows.filter(a=>a.colour===0xff3030).length,1);
  assert.equal(m.cells.length,5);assert.equal(new Set(m.cells.map(c=>c.id)).size,5);
  assert.equal(m.cells.filter(c=>c.kind==='tetrahedron').length,3);assert.equal(m.cells.filter(c=>c.kind==='octahedron').length,2);
  assert.equal(m.faces.filter(f=>f.owners.length===2).length,4);assert.equal(m.faces.length,24);assert.equal(m.edges.length,30);
  const octFaces=new Set(closed.bridge.cell.faces.map(faceKey));
  for(const tet of [last.cells[0],fresh.cells[0]])assert.equal(tet.faces.filter(f=>octFaces.has(faceKey(f))).length,1);
  assert.equal(m.previous.cells[0].faces.filter(f=>octFaces.has(faceKey(f))).length,0);
  assert.equal(m.previous.bridge.cell.faces.filter(f=>octFaces.has(faceKey(f))).length,0);
  assert.deepEqual(closed.bridge.shared,origin);assert.equal(closed.bridge.arrows.length,4);
  assert.equal(closed.bridge.scaffold.faces.length,6);assert.equal(closed.bridge.scaffold.edges.length,6);
  // The complete old assembly is retained without duplicate cells.
  assert.deepEqual(m.cells.slice(0,m.previous.cells.length),m.previous.cells);
 }
});
test('one tetrahedron grows, then the adjoining octahedron closes; replay retains the previous assembly',()=>{
 const model=buildCellulationStep(9),group=createCellulation(model),audit=group.userData.audit,{tetrahedron,total}=cycleTiming;
 for(const [time,phase] of [[0,'first-tetrahedron'],[tetrahedron,'octahedron'],[total,'complete']]){
  group.userData.animate(time,{});assert.equal(audit.animation.phase,phase);assert.equal(audit.previous.animation.whiteFaceCount,8);assert.equal(audit.previous.animation.phase,'complete');
 }
 assert.equal(audit.animation.current.animation.whiteFaceCount,8);assert.equal(group.userData.cellulationAnchors.length,12);assert.equal(new Set(group.userData.cellulationAnchors.map(a=>key(a.point))).size,12);
 assert(group.userData.cellulationAnchors.some(a=>a.id==='cycle:octahedron:opposite'));
 assert.equal(group.userData.animate(Infinity,{}),false);
 group.userData.animate(0,{});assert.equal(group.userData.cellulationAnchors.length,8);assert.equal(audit.previous.animation.whiteFaceCount,8);
 group.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});
});
