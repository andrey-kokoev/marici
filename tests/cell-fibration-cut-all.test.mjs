import test from 'node:test';
import assert from 'node:assert/strict';
import {cellFibrationProcess} from '../research/realization-tower/cell-fibration-history.mjs';
import {applyCellFibrationCut} from '../research/realization-tower/cell-fibration-cut.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
const ids=bs=>bs.map(b=>b.id).sort();
test('All is the deduplicated union of the four individual ranges, not their intersection or nearest-vertex range',()=>{
 for(const stage of [0,4,6])for(let startLayer=0;startLayer<=6;startLayer++)for(let layer=startLayer;layer<=6;layer++){
  const full=cellFibrationProcess(7,stage),cut={enabled:true,vertex:'all',startLayer,layer,showEmpty:true};
  const all=applyCellFibrationCut(full,cut),individual=[1,2,3,4].map(vertex=>applyCellFibrationCut(full,{...cut,vertex}));
  assert.deepEqual(ids(all.retainedBodies),[...new Set(individual.flatMap(v=>ids(v.retainedBodies)))].sort());
  assert.deepEqual(ids(all.presentationWireframes),[...new Set(individual.flatMap(v=>ids(v.presentationWireframes)))].sort());
  assert.equal(all.cutAudit.counts.total,all.retainedBodies.length);
  assert.equal(all.cutAudit.slotCount,all.retainedBodies.length+all.presentationWireframes.length);
  assert.equal(new Set(all.presentationLabels.map(p=>p.cell)).size,all.presentationLabels.length);
  const visible=new Set([...ids(all.retainedBodies),...ids(all.contextBodies)]);
  for(const c of full.cellFibrationAudit.corners)assert.ok(visible.has(c.cell));
  assert.ok(all.contextBodies.every(b=>!all.cutAudit.visibleIds.includes(b.id)));
  assert.deepEqual(all.cutAudit.vertices,[1,2,3,4]);assert.equal(all.cutAudit.combination,'union');
 }
});
test('All layer 1 shows every complementary addition alongside twelve same-orientation cells',()=>{
 const full=cellFibrationProcess(7,6),view=applyCellFibrationCut(full,{enabled:true,vertex:'all',startLayer:1,layer:1,showEmpty:true});
 assert.equal(view.retainedBodies.length,16);assert.equal(view.contextBodies.length,4);
 assert.equal(view.retainedBodies.filter(b=>b.layer===6).length,4);
 assert.equal(view.retainedBodies.filter(b=>b.kind==='octahedron').length,4);
 assert.deepEqual(view.cutAudit.counts,{proton:4,neutron:8,electron:4,total:16});
 const entire=applyCellFibrationCut(full,{enabled:true,vertex:'all',startLayer:0,layer:6});
 assert.equal(entire.retainedBodies.length,88);assert.equal(entire.contextBodies.length,0);
});
test('All persists alongside backward-compatible numeric vertex selections',()=>{
 const cut={enabled:true,vertex:'all',startLayer:1,layer:2,showEmpty:false};
 assert.deepEqual(normalizeSceneSettings({cut}).cut,{...cut,highlightUnassigned:false});
 assert.equal(normalizeSceneSettings({cut:{...cut,highlightUnassigned:true}}).cut.highlightUnassigned,true);
 for(let vertex=1;vertex<=4;vertex++)assert.equal(normalizeSceneSettings({cut:{...cut,vertex}}).cut.vertex,vertex);
 assert.equal(normalizeSceneSettings({cut:{vertex:'invalid'}}).cut.vertex,1);
});
