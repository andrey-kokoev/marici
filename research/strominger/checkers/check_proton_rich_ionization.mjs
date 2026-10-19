// Bounded charge-state probes with the repaired all-contact admission gate.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {searchCounts} from './proton-rich-probe-model.mjs';
import {compilePhaseAssembly,auditPhaseAssembly,auditAssemblyContacts} from '../demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
const hash=b=>createHash('sha256').update(b).digest('hex');
const files=['./check_proton_rich_ionization.mjs','./proton-rich-probe-model.mjs','./n14-probe-model.mjs',...['phase-assembly-model.mjs','lithium6-assembly-model.mjs','phase-advance-model.mjs','phase-discipline-model.mjs','window-construction-model.mjs','deuterium-tunnel-model.mjs','fiber-coverage-model.mjs','simplex-model.mjs','simplex-components.mjs','lattice-items.mjs'].map(f=>'../demos/particle-overlap-tetrahedron/'+f)],sourceHashes={};
for(const f of files)sourceHashes[f]=hash(await readFile(new URL(f,import.meta.url)));
const cap=250000,rows=[];
for(const p of [7,8])for(const e of [5,4]){
 const geometry=searchCounts(p,6,e),total=geometry.candidates.reduce((s,c)=>s+2**c.interfaces.filter(x=>x.kind==='PN').length,0);
 const rejections={};let tested=0,witness=null,stop=null;
 outer:for(const [candidateIndex,c] of geometry.candidates.entries())for(let orientation=0;orientation<2**c.interfaces.filter(x=>x.kind==='PN').length;orientation++){
  if(tested>=cap){stop='reader-assignment-resource-cap';break outer;}tested++;
  const r=compilePhaseAssembly(c,orientation);if(r.status!=='phase-coherent-reference'){rejections[r.reason]=(rejections[r.reason]??0)+1;continue;}
  const audit=auditPhaseAssembly(r);assert.equal(audit.contacts.status,'all-physical-contacts-witnessed');assert.equal(audit.coverage.coveredCells,p+6+e);assert.equal(auditAssemblyContacts(r).missing.length,0);
  witness={candidateIndex,orientation,reference:r,audit};stop='first-passing-witness';break outer;
 }
 assert.equal(tested,Object.values(rejections).reduce((s,n)=>s+n,0)+(witness?1:0));
 const {candidates,...search}=geometry;
 const row={isotope:p===7?'N-13':'O-14',counts:{proton:p,neutron:6,electron:e},formalCharge:p-e,geometrySearch:{...search,geometryCandidates:candidates.length},phaseSearch:{totalReaderAssignments:total,tested,complete:tested===total,stop,rejections,assignmentCap:cap},status:witness?'all-contact-phase-reference-found':tested===total?'no-reference-in-bounded-charge-state':'phase-search-incomplete',witness};
 rows.push(row);console.log(JSON.stringify({isotope:row.isotope,electrons:e,geometryCandidates:candidates.length,status:row.status,phaseSearch:row.phaseSearch,witness:witness?{orientation:witness.orientation,candidateIndex:witness.candidateIndex,coveredCells:witness.audit.coverage.coveredCells,phaseStates:witness.audit.phaseStateCount}:null}));
}
for(const f of files)assert.equal(hash(await readFile(new URL(f,import.meta.url))),sourceHashes[f]);
await mkdir('research/strominger/results/proton-rich-ionization',{recursive:true});await writeFile('research/strominger/results/proton-rich-ionization/verification.json',JSON.stringify({status:'bounded-ionization-probes-recorded',sourceHashes,rows,scope:'Rooted 343-cell ansatz, independently rearranged nuclei; original contact and native-reader assumptions and repaired all-contact phase gate. Five/four electrons, not neutral atoms or bare nuclei. Geometry exhaustive; phase stops at first witness or explicit resource cap. No uniqueness, physical binding, stability, decay or reaction dynamics claim. No production/viewer changes.'},null,2)+'\n');
