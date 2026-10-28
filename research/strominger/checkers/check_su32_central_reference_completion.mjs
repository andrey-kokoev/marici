import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildFiveSideOctComparisonDomain} from '../../realization-tower/five-side-oct-comparison-domain.mjs';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,reconcileBothOrders} from '../su32-layer4-comparison.mjs';
import {prepareCentralReferencePacket,selectCentralReference,validateCentralReferencePacket,
 currentCentralReferenceState,centralReferenceHistory,centralReferenceBoundary} from '../su32-central-reference-completion.mjs';
const fixturePath='research/strominger/results/su32-hopf-tests-v1/fixture.json';
const fixture=JSON.parse(await fs.readFile(fixturePath,'utf8'));
for(const [p,h] of Object.entries(fixture.sourceHashes))assert.equal(createHash('sha256').update(await fs.readFile(p)).digest('hex'),h);
const reading=fixture.readings.find(r=>r.id==='reading:0:-1'),atlas=buildSu32SignedReferenceAtlas(fixture);
const chart=atlas.charts.find(c=>c.reading===reading.id&&c.source===reading.incomingN);assert(chart);
const domain=buildFiveSideOctComparisonDomain(buildPESymmetricSector(1),{readingIds:[reading.id]}).readings[0];
const labels=['P+','P-','E+','E-'],references=['E+','E-'];
const booleanRecords=bits=>Object.fromEntries(labels.map((k,i)=>[k,(bits>>i)&1]));
const tagged=Object.fromEntries(labels.map((k,i)=>[k,{id:'input:'+k,value:{index:i},provenance:{entry:reading.incomingN,label:k}}]));
let cases=0,compositionChecks=0,roundTrips=0,boundaryChecks=0;let example;
const sites=(layout,packet)=>domain.arrows.filter(e=>e.from===centralReferenceBoundary(layout,packet).at);
for(const p of [0,1])for(const e of [0,1]){
 const layout=comparisonLayout(atlas,fixture,chart.id,[p,e]);
 for(const records of [...Array.from({length:16},(_,i)=>booleanRecords(i)),tagged]){
  const built=reconcileBothOrders(layout,records),before=structuredClone(built);
  for(const initial of references){
   const start=prepareCentralReferencePacket(layout,built.byE,built.byP,initial),snapshot=structuredClone(start);
   assert.equal(sites(layout,start).length,4);
   assert(Object.isFrozen(start));assert(Object.isFrozen(start.core.records));
   assert.deepEqual(start.core.derivations,{byE:built.byE,byP:built.byP});
   for(const target of references){
    const changed=selectCentralReference(layout,start,target),returned=selectCentralReference(layout,changed,initial);
    assert.deepEqual(changed.view.activePair,start.view.activePair);
    assert.deepEqual(changed.core,start.core);
    assert.deepEqual(currentCentralReferenceState(layout,returned),currentCentralReferenceState(layout,start));
    assert.notDeepEqual(returned,start);assert.equal(centralReferenceHistory(layout,returned).length,2);roundTrips++;
    assert.deepEqual(centralReferenceBoundary(layout,changed),centralReferenceBoundary(layout,start));
    assert.deepEqual(sites(layout,changed),sites(layout,start));boundaryChecks++;
    assert.equal(changed.view.reference.record.referenceCell,changed.core.records[target].referenceCell);
    assert.equal(changed.view.sourceComparison.at,layout.template.comparisons.find(c=>c.sharedRecord===target).cell);
    for(const last of references){
     const staged=selectCentralReference(layout,changed,last),direct=selectCentralReference(layout,start,last);
     assert.deepEqual(currentCentralReferenceState(layout,staged),currentCentralReferenceState(layout,direct));
     assert.equal(centralReferenceHistory(layout,staged).length,2);assert.equal(centralReferenceHistory(layout,direct).length,1);
     assert.deepEqual(staged.parent,changed);assert.deepEqual(staged.parent.parent,start);compositionChecks++;
    }
   }
   assert.deepEqual(start,snapshot);
   if(!example&&records===tagged&&initial==='E+')example={layout,start,built};
  }
  assert.deepEqual(built,before);cases++;
 }
}
const {layout,start,built}=example;let refusals=0;
const reject=fn=>{assert.throws(fn);refusals++;};
const corrupt=fn=>{const bad=structuredClone(start);fn(bad);reject(()=>validateCentralReferencePacket(layout,bad));};
reject(()=>selectCentralReference(layout,built.comparisons[0],'E-'));
reject(()=>selectCentralReference(layout,start,'P+'));
corrupt(p=>{delete p.core.records['E-'];});
corrupt(p=>{p.view.activePair['P+'].payload={invented:true};});
corrupt(p=>{p.view.complement.record.payload={invented:true};});
corrupt(p=>{p.view.at=p.view.sourceComparison.at;});
corrupt(p=>{p.core.anchor.binding=[1,1];});
corrupt(p=>{p.core.derivations.byP=structuredClone(p.core.derivations.byE);});
corrupt(p=>{p.view.sourceComparison.children.reverse();});
const changed=selectCentralReference(layout,start,'E-');
const badStep=structuredClone(changed);badStep.operation.from='E-';reject(()=>validateCentralReferencePacket(layout,badStep));
const foreign=reconcileBothOrders(layout,{...tagged,'E-':{independent:'different'}});
const badParent=structuredClone(changed);badParent.parent=prepareCentralReferencePacket(layout,foreign.byE,foreign.byP,'E+');
reject(()=>validateCentralReferencePacket(layout,badParent));
const cyclic=structuredClone(changed);cyclic.parent=cyclic;cyclic.operation.from='E-';
reject(()=>validateCentralReferencePacket(layout,cyclic));
// A validated mutable input is snapshotted, not frozen or subsequently aliased.
const mutable=structuredClone(start),snapshot=structuredClone(mutable),snapshotChild=selectCentralReference(layout,mutable,'E-');
assert(!Object.isFrozen(mutable));assert.deepEqual(mutable,snapshot);
mutable.core.records['E-'].payload={changedAfterSelection:true};assert.deepEqual(snapshotChild.parent,snapshot);
// Information-theoretic refusal witness: SAME COMPLETE E+ comparison tree,
// different needed E- reference. No local-view-only function can do this task.
const zero=booleanRecords(0),one={...zero,'E-':1};
const a=reconcileBothOrders(layout,zero),b=reconcileBothOrders(layout,one);
const cell=layout.template.comparisons.find(c=>c.sharedRecord==='E+').cell;
assert.deepEqual(a.comparisons.find(c=>c.at===cell),b.comparisons.find(c=>c.at===cell));
const targetA=selectCentralReference(layout,prepareCentralReferencePacket(layout,a.byE,a.byP),'E-');
const targetB=selectCentralReference(layout,prepareCentralReferencePacket(layout,b.byE,b.byP),'E-');
assert.notDeepEqual(targetA.view.reference.record.payload,targetB.view.reference.record.payload);
// Consistent local renaming must not change the physical references or data.
// This is stronger than merely running four independent binding choices.
let relabellingChecks=0;
for(const p of [0,1])for(const e of [0,1]){
 const rename=k=>k[0]+(((k[1]==='+')!==Boolean(k[0]==='P'?p:e))?'+':'-');
 const rekey=r=>Object.fromEntries(Object.entries(r).map(([k,v])=>[rename(k),structuredClone(v)]));
 const renamedLayout=comparisonLayout(atlas,fixture,chart.id,[p,e]);
 const renamedBuilt=reconcileBothOrders(renamedLayout,rekey(tagged));
 const renamed=selectCentralReference(renamedLayout,
  prepareCentralReferencePacket(renamedLayout,renamedBuilt.byE,renamedBuilt.byP,rename('E+')),rename('E-'));
 assert.deepEqual(renamed.core.records,rekey(changed.core.records));
 assert.deepEqual(renamed.view.activePair,rekey(changed.view.activePair));
 assert.deepEqual(renamed.view.reference.record,changed.view.reference.record);
 assert.deepEqual(renamed.view.complement.record,changed.view.complement.record);
 assert.equal(renamed.view.sourceComparison.at,changed.view.sourceComparison.at);
 assert.equal(renamed.view.at,changed.view.at);relabellingChecks++;
}
const sources=[fixturePath,'research/strominger/su32-central-reference-completion.mjs',
 'research/strominger/su32-layer4-comparison.mjs','research/strominger/su32-signed-reference-encoder.mjs',
 'research/realization-tower/five-side-oct-comparison-domain.mjs',
 'research/strominger/checkers/check_su32_central_reference_completion.mjs'];
const hashes={};for(const p of sources)hashes[p]=createHash('sha256').update(await fs.readFile(p)).digest('hex');
const report={schema:'su32.central-reference-completion-candidate.v1',passed:true,reading:reading.id,cases,
 compositionChecks,roundTrips,boundaryChecks,relabellingChecks,negativeControls:refusals,
 contract:{inputs:'Both validated reconciliation trees at the same central N and binding; E+ or E- selection.',
  state:'Complete four-record core plus selected P/P contextual view and immutable parent versions.',
  identityAndComposition:'Equality of current state, not equality of logged construction histories.',
  attachment:'Central occurrence and its four outgoing geometric interfaces remain unchanged. No outgoing operation is implemented.'},
 example:{initial:start,changed,geometricNextSites:sites(layout,start)},
 refusalWitness:{sourceEPlusViewsEqual:true,changedIndependentRecord:'E-',requiredEminusViewsDifferent:true},
 nativeBindings:{coefficientOrDGAdapter:null,comparisonCompilerAdapter:null,nativeFiller:null,physicalContinuation:null},
 limits:['An explicit proposed information-level completion, not recovered native dynamics.',
  'Complete-core availability is a constructor precondition, not inferred from an isolated ternary view.',
  'Both supplied derivations are retained; neither is asserted to be an executed physical history.',
  'The active P/P pair is invariant; the selected E context changes. Full active-view equality is not required.',
  'No circular order, phase action, temporal reversal, global middle routing or outgoing payload law is supplied.'],sourceHashes:hashes};
const dir='research/strominger/results/su32-central-reference-completion-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,example:undefined,sourceHashes:undefined},null,2));
