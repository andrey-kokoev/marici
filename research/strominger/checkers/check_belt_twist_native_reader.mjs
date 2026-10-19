// Compare belt-chart monodromy with native marked N reader geometry.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
const files={interface:'research/strominger/results/neutron-reader-field-interface/verification.json',metrics:'research/strominger/results/T-metric-gluing/verification.json',seeds:'research/strominger/results/hydrogen-edge-attachment/verification.json'},inputs={},hashes={};for(const [k,f] of Object.entries(files)){const b=await readFile(f);inputs[k]=JSON.parse(b);hashes[f]=createHash('sha256').update(b).digest('hex');}
const vertices=['b','c','u','v'],identity=Object.fromEntries(vertices.map(v=>[v,v])),H=inputs.interface.properPermutationLoop.vertexMonodromy,K={b:'v',v:'b',u:'c',c:'u'},alias={b:'M0',u:'C1',v:'M1',c:'C2'},same=(a,b)=>vertices.every(v=>a[v]===b[v]);
// Four markings preserve the two-face arrangement as an unordered face pair:
// either order on the core edge, and either order on the two outer vertices.
const markingChoices=[];
for(const flipCore of [false,true])for(const flipOuter of [false,true]){
 const q={...identity};if(flipCore){q.u='v';q.v='u';}if(flipOuter){q.b='c';q.c='b';}
 const monodromy=Object.fromEntries(vertices.map(v=>[v,q[H[q[v]]]]));
 markingChoices.push({flipCore,flipOuter,monodromy,matchesNativeAdvance:same(monodromy,K)});
}
assert.equal(markingChoices.filter(m=>m.matchesNativeAdvance).length,2);
const rows=[];
for(const sample of inputs.seeds.rows){
 const r=new GenerativeAssemblyRules({seedBindings:sample.seedBindings}),pn=r.outgoing(r.root).map(i=>r.operations[i]).find(o=>o.kind==='PN'),n=r.packets[pn.target],chart=r.charts[n.chart];
 const advance=r.outgoing(pn.target).map(i=>r.operations[i]).find(o=>o.kind==='reader-phase-advance');
 const metric=inputs.metrics.rows.find(x=>JSON.stringify(x.marking)===JSON.stringify(sample.marking)).metric;
 const key=(a,b)=>[a,b].sort().join('|');let preservesMetric=true;
 for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)if(metric[key(vertices[i],vertices[j])]!==metric[key(K[vertices[i]],K[vertices[j]])])preservesMetric=false;
 assert.equal(Boolean(advance),preservesMetric);
 let witness=null;
 if(advance){
  r.validateTransfer(advance);const target=r.packets[advance.target],next=r.charts[target.chart],actual={};
  for(const v of vertices)actual[v]=vertices.find(w=>chart.aliases[alias[w]]===next.aliases[alias[v]]);
  assert.ok(same(actual,K));assert.equal(target.origin,n.origin+1);assert.equal(next.cell,chart.cell);
  const second=r.outgoing(target.id??advance.target).map(i=>r.operations[i]).find(o=>o.kind==='reader-phase-advance');assert.ok(second);r.validateTransfer(second);const end=r.packets[second.target],endChart=r.charts[end.chart];assert.equal(end.origin,n.origin+2);for(const v of vertices)assert.equal(endChart.aliases[alias[v]],chart.aliases[alias[v]]);
  witness={geometricPermutation:actual,originDelta:1,coefficientPermutation:advance.permutation??null,twoAdvancesRestoreFourVertexGeometry:true,twoAdvancesOriginDelta:2};
 }
 rows.push({marking:sample.marking,nativeAdvanceAvailable:Boolean(advance),candidateTwistPreservesMetric:preservesMetric,witness});
}
const admitted=rows.filter(r=>r.nativeAdvanceAvailable).length;assert.equal(admitted,8);
const self='research/strominger/checkers/check_belt_twist_native_reader.mjs';for(const f of [self,'research/nima/generative-phase-assembly.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs'])hashes[f]=createHash('sha256').update(await readFile(f)).digest('hex');
const out='research/strominger/results/belt-twist-native-reader';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify({status:'belt-chart-twist-matches-admitted-native-reader-geometry',nativeGeometricTwist:K,markingChoices,rows,admitted,sourceHashes:hashes,scope:'Matches finite marked-vertex monodromy, after explicitly constrained chart marking, with native same-body N reader advance in 8/24 seeds. Those and only those 8 preserve the N facet metric under this twist in this sample. No native operation traversing the belt chart loop has been supplied: equal endpoint permutations do not identify paths, origin increments or coefficient actions. No derived action on 36 field components, global PNE sewing, physical twist or production change.'},null,2)+'\n');console.log(JSON.stringify({status:'passed',compatibleMarkings:2,markingChoices:4,nativeReaderCases:admitted,totalSeeds:rows.length,metricGateAgreesExactly:true}));
