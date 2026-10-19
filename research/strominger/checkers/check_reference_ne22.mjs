// Fresh source-rule replay of the saved Ne-22 witness, without invoking Z3.
import assert from 'node:assert/strict';
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {phaseUniverse} from '../../nima/origin-bounded-assemblies.mjs';
const out='research/strominger/results/reference-ne22-search',hash=b=>createHash('sha256').update(b).digest('hex');
const summary=JSON.parse(await readFile(out+'/verification.json'));assert.deepEqual(summary.target,{proton:10,neutron:12,electron:10});
for(const [f,h] of Object.entries(summary.sourceHashes))assert.equal(hash(await readFile(new URL(f,import.meta.url))),h);
const positive=summary.rows.find(r=>r.witnessFile);assert.ok(positive);const saved=JSON.parse(await readFile(out+'/'+positive.witnessFile)),w=saved.witness;
const input=await readFile(out+`/D${saved.maxOrigin}-input.json`);assert.equal(hash(input),saved.inputSha256);
const u=phaseUniverse({maxOrigin:saved.maxOrigin,maxPackets:5000});assert.equal(u.complete,true);const {rules}=u;const selected=new Set(w.selectedPackets);assert.equal(selected.size,w.selectedPackets.length);assert.ok(selected.has(rules.root));assert.ok([...selected].every(p=>u.packets.includes(p)));
const originalOrder=w.packets.map(p=>p.id);assert.deepEqual([...originalOrder].sort((a,b)=>a-b),w.selectedPackets);
assert.deepEqual(w.packets,originalOrder.map(p=>rules.packets[p]));assert.deepEqual(w.charts,[...new Set(originalOrder.map(p=>rules.packets[p].chart))].map(c=>rules.charts[c]));
const reached=new Set([rules.root]);assert.deepEqual(w.prefixes[0],[rules.root]);
for(const [index,id] of w.word.entries()){
 assert.ok(u.operations.includes(id));const op=rules.operations[id];assert.ok(reached.has(op.source));assert.ok(selected.has(op.target));assert.ok(!reached.has(op.target));rules.validateTransfer(op);reached.add(op.target);
 const prefix=[...reached].sort((a,b)=>a-b);assert.deepEqual(prefix,w.prefixes[index+1]);assert.equal(rules.describe(prefix).valid,true);
}
assert.deepEqual([...reached].sort((a,b)=>a-b),w.selectedPackets);assert.equal(w.prefixes.length,w.word.length+1);
const description=rules.describe(originalOrder);assert.equal(description.valid,true);const inspection=rules.inspect(originalOrder);assert.deepEqual(inspection,w.inspection);assert.deepEqual(inspection.counts,summary.target);assert.equal(inspection.certifiedExit,true);assert.equal(inspection.pendingContacts.length,0);assert.equal(inspection.allPacketsCanReachExit,true);
const ops=u.operations.map(id=>rules.operations[id]).filter(o=>selected.has(o.source)&&selected.has(o.target));assert.deepEqual(ops,w.operations);
for(const op of ops)rules.validateTransfer(op);
const bodyRows=[...description.bodies].map(([cell,species])=>({cell,species,key:rules.geometry.cells[cell].key,vertices:rules.geometry.cells[cell].vertices.map(v=>rules.geometry.points.get(v))}));assert.deepEqual(bodyRows,w.bodies);assert.equal(bodyRows.length,32);
// Independently enumerate face-sharing occupied cell pairs by vertex equality,
// rather than using the generator's neighbor/contact enumeration.
const contacts=[];for(let a=0;a<bodyRows.length;a++)for(let b=a+1;b<bodyRows.length;b++){
 const ca=bodyRows[a].cell,cb=bodyRows[b].cell,face=rules.geometry.cells[ca].vertices.filter(v=>rules.geometry.cells[cb].vertices.includes(v));if(face.length!==3)continue;
 const witnesses=ops.filter(o=>{const x=rules.charts[rules.packets[o.source].chart].cell,y=rules.charts[rules.packets[o.target].chart].cell;return x===ca&&y===cb||x===cb&&y===ca;});assert.ok(witnesses.length,'Unwitnessed occupied face');contacts.push({cells:[ca,cb],face,operations:witnesses.map(o=>o.id)});
}
assert.equal(contacts.length,description.contacts.length);
// Independent reverse BFS across selected actual operations, not rank values.
const exits=w.selectedPackets.filter(p=>rules.charts[rules.packets[p].chart].species==='electron'),canExit=new Set(exits),queue=[...exits];
for(let i=0;i<queue.length;i++)for(const op of ops)if(op.target===queue[i]&&!canExit.has(op.source)){canExit.add(op.source);queue.push(op.source);}assert.equal(canExit.size,selected.size);
const receipt={status:'neutral-Ne22-saved-witness-replayed',target:summary.target,maxOrigin:saved.maxOrigin,grade:Math.max(...w.packets.map(p=>p.origin)),selectedRecords:selected.size,constructionSteps:w.word.length,occupiedBodies:bodyRows.length,occupiedFaceContacts:contacts.length,allSelectedRecordsReachExit:true,contacts,witnessSha256:hash(await readFile(out+'/'+positive.witnessFile)),inputSha256:hash(input),checkerSha256:hash(await readFile(new URL('./check_reference_ne22.mjs',import.meta.url))),sourceHashes:summary.sourceHashes,scope:'Fresh original-generator replay plus direct vertex-based contact enumeration and reverse exit BFS. Shares the original generator and geometry; not an independent physical model. Local certificate only, no global coupled-field sewing, binding or stability claim.'};await writeFile(out+'/replay-verification.json',JSON.stringify(receipt,null,2)+'\n');console.log(JSON.stringify({status:receipt.status,counts:receipt.target,grade:receipt.grade,records:receipt.selectedRecords,constructionSteps:receipt.constructionSteps,contacts:receipt.occupiedFaceContacts}));
