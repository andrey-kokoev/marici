// Fresh native reconstruction of a benchmark SAT candidate; old receipts untouched.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {dirname} from 'node:path';
import {createHash} from 'node:crypto';
import {phaseUniverse} from '../../nima/origin-bounded-assemblies.mjs';
const [inputPath,candidatePath,outputPath]=process.argv.slice(2);assert(inputPath&&candidatePath&&outputPath);
const hash=x=>createHash('sha256').update(x).digest('hex'),inputBytes=await readFile(inputPath),input=JSON.parse(inputBytes),candidate=JSON.parse(await readFile(candidatePath));
assert.equal(candidate.status,'sat');assert.equal(candidate.inputSha256,hash(inputBytes));
const summary=JSON.parse(await readFile(dirname(inputPath)+'/verification.json'));
for(const [path,digest] of Object.entries(summary.sourceHashes))assert.equal(hash(await readFile(new URL(path,import.meta.url))),digest);
assert.equal(summary.rows.find(row=>row.maxOrigin===input.maxOrigin).inputSha256,hash(inputBytes));
const u=phaseUniverse({maxOrigin:input.maxOrigin,maxPackets:5000});assert(u.complete);
const r=u.rules;assert.deepEqual(u.packets,input.packets);assert.deepEqual(u.operations.map(id=>r.operations[id]),input.operations);
const ids=candidate.selectedPackets,selected=new Set(ids);assert.equal(selected.size,ids.length);assert(selected.has(r.root));assert(ids.every(id=>u.packets.includes(id)));
const inspection=r.inspect(ids);assert(inspection.valid&&inspection.certifiedExit&&inspection.allContactsWitnessed&&inspection.allPacketsCanReachExit);assert.deepEqual(inspection.counts,input.target);
const reached=new Set([r.root]),word=[],prefixes=[[r.root]];
for(let changed=true;changed;){changed=false;for(const id of u.operations){const op=r.operations[id];if(reached.has(op.source)&&selected.has(op.target)&&!reached.has(op.target)){
 r.validateTransfer(op);reached.add(op.target);word.push(id);const prefix=[...reached].sort((a,b)=>a-b);assert(r.describe(prefix).valid);prefixes.push(prefix);changed=true;
}}}
assert.equal(reached.size,selected.size);
const description=r.describe(ids),operations=u.operations.map(id=>r.operations[id]).filter(op=>selected.has(op.source)&&selected.has(op.target));
const bodies=[...description.bodies].map(([cell,species])=>({cell,species,vertices:r.geometry.cells[cell].vertices}));
const contacts=[];
for(let i=0;i<bodies.length;i++)for(let j=i+1;j<bodies.length;j++){
 const a=bodies[i],b=bodies[j],face=a.vertices.filter(v=>b.vertices.includes(v));if(face.length!==3)continue;
 const witnesses=operations.filter(op=>{const x=r.charts[r.packets[op.source].chart].cell,y=r.charts[r.packets[op.target].chart].cell;return x===a.cell&&y===b.cell||x===b.cell&&y===a.cell;});
 assert(witnesses.length);contacts.push({cells:[a.cell,b.cell],face,operations:witnesses.map(op=>op.id)});
}
assert.equal(contacts.length,description.contacts.length);
const exits=ids.filter(id=>r.charts[r.packets[id].chart].species==='electron'),canExit=new Set(exits),queue=[...exits];
for(let i=0;i<queue.length;i++)for(const op of operations)if(op.target===queue[i]&&!canExit.has(op.source)){canExit.add(op.source);queue.push(op.source);}
assert.equal(canExit.size,selected.size);
const result={status:'native-candidate-replayed',target:input.target,maxOrigin:input.maxOrigin,mode:candidate.mode,seed:candidate.seed,inputSha256:hash(inputBytes),candidateSha256:hash(await readFile(candidatePath)),
 selectedRecords:ids.length,occupiedBodies:bodies.length,occupiedFaceContacts:contacts.length,constructionSteps:word.length,
 witness:{selectedPackets:ids,packets:ids.map(id=>r.packets[id]),charts:[...new Set(ids.map(id=>r.packets[id].chart))].map(id=>r.charts[id]),bodies,operations,word,prefixes,inspection,contacts},
 sourceHashes:summary.sourceHashes,checkerSha256:hash(await readFile(new URL('./replay_reference_solver_candidate.mjs',import.meta.url))),scope:'Fresh native reconstruction and direct contact/exit checks. No experimental PE or physical stability claim.'};
await mkdir(dirname(outputPath),{recursive:true});await writeFile(outputPath,JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:result.status,mode:candidate.mode,counts:input.target,origin:input.maxOrigin,records:ids.length,contacts:contacts.length}));
