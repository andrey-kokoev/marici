import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildFiveSideOctComparisonDomain} from '../../realization-tower/five-side-oct-comparison-domain.mjs';
import {buildSu32SignedReferenceAtlas,decodeSignedReferences} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,readRecords} from '../su32-layer4-comparison.mjs';
import {splitAttachment} from '../su32-cross-cone-reference-fibre.mjs';
import {contextualExchangeInterface} from '../su32-contextual-path-exchange.mjs';
const root='research/strominger',fixturePath=root+'/results/su32-hopf-tests-v1/fixture.json';
const digest=async p=>createHash('sha256').update(await fs.readFile(p)).digest('hex');
const fixture=JSON.parse(await fs.readFile(fixturePath,'utf8'));
for(const [p,h] of Object.entries(fixture.sourceHashes))assert.equal(await digest(p),h);
const reading=buildFiveSideOctComparisonDomain(buildPESymmetricSector(1),{readingIds:['reading:0:-1']}).readings[0];
const cone=reading.overlaps.find(o=>o.length===4&&o.source==='neutron:0,0,2,1'&&o.residualCycleRank);
const move=cone.moves.find(m=>m.position===2),A=cone.paths.find(p=>p.id===move.from),B=cone.paths.find(p=>p.id===move.to);
const atlas=buildSu32SignedReferenceAtlas(fixture),chart=atlas.charts.find(c=>c.reading===reading.id&&c.source===cone.source&&c.target===cone.target);
const layout=comparisonLayout(atlas,fixture,chart.id,[0,0]),op=contextualExchangeInterface(atlas,fixture,layout,A,B);
const targetCharts=atlas.charts.filter(c=>c.reading===reading.id&&c.joints.some(j=>j.cell===chart.target&&[j.P,j.E].includes(op.cell)&&
 [j.P,j.E].filter(id=>id!==op.cell).every(id=>layout.template.comparisons.some(p=>p.cell===id))));
assert(targetCharts.length>0,'No actual continuation of the required kind');
const targets=targetCharts.flatMap(c=>[[0,0],[0,1],[1,0],[1,1]].map(b=>comparisonLayout(atlas,fixture,c.id,b)));
const labels=['P+','P-','E+','E-'];let exchanges=0,attachmentChecks=0;let example;
for(let bits=0;bits<16;bits++){
 const registry=Object.fromEntries(labels.map((label,i)=>[label,{id:'input:'+label,value:{bit:(bits>>i)&1,opaque:[null,false]},origin:{entry:chart.source,label}}]));
 const antecedent=[{kind:'supplied-preparation',reading:reading.id,retained:{tag:bits}}];
 const left=op.make(registry,0,antecedent),snapshot=structuredClone(left),right=op.exchange(left);
 assert.deepEqual(left,snapshot);assert.deepEqual(op.exchange(right),left);
 assert.deepEqual(right.preparation,left.preparation);assert.deepEqual(decodeSignedReferences(atlas,right.preparation),registry);
 assert.deepEqual(right.antecedent,left.antecedent);assert.deepEqual(right.orderedPaths,[B,A]);
 assert.deepEqual(readRecords(layout,left.point),readRecords(layout,right.point));
 assert.notDeepEqual(left.point,right.point);assert.equal(left.point.children[0].at,A.cells[2]);assert.equal(right.point.children[0].at,B.cells[2]);
 assert.deepEqual(right.point.children,[left.point.children[1],left.point.children[0]]);exchanges++;
 for(const target of targets){
  const before=op.attach(left,target),afterByLift=op.exchangeAttached(before,target),afterDirect=op.attach(right,target);
  assert.deepEqual(afterByLift,afterDirect);assert.deepEqual(op.exchangeAttached(afterByLift,target),before);
  assert.deepEqual(op.recover(before,target),left);assert.deepEqual(op.recover(afterByLift,target),right);
  assert.notDeepEqual(before.consumer,afterByLift.consumer,'Full history-sensitive consumer must distinguish the presentations');
  assert.deepEqual(before.consumer.anchor,afterByLift.consumer.anchor);assert.equal(before.consumer.at,chart.target);
  const b=splitAttachment(layout,target,op.cell,chart.target,before.consumer),a=splitAttachment(layout,target,op.cell,chart.target,afterByLift.consumer);
  assert.deepEqual(b.otherPayload,a.otherPayload);assert.deepEqual(a.point,right.point);
  assert.deepEqual(afterByLift.preparation,before.preparation);assert.deepEqual(afterByLift.antecedent,before.antecedent);attachmentChecks++;
  if(!example){
   const first=op.perform(left),second=op.perform(first.state,first.receipts);assert.deepEqual(second.state,left);
   example={left,right,targetAnchor:target.anchor,before,after:afterByLift,applicationReceipts:second.receipts};
  }
 }
}
const {left,right,before}=example,target=targets[0];
const controls={
 droppedContext:s=>{s.point.children.pop();},
 changedRecord:s=>{s.point.children[0].records['P+'].payload={different:true};},
 alteredPathWord:s=>{s.orderedPaths[0].arrows[0]='invented';},
 wrongPreparationBinding:s=>{s.preparation.binding=[1,0];}
};
for(const mutate of Object.values(controls)){const bad=structuredClone(left);mutate(bad);assert.throws(()=>op.exchange(bad));}
const stale=structuredClone(before);stale.orderedPaths=structuredClone(right.orderedPaths);assert.throws(()=>op.recover(stale,target));
const changedOther=structuredClone(before),otherLabel=Object.keys(changedOther.consumer.records).find(label=>changedOther.consumer.records[label].referenceCell!==op.cell);
changedOther.consumer.records[otherLabel].payload={unrelated:true};assert.throws(()=>op.recover(changedOther,target));
assert.equal(example.applicationReceipts.length,2);assert.notDeepEqual(example.applicationReceipts,[]);
const forgedReceipts=structuredClone(example.applicationReceipts);forgedReceipts[0].target=structuredClone(left);
assert.throws(()=>op.perform(left,forgedReceipts));
const sourceHashes={};for(const p of [fixturePath,root+'/su32-contextual-path-exchange.mjs',root+'/checkers/check_su32_contextual_path_exchange.mjs',
 root+'/su32-cross-cone-reference-fibre.mjs',root+'/su32-layer4-comparison.mjs',root+'/su32-signed-reference-encoder.mjs',root+'/pe-symmetric-sector.mjs',
 'research/realization-tower/five-side-oct-comparison-domain.mjs','research/realization-tower/five-side-oct-routing-obligations.mjs'])sourceHashes[p]=await digest(p);
const result={schema:'su32.contextual-path-exchange.v1',passed:true,nativeComparisonCompiled:false,
 counts:{fixedSourceCharts:1,preparationFixtures:16,consumerCharts:targetCharts.length,consumerBindings:targets.length,exchanges,attachmentChecks,negativeControls:7},
 construction:'Exchange the ordered inputs of the existing shared-reference comparison while retaining the whole preparation, both source path words, both operands and antecedent records.',
 attachmentLaw:'The lift is DEFINED as attach composed with exchange composed with recover. Existing splitAttachment supplies recovery; the tests verify its domain, inverse and retained records, not an independent native interchange law.',
 example,negativeControls:[...Object.keys(controls),'unchanged consumer after claimed producer exchange','changed other consumer operand','forged exchange receipt'],
 conclusion:'A fixed-preparation contextual presentation exchange and its reversible reference-attachment lift are constructed. Full history readers change by the explicit map; record readers and the other operand are preserved.',
 limits:['Domain includes both branches and the complete preparation; this is not an equivalence of standalone pair operands.',
 'First-input order is a presentation marker, not an inferred physical active-branch selector.',
 'The two exchange receipts remain even when the presentation returns. No raw history equality or period-return relation is admitted.',
 'The underlying comparison and attachment APIs remain declared candidates, not compiled Su-32 native rules.'],sourceHashes};
const dir=root+'/results/su32-contextual-path-exchange-v1';await fs.mkdir(dir,{recursive:true});await fs.writeFile(dir+'/verification.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({passed:true,nativeComparisonCompiled:false,counts:result.counts,conclusion:result.conclusion,attachmentLaw:result.attachmentLaw,limits:result.limits},null,2));
