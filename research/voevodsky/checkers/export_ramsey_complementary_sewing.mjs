import fs from 'node:fs';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
const source='research/strominger/results/channel-assembled-native-fixture.json';
const f=JSON.parse(fs.readFileSync(source,'utf8'));
const oldPackets=new Map(f.packets.map(p=>[p.id,p])),oldCharts=new Map(f.charts.map(c=>[c.index,c])),oldCells=new Map(f.cells.map(c=>[c.id,c]));
const vertices=['1,0,0,0','0,1,0,0','0,0,1,0','0,0,0,1'];
const paths=[source,'research/nima/generative-phase-assembly.mjs','research/voevodsky/contracts/ramsey-complementary-sewing-attempt.v1.json','research/voevodsky/checkers/export_ramsey_complementary_sewing.mjs'];
const sourceHashes=()=>Object.fromEntries(paths.map(p=>[p,createHash('sha256').update(fs.readFileSync(p)).digest('hex')]));
for(const [label,marking] of [['base',[0,1,2,3]],['complement',[1,0,3,2]]]){
 const transform=v=>{const x=v.split(',').map(Number),y=[0,0,0,0];for(let i=0;i<4;i++)y[marking[i]]=x[i];return y.join(',');};
 const r=new GenerativeAssemblyRules({seedBindings:Object.fromEntries(['C0','M0','C1','M1'].map((n,i)=>[n,vertices[marking[i]]]))});
 const map=new Map([[f.rootPacket,r.root]]),retained=new Set([r.root]),histories=[];
 for(const h of f.histories){
  let active=r.root;const packets=[active],operations=[];
  for(const [i,kind] of h.word.entries()){
   const op=r.outgoing(active).map(j=>r.operations[j]).find(o=>o.kind===kind);assert(op);assert(r.validateTransfer(op));
   active=op.target;const old=h.packets[i+1];if(map.has(old))assert.equal(map.get(old),active);else map.set(old,active);
   retained.add(active);packets.push(active);operations.push(op.id);
  }
  histories.push({id:h.id,word:h.word,packets,operations});
 }
 const audit=r.inspect([...retained]);assert(audit.valid&&audit.certifiedExit&&audit.allContactsWitnessed&&audit.allPacketsCanReachExit&&audit.allCellsOnEntryExitPaths);assert.equal(audit.pendingContacts.length,0);
 assert.equal(map.size,14);assert.equal(new Set(map.values()).size,14);assert.equal(audit.links.length,18);
 for(const [old,id] of map){
  const a=oldPackets.get(old),b=r.packets[id],ca=oldCharts.get(a.chart),cb=r.charts[b.chart];
  assert.equal(a.origin,b.origin);assert.deepEqual(a.permutation,b.permutation);assert.equal(ca.species,cb.species);
  assert.deepEqual(Object.fromEntries(Object.entries(ca.aliases).map(([n,v])=>[n,transform(v)])),cb.aliases);
  assert.deepEqual(oldCells.get(ca.cell).vertices.map(transform).sort(),[...r.geometry.cells[cb.cell].vertices].sort());
 }
 const operations=audit.links.map(i=>r.operations[i]);
 for(const op of f.operations){
  const matches=operations.filter(o=>o.source===map.get(op.source)&&o.target===map.get(op.target)&&o.kind===op.kind);assert.equal(matches.length,1);const o=matches[0];
  assert.equal(o.phaseDelta,op.phaseDelta);assert.deepEqual(o.permutation,op.permutation);
  assert.deepEqual(o.face?[...o.face].sort():null,op.face?op.face.map(transform).sort():null);
 }
 const rootCell=r.charts[r.packets[r.root].chart].cell;
 const facets=[...new Set(operations.filter(o=>o.kind==='PN'&&r.charts[r.packets[o.source].chart].cell===rootCell).map(o=>vertices.findIndex(v=>!o.face.includes(v))))].sort();
 assert.deepEqual(facets,label==='base'?[0,2]:[1,3]);
 const packets=[...retained].map(i=>r.packets[i]),charts=[...new Set(packets.map(p=>p.chart))].map(i=>({index:i,...r.charts[i]}));
 const out={status:'certified-native-retained-assembly',rootPacket:r.root,packets,charts,
  cells:[...new Set(charts.map(c=>c.cell))].map(i=>r.geometry.cells[i]),operations,histories,
  comparisonPackets:f.comparisonPackets.map(i=>map.get(i)),audit,sourceHashes:sourceHashes(),
  marking,rootFacets:facets,sourcePacketCorrespondence:[...map],fullReferenceCovariance:true,
  scope:'Independent marked context. Coordinate covariance of native records, not a world-field intertwiner or a cross-context occupied assembly.'};
 fs.writeFileSync(`research/voevodsky/results/ramsey-complementary-sewing-${label}-fixture-v1.json`,JSON.stringify(out,null,2)+'\n');
 console.log(JSON.stringify({label,packets:packets.length,interfaces:operations.length,facets}));
}
