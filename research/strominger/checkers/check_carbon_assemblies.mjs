import assert from 'node:assert/strict';
import {mkdir,writeFile} from 'node:fs/promises';
import {searchCarbonAssemblies,assemblyDomain} from '../demos/particle-overlap-tetrahedron/lithium6-assembly-model.mjs';
import {selectPhaseAssembly,compilePhaseAssembly,auditPhaseAssembly,createPhaseAssembly} from '../demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
const domain=assemblyDomain(),old=selectPhaseAssembly('boron11'),c12=selectPhaseAssembly('carbon12'),c13=selectPhaseAssembly('carbon13');
const chartKey=c=>JSON.stringify([c.cell,c.species,c.aliases]);
const preservesReaders=r=>old.charts.every(c=>r.charts.some(d=>chartKey(c)===chartKey(d)));
const blocked=searchCarbonAssemblies({neutronCount:7,retained:c12.candidate});assert.equal(blocked.candidates.length,0);
// Each proton has exactly two MCM faces, both occupied in selected C-12.
// A further neutron cannot get the native P reader required by this ansatz.
const protonPorts=c12.candidate.nucleus.filter(i=>domain.species[i]==='proton').map(cell=>({cell,occupied:c12.candidate.interfaces.filter(e=>e.kind==='PN'&&(e.from===cell||e.to===cell)).length}));
assert.equal(protonPorts.length,6);assert.ok(protonPorts.every(p=>p.occupied===2));
const oldItems=createPhaseAssembly('boron11').snapshot().items,rows=[];
for(const [isotope,neutronCount,selected,expected] of [['carbon12',6,c12,{p:[47],n:[],e:[251]}],['carbon13',7,c13,{p:[112],n:[253],e:[254]}]]){
 const search=searchCarbonAssemblies({neutronCount,retained:old.candidate});let tested=0;const accepted=[],rejections={};
 for(const [candidateIndex,candidate] of search.candidates.entries()){
  assert.equal(candidate.nucleus.filter(i=>domain.species[i]==='proton').length,6);assert.equal(candidate.nucleus.filter(i=>domain.species[i]==='neutron').length,neutronCount);assert.equal(candidate.electrons.length,6);
  for(let orientations=0;orientations<2**candidate.interfaces.filter(e=>e.kind==='PN').length;orientations++){
   tested++;const r=compilePhaseAssembly(candidate,orientations);
   if(r.status!=='phase-coherent-reference'){rejections[r.reason]=(rejections[r.reason]??0)+1;continue;}
   assert.equal(auditPhaseAssembly(r).coverage.coveredCells,12+neutronCount);
   accepted.push({candidateIndex,orientations,retainsBoron11Readers:preservesReaders(r)});
  }
 }
 assert.equal(tested,accepted.length+Object.values(rejections).reduce((a,b)=>a+b,0));
 assert.ok(accepted.some(a=>a.orientations===selected.orientations&&a.retainsBoron11Readers&&JSON.stringify(search.candidates[a.candidateIndex])===JSON.stringify(selected.candidate)));
 assert.equal(selected.retainedAssembly.isotope,'boron11');assert.deepEqual(selected.retainedAssembly.addedProtons,expected.p);assert.deepEqual(selected.retainedAssembly.addedNeutrons,expected.n);assert.deepEqual(selected.retainedAssembly.addedElectrons,expected.e);
 for(const e of old.edges)assert.ok(selected.edges.some(f=>chartKey(old.charts[e.from])===chartKey(selected.charts[f.from])&&chartKey(old.charts[e.to])===chartKey(selected.charts[f.to])&&e.kind===f.kind&&e.phaseDelta===f.phaseDelta&&JSON.stringify(e.permutation)===JSON.stringify(f.permutation)));
 const state=createPhaseAssembly(isotope).snapshot();assert.deepEqual(state.counts,{proton:6,neutron:neutronCount,electron:6});assert.equal(new Set(state.items.map(i=>i.key)).size,12+neutronCount);
 for(const item of oldItems)assert.equal(state.items.find(i=>i.key===item.key)?.species,item.species);
 for(const [v,t] of Object.entries(old.candidate.types))assert.equal(selected.candidate.types[v],t);
 rows.push({isotope,counts:state.counts,search:{prefixStartSize:search.prefixStartSize,prefixCounts:search.prefixCounts,typedNuclei:search.typedNuclei,geometryCandidates:search.candidates.length,readerAssignmentsTested:tested,complete:true,accepted,rejections,retainedPrevious:'boron11'},candidate:selected.candidate,orientations:selected.orientations,retainedAssembly:selected.retainedAssembly,phaseStateCount:auditPhaseAssembly(selected).phaseStateCount,coverage:'covered'});
}
assert.ok(!c12.candidate.nucleus.every(i=>c13.candidate.nucleus.includes(i)));assert.throws(()=>searchCarbonAssemblies({neutronCount:8}),/Supported carbon/);
await mkdir('research/strominger/results/carbon-assembly',{recursive:true});
await writeFile('research/strominger/results/carbon-assembly/verification.json',JSON.stringify({status:'pass-phase-coherent-reference',retainedC12ToC13:{status:'no-candidate-in-bounded-domain',prefixStartSize:blocked.prefixStartSize,prefixCounts:blocked.prefixCounts,typedNuclei:blocked.typedNuclei,geometryCandidates:0,protonPorts,obstruction:'All six protons have both MCM ports occupied; an additional neutron cannot obtain the required native proton reader without changing retained carriers.'},rows,boron11CellsRolesReadersAndTransportPreserved:true,scope:'Stable targets, separate extensions of selected B-11. C-13 does not retain selected C-12. Existing phase/interface rules; finite domain and explicit retained-core restrictions, not global uniqueness or physical stability/reaction derivations.'},null,2)+'\n');
console.log('PASS C-12 / C-13: 6P/6N/6e and 6P/7N/6e; both retain B-11; C-12-to-C-13 addition blocked; 18/19 carriers covered.');
