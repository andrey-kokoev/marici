import assert from 'node:assert/strict';
import {readFileSync,writeFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
import {packetSnapshot} from '../ramsey-native-word-trace.mjs';
import {phaseFrame} from '../../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const sha=p=>createHash('sha256').update(readFileSync(p)).digest('hex');
const diagnostic='research/voevodsky/results/ramsey-parent-face-binding-diagnostic-v1.json';
const priorPath='research/voevodsky/results/ramsey-native-PN-overlap-span-v1.json';
const d=JSON.parse(readFileSync(diagnostic)),prior=JSON.parse(readFileSync(priorPath));
for(const data of [d,prior])for(const [p,h] of Object.entries(data.source_sha256))assert.equal(sha(p),h,`stale ${p}`);
const r=new GenerativeAssemblyRules(),cell=r.charts[r.packets[r.root].chart].cell,vertices=r.geometry.cells[cell].vertices;
const key=f=>[...f].sort().join('|'),names=['C0','M0','C1','M1'];
function normalized(s,offset){return {cell:s.cell.key,species:s.chart.species,aliases:s.chart.aliases,
 origin:s.packet.origin-offset,permutation:s.packet.permutation};}
const contexts=[],ports=[],requests=[];let validated=0;
for(const [c,row] of d.rows.entries()){
 const chart=r.completeP(cell,row.targetFullReference);assert.notEqual(chart,null);
 const base=r.packet(chart,2,[0,1,2,3,4]),out=r.outgoing(base).map(i=>r.operations[i]);
 const direct=out.find(o=>o.kind==='PN'),reader=out.find(o=>o.kind==='reader-phase-advance');
 const next=r.outgoing(reader.target).map(i=>r.operations[i]).find(o=>o.kind==='PN');
 // Replay the original P->N->E history to materialize every dual reference point.
 const original=r.completeP(cell,Object.fromEntries(names.map((n,i)=>[n,vertices[row.marking[i]]])));
 const originalPN=r.outgoing(r.packet(original,0,[0,1,2,3,4])).map(i=>r.operations[i]).find(o=>o.kind==='PN');
 const originalNE=r.outgoing(originalPN.target).map(i=>r.operations[i]).find(o=>o.kind==='NE');
 assert(r.validateTransfer(originalPN)&&r.validateTransfer(originalNE));
 const e=r.chart(cell,'electron',row.dualFullReference),ep=r.packet(e,0,[4,3,2,1,0]);
 const epacket=packetSnapshot(r,ep),ef=phaseFrame(r.charts[e],0),pf=phaseFrame(r.charts[chart],2);
 const occurrences=[...ef.window,ef.context].map(x=>{const y=[...pf.window,pf.context].find(y=>y.vertex===x.vertex);assert(y&&x.role===y.role);return {source:x,target:y,delta:y.index-x.index};});
 assert.deepEqual(occurrences.map(x=>x.delta).sort(),[0,0,2,2]);
 contexts.push({chart:c,e:epacket,eFrame:ef,p:packetSnapshot(r,base),pFrame:pf,occurrences,
  convention:'same chamber; P origin = E origin +2; P.C0=E.C2, P.M0=E.M2, P.C1=E.C1, P.M1=E.M1; completeP supplies outside C2',
  admission:'independently validated complete contextual inputs; not an E->P emitted operation'});
 for(const op of [direct,reader,next]){assert(op&&r.validateTransfer(op));validated++;}
 for(const [op,prefix] of [[direct,[]],[next,[reader]]]){
  const f=vertices.findIndex(v=>!op.face.includes(v));assert(f>=0);
  const source=packetSnapshot(r,op.source),target=packetSnapshot(r,op.target);
  const old=prior.witness.ports.find(p=>p.face===f&&names.every(n=>p.base.chart.aliases[n]===row.targetFullReference[n]));assert(old);
  // Full references and all five slots agree with the existing port family;
  // only allocation IDs and the explicit +2 origin lift are normalized away.
  assert.deepEqual(normalized(source,2),normalized(old.source,0));
  assert.deepEqual(normalized(target,2),normalized(old.target,0));
  for(const field of ['kind','phaseDelta','permutation','face'])assert.deepEqual(op[field],old.operation[field]);
  assert.equal(prefix.length,old.prefix.length);
  const role=Object.fromEntries(names.map(n=>[row.targetFullReference[n],n[0]]));
  assert.equal(op.face.filter(v=>role[v]==='M').length,2);
  ports.push({chart:c,face:f,role,base:packetSnapshot(r,base),prefix,source,operation:op,target,priorChart:old.chart,priorFace:old.face,originLift:2});
 }
 for(let f=0;f<4;f++){
  const available=ports.some(p=>p.chart===c&&p.face===f);
  const sourceFace=key(vertices.filter((_,i)=>i!==f));
  assert.equal(available,row.targetDomain.includes(sourceFace));
  assert.equal(available,!row.sourceDomain.includes(sourceFace));
  requests.push({chart:c,face:f,accepted:available,reason:available?'target P permit; E retained as context':'target P has only one M on this face'});
 }
}
assert.equal(ports.length,48);assert.equal(requests.filter(x=>x.accepted).length,48);
const controls=[];function rejects(n,f){assert.throws(f);controls.push(n);}
rejects('all E-context faces silently admitted as PN',()=>assert(requests.every(x=>x.accepted)));
rejects('drop outside reference from existing PN binding',()=>{const s=structuredClone(ports[0].source);delete s.chart.aliases.C2;assert.deepEqual(normalized(s,2),normalized(ports[0].source,2));});
rejects('erase origin lift',()=>assert.equal(ports[0].source.packet.origin,prior.witness.ports.find(p=>p.chart===ports[0].priorChart&&p.face===ports[0].priorFace).source.packet.origin));
rejects('all occurrences retained identically',()=>assert(contexts[0].occurrences.every(x=>x.delta===0)));
const pins=new Set([diagnostic,priorPath,'research/voevodsky/checkers/check_ramsey_passive_EP_port.mjs','research/voevodsky/ramsey-native-word-trace.mjs',...Object.keys(d.source_sha256),...Object.keys(prior.source_sha256)]);
const result={status:'passed',contexts,ports,requests,validatedTransfers:validated,controls,
 policy:'all listed E contexts and independently validated target P/PN records admitted before selecting requests',
 scope:'finite structural passive contextual adapter and +2 port-family binding; no field-amplitude E/P equality, source-only generation or active transition claimed',
 source_sha256:Object.fromEntries([...pins].map(p=>[p,sha(p)]))};
writeFileSync('research/voevodsky/results/ramsey-passive-EP-port-input-v1.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:'passed',contexts:24,ports:48,accepted:48,refused:48,validatedTransfers:validated,controls:controls.length}));
