// Audit a fixed complete candidate against all source-enumerated cones.
// No new local operations, filling maps, or requirement to activate every path.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildFiveSideOctComparisonDomain} from '../../realization-tower/five-side-oct-comparison-domain.mjs';
const paths={wiring:'research/strominger/results/su32-global-reference-wiring-v1/verification.json',
 symmetry:'research/strominger/results/su32-global-wiring-symmetry-v1/verification.json',
 trace:'research/strominger/results/su32-fixed-reading-trace-v1/verification.json',
 fixture:'research/strominger/results/su32-hopf-tests-v1/fixture.json'};
const hash=x=>createHash('sha256').update(x).digest('hex'),docs={};
for(const [name,path] of Object.entries(paths)){
 docs[name]=JSON.parse(await fs.readFile(path,'utf8'));
 for(const [p,h] of Object.entries(docs[name].sourceHashes))assert.equal(hash(await fs.readFile(p)),h,`Stale input: ${p}`);
}
const {wiring,symmetry,trace,fixture}=docs,copy=x=>structuredClone(x),base=wiring.witness.plan;
// Independently enumerate the WHOLE comparison domain before restricting plans.
const domain=buildFiveSideOctComparisonDomain(buildPESymmetricSector(1),{readingIds:[trace.reading]}).readings[0];
const cones=domain.overlaps.filter(o=>o.residualCycleRank);assert.equal(cones.length,6);
const layer=new Map(base.nodes.map(n=>[n.cell,n.layer]));
assert.deepEqual(cones.map(c=>layer.get(c.source)).sort((a,b)=>a-b),[1,3,3,3,3,5]);
const between=(a,b)=>fixture.interfaces.filter(f=>f.ports.some(p=>p.split('@')[0]===a)&&f.ports.some(p=>p.split('@')[0]===b));
const plans=trace.middleAssignments.map(cover=>{
 const plan=copy(base);plan.cover=cover.index;const nodes=new Map(plan.nodes.map(n=>[n.cell,n]));
 plan.channels=cover.routes.map(r=>({channel:r.channel,members:copy(r.members)}));plan.bridges=[];
 for(const r of cover.routes)for(const [source,target] of [[r.sourceP,r.targetE],[r.sourceE,r.targetP]]){
  const members=r.members.filter(m=>between(source,m).length&&between(m,target).length);assert.equal(members.length,1);
  plan.bridges.push({channel:r.channel,source,middle:members[0],target,kind:'peripheral',records:copy(nodes.get(source).records)});
 }
 plan.bridges.push(...copy(base.bridges.filter(b=>b.kind==='central-comparison-context')));
 for(const n of plan.nodes)if(n.layer===5)n.records=[...new Set(plan.bridges.filter(b=>b.middle===n.cell).flatMap(b=>b.records))].sort();
 plan.edges=copy(base.edges.filter(e=>nodes.get(e.from).layer!==4&&nodes.get(e.from).layer!==5));
 for(const b of plan.bridges)for(const [from,to] of [[b.source,b.middle],[b.middle,b.target]]){
  const fs=between(from,to);assert.equal(fs.length,1);const face=fs[0];
  plan.edges.push({face:face.id,from,to,fromPort:from+'@'+face.id,toPort:to+'@'+face.id,records:copy(b.records)});
 }
 return plan;
});
assert.deepEqual(plans.find(p=>p.cover===base.cover),base);
let overlapRecordChecks=0,allPresentationCovers=0;const results=[];
for(const plan of plans){
 const nodes=new Map(plan.nodes.map(n=>[n.cell,n])),selected=new Map(plan.edges.map(e=>[e.face,e]));
 const states=new Map();
 for(const node of [...plan.nodes].sort((a,b)=>a.layer-b.layer)){
  const state=node.cell===plan.entry?copy(trace.registry):{};
  for(const edge of plan.edges.filter(e=>e.to===node.cell))for(const label of edge.records){
   const value=states.get(edge.from)[label];assert.notEqual(value,undefined);
   if(Object.hasOwn(state,label))assert.deepEqual(state[label],value,'Conflicting repeated record');else state[label]=copy(value);
  }
  assert.deepEqual(Object.keys(state).sort(),node.records);states.set(node.cell,state);
 }
 assert.deepEqual(states.get(plan.exit),trace.registry);
 const restrictions=cones.map(cone=>{
  const ids=new Set(cone.paths.flatMap(p=>p.cells)),faces=[...new Set(cone.paths.flatMap(p=>p.arrows))];
  assert.equal(cone.paths.length,16);assert.equal(ids.size,14);
  const internal=plan.edges.filter(e=>faces.includes(e.face));
  const imports=plan.edges.filter(e=>ids.has(e.to)&&!ids.has(e.from));
  const exports=plan.edges.filter(e=>ids.has(e.from)&&!ids.has(e.to));
  const unavailable=faces.filter(f=>!selected.has(f));
  const pathsSelected=cone.paths.filter(p=>p.arrows.every(id=>selected.has(id)));
  // Test an explicitly stronger rival: treat each cone as a CLOSED copy of
  // the entry constructor, seeded only by its source packet. No external
  // incoming context is admitted in this diagnostic, unlike the full plan.
  const available=new Map([...ids].map(id=>[id,new Set()]));
  nodes.get(cone.source).records.forEach(k=>available.get(cone.source).add(k));
  const deficits=[];
  for(const id of [...ids].sort((a,b)=>layer.get(a)-layer.get(b))){
   const missing=nodes.get(id).records.filter(k=>!available.get(id).has(k));
   if(missing.length)deficits.push({at:id,missing});
   for(const e of internal.filter(e=>e.from===id))for(const k of e.records)if(available.get(id).has(k))available.get(e.to).add(k);
  }
  const unbound=domain.comparisons.filter(c=>cone.moves.some(m=>m.comparison===c.id));
  assert(unbound.every(c=>c.comparisonMap===null&&c.fillingWitness===null));
  return {id:cone.id,source:cone.source,target:cone.target,startLayer:layer.get(cone.source),
   cellStates:[...ids].sort().map(id=>({cell:id,records:copy(nodes.get(id).records),values:copy(states.get(id))})),
   nativePresentations:cone.paths.length,selectedPresentations:pathsSelected.length,
   nativeFaces:faces.length,selectedFaces:faces.length-unavailable.length,unselectedFaces:unavailable,
   contextImports:imports,contextExports:exports,
   closedCopyDiagnostic:{sourceRecords:copy(nodes.get(cone.source).records),deficits,
    targetRecordsReachable:[...available.get(cone.target)].sort(),
    disposition:deficits.length?'Not a closed source-only copy; retained context is needed.':'No source-only record deficit in this plan.'},
   comparisonObligations:unbound.map(c=>({id:c.id,status:c.status,comparisonMap:c.comparisonMap,fillingWitness:c.fillingWitness})),
   nativeCompositionCompatibility:'not-formulated: operation maps and required filling law unbound'};
 });
 const overlaps=[];
 for(let i=0;i<restrictions.length;i++)for(let j=i+1;j<restrictions.length;j++){
  const a=restrictions[i],b=restrictions[j];
  const common=a.cellStates.filter(n=>b.cellStates.some(m=>m.cell===n.cell));
  for(const n of common){assert.deepEqual(n,b.cellStates.find(m=>m.cell===n.cell));overlapRecordChecks++;}
  overlaps.push({left:a.id,right:b.id,sharedCells:common.map(n=>n.cell),recordRestrictionAgrees:true,
   compositionComparison:null});
 }
 if(restrictions.every(r=>r.selectedPresentations===r.nativePresentations))allPresentationCovers++;
 results.push({cover:plan.cover,restrictions,overlaps});
}
// The two orbit families each contain two pair placements in every cover.
// Their underlying relay plans, states and cone restrictions are identical
// within a cover. Any filter using ONLY those data cannot separate the orbits.
const coarse=symmetry.classifications.find(c=>c.name==='unoriented-boundary-PE-dual-shapes');assert.equal(coarse.orbits.length,2);
const indistinguishableByPlan=plans.map(plan=>({cover:plan.cover,
 orbitCandidateIds:coarse.orbits.map(o=>o.members.filter(id=>wiring.localizedSurvivors[id].cover===plan.cover))}));
for(const r of indistinguishableByPlan)assert.deepEqual(r.orbitCandidateIds.map(ids=>ids.length),[2,2]);
// Retain the genuinely different selected-pair data as well. These are not
// erased merely because the existing relay does not consult them.
const selectedPairRestrictions=wiring.localizedSurvivors.map((candidate,id)=>({candidate:id,cover:candidate.cover,
 cones:results.find(r=>r.cover===candidate.cover).restrictions.map(cone=>({cone:cone.id,
  placements:copy(candidate.placements.filter(p=>cone.cellStates.some(n=>n.cell===p.at))),
  operationOnSelectedPairs:null}))}));
const sources=[...Object.values(paths),'research/strominger/pe-symmetric-sector.mjs',
 'research/realization-tower/five-side-oct-comparison-domain.mjs',
 'research/strominger/checkers/check_su32_six_cone_compatibility.mjs'];
const sourceHashes={};for(const p of sources)sourceHashes[p]=hash(await fs.readFile(p));
const report={schema:'su32.six-cone-compatibility-audit.v1',passed:true,reading:trace.reading,
 coneCount:cones.length,completePlans:plans.length,overlapRecordChecks,allPresentationCovers,results,indistinguishableByPlan,selectedPairRestrictions,
 verdict:{recordRestrictions:'Agree on all intersections. This follows from restriction of the one global assignment; it is not an independent Segal/filling theorem.',
  geometricPresentationCoverage:'Reported separately; no assumption that every potential path must be an active wire is imposed.',
  nativeComposition:'Not formulated: the independently sourced comparison maps and filling witnesses are null. Native compatibility cannot be marked passed.',
  orbitSelection:'The tested plan/record/context data cannot distinguish the two placement orbits. Both have the same two candidates per cover.',
  closedConeRival:'Source-only propagation is tested separately; any deficit is a refusal of that extra autonomy assumption, not of the contextual global plan.'},
 nextMissingContract:'A comparison task that actually consumes the selected pair placement, with typed contextual inputs and an independently specified compatibility/filling condition across the middle cones.',
 nativeCoherence:null,sourceHashes};
const dir='research/strominger/results/su32-six-cone-compatibility-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,sourceHashes:undefined,selectedPairRestrictions:undefined,results:results.map(r=>({cover:r.cover,
 restrictions:r.restrictions.map(c=>({startLayer:c.startLayer,selectedPresentations:c.selectedPresentations,nativePresentations:c.nativePresentations,
 selectedFaces:c.selectedFaces,nativeFaces:c.nativeFaces,importEdges:c.contextImports.length,deficientSites:c.closedCopyDiagnostic.deficits.length,
 comparisonObligations:c.comparisonObligations.length})),overlaps:r.overlaps.length}))},null,2));
