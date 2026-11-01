import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,reconcileBothOrders,readRecords} from '../su32-layer4-comparison.mjs';
import {attachReference,splitAttachment} from '../su32-cross-cone-reference-fibre.mjs';
import {buildSulfur32Wiring} from '../../realization-tower/sulfur-32-wiring.mjs';
const root='research/strominger',geometryPath=root+'/results/su32-native-join-binding-v1/geometry.json';
const sha=async p=>createHash('sha256').update(await fs.readFile(p)).digest('hex');
const geometry=JSON.parse(await fs.readFile(geometryPath,'utf8'));
for(const [p,h] of Object.entries(geometry.sourceHashes))assert.equal(await sha(p),h);
const fixturePath=root+'/results/su32-hopf-tests-v1/fixture.json',fixture=JSON.parse(await fs.readFile(fixturePath,'utf8'));
const atlas=buildSu32SignedReferenceAtlas(fixture),layout=comparisonLayout(atlas,fixture,geometry.chartId,geometry.binding),target=comparisonLayout(atlas,fixture,geometry.consumerChartId,geometry.consumerBinding);
const labels=['P+','P-','E+','E-'],C=geometry.comparison.cell,D=geometry.otherComparison.cell;
assert.equal(geometry.otherComparison.sharedRecord,'P+');
const cs=new Map(),ds=new Map(),contexts=[];const key=JSON.stringify;
for(let bits=0;bits<16;bits++){
 const registry=Object.fromEntries(labels.map((k,i)=>[k,(bits>>i)&1])),built=reconcileBothOrders(layout,registry);
 const c=built.comparisons.find(x=>x.at===C),d=built.comparisons.find(x=>x.at===D);
 cs.set(key(c),c);ds.set(key(d),d);contexts.push({registry,c,d});
}
assert.equal(cs.size,8);assert.equal(ds.size,8);
const overlap=['P+','E+'];let unrestricted=0,compatible=0,rejectedByContext=0;let mismatch;
const contextual=new Set(contexts.map(({c,d})=>key([c,d])));
assert.equal(contextual.size,16);
for(const c of cs.values())for(const d of ds.values()){
 const consumer=attachReference(layout,target,C,layout.chart.target,c,d);
 const split=splitAttachment(layout,target,C,layout.chart.target,consumer);
 assert.deepEqual(split.point,c);assert.deepEqual(split.otherPayload,d);unrestricted++;
 const agrees=overlap.every(k=>key(c.records[k])===key(d.records[k]));
 assert.equal(agrees,contextual.has(key([c,d])));
 if(agrees)compatible++;else{rejectedByContext++;if(!mismatch)mismatch={c,d,consumer,sharedDisagreements:overlap.filter(k=>key(c.records[k])!==key(d.records[k]))};}
}
assert.equal(unrestricted,64);assert.equal(compatible,16);assert.equal(rejectedByContext,48);
let rawPreparationAndJoin=0,coherentPreparationAndJoin=0;
for(const {registry} of contexts)for(const c of cs.values()){
 rawPreparationAndJoin++;if(Object.entries(readRecords(layout,c)).every(([k,v])=>registry[k]===v))coherentPreparationAndJoin++;
}
assert.equal(rawPreparationAndJoin,128);assert.equal(coherentPreparationAndJoin,16);
const fixedPortProfile={producer:geometry.contacts.cOut.fromPort,consumer:geometry.contacts.cOut.toPort,other:geometry.contacts.dOut.fromPort};
const portFibres={producer:cs.size,commonPreparationConsumer:contexts.length};
const wiring=buildSulfur32Wiring(),port=geometry.blockedSingleWireTransfers[0].outgoingQuotientPort;
const outgoing=wiring.edges.filter(e=>e.from===port||e.to===port).map(e=>({edge:e.id,target:e.from===port?e.to:e.from,kind:e.kind}));
assert.equal(outgoing.length,1);assert.equal(outgoing[0].kind,'shared-quotient-face');
for(const p of wiring.ports){const ns=wiring.edges.filter(e=>e.from===p.id||e.to===p.id).map(e=>e.from===p.id?e.to:e.from);assert.equal(new Set(ns).size,ns.length,'Port graph has parallel outgoing edges');}
const sources=[geometryPath,fixturePath,root+'/checkers/check_su32_continuation_carriers.mjs',root+'/agda/Su32CoherentReferenceCarrier.agda',root+'/agda/NativeSharedReaderJoin.agda',
 root+'/su32-layer4-comparison.mjs',root+'/su32-cross-cone-reference-fibre.mjs',root+'/su32-signed-reference-encoder.mjs',
 'research/realization-tower/sulfur-32-wiring.mjs',root+'/agda/InternalSourceComparisons.agda',root+'/agda/GeneratedReaderClassification.agda'];
const sourceHashes={};for(const p of sources)sourceHashes[p]=await sha(p);
const report={passed:true,schema:'su32.continuation-carrier-audit.v1',nativeSignalExecuted:false,
 counts:{producerValues:cs.size,otherProducerValues:ds.size,rawProductConsumers:unrestricted,commonPreparationConsumers:compatible,inconsistentProductConsumers:rejectedByContext,
 rawPreparationAndJoin,coherentPreparationAndJoin},mismatch,fixedPortProfile,portReaderFibreSizes:portFibres,
 nativeAllOutgoingProbe:{port,outgoing,fixedOperandCurrentCarrierSizeInSetFragment:1,
  scope:'For a FIXED actual input package with set-valued carrier, the existing loop-retaining all-outgoing attachment normalizes to Out(port). This does not count the family over varying retained preparations.'},
 conclusion:'Literal reference attachment accepts independent producer packets. Common preparation adds a real carrier constraint: 64 combinations reduce to 16. Likewise raw preparation-times-join has 128 values, not 16. Port-only readers forget payloads. These carriers cannot be silently substituted for a fixed-input all-outgoing attachment carrier.',
 limits:['Boolean finite current-value diagnostic; no proof irrelevance of Resolve or identification of histories.',
 'Changing the retained preparation changes the native package. A disjoint union over preparations is not one fixed package carrier.',
 'Geometry contacts certify incidence only; missing interface witnesses and charged-cell wire transfers remain missing.',
 'The coherent carrier construction does not establish reader injectivity for arbitrary payload/history-bearing Su-32 packets or invoke the old four-vertex filler compiler.'],sourceHashes};
const dir=root+'/results/su32-native-join-binding-v1';await fs.writeFile(dir+'/carrier-audit.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({passed:true,counts:report.counts,portReaderFibreSizes:portFibres,fixedInputNativeOutgoingCarrier:1,nativeSignalExecuted:false,conclusion:report.conclusion},null,2));
