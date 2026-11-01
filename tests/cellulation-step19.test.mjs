import {test} from 'node:test';
import assert from 'node:assert/strict';
import {Vector3} from 'three';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {blueCloneColour,blueClonePoint,blueCloneDuration,blueCloneVector} from '../research/realization-tower/cellulation-blue-clone.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
const key=c=>c.vertices.map(p=>p.map(x=>Math.round(x*Math.SQRT2)).join(',')).sort().join('|');
const near=(a,b)=>a.forEach((v,i)=>assert(Math.abs(v-b[i])<1e-10));
test('Step 19 attaches a lattice-preserving blue reflection with first arrow 880→781 of the actual red assembly',()=>{
 for(const size of [.5,1,2]){
  const m=buildCellulationStep(19,size),c=m.blueClone;assert.equal(c.source.step,10);assert.equal(c.arrows.length,8);assert.equal(c.cells.length,15);assert.equal(m.cells.length,36);assert.equal(c.sharedCells.length,1);assert.equal(c.newCells.length,14);assert.deepEqual(c.linearTransform,[[0,0,-1],[0,-1,0],[1,0,0]]);
  assert.deepEqual(m.cells.slice(0,22),m.previous.cells);assert.deepEqual(c.attachmentLattice,[8,8,0]);assert.deepEqual(c.endLattice,[0,8,8]);
  near(c.attachment,m.previous.whiteRepeats.at(-1).stages[0].directedArrow.to);near(blueClonePoint(c,c.sourceStart),c.attachment);near(blueClonePoint(c,c.sourceEnd),c.end);
  c.cells.forEach((cell,i)=>cell.vertices.forEach((p,j)=>near(p,blueClonePoint(c,c.source.cells[i].vertices[j]))));
  for(const a of c.arrows){assert.equal(a.colour,blueCloneColour);assert(Math.abs(new Vector3(...a.from).distanceTo(new Vector3(...a.to))-size)<1e-12);}
  for(let i=1;i<c.arrows.length;i++)near(c.arrows[i-1].to,c.arrows[i].from);
  near(c.arrows[0].to,[7,8,1].map(x=>x*size/Math.SQRT2));
  // A fourth equal-length lattice side can still close at the original start.
  assert(Math.abs(new Vector3(...c.end).distanceTo(new Vector3(...c.sourceStart))-new Vector3(...c.sourceEnd).distanceTo(new Vector3(...c.sourceStart)))<1e-10);
  if(size===1){assert.equal(new Set(m.cells.map(key)).size,36);assert(m.faces.every(f=>f.owners.length<=2));}
 }
});
test('only the fresh copy turns blue; shared dots keep their IDs and prior geometry stays complete',()=>{
 const m=buildCellulationStep(19),g=createCellulation(m),[previous,copy]=g.children,ids=previous.userData.cellulationAnchors.map(a=>a.id);
 const colors=root=>{const result=[];root.traverse(o=>{if(o.material?.color)result.push(o.material.color.getHex());});return result;};
 assert(colors(previous).includes(0xff3030));assert(!colors(copy).includes(0xff3030));assert(colors(copy).includes(blueCloneColour));assert(colors(copy).includes(0xffffff));
 for(const elapsed of [0,blueCloneDuration/2,Infinity]){
  g.userData.animate(elapsed,{});assert.equal(previous.userData.audit.animation.completed,5);assert(Math.abs(copy.matrix.determinant()+1)<1e-10);
  near(new Vector3(...m.blueClone.sourceStart).applyMatrix4(copy.matrix).toArray(),m.blueClone.attachment);
  near(new Vector3(...m.blueClone.sourceEnd).applyMatrix4(copy.matrix).toArray(),m.blueClone.end);
  if(elapsed===Infinity)near(new Vector3(...m.blueClone.normal).transformDirection(copy.matrix).toArray(),blueCloneVector(m.blueClone,m.blueClone.normal));
  for(const id of ids)assert(g.userData.cellulationAnchors.some(a=>a.id===id));
 }
 for(const cell of m.blueClone.source.cells)for(const p of cell.vertices)near(new Vector3(...p).applyMatrix4(copy.matrix).toArray(),blueClonePoint(m.blueClone,p));
 assert.equal(g.userData.cellulationCells.length,36);assert.equal(new Set(g.userData.cellulationAnchors.map(a=>a.id)).size,g.userData.cellulationAnchors.length);
 const positions=g.userData.cellulationAnchors.map(a=>a.point.map(x=>Math.round(x*Math.SQRT2)).join(','));assert.equal(new Set(positions).size,positions.length);assert(positions.includes('0,8,8'));
 assert(g.userData.cellulationAnchors.some(a=>a.id.startsWith('blue:')));
 g.userData.animate(0,{});assert.equal(g.userData.cellulationCells.length,22);assert.deepEqual(g.userData.cellulationAnchors.map(a=>a.id),ids);
});
