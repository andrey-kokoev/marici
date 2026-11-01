import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {repeatTiming,cellulationRepeatAt} from '../research/realization-tower/cellulation-repeat.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
test('step 7 translates steps 2–6 from the witnessed white vertex in the same lattice direction',()=>{
 for(const size of [.5,1,2]){
  const model=buildCellulationStep(7,size),original=buildCellulationStep(6,size);assert.deepEqual(model.previous,original);assert.equal(model.cells.length,2);
  const delta=original.proposedVertex;assert.deepEqual(model.repeat.origin,delta);
  for(const translated of model.repeat.stages){const source=buildCellulationStep(translated.step,size);assert.deepEqual(translated.cells[0].vertices,source.cells[0].vertices.map(p=>p.map((x,i)=>x+delta[i])));assert.deepEqual(translated.markedVertex,delta);}
  const next=model.repeat.stages[1];assert.deepEqual(next.arrows[0].from,delta);assert.deepEqual(next.arrows[0].to,delta.map(x=>2*x));
  assert.equal(model.cells[0].vertices.filter(p=>model.cells[1].vertices.some(q=>JSON.stringify(p)===JSON.stringify(q))).length,1);
 }
});
test('repeat preserves the completed first tetrahedron and completes the new step 6',()=>{
 const model=buildCellulationStep(7),group=createCellulation(model),audit=group.userData.audit,{seed,arrow,firstLoop,total}=repeatTiming;
 for(const [time,stage] of [[0,2],[seed+arrow/2,3],[seed+arrow,4],[seed+arrow+firstLoop,5],[total,6]]){
  const active=group.userData.animate(time,{});assert.equal(audit.animation.stage,stage);assert.equal(active,time<total);
  assert.equal(audit.previous.animation.redFaceCount,2);assert.equal(audit.previous.animation.whiteFaceCount,2);assert(audit.previous.animation.turnMarkers.every(m=>m.fillProgress===1));
 }
 const next=audit.animation.current.animation;assert.equal(next.redFaceCount,2);assert.equal(next.whiteDotVisible,true);assert.equal(next.whiteFaceCount,2);assert(next.turnMarkers.every(m=>m.solidVisible&&!m.outlineVisible&&m.fillProgress===1));
 assert.equal(group.userData.cellulationAnchors.length,7);assert.equal(new Set(group.userData.cellulationAnchors.map(a=>a.point.join(','))).size,7);
 group.userData.animate(0,{});assert.equal(audit.animation.stage,2);assert.equal(group.userData.cellulationAnchors.length,4);assert.equal(audit.previous.animation.whiteFaceCount,2);
 assert.equal(cellulationRepeatAt(total).active,false);
 group.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});
});
