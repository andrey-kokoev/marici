import test from 'node:test';
import assert from 'node:assert/strict';
import {cellFibrationProcess} from '../research/realization-tower/cell-fibration-history.mjs';
import {applyCellFibrationCut,geometricCellLayer} from '../research/realization-tower/cell-fibration-cut.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
test('all inclusive depth ranges retain precisely the admitted cells and preserve corner context',()=>{
 for(const stage of [5,6]){
  const full=cellFibrationProcess(7,stage),before=JSON.stringify(full);
  for(let vertex=1;vertex<=4;vertex++)for(let startLayer=0;startLayer<=6;startLayer++)for(let layer=startLayer;layer<=6;layer++){
   const view=applyCellFibrationCut(full,{enabled:true,vertex,startLayer,layer,showEmpty:true});
   const inside=b=>{const d=geometricCellLayer(b,vertex);return d>=startLayer&&d<=layer;};
   assert.deepEqual(view.retainedBodies,full.retainedBodies.filter(inside));
   assert.equal(view.cutAudit.startLayer,startLayer);
   assert.equal(view.cutAudit.includesVertexComplex,startLayer===0);
   assert.equal(view.cutAudit.counts.total,view.retainedBodies.length);
   assert.equal(view.cutAudit.slotCount,view.retainedBodies.length);
   assert.equal(view.cutAudit.emptyCount,0);
   if(stage===5)assert.equal(view.retainedBodies.length,(layer+1)*(layer+2)*(layer+3)/6-startLayer*(startLayer+1)*(startLayer+2)/6);
   assert.ok(view.contextBodies.every(b=>b.layer===0&&!inside(b)));
   const shown=[...view.retainedBodies,...view.contextBodies];
   assert.equal(new Set(shown.map(b=>b.id)).size,shown.length);
   for(const c of full.cellFibrationAudit.corners)assert.ok(shown.some(b=>b.id===c.cell));
   for(const p of view.presentationLabels)assert.ok(shown.some(b=>b.id===p.cell));
  }
  assert.equal(JSON.stringify(full),before);
 }
});
test('empty wireframes obey both bounds, including single-depth slices',()=>{
 const full=cellFibrationProcess(7,0);
 for(let vertex=1;vertex<=4;vertex++){
  const view=applyCellFibrationCut(full,{enabled:true,vertex,startLayer:2,layer:2,showEmpty:true});
  assert.equal(view.retainedBodies.length,0);assert.equal(view.contextBodies.length,4);
  assert.equal(view.presentationWireframes.length,6);assert.equal(view.cutAudit.emptyCount,6);
  assert.ok(view.presentationWireframes.every(b=>geometricCellLayer(b,vertex)===2));
  assert.equal(view.presentationLabels.filter(p=>p.text==='∅').length,6);
  const hidden=applyCellFibrationCut(full,{enabled:true,vertex,startLayer:2,layer:2,showEmpty:false});
  assert.equal(hidden.presentationWireframes.length,0);assert.equal(hidden.cutAudit.emptyCount,6);
 }
});
test('layer 1 includes only the admitted complementary octahedron for each vertex',()=>{
 const full=cellFibrationProcess(7,6);
 for(let vertex=1;vertex<=4;vertex++){
  const view=applyCellFibrationCut(full,{enabled:true,vertex,startLayer:1,layer:1,showEmpty:true});
  const additions=view.retainedBodies.filter(b=>b.layer===6);
  assert.equal(additions.length,1);
  assert.deepEqual(additions.map(b=>b.kind).sort(),['octahedron']);
  assert.ok(additions.every(b=>geometricCellLayer(b,vertex)===1));
  assert.equal(view.retainedBodies.length,4);
  for(const b of additions)assert.ok(view.presentationLabels.some(p=>p.cell===b.id));
 }
});
test('range settings migrate old records, persist new bounds, and reject invalid runtime ranges',()=>{
 const cut={enabled:true,vertex:3,startLayer:2,layer:4,showEmpty:false};
 assert.deepEqual(normalizeSceneSettings({cut}).cut,{...cut,highlightUnassigned:false});
 assert.equal(normalizeSceneSettings({cut:{layer:4}}).cut.startLayer,0);
 assert.equal(normalizeSceneSettings({cut:{startLayer:6,layer:2}}).cut.startLayer,2);
 assert.equal(normalizeSceneSettings({cut:{startLayer:-1,layer:2}}).cut.startLayer,0);
 const full=cellFibrationProcess(7,6);
 for(const startLayer of [-1,1.5,7,NaN])assert.throws(()=>applyCellFibrationCut(full,{...cut,startLayer}),/start layer/);
});
