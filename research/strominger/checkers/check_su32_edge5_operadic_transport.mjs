import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,channelOperand,compareAt,reconcileAt} from '../su32-layer4-comparison.mjs';
import {signature,dual,corolla,rotate,glue,decompose,assemble,key} from '../su32-cyclic-port-fragment.mjs';
import {identifyCone,targetFixture,transportNode} from '../su32-cone-operation-transport.mjs';
const root='research/strominger';
const paths={source:root+'/results/su32-hopf-tests-v1/fixture.json',edge5:root+'/results/su32-edge5-extension-contract-v1/verification.json',
 fragment:root+'/results/su32-cyclic-port-fragment-v1/verification.json',contract:root+'/contracts/su32-edge5-operadic-transport-v1.json'};
const digest=async p=>createHash('sha256').update(await fs.readFile(p)).digest('hex');
const docs={},sourceHashes={};for(const [k,p] of Object.entries(paths)){
 docs[k]=JSON.parse(await fs.readFile(p,'utf8'));sourceHashes[p]=await digest(p);
 for(const [s,h] of Object.entries(docs[k].sourceHashes??{}))assert.equal(await digest(s),h,`Stale source ${s}`);
}
const source=docs.source,carrier=docs.edge5.edge5Carrier,cones=carrier.comparisonCones;assert.equal(cones.length,44);
const sourceAtlas=buildSu32SignedReferenceAtlas(source),reading=source.readings.find(r=>r.id==='reading:0:-1');
const sourceChart=sourceAtlas.charts.find(c=>c.reading===reading.id&&c.source===reading.incomingN);
const sourceCone=reading.cones.find(c=>c.source===sourceChart.source&&c.target===sourceChart.target);
// All identifications are constructed and certified before testing any local reader.
const identifications=cones.map(c=>identifyCone(source,sourceChart,sourceCone,carrier,c));
// Geometry and scope controls: matching endpoints/counts is insufficient.
const reversedPathCone=structuredClone(cones[0]);reversedPathCone.paths[0].cells.reverse();
assert.throws(()=>identifyCone(source,sourceChart,sourceCone,carrier,reversedPathCone));
const wrongRoleCarrier=structuredClone(carrier);
wrongRoleCarrier.cells.find(c=>c.id===cones[0].source).role='proton';
assert.throws(()=>identifyCone(source,sourceChart,sourceCone,wrongRoleCarrier,cones[0]));
assert.throws(()=>buildSu32SignedReferenceAtlas({...source,edgeUnits:5}));
const atlas={schema:'su32.transported-occurrence-atlas.v1',charts:identifications.map(x=>x.chart),
 roles:Object.fromEntries(carrier.cells.map(c=>[c.id,c.role])),globalAssignment:null};
const fixture=targetFixture(carrier),labels=['P+','P-','E+','E-'];
const bank=Object.fromEntries(carrier.cells.filter(c=>c.role!=='neutron').map((c,i)=>[c.id,
 {token:i,literalSourceCell:sourceChart.P[0],nested:{at:sourceChart.target},value:[false,null,c.id]}]));
const byE=layout=>({plus:layout.template.comparisons.find(c=>c.sharedRecord==='E+'),minus:layout.template.comparisons.find(c=>c.sharedRecord==='E-')});
function output(layout,registry,reverseB=false){
 const {plus,minus}=byE(layout),a=plus.inputs.map(c=>channelOperand(layout,c,registry)),b=minus.inputs.map(c=>channelOperand(layout,c,registry));
 const c=compareAt(layout,plus.cell,...a),d=compareAt(layout,minus.cell,...(reverseB?[...b].reverse():b));return reconcileAt(layout,c,d);
}
function section(layout){return Object.fromEntries(Object.entries(layout.template.referenceBinding).map(([cell,label])=>[label,{cell,payload:bank[cell]}]));}
const restrict=(s,ids)=>Object.fromEntries(ids.map(id=>{const e=Object.values(s).find(e=>e.cell===id);assert(e);return [id,e.payload];}));
const cyclicKey=g=>Array.from({length:g.ports.length},(_,i)=>key(rotate(g,i).ports)).sort()[0];
let naturality=0,reconstructions=0,dualityChecks=0,cyclicChecks=0,payloadSentinels=0;
const sections=[],reports=[];let example=null;
for(let ci=0;ci<cones.length;ci++){
 const iso=identifications[ci],chart=iso.chart,views=[];
 for(const p of [0,1])for(const e of [0,1]){
  const sl=comparisonLayout(sourceAtlas,source,sourceChart.id,[p,e]),tl=comparisonLayout(atlas,fixture,chart.id,[p,e]);
  const ss=signature(sl,source),ts=signature(tl,fixture);
  for(const c of ss.colours){
   const t=ts.colours.find(t=>t.wire===c.wire&&t.end===c.end);assert(t);
   const expected={...structuredClone(c),packetType:{...structuredClone(c.packetType),anchor:tl.anchor,
    origin:iso.cellMap[c.packetType.origin],referenceCells:Object.fromEntries(Object.entries(c.packetType.referenceCells).map(([k,v])=>[k,iso.cellMap[v]]))}};
   assert.deepEqual(t,expected);const cd=dual(ss,c),td=dual(ts,t);assert.equal(cd.wire,td.wire);assert.equal(cd.end,td.end);dualityChecks++;
  }
  for(let bits=0;bits<16;bits++)for(const reverseB of [false,true]){
   const registry=Object.fromEntries(labels.map((k,i)=>[k,(bits>>i)&1]));
   const original=output(sl,registry,reverseB),actual=output(tl,registry,reverseB);
   assert.deepEqual(transportNode(sl,tl,iso,original),actual);naturality++;
   assert.deepEqual(assemble(tl,ts,decompose(tl,ts,actual)),actual);reconstructions++;
   if(bits===0&&!reverseB){
    const local=decompose(tl,ts,actual),g=glue(ts,local.left,2,local.right,0);
    for(let a=0;a<3;a++)for(let b=0;b<3;b++){
     const l=rotate(local.left,a),r=rotate(local.right,b);
     const h=glue(ts,l,l.ports.findIndex(x=>x.colour.wire==='C-R'),r,r.ports.findIndex(x=>x.colour.wire==='C-R'));
     assert.equal(cyclicKey(g),cyclicKey(h));cyclicChecks++;
    }
   }
  }
  const view=section(tl),registry=Object.fromEntries(Object.entries(view).map(([label,r])=>[label,r.payload]));
  const original=output(sl,registry),actual=output(tl,registry),moved=transportNode(sl,tl,iso,original);
  assert.deepEqual(moved,actual);
  for(const label of labels){assert.deepEqual(moved.records[label].payload,registry[label]);payloadSentinels++;}
  views.push({binding:[p,e],section:view});example??={identification:iso,binding:[p,e],sourceOutput:original,transportedOutput:moved};
 }
 sections.push({chart:chart.id,views});reports.push({cone:cones[ci].id,translation:iso.translation,cellMap:iso.cellMap,
  translatedSharedFaces:iso.sharedFaces,localPaths:16,operationMapFromGeometryAlone:false});
}
let pairRestrictions=0,tripleRestrictions=0;const overlaps=[];let wrongSignWitness=null;
for(let i=0;i<sections.length;i++)for(let j=i+1;j<sections.length;j++){
 const a=sections[i],b=sections[j],aa=Object.values(a.views[0].section).map(r=>r.cell),bb=new Set(Object.values(b.views[0].section).map(r=>r.cell));
 const common=aa.filter(c=>bb.has(c)).sort();if(!common.length)continue;
 for(const av of a.views)for(const bv of b.views){
  assert.deepEqual(restrict(av.section,common),restrict(bv.section,common));pairRestrictions++;
  for(const cell of common){
   const la=Object.keys(av.section).find(k=>av.section[k].cell===cell),lb=Object.keys(bv.section).find(k=>bv.section[k].cell===cell);
   if(la!==lb&&!wrongSignWitness){
    assert.notDeepEqual(av.section[la].payload,bv.section[la].payload);
    wrongSignWitness={cell,left:{chart:a.chart,binding:av.binding,label:la},right:{chart:b.chart,binding:bv.binding,label:lb},
     correctMatchedPayload:av.section[la].payload,incorrectSameLabelPayload:bv.section[la].payload};
   }
  }
 }
 overlaps.push({left:a.chart,right:b.chart,referenceSupport:common,fullPacketIdentification:false});
 for(let k=j+1;k<sections.length;k++){
  const c=sections[k],cc=new Set(Object.values(c.views[0].section).map(r=>r.cell)),triple=common.filter(id=>cc.has(id));
  if(!triple.length)continue;
  const ab=restrict(a.views[0].section,common),abc=Object.fromEntries(triple.map(id=>[id,ab[id]]));
  assert.deepEqual(abc,restrict(a.views[0].section,triple));
  assert.deepEqual(abc,restrict(b.views[0].section,triple));assert.deepEqual(abc,restrict(c.views[0].section,triple));tripleRestrictions++;
 }
}
assert(pairRestrictions>0);assert(wrongSignWitness);
const referenceMultiplicity={};
for(const s of sections)for(const r of Object.values(s.views[0].section))
 (referenceMultiplicity[r.cell]??=[]).push(s.chart);
const maxReferenceMultiplicity=Math.max(...Object.values(referenceMultiplicity).map(xs=>xs.length));
assert.equal(maxReferenceMultiplicity,2);assert.equal(tripleRestrictions,0);
// No reference belongs to three distinct cones: triple restriction tests are
// vacuous here, not evidence for a higher operational coherence cell.
// Audit the cross-level contacts that reference-section descent does NOT settle.
const crossLevel=[];
for(let i=0;i<identifications.length;i++)for(let j=0;j<identifications.length;j++)if(i!==j){
 const a=identifications[i].chart,b=identifications[j].chart,refs=new Set([...b.P,...b.E]);
 for(const c of a.comparisons)if(refs.has(c.cell)){
  const joints=c.inputs.map(id=>a.joints.find(x=>x.cell===id));
  const recordSupport=[...new Set(joints.flatMap(x=>[x.P,x.E]))].sort();
  assert.equal(recordSupport.length,3);
  crossLevel.push({producerChart:a.id,consumerChart:b.id,cell:c.cell,
   producerType:{kind:'comparison',recordReferenceCells:recordSupport,retainedChildren:c.inputs},
   consumerType:{kind:'reference payload',referenceCell:c.cell},transitionFromExistingFibration:null});
 }
}
assert(crossLevel.length>0);
const sources=[root+'/su32-cone-operation-transport.mjs',root+'/checkers/check_su32_edge5_operadic_transport.mjs',
 root+'/su32-cyclic-port-fragment.mjs',root+'/su32-layer4-comparison.mjs',root+'/su32-signed-reference-encoder.mjs',
 root+'/su32-undirected-reference-attachment.mjs',root+'/su32-rooted-comparison-gluing.mjs'];
for(const p of sources)sourceHashes[p]=await digest(p);
const result={schema:'su32.edge5-operadic-transport.v1',passed:true,
 counts:{cones:44,chartsWithBindings:176,translatedPaths:44*16,constructorNaturality:naturality,segalReconstructions:reconstructions,
 arcDualityChecks:dualityChecks,cyclicGluingChecks:cyclicChecks,opaquePayloadSentinels:payloadSentinels,
 overlappingReferencePairs:overlaps.length,pairRestrictions,tripleRestrictions,maxReferenceMultiplicity,crossLevelContacts:crossLevel.length},
 tripleRestrictionStatus:'No nonempty triple reference overlaps. No higher cocycle test is claimed.',
 negativeControls:{reversedNativePathRejected:true,wrongNativeRoleRejected:true,edgeThreeAtlasGuardRetained:true,rawSignMatchingRefuted:true},
 testSectionStatus:'The cell-indexed opaque payload bank is a test section, not a source-selected physical state or global operational descent witness.',
 scope:'Geometry-certified local operation transport and reference-section overlap only. No global operational fibration or higher filler claimed.',
 coneIdentifications:reports,referenceOverlaps:overlaps,crossLevelContacts:crossLevel,example,wrongSignWitness,
 remaining:'Extract the existing fibration transition from an upstream comparison packet to a downstream reference fibre at each recorded cross-level contact; retain its context and test composition. No arbitrary payload reassignment was installed.',
 sourceHashes};
const dir=root+'/results/su32-edge5-operadic-transport-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({passed:true,counts:result.counts,scope:result.scope,remaining:result.remaining},null,2));
