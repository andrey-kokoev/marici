import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,channelOperand,compareAt,reconcileBothOrders,readRecords,validateComparisonNode} from '../su32-layer4-comparison.mjs';
const fixturePath='research/strominger/results/su32-hopf-tests-v1/fixture.json';
const fixture=JSON.parse(await fs.readFile(fixturePath,'utf8'));
for(const [path,hash] of Object.entries(fixture.sourceHashes))assert.equal(createHash('sha256').update(await fs.readFile(path)).digest('hex'),hash);
const atlas=buildSu32SignedReferenceAtlas(fixture),labels=['P+','P-','E+','E-'];
const registry=bits=>Object.fromEntries(labels.map((k,i)=>[k,(bits>>i)&1]));
let cases=0,comparisonChecks=0,outerChecks=0,phaseChecks=0;let example;
for(const chart of atlas.charts)for(const p of [0,1])for(const e of [0,1]){
 const layout=comparisonLayout(atlas,fixture,chart.id,[p,e]);
 for(let bits=0;bits<16;bits++){
  const records=registry(bits),before=JSON.stringify(records),built=reconcileBothOrders(layout,records);
  assert.deepEqual(readRecords(layout,built.byE),records);assert.deepEqual(readRecords(layout,built.byP),records);
  assert.deepEqual(readRecords(layout,JSON.parse(JSON.stringify(built.byE))),records);
  for(const c of built.comparisons){assert.equal(Object.keys(c.records).length,3);assert.equal(c.children.length,2);comparisonChecks++;}
  assert.equal(JSON.stringify(records),before);cases++;
  const reading=fixture.readings.find(r=>r.id===chart.reading);
  if(chart.source===reading.incomingN)for(const outer of reading.outer){
   const view=built.channels[outer.input];assert(view);
   const again=channelOperand(layout,outer.input,records);assert.deepEqual(view,again);outerChecks++;
  }
  if(!example&&bits===6)example={layout,built};
 }
 // No complex structure is required by join. Two phase laws remain compatible.
 const amplitudes={'P+':[1,0],'P-':[0,1],'E+':[2,1],'E-':[1,-1]};
 const rotate=([x,y])=>[-y,x].map(x=>x===0?0:x);
 const common=Object.fromEntries(labels.map(k=>[k,rotate(amplitudes[k])]));
 const independent={...amplitudes,'E+':rotate(amplitudes['E+'])};
 const base=reconcileBothOrders(layout,amplitudes),joint=reconcileBothOrders(layout,common),separate=reconcileBothOrders(layout,independent);
 assert.deepEqual(readRecords(layout,joint.byE),common);assert.deepEqual(readRecords(layout,separate.byP),independent);
 assert.notDeepEqual(joint.byE.records,separate.byE.records);
 for(const result of [base,joint,separate])assert.deepEqual(result.byE.records,result.byP.records);
 phaseChecks++;
}
const {layout,built}=example;
const sharedE=layout.template.comparisons.find(c=>c.sharedRecord==='E+');assert(sharedE);
const leftId=sharedE.inputs.find(id=>layout.template.channels.find(c=>c.cell===id).P.record==='P+');
const rightId=sharedE.inputs.find(id=>id!==leftId);
const r0=registry(0),r1={...r0,'P-':1};
const x0=channelOperand(layout,leftId,r0),x1=channelOperand(layout,leftId,r1);
const y0=channelOperand(layout,rightId,r0),y1=channelOperand(layout,rightId,r1);
assert.deepEqual(x0,x1);assert.notDeepEqual(y0,y1); // No left-view-only function yields right.
const validTriples=[];for(let p=0;p<2;p++)for(let q=0;q<2;q++)for(let e=0;e<2;e++)validTriples.push([p,q,e]);
assert.equal(validTriples.length,8);assert.equal(validTriples.filter(([p,q])=>p===q).length,4);
const badShared=structuredClone(y0);badShared.records['E+'].payload=1;
assert(validateComparisonNode(layout,badShared));
assert.throws(()=>compareAt(layout,sharedE.cell,x0,badShared));
const mutations={
 wrongReferenceIdentity:n=>{n.children[0].children[0].records[Object.keys(n.children[0].children[0].records)[0]].referenceCell='absent';},
 discardedOperand:n=>{n.children[0].children.pop();},
 erasedComparisonHistory:n=>{n.children=[];},
 alteredResult:n=>{n.records['P+'].payload='edited';},
 wrongCentralN:n=>{n.at='absent';},
 wrongReading:n=>{n.anchor.chartId='absent';}
};
for(const mutate of Object.values(mutations)){const node=structuredClone(built.byE);mutate(node);assert.throws(()=>validateComparisonNode(layout,node));}
const sources=[fixturePath,'research/strominger/sulfur-32-reversible-channel-specification.md','research/strominger/internal-source-comparison-and-interchange-v1.md','research/strominger/canonical-comparison-synthesis-v1.md','research/strominger/native-reader-comparison-v1.md','research/strominger/su32-signed-reference-encoder.mjs','research/strominger/su32-layer4-comparison.mjs','research/strominger/checkers/check_su32_layer4_comparison.mjs'];
const sourceHashes={};for(const path of sources)sourceHashes[path]=createHash('sha256').update(await fs.readFile(path)).digest('hex');
const report={schema:'su32.layer4-comparison.v1',passed:true,classification:'lossless shared-record fiber-product candidate; two-order data agreement with retained distinct derivations',
 charts:atlas.charts.length,bindingsPerChart:4,booleanAssignmentsPerChart:16,cases,comparisonChecks,outerChecks,phaseChecks,
 referenceOnlyEquivalenceRefuted:{sameLeftOperands:[x0,x1],differentRightOperands:[y0,y1],fiberProductBooleanSize:8,wholeOperandEqualityBooleanSize:4},
 negativeControls:['valid operands with incompatible shared payload rejected',...Object.keys(mutations)],
 example:{chartId:layout.chart.id,source:layout.chart.source,target:layout.chart.target,byE:built.byE,byP:built.byP},sourceHashes,
 nativeFiller:null,nativeHopfBinding:false,crossConePayloadTransport:null,
 residuals:['Candidate is a set-valued information-preserving operation, not a derived physical interaction','Existing Agda equivalence compiler was inspected, not applied to this different operand type','No phase law or spin lift is selected by reference joins','Actual continuation and cross-cone payload transport still require source operations'],
 next:'Compare any proposed physical layer-4 law against both projections of this lossless baseline and test its extra phase-sensitive readout; do not infer a nontrivial Hopf class from the reference join.'};
if(process.argv.includes('--record')){const dir='research/strominger/results/su32-layer4-comparison-v1';await fs.mkdir(dir,{recursive:true});await fs.writeFile(`${dir}/verification.json`,JSON.stringify(report,null,2)+'\n');}
console.log(JSON.stringify(Object.fromEntries(Object.entries(report).filter(([k])=>!['sourceHashes','example','referenceOnlyEquivalenceRefuted'].includes(k))),null,2));
