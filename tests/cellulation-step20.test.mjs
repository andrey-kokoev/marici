import {test} from 'node:test';
import assert from 'node:assert/strict';
import {Vector3} from 'three';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {closingWhitePoint,closingWhiteVector,whiteCloneDuration} from '../research/realization-tower/cellulation-white-clone.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
const near=(a,b)=>a.forEach((v,i)=>assert(Math.abs(v-b[i])<1e-10));
const key=c=>c.vertices.map(p=>p.map(x=>Math.round(x*Math.SQRT2)).join(',')).sort().join('|');
test('Step 20 reflects and rotates only the white bar to close blue 088 back to red 000',()=>{
 for(const size of [.5,1,2]){
  const m=buildCellulationStep(20,size),c=m.closingWhiteClone,blue=m.previous.blueClone;
  assert.equal(c.source.cells.length,7);assert.equal(c.newCells.length,6);assert.equal(c.sharedCells.length,1);assert.equal(m.cells.length,42);assert.deepEqual(m.cells.slice(0,36),m.previous.cells);
  assert.deepEqual(c.attachmentLattice,[0,8,8]);assert.deepEqual(c.endLattice,[0,0,0]);assert.deepEqual(c.linearTransform,[[-1,0,0],[0,0,1],[0,-1,0]]);
  near(c.attachment,blue.end);near(c.sourceStart,blue.sourceEnd);near(c.sourceEnd,blue.attachment);near(closingWhitePoint(c,c.sourceStart),c.attachment);near(closingWhitePoint(c,c.sourceEnd),blue.sourceStart);
  c.cells.forEach((cell,i)=>cell.vertices.forEach((p,j)=>near(p,closingWhitePoint(c,c.source.cells[i].vertices[j]))));
  const loop=[blue.sourceStart,blue.sourceEnd,blue.attachment,blue.end,c.end];for(let i=0;i<4;i++)assert(Math.abs(new Vector3(...loop[i]).distanceTo(new Vector3(...loop[i+1]))-8*size)<1e-10);
  for(const a of c.arrows){assert.equal(a.colour,0xffffff);assert(Math.abs(new Vector3(...a.from).distanceTo(new Vector3(...a.to))-size)<1e-10);}
  if(size===1){assert.equal(new Set(m.cells.map(key)).size,42);assert(m.faces.every(f=>f.owners.length<=2));}
 }
});
test('white-only copy preserves colored joins, existing IDs, and restores previous work on replay',()=>{
 const m=buildCellulationStep(20),g=createCellulation(m),[previous,copy]=g.children,c=m.closingWhiteClone,ids=previous.userData.cellulationAnchors.map(a=>a.id);
 copy.traverse(o=>{if(o.material?.color)assert.equal(o.material.color.getHex(),0xffffff);});
 for(const elapsed of [0,whiteCloneDuration/2,Infinity]){
  g.userData.animate(elapsed,{});assert.equal(previous.userData.audit.animation.phase,'complete');assert(Math.abs(copy.matrix.determinant()+1)<1e-10);
  near(new Vector3(...c.sourceStart).applyMatrix4(copy.matrix).toArray(),c.attachment);
  for(const id of ids)assert(g.userData.cellulationAnchors.some(a=>a.id===id));
 }
 near(new Vector3(...c.sourceEnd).applyMatrix4(copy.matrix).toArray(),c.end);assert.equal(g.userData.cellulationCells.length,42);assert.equal(g.userData.audit.animation.closed,true);
 const anchors=g.userData.cellulationAnchors;assert.equal(new Set(anchors.map(a=>a.id)).size,anchors.length);assert.equal(new Set(anchors.map(a=>a.point.map(x=>Math.round(x*Math.SQRT2)).join(','))).size,anchors.length);
 const newAnchor=anchors.find(a=>a.id.startsWith('closing-white:'));assert(newAnchor);
 const original=copy.userData.cellulationAnchors.find(a=>'closing-white:'+a.id===newAnchor.id);near(newAnchor.normal,closingWhiteVector(c,original.normal));
 const sharedArrows=[];copy.traverse(o=>{if(o.userData.cellulationArrow&&!o.visible)sharedArrows.push(o);});assert(sharedArrows.length>0);
 g.userData.animate(0,{});assert.equal(g.userData.cellulationCells.length,36);assert.deepEqual(g.userData.cellulationAnchors.map(a=>a.id),ids);
});
