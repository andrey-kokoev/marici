import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {deriveObstruction} from './pne-source-obstructions.mjs';
const fingerprint=u=>createHash('sha256').update(JSON.stringify({maxOrigin:u.maxOrigin,mode:u.mode,packets:u.packets.map(p=>u.rules.packets[p]),charts:u.rules.charts,cells:u.rules.geometry.cells.map(c=>({key:c.key,vertices:c.vertices,geometry:c.geometry})),operations:u.operations.map(i=>u.rules.operations[i]),shortcuts:u.shortcuts})).digest('hex');
export function admitPruning(u,proof,{maxOrigin,mode,proofSha256,sourceHashes,actualSourceHashes}){
 assert.equal(u.maxOrigin,maxOrigin,'Proof budget mismatch');assert.equal(u.mode,mode,'Proof mode mismatch');assert.deepEqual(actualSourceHashes,sourceHashes,'Proof source hash mismatch');
 assert.equal(proof.status,'pass-all-nine-source-local-obstructions');
 let leaves=0;
 function verify(tree,required,forbidden){
  assert.ok(tree);if(tree.kind==='split'){assert.ok(u.packets.includes(tree.packet));assert.ok(tree.packet!==u.rules.root&&!required.includes(tree.packet)&&!forbidden.includes(tree.packet));verify(tree.present,[...required,tree.packet],forbidden);verify(tree.absent,required,[...forbidden,tree.packet]);return;}
  assert.equal(tree.kind,'contradiction');assert.deepEqual(tree.required,required);assert.deepEqual(tree.forbidden,forbidden);assert.equal(deriveObstruction(u,required,{forbidden}).status,'obstructed');leaves++;
 }
 const cores=[];for(const r of proof.results){assert.ok(r.core.length&&r.core.every(p=>u.packets.includes(p)));if(r.sourceCertificate.status==='obstructed'){assert.equal(deriveObstruction(u,r.core).status,'obstructed');leaves++;}else{assert.equal(r.jointProof.status,'complete');verify(r.jointProof.tree,r.core,[]);}cores.push([...r.core]);}
 assert.equal(cores.length,9);
 return {maxOrigin,mode,proofSha256,sourceHashes,universeFingerprint:fingerprint(u),cores,replayedContradictionLeaves:leaves};
}
export function synthesizePruned(u,c,admission,{maxConfigurations=1000000}={}){
 assert.equal(admission.maxOrigin,u.maxOrigin,'Proof budget mismatch');assert.equal(admission.mode,u.mode,'Proof mode mismatch');assert.equal(admission.universeFingerprint,fingerprint(u),'Proof universe mismatch');assert.deepEqual(c.packets,u.packets);
 const coreMasks=admission.cores.map(ps=>c.mask(ps));assert.ok(coreMasks.every(m=>(c.root&m)!==m));
 let active=0n;for(const o of c.interfaces)if(c.enabled(o,c.root))active|=o.bit;
 const nodes=[{mask:c.root,active,parent:-1,added:-1}],byMask=new Map([[c.root,0]]),rejected=new Set(),pruned=new Set();const prunedByCore=coreMasks.map(()=>0);let lostRootCandidates=0;
 for(let i=0;i<nodes.length;i++){
  const n=nodes[i];let targets=0n;for(const o of c.interfaces)if(n.mask&o.sourceBit)targets|=o.targetBit;targets&=~n.mask;
  for(let p=0;p<c.packets.length;p++){
   if(!(targets&c.bit[p])||(n.mask&c.conflicts[p]))continue;
   const m=n.mask|c.bit[p];if(byMask.has(m)||rejected.has(m)||pruned.has(m))continue;
   const obstruction=coreMasks.findIndex(core=>(m&core)===core);if(obstruction>=0){pruned.add(m);prunedByCore[obstruction]++;continue;}
   const a=c.update(n.active,m,p);if(!c.rooted(m,a)){rejected.add(m);lostRootCandidates++;continue;}
   if(nodes.length>=maxConfigurations)return {complete:false,reason:'configuration-resource-limit',nodes,byMask};
   byMask.set(m,nodes.length);nodes.push({mask:m,active:a,parent:i,added:c.packets[p]});
  }
 }
 return {complete:true,nodes,byMask,prunedCandidates:pruned.size,prunedByCore,lostRootCandidates};
}
