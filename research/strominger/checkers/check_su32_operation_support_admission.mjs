// Frozen global support audit. No record-to-coefficient encoding is invented.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
import {runAlignedNativeGrowth} from '../aligned-native-growth-model.mjs';
const dir='research/strominger/results/su32-operation-support-admission-v1';
const contractPath=dir+'/contract.json',contractBytes=await fs.readFile(contractPath),contract=JSON.parse(contractBytes);
const hash=x=>createHash('sha256').update(x).digest('hex');
const paths={wiring:'research/strominger/results/su32-global-reference-wiring-v1/verification.json',
 symmetry:'research/strominger/results/su32-global-wiring-symmetry-v1/verification.json',
 trace:'research/strominger/results/su32-fixed-reading-trace-v1/verification.json',
 fixture:'research/strominger/results/su32-hopf-tests-v1/fixture.json'};
const docs={};
for(const [name,path] of Object.entries(paths)){
 docs[name]=JSON.parse(await fs.readFile(path,'utf8'));
 for(const [p,h] of Object.entries(docs[name].sourceHashes))assert.equal(hash(await fs.readFile(p)),h,`Stale input: ${p}`);
}
const {wiring,symmetry,trace,fixture}=docs,labels=['P+','P-','E+','E-'],marks=['C0','M0','C1','M1','C2'];
// Fix the real operation before considering ANY target assignment or injection.
const rules=new GenerativeAssemblyRules();
const pn=rules.outgoing(rules.root).map(i=>rules.operations[i]).filter(o=>o.kind==='PN');assert.equal(pn.length,1);
const choices=rules.outgoing(pn[0].target).map(i=>rules.operations[i]).filter(o=>o.kind==='NE');assert.equal(choices.length,1);
const operation=choices[0];assert(rules.validateTransfer(operation));
const source=rules.packets[operation.source],target=rules.packets[operation.target];
const sourceChart=rules.charts[source.chart],targetChart=rules.charts[target.chart];
const moved=operation.permutation.flatMap((from,to)=>from!==to?[to]:[]);
assert.deepEqual(moved,[1,4]);assert.deepEqual(moved.map(i=>marks[i]),['M0','C2']);
// Independent positive control on the ORIGINAL reference bank, not Su32.
const control=runAlignedNativeGrowth(Array.from({length:8},(_,i)=>[i+2,3*i-1]));
assert.equal(control.assembly.certifiedExit,true);
assert.deepEqual(control.records.filter(r=>r.operation).map(r=>[r.stage,r.operation.kind]),[[3,'PN'],[5,'NE']]);
for(const stage of control.records.filter(r=>r.operation))for(let i=0;i<8;i++)if(stage.permutation[i]!==i)assert.equal(i^stage.permutation[i],stage.direction);
assert.deepEqual(control.normalized,control.initial);assert.deepEqual(control.recovered,control.initial);
// Replay fixed whole-plan middle lanes; no alternative edges are introduced.
const between=(a,b)=>fixture.interfaces.filter(f=>f.ports.some(p=>p.split('@')[0]===a)&&f.ports.some(p=>p.split('@')[0]===b));
const role=new Map(fixture.cells.map(c=>[c.id,c.role]));
const outgoing=new Map(trace.middleAssignments.map(cover=>{
 const edges=[];
 for(const r of cover.routes)for(const [from,to] of [[r.sourceP,r.targetE],[r.sourceE,r.targetP]]){
  const members=r.members.filter(m=>between(from,m).length&&between(m,to).length);assert.equal(members.length,1);
  edges.push({from:members[0],to,face:between(members[0],to)[0].id,targetRole:role.get(to)});
 }
 return [cover.index,edges];
}));
const inject=(remaining,n)=>n===0?[[]]:remaining.flatMap((x,i)=>inject(remaining.filter((_,j)=>i!==j),n-1).map(t=>[x,...t]));
const injections=inject([0,1,2,3,4],4);assert.equal(injections.length,120);
const candidates=wiring.localizedSurvivors,coarse=symmetry.classifications.find(c=>c.name==='unoriented-boundary-PE-dual-shapes');
assert.equal(candidates.length,16);assert.equal(coarse.orbits.length,2);
const orbitOf=id=>coarse.orbits.findIndex(o=>o.members.includes(id));
const pairCounts={},trials=[];let supportClosed=0;
const candidateCounts=candidates.map((c,id)=>({id,cover:c.cover,orbit:orbitOf(id),supportMatches:0,faceRoleMatches:0}));
for(const injection of injections){
 const image=new Set(injection),closed=[...image].every(i=>image.has(operation.permutation[i]));
 const pair=labels.filter((_,i)=>moved.includes(injection[i]));
 if(closed){assert.equal(pair.length,2);supportClosed++;pairCounts[pair.join('|')]=(pairCounts[pair.join('|')]??0)+1;}
 else assert.notEqual(pair.length,2);
 const matches=candidates.map((candidate,id)=>{
  const placement=closed?candidate.placements.find(p=>pair.every(k=>p.pair.includes(k))):null;
  if(closed)assert(placement,'All six pair identities must occur in each complete candidate');
  const faces=placement?outgoing.get(candidate.cover).filter(e=>e.from===placement.at&&e.targetRole==='electron'):[];
  if(placement)candidateCounts[id].supportMatches++;
  if(faces.length)candidateCounts[id].faceRoleMatches++;
  return {candidate:id,supportMatch:Boolean(placement),selectedSite:placement?.at??null,
   matchingElectronFaces:faces,nativeAdmission:null};
 });
 const orbitFaceRoleMatches=coarse.orbits.map(o=>matches.filter(m=>o.members.includes(m.candidate)&&m.matchingElectronFaces.length).length);
 assert.equal(orbitFaceRoleMatches[0],orbitFaceRoleMatches[1],'Compare each globally fixed injection, not merely aggregate counts');
 trials.push({orbitFaceRoleMatches,injection:Object.fromEntries(labels.map((k,i)=>[k,{slot:injection[i],mark:marks[injection[i]],vertex:sourceChart.aliases[marks[injection[i]]]}])),
  omittedMark:marks.find((_,i)=>!image.has(i)),supportClosed:closed,matchedPair:closed?pair:null,matches});
}
assert.equal(supportClosed,72);assert.equal(Object.keys(pairCounts).length,6);
assert(Object.values(pairCounts).every(n=>n===12));assert(candidateCounts.every(c=>c.supportMatches===72));
const orbitTotals=coarse.orbits.map((o,index)=>({orbit:index,distanceClass:o.invariantSummaries[0].splitTipToPPandEESquaredDistances,
 candidates:o.members.length,supportMatches:candidateCounts.filter(c=>c.orbit===index).reduce((n,c)=>n+c.supportMatches,0),
 faceRoleMatches:candidateCounts.filter(c=>c.orbit===index).reduce((n,c)=>n+c.faceRoleMatches,0)}));
// Native inputs retain their independently supplied full marked state and face.
// The relaxed injections do not discharge any of these bindings.
let negativeControls=0;const reject=f=>{assert.throws(f);negativeControls++;};
reject(()=>rules.validateTransfer({...operation,permutation:[0,1,2,3,4]}));
reject(()=>rules.validateTransfer({...operation,face:['absent']}));
reject(()=>runAlignedNativeGrowth(Array.from({length:4},(_,i)=>({record:labels[i]}))));
const sources=[contractPath,...Object.values(paths),'research/nima/generative-phase-assembly.mjs',
 'research/strominger/aligned-native-growth-model.mjs','research/strominger/aligned-pair-channel-model.mjs',
 'research/strominger/retained-context-braid-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs',
 'research/strominger/checkers/check_su32_operation_support_admission.mjs'];
const sourceHashes={};for(const p of sources)sourceHashes[p]=hash(await fs.readFile(p));
assert.equal(sourceHashes[contractPath],hash(contractBytes));
const report={schema:'su32.operation-support-admission-audit.v1',passed:true,contractPath,contractHash:hash(contractBytes),
 nativeSource:{operation,sourcePacket:source,targetPacket:target,sourceChart,targetChart,movedSlots:moved,movedMarks:moved.map(i=>marks[i]),
  primitiveSourceVertices:rules.geometry.cells[sourceChart.cell].vertices,primitiveTargetVertices:rules.geometry.cells[targetChart.cell].vertices},
 positiveControl:{carrier:'original eight-reference bank, not Su32',moves:control.records.filter(r=>r.operation).map(r=>[r.stage,r.operation.kind]),
 certifiedExit:control.assembly.certifiedExit,transportNormalizedRecovery:true},
 relaxedTrials:injections.length,supportClosed,supportUnclosed:injections.length-supportClosed,
 perInjectionOrbitCountsEqual:trials.every(t=>t.orbitFaceRoleMatches[0]===t.orbitFaceRoleMatches[1]),
 orbitCountProfiles:[...new Set(trials.map(t=>JSON.stringify(t.orbitFaceRoleMatches)))].map(JSON.parse),
 pairCounts,candidateCounts,orbitTotals,trials,negativeControls,
 bindingGaps:{sourceRecordToMarkedCoordinate:null,complementaryNativeState:null,primitiveOccurrenceAtSelectedWholeN:null,actualFaceRealization:null},
 verdict:{nativeAdmission:'Not formulated for all sixteen Su32 candidates. No supplied coordinate/occurrence/face binding, so no candidate is certified or rejected as a native NE execution.',
 supportAlone:'Every support-closed label injection matches one selected pair in every candidate. Pair membership alone cannot select a placement.',
 faceRoleScreen:'Actual outgoing E faces are checked in the fixed plans. Their availability is only a necessary role/incidence condition, not a marked-primitive transfer witness.',
 noSelection:'No source-authorized injection or complementary state is chosen from these diagnostic alternatives.'},
 limits:['The 120 injections are a label-only diagnostic class, not all possible encoders and not admitted native maps.',
 'The same injection is used across all sixteen candidates in each trial; none is fitted to a desired orbit.',
 'Four cell-attached directional records are not automatically marked geometric vertices or native coefficient coordinates.',
 'The native N carrier in this operation is a tetrahedral primitive; a selected Su32 N is a whole octahedron. A subdivision/occurrence binding is required.',
 'No fifth coefficient, schedule, output law, geometric adapter, or new local growth step was added.'],sourceHashes};
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,trials:undefined,sourceHashes:undefined},null,2));
