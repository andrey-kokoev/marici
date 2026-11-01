import {test} from 'node:test';
import assert from 'node:assert/strict';
import {Vector3,Euler,MathUtils} from 'three';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
test('step 14 draws white 936→837 at XYZ (180,-45,180), then 837→927, closing the unit triangle',()=>{
 for(const size of [.5,1,2]){
  const m=buildCellulationStep(14,size),c=m.triangleClosure;assert.deepEqual(m.cells,m.previous.cells);
  assert.deepEqual(c.latticeFace,[[8,2,6],[8,3,5],[7,3,6]]);
  const a=c.arrows[0],direction=new Vector3(1,0,0).applyEuler(new Euler(...a.euler.map(MathUtils.degToRad),'XYZ'));
  assert(new Vector3(...a.to).sub(new Vector3(...a.from)).normalize().distanceTo(direction)<1e-12);
  assert.deepEqual(a.from,c.face[1]);assert.deepEqual(a.to,c.face[2]);assert.deepEqual(c.arrows[1].from,c.face[2]);assert.deepEqual(c.arrows[1].to,c.face[0]);
  for(const arrow of c.arrows)assert.equal(arrow.colour,0xffffff);
  for(let i=0;i<3;i++)assert(Math.abs(new Vector3(...c.face[i]).distanceTo(new Vector3(...c.face[(i+1)%3]))-size)<1e-12);
 }
});
test('the two arrows play sequentially, then the white face fills without changing previous dots',()=>{
 const g=createCellulation(buildCellulationStep(14)),a=g.userData.audit.animation,ids=g.userData.cellulationAnchors.map(a=>a.id);
 for(const elapsed of [0,500,1000,1500,2000,2325,Infinity]){
  g.userData.animate(elapsed,{});
  assert.equal(a.firstArrowProgress,Math.min(1,elapsed/1000));assert.equal(a.secondArrowProgress,Math.min(1,Math.max(0,(elapsed-1000)/1000)));
  assert.equal(a.faceFillProgress,Math.min(1,Math.max(0,(elapsed-2000)/650)));
  assert.deepEqual(g.userData.cellulationAnchors.filter(a=>a.id!=='step14:candidate').map(a=>a.id),ids);
  assert.equal(g.children[3].visible,elapsed>=1000);assert.equal(a.candidateVisible,elapsed>=1000);assert.equal(g.children[0].userData.audit.animation.candidateVisible,true);
 }
 assert.deepEqual(g.userData.cellulationAnchors.find(a=>a.id==='step14:candidate').point.map(x=>Math.round(x*Math.SQRT2)),[7,3,6]);assert.equal(g.children[3].geometry.type,'RingGeometry');assert.equal(g.children[3].material.color.getHex(),0xffffff);
 assert.equal(a.whiteFaceCount,1);assert.equal(g.children[2].children[1].material.color.getHex(),0xffffff);
 g.userData.animate(Infinity,{edgesOnly:true});assert.equal(a.whiteFaceCount,0);
 g.userData.animate(Infinity,{faceOpacity:.4});assert(Math.abs(a.whiteFaceOpacity-.22)<1e-12);
});
