// Observation-relative state audit, not a new physical state or transport API.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,reconcileBothOrders,compareAt,reconcileAt,readRecords} from '../su32-layer4-comparison.mjs';
import {prepareCentralReferencePacket,selectCentralReference,currentCentralReferenceState,
 centralReferenceHistory,centralReferenceBoundary,validateCentralReferencePacket} from '../su32-central-reference-completion.mjs';
const fixturePath='research/strominger/results/su32-hopf-tests-v1/fixture.json';
const fixture=JSON.parse(await fs.readFile(fixturePath,'utf8'));
const hash=x=>createHash('sha256').update(x).digest('hex');
for(const [p,h] of Object.entries(fixture.sourceHashes))assert.equal(hash(await fs.readFile(p)),h);
const atlas=buildSu32SignedReferenceAtlas(fixture),reading=fixture.readings.find(r=>r.id==='reading:0:-1');
const chart=atlas.charts.find(c=>c.reading===reading.id&&c.source===reading.incomingN);assert(chart);
const labels=['P+','P-','E+','E-'];
const registries=[...Array.from({length:16},(_,bits)=>Object.fromEntries(labels.map((k,i)=>[k,(bits>>i)&1]))),
 Object.fromEntries(labels.map((k,i)=>[k,{id:k,value:i}]))];
const words=[[],['E+'],['E-'],['E+','E+'],['E+','E-'],['E-','E+'],['E-','E-']];
const run=(layout,p,word)=>word.reduce((state,r)=>selectCentralReference(layout,state,r),p);
// This is an explicitly REDUCED observation, not an existing full-state API.
const dataObservation=p=>structuredClone({anchor:p.core.anchor,at:p.core.at,records:p.core.records,activeReference:p.activeReference});
const sortedJSON=x=>JSON.stringify(x,(_,v)=>v&&typeof v==='object'&&!Array.isArray(v)?Object.fromEntries(Object.entries(v).sort(([a],[b])=>a.localeCompare(b))):v);
let preparations=0,logErasureCurrentStateChecks=0,derivationDataAgreementChecks=0,derivationCurrentStateDistinctions=0;let example;
for(const p of [0,1])for(const e of [0,1]){
 const layout=comparisonLayout(atlas,fixture,chart.id,[p,e]);
 for(const registry of registries){
  const built=reconcileBothOrders(layout,registry);
  const start=prepareCentralReferencePacket(layout,built.byE,built.byP);
  const returned=run(layout,start,['E-','E+']);
  assert.notDeepEqual(centralReferenceHistory(layout,start),centralReferenceHistory(layout,returned));
  const plus=layout.template.comparisons.find(c=>c.sharedRecord==='E+');
  const changedChildren=built.byE.children.map(c=>c.at===plus.cell?compareAt(layout,c.at,...[...c.children].reverse()):c);
  const changedE=reconcileAt(layout,...changedChildren);
  const otherDerivation=prepareCentralReferencePacket(layout,changedE,built.byP);
  assert.deepEqual(dataObservation(start),dataObservation(otherDerivation));
  assert.notDeepEqual(start.view.sourceComparison,otherDerivation.view.sourceComparison);
  for(const word of words){
   const a=run(layout,start,word),b=run(layout,returned,word),c=run(layout,otherDerivation,word);
   assert.deepEqual(currentCentralReferenceState(layout,a),currentCentralReferenceState(layout,b));logErasureCurrentStateChecks++;
   assert.notDeepEqual(centralReferenceHistory(layout,a),centralReferenceHistory(layout,b));
   assert.deepEqual(dataObservation(a),dataObservation(c));derivationDataAgreementChecks++;
   assert.deepEqual(readRecords(layout,a.core.derivations.byE),readRecords(layout,c.core.derivations.byE));
   assert.deepEqual(centralReferenceBoundary(layout,a),centralReferenceBoundary(layout,c));
   assert.notDeepEqual(currentCentralReferenceState(layout,a),currentCentralReferenceState(layout,c));derivationCurrentStateDistinctions++;
   assert.deepEqual(centralReferenceHistory(layout,a),centralReferenceHistory(layout,c));
  }
  preparations++;
  if(!example&&registry['P+']?.id)example={layout,built,start,returned,otherDerivation};
 }
}
const {layout,built,start,returned,otherDerivation}=example;
// Exhaust the ENTIRE permitted ordering freedom at fixed records and anchor:
// two child swaps and one root swap per reconciliation route = 3+3 bits.
function routeVariant(route,bits){
 const children=route.children.map((c,i)=>compareAt(layout,c.at,...((bits>>i)&1?[...c.children].reverse():c.children)));
 return reconcileAt(layout,...((bits>>2)&1?children.reverse():children));
}
const cores=new Set(),currentStates=new Set(),reducedStates=new Set();
for(let e=0;e<8;e++)for(let p=0;p<8;p++)for(const ref of ['E+','E-']){
 const packet=prepareCentralReferencePacket(layout,routeVariant(built.byE,e),routeVariant(built.byP,p),ref);
 assert(validateCentralReferencePacket(layout,packet));
 assert.deepEqual(packet.core.records,start.core.records);
 cores.add(sortedJSON(packet.core));currentStates.add(sortedJSON(currentCentralReferenceState(layout,packet)));
 reducedStates.add(sortedJSON(dataObservation(packet)));
}
assert.equal(cores.size,64);assert.equal(currentStates.size,128);assert.equal(reducedStates.size,2);
// These are task-relevant distinctions in the candidate API, not physical laws.
const selectedMinus=prepareCentralReferencePacket(layout,built.byE,built.byP,'E-');
assert.deepEqual(start.core,selectedMinus.core);assert.notDeepEqual(start.view.reference,selectedMinus.view.reference);
// An omitted complement becomes visible under an already supplied selection.
const zero=Object.fromEntries(labels.map(k=>[k,0])),one={...zero,'E-':1};
const packetFor=records=>{const b=reconcileBothOrders(layout,records);return prepareCentralReferencePacket(layout,b.byE,b.byP);};
const a=packetFor(zero),b=packetFor(one);
assert.deepEqual(a.view.activePair,b.view.activePair);assert.deepEqual(a.view.reference,b.view.reference);
assert.notDeepEqual(selectCentralReference(layout,a,'E-').view.reference,selectCentralReference(layout,b,'E-').view.reference);
// Equivalences above apply only AFTER full admission. They do not authorize
// erasing validation evidence from current API inputs.
let negativeControls=0;const reject=f=>{assert.throws(f);negativeControls++;};
const stripped=structuredClone(start);delete stripped.core.derivations;
reject(()=>validateCentralReferencePacket(layout,stripped));
const badLog=structuredClone(returned);badLog.operation.from='E+';
assert.deepEqual(dataObservation(badLog),dataObservation(returned));
reject(()=>validateCentralReferencePacket(layout,badLog));
const wrongAttachment=structuredClone(start);wrongAttachment.core.records['P+'].referenceCell='absent';
reject(()=>validateCentralReferencePacket(layout,wrongAttachment));
reject(()=>validateCentralReferencePacket(comparisonLayout(atlas,fixture,chart.id,[1,1]),start));
const paths=[fixturePath,'research/strominger/su32-signed-reference-encoder.mjs','research/strominger/su32-layer4-comparison.mjs',
 'research/strominger/su32-central-reference-completion.mjs','research/strominger/su32-rooted-comparison-gluing.mjs',
 'research/strominger/su32-undirected-reference-attachment.mjs','research/strominger/su32-central-outgoing-face-offer.mjs',
 'research/strominger/checkers/check_su32_native_continuation_audit.mjs','research/nima/generative-phase-assembly.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs',
 'research/strominger/checkers/check_su32_state_observation_boundary.mjs'];
const sourceHashes={};for(const path of paths)sourceHashes[path]=hash(await fs.readFile(path));
const report={schema:'su32.state-observation-boundary.v1',passed:true,preparations,
 logErasureCurrentStateChecks,derivationDataAgreementChecks,derivationCurrentStateDistinctions,
 fixedDataCensus:{derivationCores:cores.size,fullCurrentStates:currentStates.size,reducedRecordReferenceStates:reducedStates.size,
  structuralArgument:'At fixed validated layout/records, every channel is determined. Each of four comparison nodes has two child orders; each of two reconciliation roots has two child orders. Both routes together have exactly 2^6 derivations; two active references give 2^7 current states.'},
 negativeControls,example:{start,returned,otherDerivation},
 observationContracts:{currentAPI:'Full currentCentralReferenceState after any finite word of valid E-reference selections. Parent logs are observationally redundant on validated inputs; retained derivations are not.',
  reducedData:'Records with attachments, occurrence and activeReference after those selections. Derivations and parent logs are redundant for this explicitly restricted observation, not for the full API.',
  exactPacket:'Includes parent log and derivation trees; no history quotient is lossless for this task.',
  nativePhysics:'No source-bound subsequent native operation on these packets has been supplied; no physical equivalence or history-erasure law is established.'},
 allWordArgument:'selectCentralReference leaves the complete core fixed and sets the current reference/view from that core and its target label, without consulting prior selection history for the new current state. Induction extends the current-state agreement beyond the tested words; validators still require valid complete histories.',
 nativeStateContract:null,limits:['No physical payload alphabet, precision bound, or native receiver encoding is derived.',
  'The 6 ordering bits describe existing syntax distinctions, not new physical degrees of freedom.',
  'No stored histories were erased and no production packet API was changed.',
  'The finite numerical receiver obstruction remains for arbitrary admitted JSON payloads; the observation contract must be fixed before applying it to a physical task.'],sourceHashes};
const dir='research/strominger/results/su32-state-observation-boundary-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,example:undefined,sourceHashes:undefined},null,2));
