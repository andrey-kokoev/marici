// Fresh witness replay plus complete retained four-electron N13 -> O14 search.
import assert from 'node:assert/strict';
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {searchCounts,domain} from './proton-rich-probe-model.mjs';
import {compilePhaseAssembly,auditPhaseAssembly} from '../demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
const inputURL=new URL('../results/proton-rich-ionization/verification.json',import.meta.url),raw=await readFile(inputURL),input=JSON.parse(raw),hash=b=>createHash('sha256').update(b).digest('hex');
// Hash keys in this receipt are relative to its owning checker directory.
for(const [f,h] of Object.entries(input.sourceHashes))assert.equal(hash(await readFile(new URL(f,import.meta.url))),h,'Stale search receipt: '+f);
const replay=[];
for(const row of input.rows.filter(r=>r.witness)){
 const {reference:r}=row.witness,recompiled=compilePhaseAssembly(r.candidate,r.orientations),audit=auditPhaseAssembly(recompiled);
 assert.deepEqual(recompiled,r);assert.deepEqual(audit,row.witness.audit);
 assert.equal(r.candidate.nucleus.filter(i=>domain.species[i]==='proton').length,row.counts.proton);assert.equal(r.candidate.nucleus.filter(i=>domain.species[i]==='neutron').length,6);assert.equal(r.candidate.electrons.length,4);
 assert.equal(audit.contacts.missing.length,0);
 const nn=r.candidate.interfaces.filter(e=>e.kind==='NN').length;assert.equal(nn,4);
 replay.push({isotope:row.isotope,charge:row.formalCharge,coveredCells:audit.coverage.coveredCells,allContactsWitnessed:true,NNContacts:nn,remainingMCCPortBudget:12-2*nn});
}
const old=input.rows.find(r=>r.isotope==='N-13'&&r.witness).witness.reference,geometry=searchCounts(8,6,4),chartKey=c=>JSON.stringify([c.cell,c.species,c.aliases]);
const candidates=geometry.candidates.filter(c=>old.candidate.nucleus.every(i=>c.nucleus.includes(i))&&old.candidate.electrons.every(i=>c.electrons.includes(i))&&Object.entries(old.candidate.types).every(([v,t])=>c.types[v]===t));
const accepted=[],rejections={};let tested=0,first=null;
for(const [candidateIndex,c] of candidates.entries())for(let o=0;o<2**c.interfaces.filter(e=>e.kind==='PN').length;o++){
 tested++;const r=compilePhaseAssembly(c,o);if(r.status!=='phase-coherent-reference'){rejections[r.reason]=(rejections[r.reason]??0)+1;continue;}
 const audit=auditPhaseAssembly(r);const retainsReaders=old.charts.every(a=>r.charts.some(b=>chartKey(a)===chartKey(b)));if(!retainsReaders){rejections['old-readers-not-retained']=(rejections['old-readers-not-retained']??0)+1;continue;}
 for(const e of old.edges)assert.ok(r.edges.some(f=>chartKey(old.charts[e.from])===chartKey(r.charts[f.from])&&chartKey(old.charts[e.to])===chartKey(r.charts[f.to])&&e.kind===f.kind&&e.phaseDelta===f.phaseDelta&&JSON.stringify(e.permutation)===JSON.stringify(f.permutation)));
 const a={candidateIndex,orientation:o,addedProtons:c.nucleus.filter(i=>!old.candidate.nucleus.includes(i)),coveredCells:audit.coverage.coveredCells,phaseStates:audit.phaseStateCount};assert.equal(a.addedProtons.length,1);accepted.push(a);first??={...a,reference:r,audit};
}
assert.equal(tested,accepted.length+Object.values(rejections).reduce((s,n)=>s+n,0));
assert.equal(hash(await readFile(inputURL)),hash(raw));
const receipt={status:'witnesses-replayed-retained-chain-search-complete',inputSha256:hash(raw),replay,retainedN13ToO14:{geometryCandidates:candidates.length,readerAssignmentsTested:tested,phaseSearchComplete:true,accepted,rejections,first},scope:'All-reference contact/history checks retained. Direct chain fixes the found N-13 cells, four electrons, roles and readers. No physical proton-capture dynamics, binding, stability or decay law; no neutral N13/O14 claim or viewer admission.'};
await writeFile(new URL('../results/proton-rich-ionization/replay-and-chain.json',import.meta.url),JSON.stringify(receipt,null,2)+'\n');console.log(JSON.stringify({replay,retainedChain:{geometryCandidates:candidates.length,tested,accepted,rejections}},null,2));
