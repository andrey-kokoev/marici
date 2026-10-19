import assert from 'node:assert/strict';
import {mkdir,readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {searchNitrogenAssemblies,searchLithiumAssemblies} from '../demos/particle-overlap-tetrahedron/lithium6-assembly-model.mjs';
import {selectPhaseAssembly,compilePhaseAssembly,auditPhaseAssembly,createPhaseAssembly} from '../demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
const digest=x=>createHash('sha256').update(x).digest('hex'),pruningControls=[];
// Early role rejection is monotone: every full coloring restricts to a valid
// coloring on every connected prefix. Check exact output equality on smaller
// complete searches, not just agreement of their counts.
for(const neutronCount of [2,3,4,5]){
 const plain=searchLithiumAssemblies({allowNN:true,neutronCount,pruneRoles:false}),pruned=searchLithiumAssemblies({allowNN:true,neutronCount,pruneRoles:true});
 assert.deepEqual(pruned.candidates,plain.candidates);pruningControls.push({neutronCount,candidates:plain.candidates.length,identical:true});
}
const negative=searchNitrogenAssemblies({neutronCount:7});assert.equal(negative.candidates.length,0);assert.equal(negative.typedNuclei,2384);
assert.deepEqual(negative.electronPoolHistogram,{'7':1920,'8':464});assert.equal(negative.electronAdjacencyRejections,5632);
assert.throws(()=>selectPhaseAssembly('nitrogen14'),/No N-14 reference admitted/);
const old=selectPhaseAssembly('carbon13'),reference=selectPhaseAssembly('nitrogen15'),search=searchNitrogenAssemblies({neutronCount:8,retained:old.candidate});
assert.deepEqual(search.candidates,searchNitrogenAssemblies({neutronCount:8,retained:old.candidate,pruneRoles:false}).candidates);
assert.equal(search.candidates.length,4);
const chartKey=c=>JSON.stringify([c.cell,c.species,c.aliases]);let tested=0;const accepted=[],rejections={};
for(const [candidateIndex,candidate] of search.candidates.entries())for(let orientations=0;orientations<2**candidate.interfaces.filter(e=>e.kind==='PN').length;orientations++){
 tested++;const r=compilePhaseAssembly(candidate,orientations);
 if(r.status!=='phase-coherent-reference'){rejections[r.reason]=(rejections[r.reason]??0)+1;continue;}
 assert.equal(auditPhaseAssembly(r).coverage.coveredCells,22);
 accepted.push({candidateIndex,orientations,retainsCarbon13Readers:old.charts.every(c=>r.charts.some(d=>chartKey(c)===chartKey(d)))});
}
assert.equal(tested,accepted.length+Object.values(rejections).reduce((a,b)=>a+b,0));
const first=accepted.find(a=>a.retainsCarbon13Readers);assert.ok(first);assert.deepEqual(reference.candidate,search.candidates[first.candidateIndex]);assert.equal(reference.orientations,first.orientations);
for(const e of old.edges)assert.ok(reference.edges.some(f=>chartKey(old.charts[e.from])===chartKey(reference.charts[f.from])&&chartKey(old.charts[e.to])===chartKey(reference.charts[f.to])&&e.kind===f.kind&&e.phaseDelta===f.phaseDelta&&JSON.stringify(e.permutation)===JSON.stringify(f.permutation)));
const state=createPhaseAssembly('nitrogen15').snapshot();assert.deepEqual(state.counts,{proton:7,neutron:8,electron:7});assert.equal(new Set(state.items.map(i=>i.key)).size,22);
for(const item of createPhaseAssembly('carbon13').snapshot().items)assert.equal(state.items.find(i=>i.key===item.key)?.species,item.species);
assert.deepEqual(reference.retainedAssembly.addedProtons,[47]);assert.deepEqual(reference.retainedAssembly.addedNeutrons,[295]);assert.deepEqual(reference.retainedAssembly.addedElectrons,[296]);
assert.throws(()=>searchNitrogenAssemblies({neutronCount:9}),/Supported nitrogen/);
const summary=s=>({prefixCounts:s.prefixCounts,prefixStartSize:s.prefixStartSize,earlyRolePruning:s.earlyRolePruning,typedNuclei:s.typedNuclei,electronPoolHistogram:s.electronPoolHistogram,electronAdjacencyRejections:s.electronAdjacencyRejections,geometryCandidates:s.candidates.length});
const sourceHashes={};for(const file of ['lithium6-assembly-model.mjs','phase-assembly-model.mjs','nitrogen15-reference.mjs'])sourceHashes[file]=digest(await readFile(new URL('../demos/particle-overlap-tetrahedron/'+file,import.meta.url)));
await mkdir('research/strominger/results/nitrogen-assembly',{recursive:true});
await writeFile('research/strominger/results/nitrogen-assembly/verification.json',JSON.stringify({status:'bounded-N14-negative-and-N15-reference-verified',sourceHashes,pruningControls,nitrogen14:{status:'no-candidate-in-bounded-domain',geometrySearchComplete:true,search:summary(negative),scope:negative.scope,physicallyStable:true,physicalImpossibilityProved:false},nitrogen15:{status:'phase-coherent-reference',counts:state.counts,search:{...summary(search),readerAssignmentsTested:tested,phaseSearchCompleteWithinRetainedScope:true,accepted,rejections},candidate:reference.candidate,orientations:reference.orientations,retainedAssembly:reference.retainedAssembly,phaseStateCount:auditPhaseAssembly(reference).phaseStateCount,coverage:'covered',oldReadersAndTransportPreserved:true},scope:'Same finite 343-cell, split-electron, native-P-reader isotope ansatz. N-14 failure is a limitation of that ansatz, not physical instability. N-15 retains C-13. No contact, phase, or stability rule was relaxed.'},null,2)+'\n');
console.log('PASS nitrogen audit: N-14 has zero complete candidates in this ansatz; N-15 retains C-13 with 22/22 carriers covered.');
