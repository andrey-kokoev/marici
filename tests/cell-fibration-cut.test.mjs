import test from 'node:test';
import assert from 'node:assert/strict';
import {cellFibrationProcess} from '../research/realization-tower/cell-fibration-history.mjs';
import {applyCellFibrationCut,geometricCellDepth} from '../research/realization-tower/cell-fibration-cut.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
const full=cellFibrationProcess(7,5);
test('cuts retain the entire nested vertex complex through the selected depth',()=>{
 for(let vertex=1;vertex<=4;vertex++){
  let previous=[];
  for(let layer=0;layer<=6;layer++){
   const view=applyCellFibrationCut(full,{enabled:true,vertex,layer,showEmpty:true});
   assert.equal(view.cutAudit.slotCount,(layer+1)*(layer+2)*(layer+3)/6);
   assert.equal(view.cutAudit.fullBodyCount,84);assert.equal(view.cellFibrationAudit.bodyCount,84);
   assert.deepEqual(view.retainedBodies,full.retainedBodies.filter(b=>geometricCellDepth(b,vertex)<=layer));
   assert.ok(view.retainedBodies.some(b=>geometricCellDepth(b,vertex)===0));
   assert.ok(previous.every(id=>view.cutAudit.visibleIds.includes(id)));
   assert.equal(view.retainedBodies.length+view.presentationWireframes.length,view.cutAudit.slotCount);
   assert.equal(view.cutAudit.emptyCount,0);
   previous=view.cutAudit.visibleIds;
  }
  assert.equal(previous.length,84);assert.equal(new Set(previous).size,84);
 }
});
test('depth 3 is filled; earlier construction stages still expose unfilled sites',()=>{
 const before=JSON.stringify(full);
 for(let vertex=1;vertex<=4;vertex++){
  const view=applyCellFibrationCut(full,{enabled:true,vertex,layer:3,showEmpty:true});
  assert.equal(view.retainedBodies.length,20);assert.equal(view.cutAudit.emptyCount,0);
  assert.equal(view.presentationWireframes.length,0);
  assert.equal(view.presentationLabels.filter(p=>p.text==='∅').length,0);
  const deeper=applyCellFibrationCut(cellFibrationProcess(7,4),{enabled:true,vertex,layer:4,showEmpty:true});
  assert.equal(deeper.presentationWireframes.length,3);assert.equal(deeper.cutAudit.emptyCount,3);
  const hidden=applyCellFibrationCut(cellFibrationProcess(7,4),{enabled:true,vertex,layer:4,showEmpty:false});
  assert.equal(hidden.presentationWireframes.length,0);assert.equal(hidden.cutAudit.emptyCount,3);
 }
 assert.equal(JSON.stringify(full),before);
 assert.equal(applyCellFibrationCut(full,{enabled:false}),full);
});
test('cuts retain outer edges and all admitted corner cells as non-counted orientation context',()=>{
 for(let vertex=1;vertex<=4;vertex++)for(let layer=0;layer<=6;layer++){
  const view=applyCellFibrationCut(full,{enabled:true,vertex,layer,showEmpty:false});
  const shown=[...view.retainedBodies,...view.contextBodies],ids=shown.map(g=>g.id);
  assert.equal(new Set(ids).size,ids.length);
  assert.equal(view.cutAudit.keepEnvelope,true);
  for(const corner of full.cellFibrationAudit.corners){
   assert.ok(ids.includes(corner.cell));assert.ok(view.presentationLabels.some(p=>p.cell===corner.cell));
  }
  assert.ok(view.contextBodies.every(b=>b.layer===0));
  assert.equal(view.cutAudit.counts.total,view.retainedBodies.length);
  assert.equal(view.contextBodies.length,layer===6?0:3);
 }
});
test('cut respects current admission stage and validates controls',()=>{
 const initial=cellFibrationProcess(7,0),view=applyCellFibrationCut(initial,{enabled:true,vertex:1,layer:3,showEmpty:true});
 assert.equal(view.retainedBodies.length,1);assert.equal(view.cutAudit.emptyCount,19);
 assert.throws(()=>applyCellFibrationCut(full,{enabled:true,vertex:0,layer:3}),/vertex/);
 assert.throws(()=>applyCellFibrationCut(full,{enabled:true,vertex:1,layer:7}),/layer/);
 const unrelated={retainedBodies:[]};assert.equal(applyCellFibrationCut(unrelated,{enabled:true}),unrelated);
 const cut={enabled:true,vertex:4,layer:3,showEmpty:false};assert.deepEqual(normalizeSceneSettings({cut}).cut,{...cut,startLayer:0,highlightUnassigned:false});
 assert.deepEqual(normalizeSceneSettings({cut:{vertex:99,layer:99}}).cut,{enabled:false,vertex:4,startLayer:0,layer:6,showEmpty:true,highlightUnassigned:false});
});
