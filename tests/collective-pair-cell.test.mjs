import test from 'node:test';
import assert from 'node:assert/strict';
import {buildCollectivePairCell,encodeCollective,decodeCollective} from '../research/realization-tower/collective-pair-cell.mjs';
import {buildFoldedFibration,foldedFibrationProcess,foldedFibrationStages} from '../research/realization-tower/fibration-folded-process.mjs';
const model=buildFoldedFibration(),collective=buildCollectivePairCell(model);
test('collective carrier is built from the connected minority sector and its existing boundary port',()=>{
 assert.equal(collective.support.length,36);assert.equal(collective.links.length,121);
 assert.equal(collective.retention.contrasts.length,35);assert.equal(collective.witness.outerPorts,1);
 assert.ok(collective.support.includes(collective.port));assert.ok(model.outer.some(f=>f.owners.includes(collective.port)));
 assert.deepEqual(collective.polarityRoles,{positive:'electron',negative:'proton'});
 assert.equal(collective.physicalCellAdded,false);assert.equal(collective.nativeParticleRealization,false);
});
test('collective observation and retained contrasts recover every member coordinate',()=>{
 for(let i=0;i<36;i++){
  const values=Array.from({length:36},(_,j)=>Number(i===j));assert.deepEqual(decodeCollective(encodeCollective(values)),values);
 }
 assert.throws(()=>decodeCollective({sum:0,members:36,contrasts:[]}),/Complete/);
});
test('effective counts replace the minority readings rather than add to all 36',()=>{
 assert.deepEqual(collective.counts.positive,{proton:81,neutron:58,electron:1,total:140});
 assert.deepEqual(collective.counts.negative,{proton:1,neutron:58,electron:81,total:140});
 assert.deepEqual(collective.counts.chargedReadings,{proton:82,electron:82});
 assert.equal(collective.counts.sharedCarrierCount,140);
});
test('materialization adds a visible collective record, not overlapping lattice geometry',()=>{
 const last=foldedFibrationStages.length-2,before=foldedFibrationProcess(7,last-1),after=foldedFibrationProcess(7,last);
 assert.equal(before.collectiveCells.length,0);assert.equal(after.collectiveCells.length,1);
 assert.deepEqual(after.retainedBodies,before.retainedBodies);assert.equal(after.retainedBodies.length,175);
 assert.equal(after.fibrationAudit.phase,'collective-cell');assert.equal(after.canAdvance,true);
 assert.ok(after.presentationLabels.some(p=>p.cell===collective.id&&p.polarityText.negative==='P*'));
 assert.deepEqual(after.fibrationAudit.filler.confirmation,before.fibrationAudit.filler.confirmation);
 assert.equal(after.fibrationAudit.collective.independentPolarityParticles,false);
});
test('missing boundary port is rejected rather than choosing an arbitrary new cell',()=>{
 const bad=structuredClone(model);bad.outer=bad.outer.filter(f=>!f.owners.includes(collective.port));
 assert.throws(()=>buildCollectivePairCell(bad),/unique existing outer port/);
});
