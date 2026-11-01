// One actual source chart; execute existing candidates, never invent a release.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildSulfur32Wiring} from '../../realization-tower/sulfur-32-wiring.mjs';
import {buildFiveSideOctRoutingObligations} from '../../realization-tower/five-side-oct-routing-obligations.mjs';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,channelOperand,compareAt,reconcileBothOrders,readRecords} from '../su32-layer4-comparison.mjs';
const root='research/strominger',fixturePath=root+'/results/su32-hopf-tests-v1/fixture.json';
const digest=async p=>createHash('sha256').update(await fs.readFile(p)).digest('hex');
const fixture=JSON.parse(await fs.readFile(fixturePath,'utf8'));
for(const [p,h] of Object.entries(fixture.sourceHashes))assert.equal(await digest(p),h,`Stale source ${p}`);
const sector=buildPESymmetricSector(1),obligations=buildFiveSideOctRoutingObligations(sector),wiring=buildSulfur32Wiring();
const native=obligations.readings.find(r=>r.id==='reading:0:-1'),atlas=buildSu32SignedReferenceAtlas(fixture);
const chart=atlas.charts.find(c=>c.reading===native.id&&c.source===native.incomingN);assert(chart);
const layout=comparisonLayout(atlas,fixture,chart.id,[0,0]);
const registry=Object.fromEntries(['P+','P-','E+','E-'].map((k,i)=>[k,{id:'input:'+k,payload:{tag:i},provenance:{entry:chart.source,slot:k}}]));
const candidate=reconcileBothOrders(layout,registry);
assert.deepEqual(readRecords(layout,candidate.byE),registry);assert.deepEqual(readRecords(layout,candidate.byP),registry);
assert.notDeepEqual(candidate.byE.children,candidate.byP.children);assert.equal(candidate.agreement.nativeFiller,null);
// Derive the conditional alpha from ACTUAL complete candidate leaf witnesses,
// not merely their two-label supports. Preserve both intermediate trees.
const leaves=node=>node.children.flatMap((c,i)=>c.children.map((w,j)=>({position:[i,j],witness:w})));
function witnessComparison(a,b){
 const A=leaves(a),B=leaves(b);assert.equal(A.length,4);assert.equal(new Set(A.map(x=>x.witness.at)).size,4);
 const mapping=A.map(x=>{const matches=B.filter(y=>y.witness.at===x.witness.at);assert.equal(matches.length,1);
  const y=matches[0];assert.deepEqual(x.witness,y.witness);assert.deepEqual(readRecords(layout,x.witness),readRecords(layout,y.witness));
  return {occurrence:x.witness.at,from:x.position,to:y.position};});
 assert.equal(new Set(mapping.map(m=>JSON.stringify(m.to))).size,4);
 return mapping;
}
const alpha=witnessComparison(candidate.byE,candidate.byP),beta=witnessComparison(candidate.byP,candidate.byE);
for(const a of alpha){const b=beta.find(b=>b.occurrence===a.occurrence);assert.deepEqual(a.from,b.to);assert.deepEqual(a.to,b.from);}
const damaged=structuredClone(candidate.byP);const first=damaged.children[0].children[0];first.records[Object.keys(first.records)[0]].payload={tampered:true};
assert.throws(()=>witnessComparison(candidate.byE,damaged));
assert.deepEqual(native.comparisons.map(c=>c.cell).sort(),layout.template.comparisons.map(c=>c.cell).sort());
for(const c of native.comparisons){assert.equal(c.comparisonWitness,null);assert.equal(c.outputPairing,null);}
const joint=(p,e)=>{const js=layout.template.channels.filter(j=>j.P.record===p&&j.E.record===e);assert.equal(js.length,1);return js[0].cell;};
const q={pp:joint('P+','E+'),mp:joint('P-','E+'),pm:joint('P+','E-'),mm:joint('P-','E-')};
const comparison=shared=>{const cs=layout.template.comparisons.filter(c=>c.sharedRecord===shared);assert.equal(cs.length,1);return cs[0];};
// Candidate release from a pair alone is underdetermined: the constructor
// really consumes a second operand drawn from the retained global registry.
const changed=structuredClone(registry);changed['P-'].payload={tag:'different'};
const left=channelOperand(layout,q.pp,registry),sameLeft=channelOperand(layout,q.pp,changed);
assert.deepEqual(left,sameLeft);
const right=channelOperand(layout,q.mp,registry),changedRight=channelOperand(layout,q.mp,changed);
const c1=comparison('E+');
const joinA=compareAt(layout,c1.cell,left,right),joinB=compareAt(layout,c1.cell,sameLeft,changedRight);
assert.notDeepEqual(joinA,joinB);
const shape=vs=>vs.map(v=>v.join(',')).sort().join('|'),portAt=new Map();
for(const p of wiring.ports)for(const l of p.lifts)portAt.set(l.cell+'@'+shape(l.vertices),p);
const wireAt=new Map(wiring.wires.flatMap(w=>w.ports.map(p=>[p,w.id])));
function incidence(a,b){
 const faces=sector.faces.filter(f=>f.owners.includes(a)&&f.owners.includes(b));assert.equal(faces.length,1);
 const f=faces[0],pa=portAt.get(a+'@'+f.id),pb=portAt.get(b+'@'+f.id);assert(pa&&pb);
 const es=wiring.edges.filter(e=>(e.from===pa.id&&e.to===pb.id)||(e.from===pb.id&&e.to===pa.id));assert.equal(es.length,1);
 return {physicalFace:f.id,fromPort:pa.id,toPort:pb.id,edge:es[0].id};
}
function step(a,c,b){
 assert.deepEqual([a,b].sort(),[...c.inputs].sort());const incoming=incidence(a,c.cell),outgoing=incidence(c.cell,b);
 const pa=portAt.get(c.cell+'@'+incoming.physicalFace),pb=portAt.get(c.cell+'@'+outgoing.physicalFace);
 assert.notEqual(pa.id,pb.id);assert.notEqual(pa.axis,pb.axis);assert.notEqual(wireAt.get(pa.id),wireAt.get(pb.id));
 assert(!wiring.edges.some(e=>(e.from===pa.id&&e.to===pb.id)||(e.from===pb.id&&e.to===pa.id)));
 return {fromJoint:a,viaComparison:c.cell,toJoint:b,incoming,outgoing,
  missingInternalTransfer:{fromPort:pa.id,toPort:pb.id,axes:[pa.axis,pb.axis],wireIds:[wireAt.get(pa.id),wireAt.get(pb.id)],sourceEdge:null}};
}
const routes={PVariationThenE:[step(q.pp,comparison('E+'),q.mp),step(q.mp,comparison('P-'),q.mm)],
 EVariationThenP:[step(q.pp,comparison('P+'),q.pm),step(q.pm,comparison('E-'),q.mm)]};
const portEndpoints=Object.fromEntries(Object.entries(routes).map(([k,steps])=>[k,{start:steps[0].incoming.fromPort,end:steps.at(-1).outgoing.toPort}]));
assert.notEqual(portEndpoints.PVariationThenE.start,portEndpoints.EVariationThenP.start);assert.notEqual(portEndpoints.PVariationThenE.end,portEndpoints.EVariationThenP.end);
const sources=[fixturePath,root+'/checkers/check_su32_release_source_audit.mjs',root+'/su32-layer4-comparison.mjs',
 root+'/su32-signed-reference-encoder.mjs',root+'/pe-symmetric-sector.mjs',root+'/sulfur-32-reversible-channel-specification.md',
 'research/realization-tower/sulfur-32-wiring.mjs','research/realization-tower/five-side-oct-routing-obligations.mjs'];
const sourceHashes={};for(const p of sources)sourceHashes[p]=await digest(p);
const report={schema:'su32.release-source-audit.v1',passed:true,nativeReleaseExecuted:false,
 reading:native.id,chart:chart.id,binding:[0,0],registry,pairOccurrences:q,candidate,
 candidateDomainWitness:{sameStartingOperand:left,leftJoin:joinA,rightJoin:joinB,changedAdditionalInput:'P-'},
 nativeComparisonSites:native.comparisons,incidenceWalks:routes,portEndpoints,deckDiscrepancy:null,
 incidenceWalkInterpretation:'Sign-variation incidence walks from q++ to q--, NOT release histories. Candidate reconciliations instead retain all four leaves and finish at the central N.',
 candidateWitnessComparison:{alpha,beta,fullLeafWitnessesPreserved:true,readersCommute:true,bothHistoriesRetained:true,nativeAdmission:false,continuationCompatibility:null},
 deckTestStatus:'Not evaluable: these are cell-incidence walks, not two typed paths from a common port in the source wire graph.',
 firstMissingTypedObject:'A source-admitted contextual release constructor on the complete signed preparation, with output witness and occurrence/port maps. The obligation builder leaves comparisonWitness and outputPairing null.',
 acceptanceTest:'Execute its two orders on this fixed chart, retain both histories, establish the appropriate common endpoint type, then derive the reader- and continuation-compatible comparison. Use deck discrepancies only when actual port paths are supplied.',
 conclusion:'Existing candidates reconcile both orders using extra registry operands. No native release square is supplied by the inspected constructors; the incidence square cannot be substituted for native wire paths.',
 scope:'A bounded audit of the named specification, obligation builder and imported comparison implementation, not a repository-wide nonexistence theorem. A contextual or multiwire release is not excluded.',sourceHashes};
const dir=root+'/results/su32-release-source-audit-v1';await fs.mkdir(dir,{recursive:true});await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({passed:true,nativeReleaseExecuted:false,reading:report.reading,pairOccurrences:q,
 candidateTarget:candidate.byE.at,candidateWitnessComparison:report.candidateWitnessComparison,
 missingChargedTransfers:4,portEndpoints,deckDiscrepancy:null,conclusion:report.conclusion,firstMissingTypedObject:report.firstMissingTypedObject},null,2));
