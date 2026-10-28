import test from 'node:test';
import assert from 'node:assert/strict';
import {edgeProcedure} from '../research/realization-tower/edge-ray-model.mjs';
import {neutronMediation} from '../research/realization-tower/neutron-mediated-connection.mjs';
test('local face/vertex counterparts already connect through assigned neutrons',()=>{
 for(const branch of [1,3]){
  const state=edgeProcedure(4,11,branch);
  for(const comparison of state.faceVertexComparisons){
   const r=neutronMediation(4,state.assignments,comparison.cell,comparison.owner);
   assert(r.existingNeutronMediation);assert.equal(r.paths.length,2);assert.equal(r.distance,3);
   assert(r.fillerCells.every(id=>state.assignments.find(a=>a.cell===id)?.role==='neutron'));
   assert(r.witnesses.every(w=>w.faces.every(f=>f.vertices.length===3)));
  }
  assert.deepEqual(neutronMediation(4,state.assignments,132,341).paths,[[132,339,340,341],[132,339,342,341]]);
  assert.deepEqual(neutronMediation(4,state.assignments,127,311).paths,[[127,313,312,311],[127,313,314,311]]);
 }
});
test('k4 E/P admits two symmetry-related neutron routes in one octahedral filler',()=>{
 for(const branch of [1,3]){
  const state=edgeProcedure(4,11,branch),before=JSON.stringify(state.assignments);
  const r=neutronMediation(4,state.assignments,132,127);
  assert(r.connected);assert.equal(r.distance,4);
  assert.deepEqual(r.paths,[[132,333,332,331,127],[132,333,334,331,127]]);
  assert.deepEqual(r.fillerCells,[331,332,333,334]);assert.equal(r.octahedralGroup,53);
  assert(r.symmetryExchangesEndpoints&&r.symmetryPreservesAllRoutes&&r.symmetryPreservesFiller);
  assert.equal(r.attachments.length,2);assert.deepEqual(r.attachments.map(f=>f.to).sort((a,b)=>a-b),[127,132]);
  assert(r.witnesses.every(w=>w.faces.every(f=>f.vertices.length===3)));
  assert.equal(r.singleCellRuleCanStart,false);assert(r.everyCellHasTwoSupportsAfterGroupAttachment);
  assert.deepEqual(r.supportCounts.map(s=>s.existing.length),[1,0,1,0]);
  assert.equal(JSON.stringify(state.assignments),before);
 }
});
