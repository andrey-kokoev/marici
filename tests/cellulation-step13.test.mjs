import {test} from 'node:test';
import assert from 'node:assert/strict';
import {Vector3,Euler,MathUtils} from 'three';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
test('step 13 draws a white unit arrow from 927 at XYZ (-45,45,90), ending at 936',()=>{
 for(const size of [.5,1,2]){
  const m=buildCellulationStep(13,size),a=m.directedArrow;assert.deepEqual(m.cells,m.previous.cells);assert.equal(m.cells.length,16);assert.equal(a.colour,0xffffff);
  assert.deepEqual(a.fromLattice,[8,2,6]);assert.deepEqual(a.toLattice,[8,3,5]);assert.deepEqual(a.euler,[-45,45,90]);
  const direction=new Vector3(1,0,0).applyEuler(new Euler(...a.euler.map(MathUtils.degToRad),'XYZ')),delta=new Vector3(...a.to).sub(new Vector3(...a.from));
  assert(Math.abs(delta.length()-size)<1e-12);assert(delta.normalize().distanceTo(direction)<1e-12);
 }
});
test('step 12 stays filled and the new hollow candidate appears only after the arrow',()=>{
 const m=buildCellulationStep(13),g=createCellulation(m),previous=g.children[0];
 for(const elapsed of [0,500,Infinity]){
  g.userData.animate(elapsed,{});assert.equal(previous.userData.audit.animation.whiteFaceCount,3);assert.equal(previous.userData.audit.animation.filledDotVisible,true);
  assert(g.userData.cellulationAnchors.some(a=>a.id==='step11:candidate'));
  const candidate=g.userData.cellulationAnchors.find(a=>a.id==='step13:candidate');assert.equal(Boolean(candidate),elapsed===Infinity);
  if(candidate)assert.deepEqual(candidate.point,m.directedArrow.to);
 }
 assert.equal(g.children[2].geometry.type,'RingGeometry');assert.equal(g.children[2].material.color.getHex(),0xffffff);
});
