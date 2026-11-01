import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,channelOperand,compareAt} from '../su32-layer4-comparison.mjs';
import {identifyCone,targetFixture} from '../su32-cone-operation-transport.mjs';
import {attachReference} from '../su32-cross-cone-reference-fibre.mjs';
import {tree,contour,gaps,contract,normal,rootLifts,boundaryOperation,canonicalCycle} from '../su32-operadic-boundary-span.mjs';
const root='research/strominger',paths={source:root+'/results/su32-hopf-tests-v1/fixture.json',
 carrier:root+'/results/su32-edge5-extension-contract-v1/verification.json',
 attachment:root+'/results/su32-cross-cone-reference-fibre-v1/verification.json',
 contract:root+'/contracts/su32-boundary-composition-span-v1.json'};
const digest=async p=>createHash('sha256').update(await fs.readFile(p)).digest('hex');
const docs={},sourceHashes={};for(const [k,p] of Object.entries(paths)){
 docs[k]=JSON.parse(await fs.readFile(p,'utf8'));sourceHashes[p]=await digest(p);
 for(const [s,h] of Object.entries(docs[k].sourceHashes??{}))assert.equal(await digest(s),h,`Stale ${s}`);
}
const source=docs.source,carrier=docs.carrier.edge5Carrier,sa=buildSu32SignedReferenceAtlas(source);
const reading=source.readings.find(r=>r.id==='reading:0:-1'),sc=sa.charts.find(c=>c.reading===reading.id&&c.source===reading.incomingN);
const sourceCone=reading.cones.find(c=>c.source===sc.source&&c.target===sc.target);
const atlas={charts:carrier.comparisonCones.map(c=>identifyCone(source,sc,sourceCone,carrier,c).chart),globalAssignment:null};
const chartById=new Map(atlas.charts.map(c=>[c.id,c])),fixture=targetFixture(carrier),bindings=[[0,0],[0,1],[1,0],[1,1]];
const layouts=new Map();for(const c of atlas.charts)for(const b of bindings)layouts.set(JSON.stringify([c.id,b]),comparisonLayout(atlas,fixture,c.id,b));
const layout=(c,b)=>layouts.get(JSON.stringify([c,b]));
// Construct the entire geometric motif family before evaluating a decoration.
const motifs=docs.attachment.family.flatMap(c=>c.attachments.map(a=>{
 const target=chartById.get(c.consumerChart),j=target.joints.find(x=>x.cell===a.joint),role=j.P===c.cell?'P':'E';
 const ds=target.comparisons.filter(d=>d.inputs.includes(j.cell)&&d.varyingRole===role);assert.equal(ds.length,1);const d=ds[0];
 const face=carrier.faces.filter(f=>f.owners.length===2&&f.owners.includes(j.cell)&&f.owners.includes(d.cell));assert.equal(face.length,1);
 const other=d.inputs.find(x=>x!==j.cell),otherJoint=target.joints.find(x=>x.cell===other);
 assert(![otherJoint.P,otherJoint.E].includes(c.cell),'No hidden duplicate of the producer in the other boundary input');
 return {producerChart:c.producerChart,consumerChart:c.consumerChart,producerCell:c.cell,joint:j.cell,downstreamComparison:d.cell,
  otherChannel:other,internalFaces:[a.face,face[0].id],sourceGenerators:['compareAt','channelOperand restricted by producer context','compareAt']};
}));assert.equal(motifs.length,448);
// The two-edge retained-subset poset has 4 vertices, 5 strict comparable pairs,
// and 2 nondegenerate triangles. Its contraction diagram has opposite variance.
const comparable=[];for(let a=0;a<4;a++)for(let b=0;b<4;b++)if(a!==b&&(a&b)===a)comparable.push([a,b]);
assert.equal(comparable.length,5);const triangles=[[0,1,3],[0,2,3]];
let contractionSquares=0,gapPreservations=0,rootLiftChecks=0;const planarExamples=[];
for(let profile=0;profile<8;profile++){
 const t=tree(profile),u=contract(t,'u'),v=contract(t,'v'),uv=contract(u,'v'),vu=contract(v,'u');
 assert.deepEqual(normal(uv),normal(vu));contractionSquares++;
 for(const state of [t,u,v,uv]){
  assert.deepEqual(contour(state),contour(t));assert.deepEqual(gaps(state),gaps(t));gapPreservations++;
  for(const root of contour(t))rootLiftChecks+=rootLifts(state,root).length;
 }
 const reverse=tree(profile^7);assert.deepEqual(contour(reverse),canonicalCycle([...contour(t)].reverse()));
 const ports=contour(t),gs=gaps(t);for(let shift=0;shift<5;shift++){
  const rotated=[...ports.slice(shift),...ports.slice(0,shift)];
  assert.deepEqual(rotated.map((a,i)=>[a,rotated[(i+1)%5]]),[...gs.slice(shift),...gs.slice(0,shift)]);
 }
 planarExamples.push({profile,boundary:contour(t),gaps:gaps(t),retainedEdgeStates:[normal(uv),normal(v),normal(u),normal(t)]});
}
assert.notDeepEqual(contour(tree(0)),contour(tree(1)));
let sourceSquares=0,restrictionRoundTrips=0,mismatchControls=0;let example=null;
const labels=['P+','P-','E+','E-'];
for(const motif of motifs)for(const sb of bindings)for(const tb of bindings){
 const sl=layout(motif.producerChart,sb),tl=layout(motif.consumerChart,tb);
 const c=sl.template.comparisons.find(c=>c.cell===motif.producerCell),d=tl.template.comparisons.find(d=>d.cell===motif.downstreamComparison);
 const selected=tl.template.referenceBinding[motif.producerCell],joint=tl.template.channels.find(j=>j.cell===motif.joint);
 const other=[joint.P,joint.E].find(r=>r.referenceCell!==motif.producerCell);
 const C=(a,b)=>compareAt(sl,c.cell,a,b);
 const J=(p,z)=>attachReference(sl,tl,c.cell,motif.joint,p,z);
 const D=(j,k)=>compareAt(tl,d.cell,...d.inputs.map(id=>id===motif.joint?j:k));
 for(let sample=0;sample<2;sample++){
  const registry=Object.fromEntries(labels.map((l,i)=>[l,sample===0?null:{slot:i,opaque:[sc.source,false]}]));
  const [a,b]=c.inputs.map(id=>channelOperand(sl,id,registry)),p=C(a,b),z=sample===0?false:{externalReference:other.referenceCell};
  const targetRegistry=Object.fromEntries(labels.map((l,i)=>[l,{external:i}]));targetRegistry[other.record]=z;
  const k=channelOperand(tl,motif.otherChannel,targetRegistry),j=J(p,z),out=D(j,k);
  // Right-hand map denotes this operation on admissible inputs, not out as a
  // global static fibre value. Both contraction orders evaluate the same program.
  const CJ=(a,b,z)=>J(C(a,b),z),JD=(p,z,k)=>D(J(p,z),k);
  assert.deepEqual(D(CJ(a,b,z),k),out);assert.deepEqual(JD(C(a,b),z,k),out);sourceSquares++;
  const rows={C:[a,b,p],J:[p,z,j],D:[j,k,out]};
  const sew=rows=>{
   assert.deepEqual(rows.C[2],rows.J[0],'Full first internal point mismatch');
   assert.deepEqual(rows.J[2],rows.D[0],'Full second internal point mismatch');
   assert.deepEqual(C(...rows.C.slice(0,2)),rows.C[2]);assert.deepEqual(J(...rows.J.slice(0,2)),rows.J[2]);assert.deepEqual(D(...rows.D.slice(0,2)),rows.D[2]);
   return {a:rows.C[0],b:rows.C[1],p:rows.C[2],z:rows.J[1],j:rows.J[2],k:rows.D[1],out:rows.D[2]};
  };
  const whole=sew(rows);assert.deepEqual(whole,{a,b,p,z,j,k,out});
  assert.deepEqual({C:[whole.a,whole.b,whole.p],J:[whole.p,whole.z,whole.j],D:[whole.j,whole.k,whole.out]},rows);restrictionRoundTrips++;
  const bad={...rows,J:[false,z,j]};assert.throws(()=>sew(bad),/internal point mismatch/);mismatchControls++;
  example??={motif,binding:{source:sb,target:tb},compatibleDecoration:whole,
   boundaryOperation:boundaryOperation(tree(0),motif),
   interpretation:'The operation definition and decoration are retained; neither is identified with a static wire payload.'};
 }
}
const sources=[root+'/su32-operadic-boundary-span.mjs',root+'/checkers/check_su32_boundary_composition_span.mjs',
 root+'/su32-layer4-comparison.mjs',root+'/su32-cross-cone-reference-fibre.mjs',root+'/su32-cone-operation-transport.mjs',
 root+'/su32-signed-reference-encoder.mjs','references/2506.15622v2.pdf'];for(const p of sources)sourceHashes[p]=await digest(p);
const result={schema:'su32.boundary-composition-span.v1',passed:true,
 counts:{motifs:motifs.length,sourceCompositionSquares:sourceSquares,restrictionRoundTrips,mismatchControls,
 formalPlanarStructures:8,templateContractionSquares:contractionSquares,templateGapPreservations:gapPreservations,templateRootLifts:rootLiftChecks},
 cube:{retainedEdgeSubsets:[[],['u'],['v'],['u','v']],strictComparablePairs:comparable,triangles,contractionOrder:'Opposite to retained-edge inclusion.'},
 conclusion:'A finite source-generated operation span and its two-edge contraction coherence are checked. The boundary result is an operation, not a self-containing content value.',
 limits:['Uses the existing candidate context-refined reference attachment; its native global identification remains unproved.',
 'The right-hand operation lies in a formal source-generated envelope. Identification with the intended native boundary-corolla fibre remains open.',
 'Gaps and cyclic orders are computed for eight declared planar structures; no physical channel-content interpretation or native planar choice is inferred.',
 'Finite three-vertex tests are not an arbitrary-tree cyclic infinity operad or a repair of the static JSON identification.'],
 motifs,planarExamples,example,sourceHashes};
const dir=root+'/results/su32-boundary-composition-span-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({passed:true,counts:result.counts,conclusion:result.conclusion,limits:result.limits},null,2));
