import assert from 'node:assert/strict';
import fs from 'node:fs';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
const base='research/voevodsky/', source='research/strominger/results/channel-assembled-native-fixture.json';
const fixture=JSON.parse(fs.readFileSync(source,'utf8'));
const receiptPath='research/strominger/results/strict-native-comparison-verification.json';
const receipt=JSON.parse(fs.readFileSync(receiptPath,'utf8'));
const hash=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
for(const [p,h] of Object.entries(receipt.sourceHashes))assert.equal(hash(p),h,`stale input ${p}`);
const perms=a=>a.length?a.flatMap((x,i)=>perms(a.filter((_,j)=>j!==i)).map(t=>[x,...t])):[[]];
const names=['C0','M0','C1','M1'];
const oldPackets=new Map(fixture.packets.map(p=>[p.id,p]));
const oldCharts=new Map(fixture.charts.map(c=>[c.index,c]));
const oldCells=new Map(fixture.cells.map(c=>[c.id,c]));
const rootChart=oldCharts.get(oldPackets.get(fixture.rootPacket).chart);
const vertices=names.map(n=>rootChart.aliases[n]);
const outcomes=[];const coverage=new Set();
for(const marking of perms([0,1,2,3])){
 const transform=v=>{const x=v.split(',').map(Number),y=[0,0,0,0];for(let i=0;i<4;i++)y[marking[i]]=x[i];return y.join(',');};
 const aliases=Object.fromEntries(names.map((n,i)=>[n,vertices[marking[i]]]));
 const rules=new GenerativeAssemblyRules({seedBindings:aliases});
 const map=new Map([[fixture.rootPacket,rules.root]]),retained=new Set([rules.root]),histories=[];
 for(const h of fixture.histories){
  let active=rules.root;const packets=[active],operations=[];
  for(let i=0;i<h.word.length;i++){
   const op=rules.outgoing(active).map(k=>rules.operations[k]).find(o=>o.kind===h.word[i]);
   assert(op);assert(rules.validateTransfer(op));active=op.target;
   const old=h.packets[i+1];if(map.has(old))assert.equal(map.get(old),active);else map.set(old,active);
   retained.add(active);packets.push(active);operations.push(op.id);
  }
  histories.push({word:h.word,packets,operations});
 }
 const audit=rules.inspect([...retained]);
 assert(audit.valid&&audit.certifiedExit&&audit.allContactsWitnessed&&audit.allPacketsCanReachExit&&audit.allCellsOnEntryExitPaths);
 assert.equal(audit.pendingContacts.length,0);assert.equal(retained.size,14);assert.equal(audit.links.length,18);
 assert.equal(new Set(map.values()).size,14);
 for(const [old,id] of map){
  const a=oldPackets.get(old),b=rules.packets[id],ca=oldCharts.get(a.chart),cb=rules.charts[b.chart];
  assert.equal(a.origin,b.origin);assert.deepEqual(a.permutation,b.permutation);assert.equal(ca.species,cb.species);
  assert.deepEqual(Object.fromEntries(Object.entries(ca.aliases).map(([n,v])=>[n,transform(v)])),cb.aliases);
  assert.deepEqual(oldCells.get(ca.cell).vertices.map(transform).sort(),[...rules.geometry.cells[cb.cell].vertices].sort());
 }
 const actual=audit.links.map(i=>rules.operations[i]);
 for(const op of fixture.operations){
  const matched=actual.filter(o=>o.source===map.get(op.source)&&o.target===map.get(op.target)&&o.kind===op.kind);
  assert.equal(matched.length,1);const o=matched[0];
  assert.equal(o.phaseDelta,op.phaseDelta);assert.deepEqual(o.permutation,op.permutation);
  assert.deepEqual(o.face?[...o.face].sort():null,op.face?op.face.map(transform).sort():null);
 }
 const [a,b]=fixture.comparisonPackets.map(i=>rules.packets[map.get(i)]);
 assert.equal(a.chart,b.chart);assert.equal(a.origin,b.origin);assert.notDeepEqual(a.permutation,b.permutation);
 const faces=[];
 for(const op of actual){
  const p=rules.packets[op.source],c=rules.charts[p.chart];
  if(op.kind!=='PN'||c.cell!==rules.charts[rules.packets[rules.root].chart].cell)continue;
  const omitted=vertices.findIndex(v=>!op.face.includes(v));assert(omitted>=0);
  assert.equal(op.face.filter(v=>[c.aliases.M0,c.aliases.M1].includes(v)).length,2);
  faces.push(omitted);coverage.add(omitted);
 }
 assert.equal(new Set(faces).size,2);
 const packets=[...retained].map(i=>rules.packets[i]);
 const charts=[...new Set(packets.map(p=>p.chart))].map(i=>({index:i,...rules.charts[i]}));
 outcomes.push({marking,seedBindings:aliases,rootPacket:rules.root,packets,charts,
  cells:[...new Set(charts.map(c=>c.cell))].map(i=>rules.geometry.cells[i]),operations:actual,
  histories,comparisonPackets:fixture.comparisonPackets.map(i=>map.get(i)),audit,
  sourcePacketCorrespondence:[...map],rootFacets:[...new Set(faces)].sort()});
}
assert.deepEqual([...coverage].sort(),[0,1,2,3]);
const inputPaths=[source,receiptPath,'research/nima/generative-phase-assembly.mjs',
 base+'contracts/ramsey-marked-sewing-replay-attempt.v1.json',base+'checkers/check_ramsey_marked_sewing_replay.mjs'];
const result={schema:'marici.ramsey-marked-sewing-replay.verification.v1',status:'passed',
 scope_id:'independent-marked-native-sewing-family-v1',contexts:outcomes.length,
 packetOccurrences:outcomes.reduce((n,x)=>n+x.packets.length,0),interfaceOccurrences:outcomes.reduce((n,x)=>n+x.operations.length,0),
 coveredFacets:[...coverage].sort(),fullReferenceCovariance:true,coefficientAndPhaseCovariance:true,
 jointCrossContextAssemblyCertified:false,crossContextWorldFieldIntertwinerProved:false,
 nativeWGRestrictionConstructed:false,parentDescentResolved:false,
 source_sha256:Object.fromEntries(inputPaths.map(p=>[p,hash(p)])),assemblies:outcomes};
fs.writeFileSync(base+'results/ramsey-marked-sewing-replay-v1.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({...result,assemblies:undefined,source_sha256:undefined}));
