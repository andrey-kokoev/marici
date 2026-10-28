// Source-to-record gate: distinguish native references from supplied values.
// No measurement map, amplitude interpretation, or physical alphabet invented.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSu32SignedReferenceAtlas,encodeSignedReferences,decodeSignedReferences,mapReferencePayloads} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,reconcileBothOrders,readRecords} from '../su32-layer4-comparison.mjs';
const fixturePath='research/strominger/results/su32-hopf-tests-v1/fixture.json';
const fixture=JSON.parse(await fs.readFile(fixturePath,'utf8'));
const hash=x=>createHash('sha256').update(x).digest('hex');
for(const [p,h] of Object.entries(fixture.sourceHashes))assert.equal(hash(await fs.readFile(p)),h);
const atlas=buildSu32SignedReferenceAtlas(fixture),reading=fixture.readings.find(r=>r.id==='reading:0:-1');
const chart=atlas.charts.find(c=>c.reading===reading.id&&c.source===reading.incomingN);assert(chart);
const binding=[0,0],layout=comparisonLayout(atlas,fixture,chart.id,binding),labels=['P+','P-','E+','E-'];
const skeleton=packet=>{const {records,...rest}=packet;return rest;};
const zero=Object.fromEntries(labels.map(k=>[k,0]));
const baseline=encodeSignedReferences(atlas,chart.id,binding,zero),geometry=structuredClone(skeleton(baseline));
// Native attachment identities are populated without interpreting payloads.
const identities=Object.fromEntries(Object.entries(baseline.referenceBinding).map(([cell,label])=>[label,
 {occurrence:{chartId:chart.id,binding},referenceCell:cell,geometricRole:atlas.roles[cell]}]));
assert.equal(new Set(Object.values(identities).map(r=>r.referenceCell)).size,4);
for(const label of labels)assert.equal(identities[label].geometricRole,label[0]==='P'?'proton':'electron');
let booleanAssignments=0,singleSlotVariations=0;
for(let bits=0;bits<16;bits++){
 const records=Object.fromEntries(labels.map((k,i)=>[k,(bits>>i)&1]));
 const packet=encodeSignedReferences(atlas,chart.id,binding,records),built=reconcileBothOrders(layout,records);
 assert.deepEqual(skeleton(packet),geometry);assert.deepEqual(decodeSignedReferences(atlas,packet),records);
 assert.deepEqual(readRecords(layout,built.byE),records);assert.deepEqual(readRecords(layout,built.byP),records);
 for(const label of labels){
  const appearances=Object.values(built.channels).filter(c=>Object.hasOwn(c.records,label));
  assert.equal(appearances.length,2);
  for(const channel of appearances){assert.equal(channel.records[label].referenceCell,identities[label].referenceCell);assert.equal(channel.records[label].payload,records[label]);}
  const changed=mapReferencePayloads(atlas,packet,(value,key)=>key===label?1-value:value);
  assert.deepEqual(skeleton(changed),geometry);
  const next=decodeSignedReferences(atlas,changed);
  assert.equal(labels.filter(k=>next[k]!==records[k]).length,1);
  assert.deepEqual(readRecords(layout,reconcileBothOrders(layout,next).byE),next);singleSlotVariations++;
 }
 booleanAssignments++;
}
const examples=[zero,Object.fromEntries(labels.map(k=>[k,1])),
 {'P+':null,'P-':false,'E+':'opaque supplied value','E-':{retained:['input',3]}},
 Object.fromEntries(labels.map(k=>[k,'equal-content']))];
const packets=examples.map(records=>{
 const packet=encodeSignedReferences(atlas,chart.id,binding,records);
 assert.deepEqual(skeleton(packet),geometry);
 const built=reconcileBothOrders(layout,records);assert.deepEqual(readRecords(layout,built.byE),records);
 return packet;
});
assert.notDeepEqual(packets[0].records,packets[1].records);
// Distinct reference identities do not require distinct values.
assert.equal(new Set(Object.values(packets[3].records)).size,1);
assert.equal(Object.keys(packets[3].referenceBinding).length,4);
// A callback can change every payload without changing any source attachment.
// This is API-parametricity, NOT a physically admitted transformation law.
const arbitraryMap=mapReferencePayloads(atlas,baseline,(value,label)=>({suppliedBy:'test callback',label,previous:value}));
assert.deepEqual(skeleton(arbitraryMap),geometry);
assert.deepEqual(readRecords(layout,reconcileBothOrders(layout,arbitraryMap.records).byP),arbitraryMap.records);
let negativeControls=0;const reject=f=>{assert.throws(f);negativeControls++;};
reject(()=>encodeSignedReferences(atlas,chart.id,binding));
reject(()=>encodeSignedReferences(atlas,chart.id,binding,{'P+':0,'P-':0,'E+':0}));
reject(()=>encodeSignedReferences(atlas,chart.id,binding,{...zero,'extra':0}));
reject(()=>encodeSignedReferences(atlas,chart.id,binding,{...zero,'P+':Infinity}));
const bad=structuredClone(baseline);bad.channels[0].P.referenceCell='absent';
reject(()=>decodeSignedReferences(atlas,bad));
const sourcePaths=[fixturePath,'research/strominger/sulfur-32-reversible-channel-specification.md',
 'research/strominger/su32-signed-reference-encoder.mjs','research/strominger/su32-layer4-comparison.mjs',
 'research/strominger/checkers/check_su32_signed_reference_encoder.mjs',
 'research/realization-tower/sulfur-32-wiring.mjs','research/strominger/su32-native-continuation-audit-v1.md',
 'research/strominger/checkers/check_su32_record_source_contract.mjs'];
const sourceHashes={};for(const p of sourcePaths)sourceHashes[p]=hash(await fs.readFile(p));
const report={schema:'su32.record-source-contract-audit.v1',passed:true,reading:reading.id,chart:chart.id,binding,
 identities,booleanAssignments,singleSlotVariations,negativeControls,
 fixedIncidenceDifferentValues:{sameCompleteReferenceSkeleton:true,examples:packets},
 sourceContracts:{operatorSpecification:'Signs distinguish directions. Wire content transformation, amplitudes and charges are not supplied.',
  signedEncoder:'records is a required caller argument. The atlas computes reference attachments, not payload values.',
  layer4:'channelOperand receives a registry; compareAt/reconcileAt retain and check shared records. They do not measure source geometry.',
  periodicWireAPI:'groupSulfurPayloads receives a complete externally supplied 64-wire row assignment; no binding from coordinate-axis wire slots to the four directional records is supplied.',
  oldAmplitudeTests:'The encoder checker explicitly labels complex-looking payloads as test fixtures and sourceSelectedAction as null.'},
 interpretation:{whatRecordsAre:'Four occurrence-relative directional record identities with externally supplied opaque contents; not four source-defined scalar observables.',
  nativeAssignment:'The geometry-to-reference assignment exists. A native-state-to-payload assignment was not found in these audited producer contracts.',
  admissibility:'The candidate API accepts JSON data under the exact four labels and requires equal repeated appearances. It supplies no physical joint-state law.',
  independence:'Independent caller variation is verified in the information API; physical or statistical independence is not established.',
  underdetermination:'The same incidence/reference skeleton accepts different registries. This refutes determination by those constraints, not existence of a map from a richer specified native state.'},
 missingContract:{nativeStateDomain:null,nativeStateToRecords:null,physicalJointAdmissibility:null,physicalIndependenceLaw:null},
 proposedNextAdmissionGate:'Supply a native state domain and an authoritative observation/retention map at this fixed occurrence, then check reference preservation and joint admissibility. Do not infer payloads from direction signs or arbitrary geometry functions.',
 limits:['Fixed occurrence and binding; no global sign assignment or routing extension is generated.',
  'This is a bounded source-contract audit, not proof that no possible native assignment exists.',
  'Test values are API probes, not physically prepared states or measured amplitudes.',
  'No new record encoder, payload interpretation or transport wrapper was installed.'],sourceHashes};
const dir='research/strominger/results/su32-record-source-contract-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,fixedIncidenceDifferentValues:undefined,sourceHashes:undefined},null,2));
