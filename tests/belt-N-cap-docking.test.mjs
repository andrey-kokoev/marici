import test from 'node:test';import assert from 'node:assert/strict';
import {presentCentralBelt,centralParentPoint} from '../research/realization-tower/central-belt-layout.mjs';
import {doubleEsd7RuleProcess,doubleEsd7Rules} from '../research/realization-tower/double-esd7-process.mjs';
import {worldPoint} from '../research/realization-tower/normal-ray-model.mjs';
import {filterBeltView,filterComplexVisibility} from '../examples/normal-ray/complex-visibility.js';
const sub=(a,b)=>a.map((v,i)=>v-b[i]),dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0);
test('single native N tips are retained as records, cut from display, and docked without overlap',()=>{
 const source=doubleEsd7RuleProcess(7,doubleEsd7Rules.map(r=>r.id)),snapshot=JSON.stringify(source),p=presentCentralBelt(source),surface=p.beltSurface;
 assert.equal(p.parentCutAudit.caps.length,2);
 for(const cap of p.parentCutAudit.caps){
  assert.equal(cap.retainedCell.vertices.length,4);assert.equal(cap.retainedCell.id,cap.cellId);
  const target=surface.faces.find(f=>f.id===cap.targetFace);assert.equal(target.slot,3);assert.equal(target.patch,cap.copy);
  const dst=target.indices.map(i=>surface.vertices[i]);for(const v of cap.cutFace){const mapped=worldPoint(centralParentPoint(v,cap.copy));assert.ok(Math.min(...dst.map(q=>Math.hypot(...sub(mapped,q))))<1e-12);}
  const plane=p=>dot(sub(p,cap.targetCentre),cap.targetNormal);
  for(const v of surface.cellulation.vertices)assert.ok(plane(v)>=-1e-12,'belt lies inside its supporting face plane');
  const remaining=[...p.retainedBodies,...p.emptyBodies].filter(b=>b.id.startsWith(cap.copy+':')&&b.id!==cap.cellId);assert.equal(remaining.length,174);
  for(const b of remaining)for(const v of b.vertices)assert.ok(plane(worldPoint(v))<=1e-12,'retained parent lies entirely outside belt');
 }
 for(const mode of ['geometry','wiring']){const view=filterBeltView(filterComplexVisibility(p),mode);assert.equal(view.parentCutAudit.visibleCutCount,2);assert.equal(view.complexVisibilityAudit.visibleParentCells,350);assert.equal(view.parentCutAudit.visibleReplacementCount,2);for(const id of p.parentCutAudit.removedCellIds)assert.equal(view.retainedBodies.find(b=>b.id===id).role,'electron');for(const field of ['emptyBodies','presentationWireframes'])assert.ok(view[field].every(b=>!p.parentCutAudit.removedCellIds.includes(b.id)));assert.equal(view.parentCutAudit.caps.length,2);}
 assert.equal(JSON.stringify(source),snapshot);
});
