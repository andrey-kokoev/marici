import assert from 'node:assert/strict';
import {mkdir,writeFile} from 'node:fs/promises';
import {assemblyDomain,searchLithiumAssemblies} from '../demos/particle-overlap-tetrahedron/lithium6-assembly-model.mjs';
import {selectPhaseAssembly,compilePhaseAssembly,auditPhaseAssembly} from '../demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
const search=searchLithiumAssemblies({allowNN:true,neutronCount:4}),old=selectPhaseAssembly('lithium6'),selected=selectPhaseAssembly('lithium7');
const retained=search.candidates.filter(c=>old.candidate.nucleus.every(i=>c.nucleus.includes(i))&&old.candidate.electrons.every(i=>c.electrons.includes(i))&&Object.entries(old.candidate.types).every(([v,t])=>c.types[v]===t));
assert.equal(retained.length,1);
let tested=0;const admitted=[],rejections={};
for(const c of retained)for(let orientation=0;orientation<2**c.interfaces.filter(e=>e.kind==='PN').length;orientation++){
 tested++;const r=compilePhaseAssembly(c,orientation);
 if(r.status==='phase-coherent-reference'){auditPhaseAssembly(r);admitted.push(orientation);}else rejections[r.reason]=(rejections[r.reason]??0)+1;
}
assert.deepEqual(admitted,[41]);assert.equal(selected.orientations,41);assert.deepEqual(selected.candidate,retained[0]);
const added=selected.candidate.nucleus.filter(i=>!old.candidate.nucleus.includes(i));assert.deepEqual(added,[7]);assert.equal(assemblyDomain().species[added[0]],'neutron');
const attachments=selected.candidate.interfaces.filter(e=>e.from===7||e.to===7);assert.equal(attachments.length,1);assert.equal(attachments[0].kind,'PN');assert.equal(attachments[0].from,0);
const audit=auditPhaseAssembly(selected);assert.equal(audit.coverage.coveredCells,10);
await mkdir('research/strominger/results/lithium7-assembly',{recursive:true});
await writeFile('research/strominger/results/lithium7-assembly/verification.json',JSON.stringify({status:'pass-phase-coherent-reference',counts:{proton:3,neutron:4,electron:3},search:{primitiveCells:search.primitiveCells,prefixCounts:search.prefixCounts,typedNuclei:search.typedNuclei,geometryCandidates:search.candidates.length,retainedLithium6Candidates:retained.length,readerAssignmentsTested:tested,admittedOrientations:admitted,rejections},candidate:selected.candidate,retainedAssembly:selected.retainedAssembly,attachments,phaseStateCount:audit.phaseStateCount,coverage:audit.coverage.status,scope:'Bounded reference construction preserving the selected Li-6 geometry, roles and readers. No new interface law; existing NN reference assumption retained. Not uniqueness among all Li-7 assemblies, a physical capture process, or a binding/stability derivation.'},null,2)+'\n');
console.log('PASS Li-7: retained Li-6 geometry and roles; one added neutron at cell 7 through PN; 10/10 carriers have phase-bearing entry/exit witnesses.');
