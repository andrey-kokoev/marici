import test from 'node:test';
import assert from 'node:assert/strict';
import {retainedPolarityCounts} from '../research/realization-tower/particle-counts.mjs';
import {foldedFibrationProcess,foldedFibrationStages} from '../research/realization-tower/fibration-folded-process.mjs';
test('count overlay uses currently retained geometry, separately on each sheet',()=>{
 const initial=retainedPolarityCounts(foldedFibrationProcess(7,0).retainedBodies);
 assert.deepEqual(initial,{positive:{proton:1,neutron:0,electron:0,total:1},negative:{proton:0,neutron:0,electron:1,total:1}});
 for(let step=0;step<foldedFibrationStages.length;step++){
  const state=foldedFibrationProcess(7,step),counts=retainedPolarityCounts(state.retainedBodies);
  for(const sheet of ['positive','negative'])assert.equal(counts[sheet].total,state.retainedBodies.length);
  assert.equal(counts.positive.proton,counts.negative.electron);assert.equal(counts.positive.neutron,counts.negative.neutron);
 }
 const last=retainedPolarityCounts(foldedFibrationProcess(7,foldedFibrationStages.length-1).retainedBodies);
 assert.deepEqual(last,{positive:{proton:81,neutron:58,electron:36,total:175},negative:{proton:36,neutron:58,electron:81,total:175}});
});
test('duplicate references do not double geometry and incomplete roles fail',()=>{
 const [body]=foldedFibrationProcess(7,0).retainedBodies;
 assert.equal(retainedPolarityCounts([body,body]).positive.total,1);
 assert.throws(()=>retainedPolarityCounts([{id:'missing-sheet',polarityRoles:{positive:'proton'}}]),/both polarity/);
 assert.deepEqual(retainedPolarityCounts([]).positive,{proton:0,neutron:0,electron:0,total:0});
});
