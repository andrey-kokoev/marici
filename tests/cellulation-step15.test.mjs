import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
test('step 15 draws white 936→826→927 and closes exactly triangle 927/936/826',()=>{
 for(const size of [.5,1,2]){
  const m=buildCellulationStep(15,size),c=m.triangleClosure;assert.deepEqual(m.cells,m.previous.cells);assert.equal(m.previous.step,14);
  assert.deepEqual(c.latticeFace,[[8,2,6],[8,3,5],[7,2,5]]);
  assert.deepEqual(c.arrows.map(a=>[a.from,a.to]),[[c.face[1],c.face[2]],[c.face[2],c.face[0]]]);
  for(const a of c.arrows){assert.equal(a.colour,0xffffff);assert(Math.abs(Math.hypot(...a.from.map((v,i)=>v-a.to[i]))-size)<1e-12);}
 }
});
test('step 14 stays white while the new arrows and face animate sequentially',()=>{
 const g=createCellulation(buildCellulationStep(15)),a=g.userData.audit.animation,previous=g.children[0],ids=g.userData.cellulationAnchors.map(a=>a.id);
 for(const elapsed of [0,500,1000,1500,2000,2325,Infinity]){
  g.userData.animate(elapsed,{});assert.equal(previous.userData.audit.animation.whiteFaceCount,1);
  assert.equal(a.firstArrowProgress,Math.min(1,elapsed/1000));assert.equal(a.secondArrowProgress,Math.min(1,Math.max(0,(elapsed-1000)/1000)));
  assert.equal(a.faceFillProgress,Math.min(1,Math.max(0,(elapsed-2000)/650)));assert.deepEqual(g.userData.cellulationAnchors.filter(a=>a.id!=='step15:candidate').map(a=>a.id),ids);assert.equal(g.children[3].visible,elapsed>=1000);
 }
 for(const [id,position] of [['step14:candidate',[7,3,6]],['step15:candidate',[7,2,5]]])assert.deepEqual(g.userData.cellulationAnchors.find(a=>a.id===id).point.map(x=>Math.round(x*Math.SQRT2)),position);
 assert.equal(g.children[3].geometry.type,'RingGeometry');assert.equal(g.children[3].material.color.getHex(),0xffffff);
 assert.equal(g.userData.audit.faces,previous.userData.audit.faces+1);assert.equal(a.whiteFaceCount,1);assert.equal(g.children[2].children[1].material.color.getHex(),0xffffff);
 g.userData.animate(Infinity,{edgesOnly:true});assert.equal(a.whiteFaceCount,0);assert.equal(previous.userData.audit.animation.whiteFaceCount,0);
 g.userData.animate(Infinity,{faceOpacity:.4});assert(Math.abs(a.whiteFaceOpacity-.22)<1e-12);
});
