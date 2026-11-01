import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {cycleTiming,extensionTiming} from '../research/realization-tower/cellulation-cycle.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
const key=p=>p.map(x=>x.toFixed(8)).join(',');
const faceKey=f=>f.map(key).sort().join('|');
test('step 10 adds five single-tetrahedron continuations and five adjoining octahedra in the same direction',()=>{
 for(const size of [.5,1,2]){
  const m=buildCellulationStep(10,size);assert.equal(m.extensions.length,5);assert.equal(m.cells.length,15);assert.equal(new Set(m.cells.map(c=>c.id)).size,15);
  assert.equal(m.cells.filter(c=>c.kind==='tetrahedron').length,8);assert.equal(m.cells.filter(c=>c.kind==='octahedron').length,7);
  assert.equal(m.faces.length,74);assert.equal(m.edges.length,90);assert.equal(m.faces.filter(f=>f.owners.length===2).length,14);assert(m.faces.every(f=>f.owners.length<=2));
  assert.deepEqual(m.cells.slice(0,5),m.previous.cells);
  let last=m.previous.cycle.first.at(-1);const direction=last.arrows[0].to.map((x,i)=>x-last.arrows[0].from[i]);
  for(const {cycle, cells} of m.extensions){
   const fresh=cycle.first.at(-1),arrow=fresh.arrows[0],bridge=cycle.closed.bridge;
   assert.equal(cells.length,2);assert.equal(key(arrow.from),key(last.proposedVertex));assert.equal(key(cycle.origin),key(last.proposedVertex));
   arrow.to.forEach((x,i)=>assert(Math.abs(x-arrow.from[i]-direction[i])<1e-12));
   const faces=new Set(bridge.cell.faces.map(faceKey));for(const tet of [last.cells[0],fresh.cells[0]])assert.equal(tet.faces.filter(f=>faces.has(faceKey(f))).length,1);
   assert.equal(bridge.arrows.length,4);last=fresh;
  }
 }
});
test('five cycles run sequentially, preserve finished cells, whiten each octahedron, and replay only the additions',()=>{
 const model=buildCellulationStep(10),group=createCellulation(model),audit=group.userData.audit;
 for(let i=0;i<5;i++){
  group.userData.animate(i*extensionTiming.cycle,{});assert.equal(audit.animation.iteration,i+1);assert.equal(audit.animation.completed,i);assert.equal(audit.animation.current.animation.phase,'first-tetrahedron');assert.equal(audit.animation.dotCount,12+4*i);
  assert.equal(audit.previous.animation.phase,'complete');assert.equal(audit.previous.animation.current.animation.whiteFaceCount,8);
  assert.equal(group.children.filter(c=>c.visible).length,2+i);
  group.userData.animate(i*extensionTiming.cycle+cycleTiming.tetrahedron,{});assert.equal(audit.animation.current.animation.phase,'octahedron');assert.equal(audit.animation.current.animation.current.animation.arrived,0);
  for(let j=0;j<i;j++)assert.equal(group.children[j+1].userData.audit.animation.current.animation.whiteFaceCount,8);
 }
 assert.equal(group.userData.animate(Infinity,{}),false);assert.equal(audit.animation.completed,5);assert.equal(audit.animation.dotCount,32);
 assert.equal(new Set(group.userData.cellulationAnchors.map(a=>key(a.point))).size,32);
 for(const c of group.children.slice(1))assert.equal(c.userData.audit.animation.current.animation.whiteFaceCount,8);
 group.userData.animate(0,{});assert.equal(audit.animation.dotCount,12);assert.equal(audit.animation.completed,0);assert.equal(group.children.filter(c=>c.visible).length,2);
 group.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});
});
