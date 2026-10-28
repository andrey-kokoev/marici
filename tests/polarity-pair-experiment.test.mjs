import test from 'node:test';
import assert from 'node:assert/strict';
import {buildFoldedFibration} from '../research/realization-tower/fibration-folded-process.mjs';
import {cellFibrationProcess} from '../research/realization-tower/cell-fibration-history.mjs';
import {runPolarityPairExperiment,trialPairRole} from '../research/realization-tower/polarity-pair-experiment.mjs';
const geometry=buildFoldedFibration().geometry,full=cellFibrationProcess(7,5),experiment=runPolarityPairExperiment(geometry,full.retainedBodies);
const key=vs=>vs.map(v=>v.map(x=>Number(x.toFixed(8))).join(',')).sort().join('|');
test('only the two declared unordered pair rules are applied',()=>{
 assert.equal(trialPairRole('proton','proton'),'neutron');
 assert.equal(trialPairRole('proton','electron'),'proton');assert.equal(trialPairRole('electron','proton'),'proton');
 for(const a of ['proton','neutron','electron'])for(const b of ['proton','neutron','electron']){
  assert.equal(trialPairRole(a,b),trialPairRole(b,a));
  if(a!=='proton'&&b!=='proton'||a==='neutron'||b==='neutron')assert.equal(trialPairRole(a,b),null);
 }
 assert.throws(()=>trialPairRole('unknown','proton'));
});
test('strict mirroring cannot produce PP and does not turn tetrahedra into octahedra',()=>{
 assert.deepEqual(experiment.sameCell.summary,{pairs:84,PP:0,PE:44,unspecified:40});
 assert.equal(experiment.sameCell.carrierMismatch,true);
 assert.deepEqual(experiment.oppositeFace.summary,{pairs:140,PP:0,PE:74,unspecified:66});
 assert.equal(experiment.oppositeFace.boundaryDirections,84);
 assert.equal(experiment.oppositeFace.consistent,6);assert.equal(experiment.oppositeFace.conflicts,29);
 assert.deepEqual(experiment.oppositeFace.agreedRoles,{proton:1,neutron:4,electron:1});
 const byId=new Map(geometry.map(g=>[g.id,g]));
 for(const t of experiment.oppositeFace.targets){
  assert.equal(t.proposals.length,4);assert.equal(new Set(t.proposals.map(p=>p.via)).size,4);
  for(const p of t.proposals){
   const oct=byId.get(p.via),source=byId.get(p.source),target=byId.get(t.target);
   const c=oct.vertices[0].map((_,i)=>oct.vertices.reduce((s,v)=>s+v[i],0)/6);
   assert.equal(key(source.vertices.map(v=>v.map((x,i)=>2*c[i]-x))),key(target.vertices));
   assert.ok(source.faces.some(f=>oct.faces.some(o=>key(f)===key(o))));
   assert.ok(target.faces.some(f=>oct.faces.some(o=>key(f)===key(o))));
  }
  if(t.status==='conflict')assert.equal(t.suggestedRole,null);
 }
});
test('independent neighboring pairs expose PP and PE without converting pair counts to cells',()=>{
 assert.deepEqual(experiment.neighboringSources.summary,{pairs:336,PP:15,PE:55,unspecified:266});
 assert.deepEqual(experiment.neighboringSources.octahedralStatuses,{covered:1,partial:40,conflict:7,unspecified:8});
 for(const o of experiment.neighboringSources.octahedra){
  assert.equal(new Set(o.sourceNeighbors).size,4);assert.equal(o.neighborPairs.length,6);
  if(o.neighborAssessment.status==='covered'){assert.deepEqual(o.neighborAssessment.roles,['neutron']);assert.equal(o.neighborAssessment.unspecified,0);}
  if(o.neighborAssessment.status==='partial')assert.ok(o.neighborAssessment.unspecified>0);
 }
});
test('archived experiment does not mutate or participate in the active construction',()=>{
 const original=JSON.stringify(full.retainedBodies);
 runPolarityPairExperiment(geometry,full.retainedBodies);
 assert.equal(JSON.stringify(full.retainedBodies),original);
 assert.equal(full.cellFibrationAudit.polarityExperiment,undefined);
 assert.equal(cellFibrationProcess(7,6).cellFibrationAudit.polarityExperiment,undefined);
});
test('summary and coverage are independent of enumeration order',()=>{
 const reversed=runPolarityPairExperiment([...geometry].reverse(),[...full.retainedBodies].reverse());
 assert.deepEqual(reversed.neighboringSources.summary,experiment.neighboringSources.summary);
 assert.deepEqual(reversed.neighboringSources.octahedralStatuses,experiment.neighboringSources.octahedralStatuses);
 assert.deepEqual(reversed.oppositeFace.agreedRoles,experiment.oppositeFace.agreedRoles);
});
