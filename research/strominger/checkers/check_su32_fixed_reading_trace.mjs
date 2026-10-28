// One fixed reading; distinguish source geometry, candidate reference joins,
// and the first unbound continuation. No invented middle relay operation.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,reconcileBothOrders,readRecords} from '../su32-layer4-comparison.mjs';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildFiveSideOctRoutingObligations} from '../../realization-tower/five-side-oct-routing-obligations.mjs';
const fixturePath='research/strominger/results/su32-hopf-tests-v1/fixture.json';
const middlePath='research/strominger/results/sulfur-32-middle-layer/verification.json';
const fixture=JSON.parse(await fs.readFile(fixturePath,'utf8'));
for(const [p,h] of Object.entries(fixture.sourceHashes))assert.equal(createHash('sha256').update(await fs.readFile(p)).digest('hex'),h);
const middle=JSON.parse(await fs.readFile(middlePath,'utf8'));
const reading=fixture.readings.find(r=>r.id==='reading:0:-1');assert(reading);
const atlas=buildSu32SignedReferenceAtlas(fixture);
const chart=atlas.charts.find(c=>c.reading===reading.id&&c.source===reading.incomingN);assert(chart);
const layout=comparisonLayout(atlas,fixture,chart.id,[0,0]);
const labels=['P+','P-','E+','E-'];
// One authoritative registry, not an independent payload copy at every site.
const registry=Object.fromEntries(labels.map((k,i)=>[k,{id:'input:'+k,value:{token:i+1},provenance:{entry:reading.incomingN,slot:k}}]));
const built=reconcileBothOrders(layout,registry);
assert.deepEqual(readRecords(layout,built.byE),registry);assert.deepEqual(readRecords(layout,built.byP),registry);
const adjacent=(a,b)=>fixture.interfaces.some(f=>{
 const cs=f.ports.map(p=>p.split('@')[0]);return cs.includes(a)&&cs.includes(b);
});
const byCell=new Map(fixture.cells.map(c=>[c.id,c]));
// Construct the full entry-side reference assignment, then check every native
// restriction. The outer branch view is a projection, NOT a signal transfer law.
const layer2=[...chart.P,...chart.E].map(cell=>({cell,record:layout.template.referenceBinding[cell]}));
const layer3=layout.template.channels.map(c=>({cell:c.cell,records:[c.P.record,c.E.record],references:[c.P.referenceCell,c.E.referenceCell]}));
const layer4=[
 ...reading.outer.map(o=>({cell:o.cell,kind:'outer-single-channel-view',inputCells:[o.input],
  operand:built.channels[o.input],records:Object.keys(built.channels[o.input].records).sort()})),
 ...built.comparisons.map(c=>({cell:c.at,kind:'shared-reference-join-candidate',inputCells:c.children.map(n=>n.at),
  operand:c,records:Object.keys(c.records).sort()}))
];
assert.equal(layer2.length,4);assert.equal(layer3.length,4);assert.equal(layer4.length,12);
assert.equal(new Set(layer4.map(x=>x.cell)).size,12);
for(const x of layer2){assert(adjacent(reading.incomingN,x.cell));assert(registry[x.record]);}
for(const x of layer3)for(const cell of x.references)assert(adjacent(cell,x.cell));
for(const x of layer4){
 for(const cell of x.inputCells)assert(adjacent(cell,x.cell));
 for(const label of x.records)assert.deepEqual(x.operand.records[label].payload,registry[label]);
}
const middleScope=middle.results.find(r=>r.axisIndex===0&&r.incomingSign===-1);assert(middleScope);
assert.equal(middleScope.assignments.length,4);
// Verify each WHOLE assignment, including the reflected outgoing-side cells.
// None is silently selected as the native routing. Incoming supports merely
// annotate the operands offered to a still-unknown middle operation.
const center=fixture.cells.flatMap(c=>c.vertices).reduce((a,v)=>a.map((x,i)=>x+v[i]),[0,0,0,0]);
const count=fixture.cells.reduce((n,c)=>n+c.vertices.length,0);for(let i=0;i<4;i++)center[i]/=count;
const reflect=v=>{const h=reading.axis.reduce((s,a,i)=>s+a*(v[i]-center[i]),0)/2;return v.map((x,i)=>x-h*reading.axis[i]);};
const shape=c=>c.vertices.map(v=>v.join(',')).sort().join('|');
const mirrorId=id=>{const wanted=shape({vertices:byCell.get(id).vertices.map(reflect)});return fixture.cells.find(c=>shape(c)===wanted)?.id;};
const annotated=middleScope.assignments.map((routes,index)=>{
 assert.equal(routes.length,6);
 assert.deepEqual(routes.flatMap(r=>[r.sourceP,r.sourceE]).sort(),layer4.map(x=>x.cell).sort());
 for(const side of ['sourceP','sourceE','targetP','targetE'])assert.equal(new Set(routes.map(r=>r[side])).size,6);
 return {index,routes:routes.map(r=>{
  for(const side of ['sourceP','sourceE','targetP','targetE'])assert(r.members.some(cell=>adjacent(r[side],cell)));
  assert.equal(mirrorId(r.sourceP),r.targetE);assert.equal(mirrorId(r.sourceE),r.targetP);
  const p=layer4.find(x=>x.cell===r.sourceP),e=layer4.find(x=>x.cell===r.sourceE);assert(p&&e);
  const shared=p.records.filter(k=>e.records.includes(k));
  for(const k of shared)assert.deepEqual(p.operand.records[k],e.operand.records[k]);
  return {...r,sourcePSupport:p.records,sourceESupport:e.records,
   availableRecordLabels:[...new Set([...p.records,...e.records])].sort(),sharedRecordLabels:shared,
   middleOperation:null,targetPayloads:null,
   status:'Geometric complete-assignment candidate; offered operand supports only, not a computed output.'};
 })};
});
for(const a of annotated)assert.deepEqual(a.routes.map(r=>r.availableRecordLabels.length).sort(),[2,3,3,3,3,4]);
const assignmentsDistinct=new Set(annotated.map(a=>JSON.stringify(a.routes.map(r=>[r.channel,r.sourceP,r.sourceE]))));
assert.equal(assignmentsDistinct.size,4);
// Reflection supplies an opposite boundary, not an identification of records.
const outgoingN=mirrorId(reading.incomingN);assert(outgoingN);
const reverseReading=fixture.readings.find(r=>r.incomingN===outgoingN);assert(reverseReading);
assert.equal(reverseReading.id,'reading:0:1');
const reverseChart=atlas.charts.find(c=>c.reading===reverseReading.id&&c.source===outgoingN);assert(reverseChart);
for(const a of annotated)assert.deepEqual(a.routes.flatMap(r=>[r.targetP,r.targetE]).sort(),
 [...reverseReading.outer.map(o=>o.cell),...reverseChart.comparisons.map(c=>c.cell)].sort());
// The fixture's reading.comparisons is a whole-depth comparison-domain table,
// not the four entry sites. Query the actual obligation source for their status.
const obligations=buildFiveSideOctRoutingObligations(buildPESymmetricSector(1));
const nativeEntry=obligations.readings.find(r=>r.id===reading.id);
assert.deepEqual(nativeEntry.comparisons.map(c=>c.cell).sort(),built.comparisons.map(c=>c.at).sort());
for(const c of nativeEntry.comparisons){assert.equal(c.comparisonWitness,null);assert.equal(c.outputPairing,null);}
const sources=[fixturePath,middlePath,'research/strominger/sulfur-32-reversible-channel-specification.md',
 'research/realization-tower/five-side-oct-routing-obligations.mjs',
 'research/strominger/checkers/check_sulfur32_middle_layer.mjs',
 'research/strominger/su32-layer4-comparison.mjs','research/strominger/su32-signed-reference-encoder.mjs',
 'research/strominger/checkers/check_su32_fixed_reading_trace.mjs'];
const hashes={};for(const p of sources)hashes[p]=createHash('sha256').update(await fs.readFile(p)).digest('hex');
const report={schema:'su32.fixed-reading-reference-trace.v1',passed:true,reading:reading.id,binding:[0,0],
 incomingN:reading.incomingN,outgoingN,registry,layer2,layer3,layer4,
 centralReconciliation:{cell:chart.target,byE:built.byE,byP:built.byP,recordsRecovered:true,
  scope:'Candidate central join, not a replacement for eight outer branches or a completed middle route.'},
 middleAssignments:annotated,
 nativeComparisonSites:nativeEntry.comparisons.map(({cell,status,comparisonWitness,outputPairing})=>({cell,status,comparisonWitness,outputPairing})),
 firstMissingNativeOperation:'The obligation source already marks layer4 comparisonWitness and outputPairing null. The lossless join is a tested candidate, not a source-derived native operation.',
 firstMissingExtensionOfBaseline:'A joint layer4-to-layer5-to-layer6 signed-record/occurrence map, including the chosen complete routing and compatibility with central reconciliation and retained outer views.',
 stoppedBefore:'No target payload, output signed-pair assignment or full outgoing trace is invented from reflection.',
 conclusion:'The fixed-reading reference prefix is consistent. Four complete geometric middle covers remain; none supplies the missing native record continuation.',sourceHashes:hashes};
const dir='research/strominger/results/su32-fixed-reading-trace-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({passed:report.passed,reading:report.reading,incomingN:reading.incomingN,outgoingN,
 layers:{referenceCells:layer2.length,jointChannels:layer3.length,outerViews:reading.outer.length,comparisonCandidates:built.comparisons.length},
 middleAssignments:annotated.map(a=>({index:a.index,supportSizes:a.routes.map(r=>r.availableRecordLabels.length),middleOperationsBound:0})),
 firstMissingNativeOperation:report.firstMissingNativeOperation,firstMissingExtensionOfBaseline:report.firstMissingExtensionOfBaseline,conclusion:report.conclusion},null,2));
