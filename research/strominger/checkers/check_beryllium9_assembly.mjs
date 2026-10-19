import assert from 'node:assert/strict';
import {mkdir,writeFile} from 'node:fs/promises';
import {searchBeryllium9Assemblies,assemblyDomain} from '../demos/particle-overlap-tetrahedron/lithium6-assembly-model.mjs';
import {selectPhaseAssembly,compilePhaseAssembly,auditPhaseAssembly,createPhaseAssembly} from '../demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
const search=searchBeryllium9Assemblies(),old=selectPhaseAssembly('lithium7'),selected=selectPhaseAssembly('beryllium9'),domain=assemblyDomain();
const retained=search.candidates.filter(c=>old.candidate.nucleus.every(i=>c.nucleus.includes(i))&&old.candidate.electrons.every(i=>c.electrons.includes(i))&&Object.entries(old.candidate.types).every(([v,t])=>c.types[v]===t));
const chartKey=c=>JSON.stringify([c.cell,c.species,c.aliases]);
const preservesReaders=r=>old.charts.every(c=>r.charts.some(d=>chartKey(c)===chartKey(d)));
let tested=0,phaseCompatible=0;const admitted=[],rejections={};
for(const candidate of retained)for(let orientations=0;orientations<2**candidate.interfaces.filter(e=>e.kind==='PN').length;orientations++){
 tested++;const r=compilePhaseAssembly(candidate,orientations);
 if(r.status!=='phase-coherent-reference'){rejections[r.reason]=(rejections[r.reason]??0)+1;continue;}
 phaseCompatible++;auditPhaseAssembly(r);if(preservesReaders(r))admitted.push({candidate,orientations});
}
assert.equal(retained.length,12);assert.equal(tested,1536);assert.equal(admitted.length,1);assert.deepEqual(selected.candidate,admitted[0].candidate);assert.equal(selected.orientations,81);
assert.equal(selected.retainedAssembly.isotope,'lithium7');assert.deepEqual(selected.retainedAssembly.addedProtons,[44]);assert.deepEqual(selected.retainedAssembly.addedNeutrons,[6]);assert.deepEqual(selected.retainedAssembly.addedElectrons,[5]);
assert.equal(domain.species[44],'proton');assert.equal(domain.species[6],'neutron');
for(const e of old.edges)assert.ok(selected.edges.some(f=>chartKey(old.charts[e.from])===chartKey(selected.charts[f.from])&&chartKey(old.charts[e.to])===chartKey(selected.charts[f.to])&&e.kind===f.kind&&e.phaseDelta===f.phaseDelta&&JSON.stringify(e.permutation)===JSON.stringify(f.permutation)));
const audit=auditPhaseAssembly(selected),state=createPhaseAssembly('beryllium9').snapshot();assert.deepEqual(state.counts,{proton:4,neutron:5,electron:4});assert.equal(audit.coverage.coveredCells,13);
const retainedKeys=new Map(createPhaseAssembly('lithium7').snapshot().items.map(i=>[i.key,i.species]));for(const [key,species] of retainedKeys)assert.equal(state.items.find(i=>i.key===key)?.species,species);
assert.equal(new Set(state.items.map(i=>i.key)).size,13);
const newInterfaces=selected.candidate.interfaces.filter(e=>[44,6,5].includes(e.from)||[44,6,5].includes(e.to));assert.deepEqual(newInterfaces.map(e=>e.kind).sort(),['NE','NN','PN']);
await mkdir('research/strominger/results/beryllium9-assembly',{recursive:true});
await writeFile('research/strominger/results/beryllium9-assembly/verification.json',JSON.stringify({status:'pass-phase-coherent-reference',counts:state.counts,search:{primitiveCells:search.primitiveCells,prefixCounts:search.prefixCounts,typedNuclei:search.typedNuclei,geometryCandidates:search.candidates.length,retainedLithium7Candidates:retained.length,readerAssignmentsTested:tested,phaseCompatible,readerPreservingAssignments:admitted.length,rejections},candidate:selected.candidate,orientations:selected.orientations,retainedAssembly:selected.retainedAssembly,newInterfaces,phaseStateCount:audit.phaseStateCount,coverage:audit.coverage.status,existingReadersAndTransportPreserved:true,scope:'Stable-isotope target; bounded reference construction using existing PN/NE and NN phase rules. Retains selected Li-7 geometry, roles and readers, not necessarily its display-history ordering. No physical binding, stability or growth process derived.'},null,2)+'\n');
console.log('PASS Be-9: 4P/5N/4e; retained Li-7 geometry, roles, readers and transport; one P/N/e addition; 13/13 carriers covered.');
