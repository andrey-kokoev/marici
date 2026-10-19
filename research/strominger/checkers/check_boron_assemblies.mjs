import assert from 'node:assert/strict';
import {mkdir,writeFile} from 'node:fs/promises';
import {searchBoronAssemblies,assemblyDomain} from '../demos/particle-overlap-tetrahedron/lithium6-assembly-model.mjs';
import {selectPhaseAssembly,compilePhaseAssembly,auditPhaseAssembly,createPhaseAssembly} from '../demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
const domain=assemblyDomain(),be9=selectPhaseAssembly('beryllium9'),b10=selectPhaseAssembly('boron10'),b11=selectPhaseAssembly('boron11');
const blocked=searchBoronAssemblies({neutronCount:5,retained:be9.candidate});assert.equal(blocked.candidates.length,0);
assert.equal(b10.retainedAssembly,undefined);
const chartKey=c=>JSON.stringify([c.cell,c.species,c.aliases]);
for(const c of b10.charts)assert.ok(b11.charts.some(d=>chartKey(c)===chartKey(d)));
for(const e of b10.edges)assert.ok(b11.edges.some(f=>chartKey(b10.charts[e.from])===chartKey(b11.charts[f.from])&&chartKey(b10.charts[e.to])===chartKey(b11.charts[f.to])&&e.kind===f.kind&&e.phaseDelta===f.phaseDelta&&JSON.stringify(e.permutation)===JSON.stringify(f.permutation)));
assert.equal(b11.retainedAssembly.isotope,'boron10');assert.deepEqual(b11.retainedAssembly.addedProtons,[]);assert.deepEqual(b11.retainedAssembly.addedNeutrons,[252]);assert.deepEqual(b11.retainedAssembly.addedElectrons,[]);
const rows=[];
for(const [isotope,neutronCount,selected,retained] of [['boron10',5,b10,null],['boron11',6,b11,b10.candidate]]){
 const search=searchBoronAssemblies({neutronCount,retained});let tested=0;const accepted=[],rejections={};
 for(const [candidateIndex,candidate] of search.candidates.entries()){
  assert.equal(candidate.nucleus.filter(i=>domain.species[i]==='proton').length,5);assert.equal(candidate.nucleus.filter(i=>domain.species[i]==='neutron').length,neutronCount);assert.equal(candidate.electrons.length,5);
  for(let orientations=0;orientations<2**candidate.interfaces.filter(e=>e.kind==='PN').length;orientations++){
   tested++;const r=compilePhaseAssembly(candidate,orientations);
   if(r.status!=='phase-coherent-reference'){rejections[r.reason]=(rejections[r.reason]??0)+1;continue;}
   const audit=auditPhaseAssembly(r);assert.equal(audit.coverage.coveredCells,10+neutronCount);
   accepted.push({candidateIndex,orientations,retainsPreviousReaders:retained?b10.charts.every(c=>r.charts.some(d=>chartKey(c)===chartKey(d))):null});
  }
 }
 assert.equal(tested,accepted.length+Object.values(rejections).reduce((a,b)=>a+b,0));
 assert.ok(accepted.some(a=>a.orientations===selected.orientations&&(!retained||a.retainsPreviousReaders)&&JSON.stringify(search.candidates[a.candidateIndex])===JSON.stringify(selected.candidate)));
 const s=createPhaseAssembly(isotope).snapshot();assert.deepEqual(s.counts,{proton:5,neutron:neutronCount,electron:5});assert.equal(new Set(s.items.map(i=>i.key)).size,10+neutronCount);
 rows.push({isotope,counts:s.counts,search:{prefixStartSize:search.prefixStartSize,prefixCounts:search.prefixCounts,typedNuclei:search.typedNuclei,geometryCandidates:search.candidates.length,readerAssignmentsTested:tested,complete:true,accepted,rejections,retainedPreviousRequired:!!retained},candidate:selected.candidate,orientations:selected.orientations,retainedAssembly:selected.retainedAssembly??null,phaseStateCount:auditPhaseAssembly(selected).phaseStateCount,coverage:'covered'});
}
const oldKeys=new Map(createPhaseAssembly('boron10').snapshot().items.map(i=>[i.key,i.species])),newItems=createPhaseAssembly('boron11').snapshot().items;for(const [key,species] of oldKeys)assert.equal(newItems.find(i=>i.key===key)?.species,species);
assert.throws(()=>searchBoronAssemblies({neutronCount:4}),/Supported boron/);
await mkdir('research/strominger/results/boron-assembly',{recursive:true});
await writeFile('research/strominger/results/boron-assembly/verification.json',JSON.stringify({status:'pass-phase-coherent-reference',retainedBe9ToB10:{status:'no-candidate-in-bounded-domain',prefixStartSize:blocked.prefixStartSize,prefixCounts:blocked.prefixCounts,typedNuclei:blocked.typedNuclei,geometryCandidates:0},rows,boron11PreservesBoron10ReadersAndTransport:true,scope:'Stable isotope targets. B-10 is a separate whole-assembly reference, not an extension of the selected Be-9. B-11 retains selected B-10 plus one neutron. Existing phase/interface laws only; no physical stability, binding energy, or rearrangement mechanism derived.'},null,2)+'\n');
console.log('PASS B-10 / B-11: 5P/5N/5e and 5P/6N/5e; 15/16 carriers covered; retained Be-9 extension blocked, B-11 retains B-10.');
