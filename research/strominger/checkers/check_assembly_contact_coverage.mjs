import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {compilePhaseAssembly,auditPhaseAssembly,auditAssemblyContacts,selectPhaseAssembly} from '../demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
const fixtures=JSON.parse(await readFile(new URL('./fixtures/legacy-unwitnessed-contacts.json',import.meta.url))),legacy=[];
for(const f of fixtures){
 const r=compilePhaseAssembly(f.candidate,f.orientations);
 if(f.name==='carbon12'){assert.equal(r.status,'phase-coherent-reference');auditPhaseAssembly(r);}
 else {assert.equal(r.status,'rejected');assert.equal(r.reason,'unwitnessed-physical-contact');assert.deepEqual(r.contacts.missing.map(e=>[e.from,e.to,e.kind]),[[13,14,'NE']]);}
 legacy.push({name:f.name,status:r.status,reason:r.reason??null});
}
const rows=[];
for(const name of ['helium3','helium4','lithium6','lithium7','beryllium9','boron10','boron11','carbon12','carbon13','nitrogen15']){
 const r=selectPhaseAssembly(name),audit=auditPhaseAssembly(r);assert.equal(audit.contacts.status,'all-physical-contacts-witnessed');assert.equal(audit.contacts.requiredContacts,r.candidate.interfaces.length);
 // Delete ALL witnesses to one physical contact: leave all charts/states in
 // place. Contact coverage must reject before ordinary certificate checks.
 for(const kind of ['PN','NE','NN']){
  const contact=r.candidate.interfaces.find(e=>e.kind===kind);if(!contact)continue;
  const bad=structuredClone(r),pair=[contact.from,contact.to].sort((a,b)=>a-b).join(',');
  bad.edges=bad.edges.filter(e=>[bad.charts[e.from].cell,bad.charts[e.to].cell].sort((a,b)=>a-b).join(',')!==pair);
  assert.ok(auditAssemblyContacts(bad).missing.some(e=>e.kind===kind));assert.throws(()=>auditPhaseAssembly(bad),/Unwitnessed physical contact/);
 }
 const missingLedger=structuredClone(r);missingLedger.candidate.interfaces.pop();assert.throws(()=>auditPhaseAssembly(missingLedger),/ledger mismatch/);
 const duplicateLedger=structuredClone(r);duplicateLedger.candidate.interfaces.push(duplicateLedger.candidate.interfaces[0]);assert.throws(()=>auditPhaseAssembly(duplicateLedger),/ledger mismatch/);
 const invented=structuredClone(r);invented.edges.push({...invented.edges[0],from:r.root,to:r.root});assert.throws(()=>auditPhaseAssembly(invented),/actual contact/);
 const forgedChart=structuredClone(r);forgedChart.charts[0].species='electron';assert.throws(()=>auditPhaseAssembly(forgedChart),/occupied carrier/);
 rows.push({name,orientations:r.orientations,contacts:audit.contacts,coveredCells:audit.coverage.coveredCells,phaseStateCount:audit.phaseStateCount});
}
const hashes={};for(const f of ['../demos/particle-overlap-tetrahedron/phase-assembly-model.mjs','../demos/particle-overlap-tetrahedron/nitrogen15-reference.mjs','./fixtures/legacy-unwitnessed-contacts.json'])hashes[f]=createHash('sha256').update(await readFile(new URL(f,import.meta.url))).digest('hex');
await mkdir('research/strominger/results/assembly-contact-coverage',{recursive:true});await writeFile('research/strominger/results/assembly-contact-coverage/verification.json',JSON.stringify({status:'all-contact-gate-and-reselection-verified',hashes,legacy,rows,controls:['remove-all-PN-NE-NN-witnesses','delete-contact-ledger-entry','duplicate-ledger-entry','invent-self-contact-edge','forge-chart-species'],scope:'Every actual physical face contact has a validated typed transport witness; carrier and history coverage still separately required. No new physical contact law or stability criterion.'},null,2)+'\n');console.log('PASS all-contact compiler/auditor gate: ten reselected references, legacy counterexamples, missing/forged contact controls.');
