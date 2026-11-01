import {test} from 'node:test';
import assert from 'node:assert/strict';
import {Vector3,Euler,MathUtils} from 'three';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {buildCellulationNeighborhood,cellulationIncidentEdges} from '../research/realization-tower/cellulation-neighborhood.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
test('step 11 adds exactly the requested unit arrow, retaining every previous cell',()=>{
 for(const size of [.5,1,2]){
  const m=buildCellulationStep(11,size),a=m.directedArrow;assert.deepEqual(m.cells,m.previous.cells);assert.equal(m.cells.length,15);
  assert.equal(a.colour,0xffffff);assert.deepEqual(a.fromLattice,[8,1,7]);assert.deepEqual(a.toLattice,[8,2,6]);
  const direction=new Vector3(1,0,0).applyEuler(new Euler(...a.euler.map(MathUtils.degToRad),'XYZ'));
  const delta=new Vector3(...a.to).sub(new Vector3(...a.from));assert(Math.abs(delta.length()-size)<1e-12);assert(delta.normalize().distanceTo(direction)<1e-12);
  if(size===1){const edges=cellulationIncidentEdges(buildCellulationNeighborhood(m.cells).edges,a.from);assert(edges.some(e=>e.vertices.some(p=>p.every((v,i)=>Math.abs(v-a.to[i])<1e-12))));}
 }
});
test('only the new arrow animates; the step-10 assembly and dot IDs remain complete',()=>{
 const m=buildCellulationStep(11),g=createCellulation(m),previous=g.children[0];
 const source=()=>g.userData.cellulationAnchors.find(a=>a.point.every((x,i)=>Math.abs(x-m.directedArrow.from[i])<1e-12));
 assert(source());const ids=g.userData.cellulationAnchors.map(a=>a.id);
 for(const elapsed of [0,500,Infinity]){
  g.userData.animate(elapsed,{});assert.equal(g.userData.audit.animation.arrowProgress,Math.min(1,elapsed/1000));assert.equal(previous.userData.audit.animation.completed,5);
  assert.deepEqual(g.userData.cellulationAnchors.filter(a=>a.id!=='step11:candidate').map(a=>a.id),ids);assert.equal(g.userData.cellulationCells.length,15);
  const candidate=g.userData.cellulationAnchors.find(a=>a.id==='step11:candidate');assert.equal(Boolean(candidate),elapsed===Infinity);
  assert.equal(g.children[2].visible,elapsed===Infinity);assert.equal(g.children[2].geometry.type,'RingGeometry');assert.equal(g.children[2].material.color.getHex(),0xffffff);
  if(candidate)assert.deepEqual(candidate.point,m.directedArrow.to);
 }
});
