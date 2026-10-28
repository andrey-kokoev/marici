// Falsify/test a native coherent four-record realization, not just agreement
// of projected registries. No circular orders or simplicial filler installed.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildFiveSideOctRoutingObligations} from '../../realization-tower/five-side-oct-routing-obligations.mjs';
import {buildFiveSideOctComparisonDomain} from '../../realization-tower/five-side-oct-comparison-domain.mjs';
import * as comparisonAPI from '../su32-layer4-comparison.mjs';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
const fixturePath='research/strominger/results/su32-hopf-tests-v1/fixture.json';
const fixture=JSON.parse(await fs.readFile(fixturePath,'utf8'));
for(const [p,h] of Object.entries(fixture.sourceHashes))assert.equal(createHash('sha256').update(await fs.readFile(p)).digest('hex'),h);
const sector=buildPESymmetricSector(1),sites=buildFiveSideOctRoutingObligations(sector);
const reading=sites.readings.find(r=>r.id==='reading:0:-1');assert(reading);
const domain=buildFiveSideOctComparisonDomain(sector,{readingIds:[reading.id],maxLength:4});
const native=domain.readings[0];
const atlas=buildSu32SignedReferenceAtlas(fixture);
const chart=atlas.charts.find(c=>c.reading===reading.id&&c.source===reading.incomingN);assert(chart);
const layout=comparisonAPI.comparisonLayout(atlas,fixture,chart.id,[0,0]);
const labels=['P+','P-','E+','E-'],sorted=xs=>[...xs].sort(),key=xs=>JSON.stringify(sorted(xs));
const combinations=(xs,n)=>n===0?[[]]:xs.flatMap((x,i)=>combinations(xs.slice(i+1),n-1).map(t=>[x,...t]));
// Explicitly an ordinary data projection: not registered as a native map.
const project=(r,ks)=>Object.fromEntries(sorted(ks).map(k=>[k,structuredClone(r[k])]));
const registry=Object.fromEntries(labels.map((k,i)=>[k,{id:'input:'+k,value:{index:i},provenance:{entry:reading.incomingN,slot:k}}]));
const built=comparisonAPI.reconcileBothOrders(layout,registry);
const required=native.comparisons.filter(c=>c.sourceRequirement);
assert.equal(required.length,4);
for(const c of required){assert.equal(c.comparisonMap,null);assert.equal(c.fillingWitness,null);}
for(const c of reading.comparisons){assert.equal(c.comparisonWitness,null);assert.equal(c.outputPairing,null);}
const entryCone=native.overlaps.find(c=>c.source===chart.source&&c.target===chart.target&&c.length===4);assert(entryCone);
assert(entryCone.moves.every(m=>m.witness===null));
assert(entryCone.cycleBasis.every(c=>c.fillingWitness===null));
assert.equal(built.agreement.nativeFiller,null);
assert.deepEqual(sorted(built.comparisons.map(c=>key(Object.keys(c.records)))),sorted(combinations(labels,3).map(key)));
const channels=Object.values(built.channels);
const faceRestrictions=built.comparisons.map(face=>({cell:face.at,labels:sorted(Object.keys(face.records)),
 pairRestrictions:combinations(sorted(Object.keys(face.records)),2).map(pair=>{
  const child=face.children.find(c=>key(Object.keys(c.records))===key(pair));
  const existingChannel=channels.find(c=>key(Object.keys(c.records))===key(pair));
  assert.equal(Boolean(child),Boolean(existingChannel));
  if(child)assert.deepEqual(child,existingChannel);
  return {pair,existingOperand:child?.at??null,dataProjection:project(face.records,pair),
   status:child?'existing channel operand retained in candidate tree; native transition still unbound':'same-role comparison is contextual in this face; no shared pair-only operand or context-identification map is supplied by this entry template'};
 })}));
const restrictions=faceRestrictions.flatMap(f=>f.pairRestrictions);
assert.equal(restrictions.filter(r=>r.existingOperand).length,8);
assert.equal(restrictions.filter(r=>!r.existingOperand).length,4);
const sharedPairs=combinations(labels,2).map(pair=>{
 const faces=built.comparisons.filter(f=>pair.every(k=>Object.hasOwn(f.records,k)));assert.equal(faces.length,2);
 assert.deepEqual(project(faces[0].records,pair),project(faces[1].records,pair));
 const operands=faces.map(f=>f.children.find(c=>key(Object.keys(c.records))===key(pair)));
 if(operands[0])assert.deepEqual(operands[0],operands[1]);else assert(!operands[1]);
 return {pair,faces:faces.map(f=>f.at),recordIdentityAndPayloadAgree:true,sharedNativeEntryOperand:operands[0]?.at??null,
  retainedContexts:faces.map(f=>({at:f.at,referenceLabels:Object.keys(f.records).filter(k=>!pair.includes(k))}))};
});
// Test confluence of plain record restrictions independently of any claim that
// these are native restrictions, using all 16 Boolean assignments and tagged data.
let dataCases=0,commutingRestrictionChecks=0;
for(const r of [...Array.from({length:16},(_,bits)=>Object.fromEntries(labels.map((k,i)=>[k,(bits>>i)&1]))),registry]){
 const b=comparisonAPI.reconcileBothOrders(layout,r);
 for(const face of b.comparisons)assert.deepEqual(project(b.byE.records,Object.keys(face.records)),face.records);
 for(const pair of combinations(labels,2)){
  const faces=b.comparisons.filter(f=>pair.every(k=>Object.hasOwn(f.records,k)));
  assert.deepEqual(project(faces[0].records,pair),project(faces[1].records,pair));
  for(const k of pair)for(const face of faces){
   assert.deepEqual(project(project(face.records,pair),[k]),project(b.byE.records,[k]));commutingRestrictionChecks++;
  }
 }
 assert.deepEqual(b.byE.records,b.byP.records);assert.notDeepEqual(b.byE.children,b.byP.children);dataCases++;
}
// Information recovery can synthesize the other canonical derivation. That
// fact is real, but synthesis is not a source-provided comparison witness.
const synthesized=comparisonAPI.reconcileBothOrders(layout,comparisonAPI.readRecords(layout,built.byE)).byP;
assert.deepEqual(synthesized,built.byP);
const routeFaces={byE:built.byE.children.map(c=>c.at),byP:built.byP.children.map(c=>c.at)};
assert.equal(new Set([...routeFaces.byE,...routeFaces.byP]).size,4);
assert.equal(built.byE.children.length,2);assert.equal(built.byP.children.length,2);
// A malformed triangle of operand values would really be rejected. This
// positive sensitivity control must not be reported as a native contradiction.
const first=layout.template.comparisons[0],left=built.channels[first.inputs[0]],right=structuredClone(built.channels[first.inputs[1]]);
right.records[first.sharedRecord].payload={changed:true};
assert(comparisonAPI.validateComparisonNode(layout,right));
assert.throws(()=>comparisonAPI.compareAt(layout,first.cell,left,right),/Shared record disagrees/);
const sources=[fixturePath,'research/strominger/sulfur-32-reversible-channel-specification.md',
 'research/strominger/su32-layer4-comparison.mjs','research/strominger/su32-signed-reference-encoder.mjs',
 'research/realization-tower/five-side-oct-routing-obligations.mjs','research/realization-tower/five-side-oct-comparison-domain.mjs',
 'research/strominger/checkers/check_su32_native_realization_falsification.mjs'];
const hashes={};for(const p of sources)hashes[p]=createHash('sha256').update(await fs.readFile(p)).digest('hex');
const report={schema:'su32.native-realization-falsification.v1',passed:true,
 conjecture:'The four central comparisons are restrictions of one native coherent four-record realization, with a source-defined witness connecting the reconciliation routes.',
 reading:reading.id,anchor:layout.anchor,faceRestrictions,sharedPairs,routeFaces,
 dataLevel:{dataCases,commutingRestrictionChecks,allFourFacesRecoverable:true,canonicalOtherRouteReconstructible:true},
 nativeLevel:{entryChannelOperands:channels.map(c=>({cell:c.at,labels:sorted(Object.keys(c.records))})),
  requiredComparisonMaps:required.map(c=>({id:c.id,status:c.status,comparisonMap:c.comparisonMap,fillingWitness:c.fillingWitness})),
  cone:{source:entryCone.source,target:entryCone.target,paths:entryCone.paths.length,moves:entryCone.moves.length,
   witnessedMoves:entryCone.moves.filter(m=>m.witness!==null).length,cycles:entryCone.cycleBasis.length,
   suppliedCycleFillers:entryCone.cycleBasis.filter(c=>c.fillingWitness!==null).length},
  agreementKind:built.agreement.kind,nativeFiller:built.agreement.nativeFiller,comparisonExports:Object.keys(comparisonAPI).sort()},
 verdict:'Underdetermined by audited native operations; no incompatible source requirement found. The stronger claim that the current implementation already supplies a native simplicial filler is unsupported.',
 firstMissingObjects:['Native restrictions from ternary comparisons to the same-role pairs, preserving reference/occurrence meaning rather than merely dropping a field.',
  'A native higher comparison connecting byE and byP, with supplied boundary and coherence laws.'],
 limits:['Missing operations are not a proof that such a realization is impossible.',
  'The agreement wrapper contains both derivations but is not an admitted tetrahedral 3-simplex.',
  'Same-role comparisons already exist at their shared opposite-role references; absence of a channel operand does not prove absence of every possible pair object. The missing common edge needs a specified restriction or context-identification rule.',
  'Data-level projections commute; this does not license native simplicial restrictions.',
  'No circular orders, simplex attachments, Chern cocycles or route-dependent invariants were introduced.',
  'Audit covers the fixed entry template and the enumerated length-four comparison domain, not every possible future native operation.'],sourceHashes:hashes};
const dir='research/strominger/results/su32-native-realization-falsification-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,faceRestrictions:undefined,sharedPairs:undefined,sourceHashes:undefined},null,2));
