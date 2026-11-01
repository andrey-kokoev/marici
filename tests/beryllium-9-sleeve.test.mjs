import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildBeryllium8Reference} from '../research/realization-tower/beryllium-8-reference.mjs';
import {buildBeryllium9Reference} from '../research/realization-tower/beryllium-9-reference.mjs';
import {buildBranchingSeed} from '../research/realization-tower/branching-seed.mjs';
import {buildSulfurRouteComparison} from '../research/realization-tower/sulfur-route-comparison.mjs';
import {buildBerylliumDirectionComponents} from '../research/realization-tower/beryllium-8-direction-components.mjs';
import {buildBeryllium8Assembly} from '../research/realization-tower/beryllium-8-assembly.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
const source=buildBeryllium8Reference(),trial=buildBeryllium9Reference(),seed=buildBranchingSeed({processId:'beryllium-9'});
test('four mixed identities, not extra wires, pass through an explicit central sleeve',()=>{
 assert.equal(trial.strands.length,8);assert.deepEqual(trial.strands.map(s=>s.id),source.strands.map(s=>s.id));
 assert.deepEqual(trial.permutation,source.permutation);assert.deepEqual(trial.matrixBasis,source.matrixBasis);
 const selected=trial.strands.filter(s=>s.throughSleeve);assert.deepEqual(selected.map(s=>s.outputSlot+1),[7,2,1,8]);
 assert.equal(trial.sleeve.passages.length,4);assert.equal(trial.sleeve.incomingPairs.length,2);assert.equal(trial.sleeve.outgoingPairs.length,2);
 for(const pair of [...trial.sleeve.incomingPairs,...trial.sleeve.outgoingPairs])assert.equal(pair.strandIds.length,2);
 const slots=pairs=>pairs.map(pair=>pair.strandIds.map(id=>selected.find(s=>s.id===id).outputSlot+1));
 assert.deepEqual(slots(trial.sleeve.incomingPairs),[[7,2],[1,8]]);assert.deepEqual(slots(trial.sleeve.outgoingPairs),[[2,1],[7,8]]);
 for(const [i,s]of trial.strands.entries()){
  const original=source.strands[i];assert.deepEqual(s.polarities,original.polarities);assert.equal(s.inputSlot,original.inputSlot);assert.equal(s.outputSlot,original.outputSlot);
  if(s.throughSleeve){assert.equal(s.guide.length,5);assert.deepEqual(s.guide[2],trial.sleeve.point);assert.deepEqual([s.guide[0],s.guide[1],s.guide[3],s.guide[4]],original.guide);}
  else assert.deepEqual(s,original);
 }
 assert.equal(trial.edges.length,16);assert.equal(trial.edges.filter(e=>e.sleeveLink).length,4);assert(trial.edges.filter(e=>e.sleeveLink).every(e=>e.strandIds.length===2));
});
test('three assemblies contain actual separated four-strand passages inside the central region',()=>{
 const columns=buildSulfurRouteComparison(seed,{reference:trial}).reference;
 for(const current of [columns,...buildBerylliumDirectionComponents(columns).map(row=>row.columns)]){
  const model=buildBeryllium8Assembly(current,trial);assert.equal(model.audit.vertices,7);assert.equal(model.audit.shellVertices,6);assert.equal(model.audit.edges,16);assert.equal(model.audit.strands,8);assert.equal(model.audit.polarityArrows,16);
  assert.deepEqual(model.sleeve.point,[0,0,0]);const through=model.strands.filter(s=>model.sleeve.strandIds.includes(s.id));assert.equal(through.length,4);
  assert.equal(new Set(through.map(s=>JSON.stringify(s.displayGuide[2]))).size,4);
  for(const s of through){assert.deepEqual(s.guide[2],[0,0,0]);assert(Math.hypot(...s.displayGuide[2])<model.sleeve.radius);assert.equal(s.arrows.length,4);assert.equal(s.runs.length,4);assert(s.points.flat().every(Number.isFinite));}
  for(const s of model.strands.filter(s=>!model.sleeve.strandIds.includes(s.id)))assert(s.points.every(p=>Math.hypot(...p)>model.sleeve.radius));
 }
});
test('trial is switchable and does not mutate Be-8 or alter layer construction',()=>{
 const clone=buildBeryllium9Reference({centralSleeve:false});assert.deepEqual(clone.strands,source.strands);assert.deepEqual(clone.edges,source.edges);assert.equal(clone.sleeve,null);
 assert.deepEqual(source,buildBeryllium8Reference());assert.equal(seed.audit.depth,4);assert.equal(seed.audit.edges,240);
 assert.equal(normalizeSceneSettings({}).appearance.be9CentralSleeve,true);assert.equal(normalizeSceneSettings({appearance:{be9CentralSleeve:false}}).appearance.be9CentralSleeve,false);
});
