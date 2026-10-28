import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const registration='research/strominger/contracts/pb208-native-whole-fixture-attempt.v1.json';
const snapshot='research/strominger/contracts/persistent-seam-pe-conjecture-net.snapshot.rev26.json';
const fixturePath='research/strominger/results/joint-field-sewing-fixture.json';
const fieldPath='research/strominger/results/joint-field-assembly-sewing.json';
const out='research/strominger/results/native-whole-inventory-fixture';
const checks=[];function check(name,fn){fn();checks.push(name);}
const load=async p=>JSON.parse(await fs.readFile(path.join(root,p),'utf8'));
const fixture=await load(fixturePath),field=await load(fieldPath),pre=await load(snapshot);
check('registered two-criterion attempt precedes execution',()=>{
 const n=pre.conjectures.find(n=>n.id==='pb208-native-whole-fixture-attempt');
 assert.equal(n.status,'open');assert.equal(n.registration_before_execution,true);assert.equal(n.pair_binding_established,false);assert.ok(n.evidence.includes(registration));
});
const F=new GenerativeAssemblyRules(),retained=new Set([F.root]);
for(const history of fixture.histories){let active=F.root;for(const kind of history.word){
 const op=F.outgoing(active).map(i=>F.operations[i]).find(o=>o.kind===kind);assert.ok(op);F.validateTransfer(op);active=op.target;retained.add(active);
}}
const ids=[...retained],audit=F.inspect(ids);
function inventory(packets){const d=F.describe(packets);assert.equal(d.valid,true);return Object.fromEntries(['proton','neutron','electron'].map(s=>[s,[...d.bodies.values()].filter(x=>x===s).length]));}
const counts=inventory(ids);
check('native source histories construct the certified whole, not a Pb target',()=>{
 assert.equal(ids.length,14);assert.equal(audit.links.length,18);assert.equal(audit.certifiedExit,true);
 assert.deepEqual(counts,fixture.audit.counts);assert.deepEqual(counts,{proton:2,neutron:2,electron:1});
});
const chartReadings=ids.map(id=>({packet:id,readerSpecies:F.charts[F.packets[id].chart].species,inventory:inventory(ids)}));
check('all fourteen active chart choices retain the computed whole inventory',()=>{
 assert.equal(new Set(chartReadings.map(x=>x.readerSpecies)).size,3);for(const x of chartReadings)assert.deepEqual(x.inventory,counts);
});
check('all eighteen native interfaces preserve this independent whole-record projection',()=>{
 for(const i of audit.links){const op=F.operations[i];assert.ok(retained.has(op.source)&&retained.has(op.target));assert.ok(F.validateTransfer(op));
 assert.deepEqual(chartReadings.find(x=>x.packet===op.source).inventory,chartReadings.find(x=>x.packet===op.target).inventory);}
});
const noE=ids.filter(id=>F.charts[F.packets[id].chart].species!=='electron');
check('inventory is derived from occupied bodies, not a fitted constant',()=>{
 assert.deepEqual(inventory(noE),{proton:2,neutron:2,electron:0});assert.notDeepEqual(inventory(noE),counts);
});
const S=new GenerativeAssemblyRules();
const pn=S.outgoing(S.root).map(i=>S.operations[i]).find(o=>o.kind==='PN');
const options=S.outgoing(pn.target).map(i=>S.operations[i]);
const ne=options.find(o=>o.kind==='NE'),nn=options.find(o=>o.kind==='NN-phase-advance');
const sourceN=S.packets[nn.target],sourceE=S.packets[ne.target];
const sourceNChart=S.charts[sourceN.chart],sourceEChart=S.charts[sourceE.chart];
const key=vertices=>vertices.map(v=>Array.isArray(v)?v.join(','):v).sort().join('|');
const fixtureBodies=new Map([...F.describe(ids).bodies].map(([cell,species])=>[F.geometry.cells[cell].key,species]));
const bindings=[];
for(const active of ids){
 const packet=F.packets[active],chart=F.charts[packet.chart];if(chart.species!=='proton')continue;
 // A shared marked root fixes ONE affine map for BOTH alternatives.
 const columns=['C0','M0','C1','M1'].map(n=>chart.aliases[n].split(',').map(Number));
 const mapVertex=vertex=>{const w=vertex.split(',').map(Number);assert.equal(w.reduce((a,b)=>a+b,0),1);return columns[0].map((_,j)=>w.reduce((n,x,i)=>n+x*columns[i][j],0)).join(',');};
 const matches=sourceId=>{
  const p=S.packets[sourceId],c=S.charts[p.chart];
  const geometry=key(S.geometry.cells[c.cell].vertices.map(mapVertex));
  const expectedAliases=Object.fromEntries(Object.entries(c.aliases).map(([name,v])=>[name,mapVertex(v)]));
  const expectedPermutation=p.permutation.map(i=>packet.permutation[i]);
  const exact=ids.filter(id=>{const q=F.packets[id],d=F.charts[q.chart];return d.species===c.species&&q.origin===packet.origin+p.origin&&
   JSON.stringify(q.permutation)===JSON.stringify(expectedPermutation)&&Object.entries(expectedAliases).every(([n,v])=>d.aliases[n]===v);});
  return {mappedGeometry:geometry,occupiedSpecies:fixtureBodies.get(geometry)??null,exactPackets:exact,expectedAliases,expectedOrigin:packet.origin+p.origin,expectedPermutation};
 };
 const rootMatch=matches(S.root),prefix=matches(pn.target),e=matches(ne.target),n=matches(nn.target);
 assert.equal(e.mappedGeometry,n.mappedGeometry);
 bindings.push({rootPacket:active,rootReferenceMatches:rootMatch.exactPackets.includes(active),prefix,electron:e,neutron:n,
 pairAdmitted:rootMatch.exactPackets.includes(active)&&prefix.exactPackets.length>0&&e.exactPackets.length>0&&n.exactPackets.length>0});
}
check('every retained P-packet marked-root frame was tested, with one shared map',()=>{
 assert.equal(bindings.length,chartReadings.filter(x=>x.readerSpecies==='proton').length);assert.ok(bindings.length>0);
 for(const b of bindings)assert.equal(b.electron.mappedGeometry,b.neutron.mappedGeometry);
});
check('no existing fixed-species whole admits both target packets in a common marked frame',()=>{
 assert.ok(bindings.every(b=>!b.pairAdmitted));
 for(const b of bindings)assert.ok(!(b.electron.exactPackets.length&&b.neutron.exactPackets.length));
});
check('some source root and PN prefixes genuinely bind; failure is not merely an empty frame search',()=>{
 assert.ok(bindings.some(b=>b.rootReferenceMatches&&b.prefix.exactPackets.length));
});
check('same-source-cell collision cannot be removed by coefficient rebinding',()=>{
 assert.equal(sourceEChart.cell,sourceNChart.cell);assert.notEqual(sourceEChart.species,sourceNChart.species);
 assert.notDeepEqual(sourceE.permutation,sourceN.permutation);
});
const result={registration,preExecutionSnapshot:snapshot,criterionDisposition:'inventory-grounded-but-pair-not-admitted',
 inventoryCriterionPassed:true,pairBindingEstablished:false,fullPbConstructionEstablished:false,allWholeAssemblyModelsRefuted:false,
 constructedCounts:counts,chartReadings,interfacesChecked:audit.links.length,bindings,
 scope:'Existing native retained-whole fixture and all of its P-packet marked-root frames. The inventory is a projection of the retained assembly record, not of the44 field amplitudes alone. The frame search is not all possible carrier reinterpretations.',
 nextMissingDatum:'A source-backed extension distinguishing local reader type from occupied-body species, with geometric/occurrence/field intertwiners; or an alternative retained construction admitting the required charts under its actual rules. No such extension is assumed here.'};
await fs.mkdir(path.join(root,out),{recursive:true});await fs.writeFile(path.join(root,out,'attempt.json'),JSON.stringify(result,null,2)+'\n');
const inputs=[registration,snapshot,fixturePath,fieldPath,'research/strominger/checkers/check_native_whole_inventory_fixture.mjs','research/strominger/native-whole-inventory-fixture-result-v1.md',out+'/attempt.json'];
for(const receipt of [fixture,field])for(const [p,d] of Object.entries(receipt.sourceHashes??{})){
 assert.equal(crypto.createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex'),d,'stale source '+p);inputs.push(p);
}
const nativeReceipt=await load('research/strominger/results/native-reader-comparison/verification.json');
for(const [p,d] of Object.entries(nativeReceipt.sourceHashes)){
 assert.equal(crypto.createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex'),d,'stale source '+p);inputs.push(p);
}
const sourceHashes={};for(const p of inputs)sourceHashes[p]=crypto.createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex');
const report={status:'passed',check_count:checks.length,checks,criterionDisposition:result.criterionDisposition,
 inventoryCriterionPassed:true,pairBindingEstablished:false,fullPbConstructionEstablished:false,allWholeAssemblyModelsRefuted:false,
 packetCount:ids.length,interfacesChecked:audit.links.length,rootFramesChecked:bindings.length,
 prefixBindings:bindings.filter(b=>b.rootReferenceMatches&&b.prefix.exactPackets.length).length,
 electronBindings:bindings.filter(b=>b.rootReferenceMatches&&b.prefix.exactPackets.length&&b.electron.exactPackets.length).length,
 neutronBindings:bindings.filter(b=>b.rootReferenceMatches&&b.prefix.exactPackets.length&&b.neutron.exactPackets.length).length,
 sourceHashes};
await fs.writeFile(path.join(root,out,'verification.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,checks:undefined,sourceHashes:undefined}));
