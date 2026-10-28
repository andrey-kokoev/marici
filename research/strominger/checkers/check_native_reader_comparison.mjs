import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {GenerativeAssemblyRules,applyBatch} from '../native-retained-batch-attempt.mjs';
import {phaseFrame,phaseAdvanceWitness,activePhaseSlots} from '../demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const directory='research/strominger/results/native-reader-comparison';
const checks=[];function check(name,fn){fn();checks.push(name);}
const r=new GenerativeAssemblyRules();
const pn=r.outgoing(r.root).map(i=>r.operations[i]).find(o=>o.kind==='PN');
const ops=r.outgoing(pn.target).map(i=>r.operations[i]);
const ne=ops.find(o=>o.kind==='NE'),nn=ops.find(o=>o.kind==='NN-phase-advance');
const E=r.packets[ne.target],N=r.packets[nn.target],ec=r.charts[E.chart],nc=r.charts[N.chart];
const ef=phaseFrame(ec,E.origin),nf=phaseFrame(nc,N.origin);
// Row-permutation convention: map[p] sends vector v to v[p[i]].
const inverse=p=>p.map((_,i)=>p.indexOf(i));
const compose=(after,before)=>after.map(i=>before[i]);
const apply=(p,v)=>p.map(i=>v[i]);
const Q=compose(nn.permutation,inverse(ne.permutation));
const eState=applyBatch(r,[r.root,pn.target],[ne.id]);
const nState=applyBatch(r,[r.root,pn.target],[nn.id]);
check('same physical primitive, distinct admitted target charts',()=>{
 assert.equal(ec.cell,nc.cell);assert.equal(ec.species,'electron');assert.equal(nc.species,'neutron');
 assert.equal(eState.valid,true);assert.equal(nState.valid,true);
});
check('comparison derived from actual NN and inverse NE matrices',()=>{
 assert.deepEqual(Q,[0,3,1,4,2]);
 assert.deepEqual(compose(Q,E.permutation),N.permutation);
});
check('all five coordinates reconstruct through comparison and inverse',()=>{
 for(let j=0;j<5;j++){
  const v=Array.from({length:5},(_,i)=>Number(i===j));
  assert.deepEqual(apply(inverse(Q),apply(Q,v)),v);
  assert.deepEqual(apply(Q,apply(E.permutation,v)),apply(N.permutation,v));
 }
});
check('full norm preserved without identifying the two active readers',()=>{
 const v=[2,-3,5,-7,11];assert.equal(apply(Q,v).reduce((n,x)=>n+x*x,0),v.reduce((n,x)=>n+x*x,0));
});
const eOccurrences=[...ef.window,ef.context],nOccurrences=[...nf.window,nf.context];
const exact=eOccurrences.filter(e=>nOccurrences.some(n=>JSON.stringify(e)===JSON.stringify(n)));
const shifted=eOccurrences.map(e=>({from:e,to:nOccurrences.find(n=>n.vertex===e.vertex)})).filter(p=>p.to&&p.from.index!==p.to.index);
check('three occurrences agree exactly, fourth changes index on the same vertex',()=>{
 assert.equal(exact.length,3);assert.equal(shifted.length,1);
 assert.equal(shifted[0].from.role,'C');assert.equal(shifted[0].from.index,1);assert.equal(shifted[0].to.index,3);
});
const outside={electron:{vertex:ec.aliases.C0,index:E.origin},neutron:{vertex:nc.aliases.C0,index:N.origin}};
check('outside reference provenance is not identified by coefficient invertibility',()=>{
 assert.notEqual(outside.electron.vertex,outside.neutron.vertex);assert.notEqual(outside.electron.index,outside.neutron.index);
});
check('phase witness does not admit a cross-species re-reading',()=>{
 assert.throws(()=>phaseAdvanceWitness(ec,nc,E.origin),/matching P or N carriers/);
});
check('E has no outgoing native operation; inverse NE is algebraic recovery here',()=>{
 assert.deepEqual(r.outgoing(E.id),[]);
});
const activeE=activePhaseSlots.electron,activeN=activePhaseSlots.neutron;
const hidden=[0,1,0,0,0],after=apply(Q,hidden);
check('active E readout alone cannot determine active N readout',()=>{
 assert.deepEqual(activeE.map(i=>hidden[i]),[0,0,0]);
 assert.deepEqual(activeN.map(i=>after[i]),[0,1,0]);
});
check('the retained E complement recovers the missing target coordinate',()=>{
 const complement=[0,1,2,3,4].filter(i=>!activeE.includes(i));
 const recovered=Array(5).fill(0);for(const i of [...activeE,...complement])recovered[i]=hidden[i];
 assert.deepEqual(activeN.map(i=>apply(Q,recovered)[i]),[0,1,0]);
});
check('current assembly composition readout differs and cannot be declared invariant',()=>{
 assert.deepEqual(eState.inspection.counts,{proton:1,neutron:1,electron:1});
 assert.deepEqual(nState.inspection.counts,{proton:1,neutron:2,electron:0});
 assert.notDeepEqual(eState.inspection.counts,nState.inspection.counts);
});
check('coefficient equality does not erase the source occupation conflict',()=>{
 assert.equal(applyBatch(r,[r.root,pn.target],[ne.id,nn.id]).reason,'occupied-cell-species-conflict');
});
const attempt={comparisonPermutation:Q,inversePermutation:inverse(Q),sourceOperations:{PN:pn,NE:ne,NN:nn},
 targets:{electron:{packet:E,chart:ec,frame:ef},neutron:{packet:N,chart:nc,frame:nf}},
 exactOccurrences:exact,shiftedOccurrences:shifted,outsideReference:outside,
 readoutControl:{electronVector:hidden,neutronVector:after,electronActiveSlots:activeE,neutronActiveSlots:activeN,
 electronActive:activeE.map(i=>hidden[i]),neutronActive:activeN.map(i=>after[i])},
 composition:{electronAlternative:eState.inspection.counts,neutronAlternative:nState.inspection.counts},
 fullCoefficientComparisonEstablished:true,nativeCrossSpeciesArrowEstablished:false,
 currentCompositionReadoutPreserved:false,activeReaderOnlyFactorization:false,
 wholeAssemblyReaderInterpretationRefuted:false,fullPbConstructionEstablished:false,
 nextObligation:'Supply and test a particle-inventory readout distinct from reader chart species, with actual carrier/occurrence intertwiners. It must agree with the admitted physical interpretation rather than being defined constant solely to force invariance.'};
await fs.mkdir(path.join(root,directory),{recursive:true});
await fs.writeFile(path.join(root,directory,'comparison.json'),JSON.stringify(attempt,null,2)+'\n');
const sourceHashes={};
const priorPath='research/strominger/results/native-retained-batch-attempt/verification.json';
const prior=JSON.parse(await fs.readFile(path.join(root,priorPath),'utf8'));
for(const [p,digest] of Object.entries(prior.sourceHashes))assert.equal(crypto.createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex'),digest,'stale source '+p);
for(const p of [priorPath,...Object.keys(prior.sourceHashes),'research/strominger/checkers/check_native_reader_comparison.mjs','research/strominger/native-reader-comparison-v1.md',directory+'/comparison.json'])sourceHashes[p]=crypto.createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex');
const report={status:'passed',check_count:checks.length,checks,sourceHashes,
 fullCoefficientComparisonEstablished:true,nativeCrossSpeciesArrowEstablished:false,currentCompositionReadoutPreserved:false,
 activeReaderOnlyFactorization:false,wholeAssemblyReaderInterpretationRefuted:false,fullPbConstructionEstablished:false};
await fs.writeFile(path.join(root,directory,'verification.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:report.status,checks:checks.length,comparison:Q,composition:attempt.composition}));
