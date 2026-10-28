// Materialize the operator-chosen branch without another selector or quotient.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
const paths={policy:'research/strominger/contracts/su32-working-wiring-family-v1.json',
 wiring:'research/strominger/results/su32-global-reference-wiring-v1/verification.json',
 symmetry:'research/strominger/results/su32-global-wiring-symmetry-v1/verification.json',
 cones:'research/strominger/results/su32-six-cone-compatibility-v1/verification.json',
 trace:'research/strominger/results/su32-fixed-reading-trace-v1/verification.json'};
const hash=x=>createHash('sha256').update(x).digest('hex'),docs={},sourceHashes={};
for(const [name,path] of Object.entries(paths)){
 const bytes=await fs.readFile(path);sourceHashes[path]=hash(bytes);docs[name]=JSON.parse(bytes);
 for(const [p,h] of Object.entries(docs[name].sourceHashes??{}))assert.equal(hash(await fs.readFile(p)),h,`Stale input: ${p}`);
}
const {policy,wiring,symmetry,cones,trace}=docs,copy=x=>structuredClone(x);
assert.equal(policy.selectionKind,'working-assumption-not-derived-law');
assert.equal(policy.retainAllLabelledCandidates,true);assert.equal(policy.chooseRepresentative,false);
assert.equal(policy.retainOriginalProvenance,true);
const classification=symmetry.classifications.find(c=>c.name==='unoriented-boundary-PE-dual-shapes');assert(classification);
function collect(distanceClass){
 const orbit=classification.orbits.find(o=>o.invariantSummaries.every(s=>
  JSON.stringify(s.splitTipToPPandEESquaredDistances)===JSON.stringify(distanceClass)));
 assert(orbit,'Unknown working/control class');
 assert.equal(orbit.members.length,policy.expectedCandidatesPerClass);
 return orbit.members.map(id=>{
  const placement=wiring.localizedSurvivors[id];assert(placement);
  const restrictions=cones.selectedPairRestrictions.find(c=>c.candidate===id);assert(restrictions);
  assert.equal(restrictions.cover,placement.cover);
  const middleCover=trace.middleAssignments.find(c=>c.index===placement.cover);assert(middleCover);
  return {sourceCandidateId:id,cover:placement.cover,selectedPairs:copy(placement),
   retainedMiddleAssignment:copy(middleCover),selectedPairConeRestrictions:copy(restrictions),
   globalPlanRecipe:{source:'research/strominger/checkers/check_su32_global_reference_wiring.mjs',
    sourceHash:wiring.sourceHashes['research/strominger/checkers/check_su32_global_reference_wiring.mjs'],cover:placement.cover}};
 });
}
const working=collect(policy.workingClass),controls=collect(policy.controlClass);
assert.deepEqual([...working,...controls].map(c=>c.sourceCandidateId).sort((a,b)=>a-b),
 Array.from({length:wiring.localizedSurvivors.length},(_,i)=>i));
assert.equal(new Set([...working,...controls].map(c=>c.sourceCandidateId)).size,16);
const distribution=family=>Object.fromEntries(trace.middleAssignments.map(c=>[c.index,family.filter(x=>x.cover===c.index).length]));
assert.deepEqual(Object.values(distribution(working)),[2,2,2,2]);
assert.deepEqual(Object.values(distribution(controls)),[2,2,2,2]);
assert.throws(()=>collect([2,3]));
// Complete common prefix, original records and both central construction trees
// are retained once. Per-candidate covers and selected pair restrictions remain
// separate. No change to cell attachments, record contents or ordering history.
const retainedCommonState={reading:trace.reading,binding:copy(trace.binding),incomingN:trace.incomingN,outgoingN:trace.outgoingN,
 registry:copy(trace.registry),layer2:copy(trace.layer2),layer3:copy(trace.layer3),layer4:copy(trace.layer4),
 centralReconciliation:copy(trace.centralReconciliation),boundaryViews:copy(wiring.witness.plan.boundaryViews)};
const self='research/strominger/checkers/check_su32_working_wiring_family.mjs';sourceHashes[self]=hash(await fs.readFile(self));
const report={schema:'su32.working-wiring-family.v1',passed:true,policy:copy(policy),
 workingCandidates:working,controlCandidates:controls,retainedCommonState,
 counts:{working:working.length,controls:controls.length,workingByCover:distribution(working),controlsByCover:distribution(controls)},
 continuationContract:{input:'All eight working candidates, with their individual selected pairs and contexts. Do not silently replace the family by one representative.',
  comparison:'The eight control candidates remain available for differential tests; the working choice is not evidence against them.',
  provenance:'Original record data, cell references, operand trees and middle-cover provenance remain retained.',
  status:'Operator-admitted working branch, not a native selection theorem, physical admission, or C5 equivalence.'},sourceHashes};
const replay=JSON.parse(JSON.stringify(report));
assert.deepEqual(replay,report);
for(const candidate of [...replay.workingCandidates,...replay.controlCandidates]){
 assert.deepEqual(candidate.selectedPairs,wiring.localizedSurvivors[candidate.sourceCandidateId]);
 assert.deepEqual(candidate.retainedMiddleAssignment,trace.middleAssignments.find(c=>c.index===candidate.cover));
 assert.deepEqual(candidate.selectedPairConeRestrictions,cones.selectedPairRestrictions.find(c=>c.candidate===candidate.sourceCandidateId));
}
assert.deepEqual(replay.retainedCommonState.registry,trace.registry);
assert.deepEqual(replay.retainedCommonState.centralReconciliation,trace.centralReconciliation);
const dir='research/strominger/results/su32-working-wiring-family-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({passed:true,workingClass:policy.workingClass,
 workingCandidateIds:working.map(c=>c.sourceCandidateId),controlCandidateIds:controls.map(c=>c.sourceCandidateId),
 counts:report.counts,output:dir+'/verification.json',status:report.continuationContract.status},null,2));
