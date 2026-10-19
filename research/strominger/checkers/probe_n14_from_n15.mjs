// Diagnostic deletion only: preserve all other readers in the saved N-15.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {phaseUniverse} from '../../nima/origin-bounded-assemblies.mjs';
const base='research/strominger/results/reference-n15-search',summary=JSON.parse(await readFile(base+'/verification.json')),row=summary.rows.find(r=>r.witnessFile),bytes=await readFile(base+'/'+row.witnessFile),w=JSON.parse(bytes).witness;
const {rules,operations}=phaseUniverse({maxOrigin:row.maxOrigin,maxPackets:5000}),cell=p=>rules.charts[rules.packets[p].chart].cell;
assert.equal(rules.inspect(w.selectedPackets).certifiedExit,true);
const trials=[];
for(const n of w.bodies.filter(b=>b.species==='neutron')){
 const keep=w.selectedPackets.filter(p=>cell(p)!==n.cell),audit=rules.inspect(keep),selected=new Set(keep),reached=new Set([rules.root]);
 assert.deepEqual(audit.counts,{proton:7,neutron:7,electron:7});
 for(let changed=true;changed;){changed=false;for(const i of operations){const op=rules.operations[i];if(reached.has(op.source)&&selected.has(op.target)&&!reached.has(op.target)){reached.add(op.target);changed=true;}}}
 const unrooted=keep.filter(p=>!reached.has(p));
 trials.push({removedNeutron:n,counts:audit.counts,valid:audit.valid,allContactsWitnessed:audit.allContactsWitnessed,pendingContacts:audit.pendingContacts,allPacketsCanReachExit:audit.allPacketsCanReachExit,localExitCertificate:audit.certifiedExit,unrootedPackets:unrooted,unrootedBodies:[...new Set(unrooted.map(cell))],rooted:unrooted.length===0,accepted:audit.certifiedExit&&unrooted.length===0});
}
assert.equal(trials.length,8);assert.ok(trials.every(t=>!t.accepted));
const out='research/strominger/results/n14-from-n15';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify({status:'single-neutron-deletions-audited',sourceWitness:base+'/'+row.witnessFile,sourceWitnessSha256:createHash('sha256').update(bytes).digest('hex'),trials,scope:'Delete one occupied neutron and all its selected records, preserve all other saved readers. Recheck original guards/contacts/exits and rooted reachability using the full origin-4 operation universe restricted to retained records. No new readers, rearrangement, alternative root or subdivision searched. Exit-only certificate is NOT sufficient for admission.'},null,2)+'\n');
console.log(JSON.stringify(trials.map(t=>({removedCell:t.removedNeutron.cell,contacts:t.allContactsWitnessed,exit:t.allPacketsCanReachExit,unrooted:t.unrootedPackets.length,accepted:t.accepted})),null,2));
