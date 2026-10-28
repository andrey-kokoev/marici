import assert from 'node:assert/strict';
import {writeFileSync,readFileSync} from 'node:fs';
import {GenerativeAssemblyRules} from '../../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import {packetSnapshot} from '../ramsey-native-word-trace.mjs';
const canonical=x=>Array.isArray(x)?x.map(canonical):x&&typeof x==='object'?Object.fromEntries(Object.keys(x).sort().map(k=>[k,canonical(x[k])])):x;
const key=x=>JSON.stringify(canonical(x));
const r=new GenerativeAssemblyRules();
const aliases=r.charts[r.packets[r.root].chart].aliases;
const complement={C0:aliases.M0,M0:aliases.C0,C1:aliases.M1,M1:aliases.C1};
const targetRules=new GenerativeAssemblyRules({seedBindings:complement});
const names=['C0','M0','C1','M1','C2'];
function refs(r,id){const a=r.charts[r.packets[id].chart].aliases;return Object.fromEntries(names.map(k=>[k,a[k]]));}
function profile(r,id){const p=r.packets[id],c=r.charts[p.chart];return {species:c.species,origin:p.origin,permutation:p.permutation,references:refs(r,id),cell:r.geometry.cells[c.cell].key};}
const source=profile(r,r.root),target=profile(targetRules,targetRules.root);
assert.equal(source.origin,0);assert.equal(target.origin,0);assert.notEqual(key(source.references),key(target.references));
const queue=[r.root],seen=new Set(queue),kept=[],excluded=[];
for(let at=0;at<queue.length;at++){
 const id=queue[at];assert.equal(r.packets[id].origin,0);
 for(const index of r.outgoing(id)){
  const op=r.operations[index];assert.equal(r.validateTransfer(op),true);
  const delta=['reader-phase-advance','NN-phase-advance'].includes(op.kind)?1:0;
  assert.equal(op.phaseDelta,delta);assert.equal(r.packets[op.target].origin,r.packets[op.source].origin+delta);
  if(delta){excluded.push(op);continue;}
  assert(['PN','inverse-PN','NE'].includes(op.kind));assert.equal(key(refs(r,op.source)),key(refs(r,op.target)));
  kept.push(op);if(!seen.has(op.target)){seen.add(op.target);queue.push(op.target);}
  if(queue.length>1000)throw Error('Resource guard reached: closure not certified');
 }
}
assert(queue.every(id=>key(profile(r,id))!==key(target)));
assert(queue.every(id=>key(refs(r,id))===key(source.references)));
const pn=kept.find(op=>op.kind==='PN');assert(pn);
const controls=[];
assert.throws(()=>r.validateTransfer(pn,r.packets[pn.source],{...r.packets[pn.target],origin:1}));controls.push('zero-step target origin changed');
const original=r.charts[r.packets[pn.target].chart];
const fake={...original,aliases:{...original.aliases,C0:original.aliases.M0,M0:original.aliases.C0}};
const fakeChart=r.charts.length;r.charts.push(fake);
assert.throws(()=>r.validateTransfer(pn,r.packets[pn.source],{...r.packets[pn.target],chart:fakeChart}));controls.push('zero-step named references changed');
r.charts.pop();
const prior=JSON.parse(readFileSync(new URL('../results/ramsey-native-PN-overlap-span-v1.json',import.meta.url),'utf8'));
const port=prior.witness.ports.find(p=>p.chart===7&&p.face===1);assert(port);
assert.equal(key(target.references),key(port.base.chart.aliases));
assert.equal(target.origin,port.base.packet.origin);assert.equal(key(target.permutation),key(port.base.packet.permutation));
const out={status:'passed',sourceProfile:source,targetProfile:target,sourcePacket:packetSnapshot(r,r.root),targetPacket:packetSnapshot(targetRules,targetRules.root),
 exhaustedWithoutDepthCutoff:true,zeroIncrementReachablePackets:queue.map(id=>profile(r,id)),zeroIncrementOperations:kept,excludedPositiveIncrementOperations:excluded,
 canonicalComplementInClosure:false,targetIsValidSeparateSeed:true,controls,resourceGuardTriggered:false};
writeFileSync(new URL('../results/ramsey-origin-zero-source-runtime-v1.json',import.meta.url),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({status:out.status,states:queue.length,zeroOperations:kept.length,excludedPositiveOperations:excluded.length,controls}));
