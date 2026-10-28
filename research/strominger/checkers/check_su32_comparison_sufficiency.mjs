// Task-relative sufficiency/ablation audit, not a new native dynamics model.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,reconcileBothOrders,readRecords,channelOperand,compareAt} from '../su32-layer4-comparison.mjs';
const labels=['P+','P-','E+','E-'];
const fixturePath='research/strominger/results/su32-hopf-tests-v1/fixture.json';
const fixture=JSON.parse(await fs.readFile(fixturePath,'utf8'));
for(const [p,h] of Object.entries(fixture.sourceHashes))assert.equal(createHash('sha256').update(await fs.readFile(p)).digest('hex'),h);
const atlas=buildSu32SignedReferenceAtlas(fixture);
const registry=bits=>Object.fromEntries(labels.map((k,i)=>[k,(bits>>i)&1]));
const omit=(r,k)=>Object.fromEntries(Object.entries(r).filter(([s])=>s!==k));
let cases=0,reconstructedHistories=0,sharedConflicts=0,droppedRecordWitnesses=0,bindingWitnesses=0;
let example;
for(const chart of atlas.charts)for(const p of [0,1])for(const e of [0,1]){
 const layout=comparisonLayout(atlas,fixture,chart.id,[p,e]);
 for(let bits=0;bits<16;bits++){
  const r=registry(bits),built=reconcileBothOrders(layout,r);
  // No inspection of child histories is needed to recover either result's values.
  assert.deepEqual(readRecords(layout,built.byE),r);assert.deepEqual(readRecords(layout,built.byP),r);
  assert.deepEqual(built.byE.records,built.byP.records);
  // A compact representation reconstructs the exact TWO CANONICAL constructor
  // outputs; this is not a codec for arbitrary histories or permuted AST children.
  for(const route of ['byE','byP']){
   const compact=JSON.parse(JSON.stringify({anchor:layout.anchor,records:r,route}));
   const restoredLayout=comparisonLayout(atlas,fixture,compact.anchor.chartId,compact.anchor.binding);
   const restored=reconcileBothOrders(restoredLayout,compact.records)[compact.route];
   assert.deepEqual(restored,built[route]);reconstructedHistories++;
  }
  // Information-theoretic counterexamples, not validator schema failures:
  // deleting ANY independent record identifies two required, distinct outputs.
  for(let i=0;i<4;i++){
   const other=registry(bits^(1<<i));assert.deepEqual(omit(r,labels[i]),omit(other,labels[i]));
   assert.notDeepEqual(r,other);droppedRecordWitnesses++;
  }
  cases++;
 }
 // A single registry enforces consistency by construction. Independently
 // supplied operands instead require the actual shared-reference equality check.
 for(const c of layout.template.comparisons){
  const r=registry(0),a=channelOperand(layout,c.inputs[0],r);
  const b=channelOperand(layout,c.inputs[1],{...r,[c.sharedRecord]:1});
  assert.throws(()=>compareAt(layout,c.cell,a,b),/Shared record disagrees/);sharedConflicts++;
 }
 const otherLayout=comparisonLayout(atlas,fixture,chart.id,[1-p,e]);
 const a=reconcileBothOrders(layout,registry(0)),b=reconcileBothOrders(otherLayout,registry(0));
 assert.deepEqual(readRecords(layout,a.byE),readRecords(otherLayout,b.byE));
 assert.notDeepEqual(a.byE.records,b.byE.records);bindingWitnesses++;
 if(!example)example={chart:chart.id,binding:[p,e],
  equalValuesDifferentReferences:{left:a.byE.records,right:b.byE.records},
  historyOnly:{left:a.byE.children.map(c=>c.at),right:a.byP.children.map(c=>c.at)}};
}
// Forgetting directional labels loses a required channel assignment, even if
// the multiset of contents is retained. Signs are not charges or amplitudes.
const directed={'P+':0,'P-':1,'E+':2,'E-':3},swapped={...directed,'P+':1,'P-':0};
assert.deepEqual(Object.values(directed).sort(),Object.values(swapped).sort());
const layout=comparisonLayout(atlas,fixture,atlas.charts[0].id,[0,0]);
const direct=reconcileBothOrders(layout,directed),swap=reconcileBothOrders(layout,swapped);
assert.notDeepEqual(direct.channels,swap.channels);
// Chart identity matters to attachment, independently of output values.
const distinct=atlas.charts.find(c=>c.id!==layout.chart.id);assert(distinct);
const otherLayout=comparisonLayout(atlas,fixture,distinct.id,[0,0]);
const other=reconcileBothOrders(otherLayout,directed);
assert.deepEqual(readRecords(layout,direct.byE),readRecords(otherLayout,other.byE));
assert.notDeepEqual(direct.byE.anchor,other.byE.anchor);
const sources=[fixturePath,'research/strominger/sulfur-32-reversible-channel-specification.md',
 'research/strominger/su32-signed-reference-encoder.mjs','research/strominger/su32-layer4-comparison.mjs',
 'research/strominger/checkers/check_su32_comparison_sufficiency.mjs'];
const sourceHashes={};for(const p of sources)sourceHashes[p]=createHash('sha256').update(await fs.readFile(p)).digest('hex');
const report={schema:'su32.comparison-task-sufficiency.v1',passed:true,charts:atlas.charts.length,
 cases,reconstructedHistories,sharedConflicts,droppedRecordWitnesses,bindingWitnesses,
 tasks:{contents:'At fixed known layout, four independent labelled records suffice for all baseline channel projections and both comparison orders.',
 attachment:'Layout/occurrence and sign binding must remain recoverable; materialized referenceCell fields can be recomputed from them.',
 provenance:'The two canonical reconciliation derivations need their route distinction. Anchor + registry + route reconstructs their complete stored trees exactly; arbitrary history compression is not established.',
 validity:'For independent operands, inconsistent shared records must be rejected. A single source registry can enforce this by construction.'},
 residuals:['Adequacy is relative to documented retention/incidence requirements and the set-valued candidate, not a derived physical interaction.',
 'The specification requires retained histories; equal content is not equivalence for that larger task.',
 'Charts tested separately. No globally compatible signed assignment or cross-chart transport is constructed or inferred.',
 'Six-output routing, double-twist identification and downstream dynamics remain unspecified by this comparison task.',
 'Boolean ablations prove impossibility of the listed lossy summaries; they do not establish an absolute smallest encoding for arbitrary payloads.'],
 example,sourceHashes};
const dir='research/strominger/results/su32-comparison-sufficiency-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,example:undefined,sourceHashes:undefined},null,2));
