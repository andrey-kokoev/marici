import test from 'node:test';
import assert from 'node:assert/strict';
import {evaluateNativeFillerComparison} from '../research/strominger/four-by-four-filler-comparison.mjs';
import {foldedFibrationProcess,foldedFibrationStages} from '../research/realization-tower/fibration-folded-process.mjs';
import {processState} from '../research/realization-tower/normal-ray-processes.mjs';
test('candidate filler applies to all five complex coefficients and reconstructs every native basis',()=>{
 for(let basis=0;basis<5;basis++)for(const part of [0,1]){
  const source=Array.from({length:5},(_,i)=>[Number(i===basis&&part===0),Number(i===basis&&part===1)]),r=evaluateNativeFillerComparison(source);
  assert.equal(r.input.length,16);assert.equal(r.modes.length,14);
  assert.deepEqual(r.boundary.P,source);
  assert.deepEqual(r.confirmation,{maxReconstructionError:0,maxNeutralCharge:0,maxBasisReconstructionError:0,allFiveComplexCoefficients:true});
  for(const mode of r.modes.filter(m=>m.kind!=='native-N-slot'))assert.deepEqual(mode.coefficients,Array.from({length:5},()=>[0,0]));
 }
});
test('two filler actions follow the retained return in the actual fibration process',()=>{
 const {growthRounds,returnRounds}=foldedFibrationProcess(7,0).fibrationAudit,endFlow=growthRounds+returnRounds;
 const pending=foldedFibrationProcess(7,endFlow),applied=foldedFibrationProcess(7,endFlow+1),confirmed=processState('fibration-12x12',7,endFlow+2);
 assert.equal(pending.fibrationAudit.returnedToMinusP,true);assert.equal(pending.fibrationAudit.filler.state,'pending');assert.equal(pending.canAdvance,true);
 assert.equal(applied.fibrationAudit.phase,'filler-comparison');assert.equal(applied.fibrationAudit.filler.state,'applied');assert.equal(applied.canAdvance,true);
 assert.equal(confirmed.fibrationAudit.filler.state,'confirmed');assert.equal(confirmed.canAdvance,true); // collective cell materialization follows
 assert.deepEqual(pending.retainedBodies,applied.retainedBodies);assert.deepEqual(applied.retainedBodies,confirmed.retainedBodies);
 assert.equal(confirmed.retainedBodies.length,175);assert.equal(confirmed.fibrationAudit.filler.nativeRealization.independentNewNeutronStatesEstablished,false);
 assert.equal(confirmed.fibrationAudit.confirmations.length,pending.fibrationAudit.confirmations.length);
 assert.throws(()=>foldedFibrationProcess(7,foldedFibrationStages.length));
});
