// Does the opposite-half comparison structure independently filter the 40
// candidates? Reflection is tested as a geometric/reference correspondence,
// never installed as an unprovided native middle operation.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,reconcileBothOrders,readRecords,validateComparisonNode} from '../su32-layer4-comparison.mjs';
const tracePath='research/strominger/results/su32-fixed-reading-trace-v1/verification.json';
const candidatesPath='research/strominger/results/su32-six-pair-falsification-v1/verification.json';
const fixturePath='research/strominger/results/su32-hopf-tests-v1/fixture.json';
const trace=JSON.parse(await fs.readFile(tracePath,'utf8'));
const candidates=JSON.parse(await fs.readFile(candidatesPath,'utf8'));
const fixture=JSON.parse(await fs.readFile(fixturePath,'utf8'));
for(const record of [trace,candidates,fixture])for(const [p,h] of Object.entries(record.sourceHashes))
 assert.equal(createHash('sha256').update(await fs.readFile(p)).digest('hex'),h,`Stale input: ${p}`);
const atlas=buildSu32SignedReferenceAtlas(fixture),sector=buildPESymmetricSector(1);
const reading=fixture.readings.find(r=>r.id===trace.reading),opposite=fixture.readings.find(r=>r.incomingN===trace.outgoingN);
const shape=vs=>vs.map(v=>v.join(',')).sort().join('|');
const byShape=new Map(fixture.cells.map(c=>[shape(c.vertices),c.id]));
const mirror=Object.fromEntries(fixture.cells.map(c=>[c.id,byShape.get(shape(c.vertices.map(v=>{
 const h=reading.axis.reduce((s,a,i)=>s+a*(v[i]-sector.centre[i]),0)/2;
 return v.map((x,i)=>x-h*reading.axis[i]);
})))]));
for(const c of fixture.cells){assert(mirror[c.id]);assert.equal(mirror[mirror[c.id]],c.id);}
assert.equal(mirror[reading.incomingN],opposite.incomingN);
const sourceAnchor=trace.centralReconciliation.byE.anchor;
const src=comparisonLayout(atlas,fixture,sourceAnchor.chartId,sourceAnchor.binding);
const targetChart=atlas.charts.find(c=>c.reading===opposite.id&&c.source===opposite.incomingN);assert(targetChart);
const dst=comparisonLayout(atlas,fixture,targetChart.id,[0,0]);
// One globally fixed correspondence from reflected geometric references.
// Local slot names change; payload identities/provenance do NOT.
const rename=Object.fromEntries(Object.entries(src.template.referenceBinding).map(([cell,label])=>{
 const outputLabel=dst.template.referenceBinding[mirror[cell]];assert(outputLabel);return [label,outputLabel];
}));
assert.equal(new Set(Object.values(rename)).size,4);
const inverse=Object.fromEntries(Object.entries(rename).map(([a,b])=>[b,a]));
const rekey=(r,map)=>Object.fromEntries(Object.entries(r).map(([k,v])=>[map[k],structuredClone(v)]));
function reflectNode(node,targetLayout,map){
 const out={...structuredClone(node),anchor:structuredClone(targetLayout.anchor),at:mirror[node.at],
  records:Object.fromEntries(Object.entries(node.records).map(([k,v])=>[map[k],{...structuredClone(v),referenceCell:mirror[v.referenceCell]}]))};
 if(node.children)out.children=node.children.map(c=>reflectNode(c,targetLayout,map));
 return out;
}
const input=reconcileBothOrders(src,trace.registry),oppositeRegistry=rekey(trace.registry,rename);
const output=reconcileBothOrders(dst,oppositeRegistry);
let reflectedTrees=0;
for(const n of [...Object.values(input.channels),...input.comparisons,input.byE,input.byP]){
 const mapped=reflectNode(n,dst,rename);assert(validateComparisonNode(dst,mapped));
 assert.deepEqual(reflectNode(mapped,src,inverse),n);reflectedTrees++;
}
assert.deepEqual(readRecords(dst,reflectNode(input.byE,dst,rename)),oppositeRegistry);
assert.deepEqual(readRecords(dst,reflectNode(input.byP,dst,rename)),oppositeRegistry);
// The independently built opposite prefix agrees on records. Its stored child
// order can differ by the constructor's lexical convention; no history is erased.
assert.deepEqual(reflectNode(input.byE,dst,rename).records,output.byP.records);
assert.deepEqual(reflectNode(input.byP,dst,rename).records,output.byE.records);
const targetViews=new Map([
 ...opposite.outer.map(o=>[o.cell,output.channels[o.input]]),
 ...output.comparisons.map(n=>[n.at,n])
]);
const sourceViews=new Map(trace.layer4.map(x=>[x.cell,x.operand]));
const results=[];let sideChecks=0,candidateChecks=0,identityChecks=0;
for(const family of candidates.results){
 const cover=trace.middleAssignments.find(c=>c.index===family.cover);assert(cover);
 for(const r of cover.routes){
  assert.equal(mirror[r.sourceP],r.targetE);assert.equal(mirror[r.sourceE],r.targetP);
  for(const [from,to] of [[r.sourceP,r.targetE],[r.sourceE,r.targetP]]){
   const mapped=reflectNode(sourceViews.get(from),dst,rename);
   assert.deepEqual(mapped.records,targetViews.get(to).records);sideChecks++;
  }
 }
 const outcomes=family.jointAssignments.map(choice=>{
  for(let i=0;i<cover.routes.length;i++){
   const r=cover.routes[i],originalPair=candidates.pairs[choice[i]],mappedPair=originalPair.map(k=>rename[k]);
   const available={...targetViews.get(r.targetP).records,...targetViews.get(r.targetE).records};
   for(let j=0;j<2;j++){
    assert(Object.hasOwn(available,mappedPair[j]));
    assert.deepEqual(available[mappedPair[j]].payload,trace.registry[originalPair[j]]);identityChecks++;
   }
   assert.deepEqual(mappedPair.map(k=>inverse[k]),originalPair);
  }
  candidateChecks++;
  return {assignment:choice,oppositeSupportCompatible:true,referenceRoundTrip:true,nativeExecutionTested:false};
 });
 results.push({cover:family.cover,survivors:outcomes.length,outcomes});
}
assert.equal(candidateChecks,40);
// Demonstrate a hostile target-label correspondence is detected rather than
// merely accepting every proposed bijection. This is a reference-identity
// control, not evidence that reflection is a native transport law.
const bad={...rename},names=Object.keys(bad);[bad[names[0]],bad[names[1]]]=[bad[names[1]],bad[names[0]]];
assert.throws(()=>validateComparisonNode(dst,reflectNode(input.byE,dst,bad)));
const sources=[tracePath,candidatesPath,fixturePath,'research/strominger/su32-layer4-comparison.mjs',
 'research/strominger/su32-signed-reference-encoder.mjs','research/strominger/pe-symmetric-sector.mjs',
 'research/strominger/checkers/check_su32_opposite_half_falsification.mjs'];
const hashes={};for(const p of sources)hashes[p]=createHash('sha256').update(await fs.readFile(p)).digest('hex');
const report={schema:'su32.opposite-half-falsification.v1',passed:true,source:reading.id,target:opposite.id,
 referenceCorrespondence:{construction:'One middle-plane reflection fixed before candidate tests; not an admitted native record transport.',rename,
  originalPayloadIdentitiesPreserved:true,oppositeRegistry},
 reflectedTrees,sideChecks,candidateChecks,identityChecks,results,
 verdict:'0 of 40 candidates rejected by reflected opposite-half reference constraints; this test supplies no independent selection.',
 explanation:'The full opposite prefix is a reflected copy of the source prefix. Its operand supports are corresponding renamings, so joint pair availability is equivalent on both sides.',
 missingForExecution:['A native middle operation on the actual retained states/occurrences, rather than geometric reflection of reference descriptions.',
 'A forward rule through the opposite half and an inverse on the admitted state domain, including provenance and outer/central compatibility.'],
 nativeExecutionTested:false,physicalReversibilityEstablished:false,
 limits:['Reference reflection is involutive; this is not temporal reversal of a signal process.',
 'No candidate-specific output maps, independent output payloads, or new transition laws were fitted.',
 'The candidate joins remain information models, not derived native physical comparisons.',
 'The opposite registry is a pullback for checking reference compatibility, not the output of an executed middle operation.'],sourceHashes:hashes};
const dir='research/strominger/results/su32-opposite-half-falsification-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,results:results.map(({outcomes,...r})=>r),sourceHashes:undefined},null,2));
