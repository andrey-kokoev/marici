import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {GenerativeAssemblyRules,frontier,applyBatch,compatibleBatches,serializeRules} from '../native-retained-batch-attempt.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const out=path.join(root,'research/strominger/results/native-retained-batch-attempt');
const checks=[];
function check(name,fn){fn();checks.push(name);}
const r=new GenerativeAssemblyRules(),seed=[r.root];
const rootOps=r.outgoing(r.root).map(i=>r.operations[i]);
const pn=rootOps.find(o=>o.kind==='PN'),reader=rootOps.find(o=>o.kind==='reader-phase-advance');
check('root is an admitted marked proton with all five coefficient slots',()=>{
 assert.equal(r.charts[r.packets[r.root].chart].species,'proton');assert.deepEqual(r.packets[r.root].permutation,[0,1,2,3,4]);
 assert.deepEqual(rootOps.map(o=>o.kind),['PN','reader-phase-advance']);
});
const afterPN=applyBatch(r,seed,[pn.id]);
check('actual PN attachment preserves native face and full-map witness',()=>{
 assert.equal(afterPN.valid,true);assert.deepEqual(afterPN.inspection.counts,{proton:1,neutron:1,electron:0});assert.equal(afterPN.inspection.allContactsWitnessed,true);
});
const nOps=r.outgoing(pn.target).map(i=>r.operations[i]);
const ne=nOps.find(o=>o.kind==='NE'),nn=nOps.find(o=>o.kind==='NN-phase-advance');
const exited=applyBatch(r,afterPN.packets,[ne.id]),continued=applyBatch(r,afterPN.packets,[nn.id]);
check('NE and NN continuations are each globally valid from the same PN snapshot',()=>{
 assert.equal(exited.valid,true);assert.equal(continued.valid,true);
 assert.deepEqual(exited.inspection.counts,{proton:1,neutron:1,electron:1});
 assert.deepEqual(continued.inspection.counts,{proton:1,neutron:2,electron:0});
 assert.equal(exited.inspection.certifiedExit,true);
});
const conflict=applyBatch(r,afterPN.packets,[ne.id,nn.id]);
const eChart=r.charts[r.packets[ne.target].chart],nChart=r.charts[r.packets[nn.target].chart];
check('saturating both native alternatives fails at one concrete occupied cell',()=>{
 assert.equal(conflict.valid,false);assert.equal(conflict.reason,'occupied-cell-species-conflict');
 assert.equal(eChart.cell,nChart.cell);assert.notEqual(eChart.species,nChart.species);assert.deepEqual(ne.face,nn.face);
});
check('conflicting operation pair is inclusion-minimal on its admitted source snapshot',()=>{
 for(const ops of [[],[ne.id],[nn.id]])assert.equal(applyBatch(r,afterPN.packets,ops).valid,true);
});
check('joint updates cannot consume a newly created packet in the same snapshot',()=>{
 assert.throws(()=>applyBatch(r,seed,[pn.id,ne.id]),/prior snapshot/);
});
check('full coefficient maps compose and invert on every basis vector',()=>{
 for(const op of [pn,reader,ne,nn]){
  const from=r.packets[op.source],to=r.packets[op.target];
  for(let k=0;k<5;k++){
   const basis=Array.from({length:5},(_,i)=>Number(i===k));
   const a=from.permutation.map(i=>basis[i]),b=op.permutation.map(i=>a[i]);
   assert.deepEqual(b,to.permutation.map(i=>basis[i]));
   assert.deepEqual(op.permutation.map((_,i)=>b[op.permutation.indexOf(i)]),a);
  }
 }
});
check('forged coefficient and origin payloads are rejected by native validator',()=>{
 const t=r.packets[ne.target];
 assert.throws(()=>r.validateTransfer(ne,r.packets[ne.source],{...t,origin:t.origin+1}));
 assert.throws(()=>r.validateTransfer(ne,r.packets[ne.source],{...t,permutation:[0,1,2,3,4]}));
});
const rootJoint=applyBatch(r,seed,[pn.id,reader.id]);
check('first joint frontier is compatible rather than assuming all parallelism fails',()=>{
 assert.equal(rootJoint.valid,true);assert.equal(rootJoint.packets.length,3);assert.equal(rootJoint.inspection.counts.proton,1);
});
const exploratory=[];let layer=[seed];
for(let round=0;round<3;round++){
 const next=new Map();
 for(const packets of layer){
  const result=compatibleBatches(r,packets,{maxCandidates:14});
  assert.equal(result.complete,true,'unexpected resource stop');
  check(`round${round} snapshot${packets.join('-')}: exhaustive subset accounting and maximality`,()=>{
   assert.equal(result.accepted.length+Object.values(result.rejections).reduce((a,b)=>a+b,0),result.subsetsExamined);
   const full=result.accepted.filter(a=>!result.accepted.some(b=>a.mask!==b.mask&&(a.mask&b.mask)===a.mask));
   assert.deepEqual(result.maximal.map(a=>a.mask),full.map(a=>a.mask));
  });
  const batches=result.maximal.map(batch=>{
   const forward=applyBatch(r,packets,batch.operations),reverse=applyBatch(r,packets,[...batch.operations].reverse());
   assert.equal(forward.valid,true);assert.deepEqual(forward.packets,reverse.packets);
   next.set(forward.packets.join(','),forward.packets);
   return {operations:batch.operations,packets:forward.packets,inspection:forward.inspection};
  });
  exploratory.push({round,sourcePackets:packets,candidates:result.candidates,subsetsExamined:result.subsetsExamined,
   acceptedSubsets:result.accepted.length,rejections:result.rejections,maximalBatches:batches});
 }
 layer=[...next.values()];
}
check('candidate resource stop is explicit and not a completeness result',()=>{
 const stopped=compatibleBatches(r,seed,{maxCandidates:1});assert.equal(stopped.complete,false);assert.equal(stopped.reason,'candidate-resource-bound');
});
check('nonmaximal terminating PNE branch remains admissible, not erased by exploratory scheduling',()=>{
 assert.equal(r.inspect(exited.packets).certifiedExit,true);assert.ok(frontier(r,exited.packets).length>0);
});
const artifact={schema:'marici.native-retained-batch-attempt.v1',
 scope:'One fixed native marked seed; exhaustive subsets on snapshots reached by three exploratory maximal-compatible rounds. Maximality is an explicit scheduling hypothesis, not a physical selection law or all-assembly completeness.',
 seedPackets:seed,firstPN:afterPN,terminatingAlternative:exited,continuingAlternative:continued,
 failedJoint:{sourcePackets:afterPN.packets,operations:[ne.id,nn.id],result:conflict,
 witness:{cell:eChart.cell,vertices:r.geometry.cells[eChart.cell].vertices,attachmentFace:ne.face,
 electronPacket:r.packets[ne.target],neutronPacket:r.packets[nn.target],electronChart:eChart,neutronChart:nChart,
 violatedConstraint:'one occupied primitive cannot simultaneously have species electron and neutron'}},
 exploratory,terminalRoundConfigurations:layer.length,
 nextMissingRule:'A retained compatibility/selection or comparison law for competing native continuations. Shared geometry alone cannot make NE and NN simultaneous. Whole-octahedron/composite Pb carrier binding is still separate.',
 targetQuotaUsed:false,completedPbInputUsed:false,fullPbConstructionEstablished:false,physicalSelectionEstablished:false,
 nativeRecords:serializeRules(r)};
await fs.mkdir(out,{recursive:true});await fs.writeFile(path.join(out,'attempt.json'),JSON.stringify(artifact,null,2)+'\n');
// Fingerprint the live static local import closure, plus the written derivation.
const sources=new Set();
async function visit(relative){
 if(sources.has(relative))return;sources.add(relative);
 const text=await fs.readFile(path.join(root,relative),'utf8');
 for(const match of text.matchAll(/(?:from\s*|import\s*)['"](\.[^'"]+)['"]/g)){
  const child=path.posix.normalize(path.posix.join(path.posix.dirname(relative),match[1]));
  if(/\.(?:mjs|js|json)$/.test(child))await visit(child);
 }
}
await visit('research/strominger/checkers/check_native_retained_batch_attempt.mjs');
await visit('research/strominger/native-retained-batch-attempt-v1.md');
const sourceHashes=Object.fromEntries(await Promise.all([...sources].sort().map(async p=>[p,crypto.createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex')])));
const report={status:'passed',check_count:checks.length,checks,sourceHashes,
 artifactSha256:crypto.createHash('sha256').update(await fs.readFile(path.join(out,'attempt.json'))).digest('hex'),
 concreteNativeAttempt:true,minimalJointConflict:'NE versus NN-phase-advance on the same primitive after PN',
 exploredRounds:3,exploredSnapshots:exploratory.length,terminalRoundConfigurations:layer.length,
 targetQuotaUsed:false,completedPbInputUsed:false,fullPbConstructionEstablished:false,physicalSelectionEstablished:false};
await fs.writeFile(path.join(out,'verification.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report,null,2));
