import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildBranchingSeed} from '../research/realization-tower/branching-seed.mjs';
import {buildBeryllium8Reference} from '../research/realization-tower/beryllium-8-reference.mjs';
import {traceSeedConductors} from '../research/realization-tower/seed-retained-conductors.mjs';
import {buildSulfurRouteComparison,projectComparisonColumns} from '../research/realization-tower/sulfur-route-comparison.mjs';
const model=buildBranchingSeed({processId:'beryllium-8'}),reference=buildBeryllium8Reference();
test('depth four regenerates geometry, pair count, sleeves, and reflection centre; keeps eight copy histories',()=>{
 const a=model.audit;assert.equal(a.depth,4);assert.equal(a.layers,8);assert.equal(a.edgeLayers,8);
 assert.equal(a.edges,240);assert.equal(a.nodes,200);assert.equal(a.whiteEdges,80);assert.equal(a.paths,128);
 assert.deepEqual(a.reflectionCenter,[0,-3.5,-1]);assert.equal(model.sidePairs.length,32);
 for(const pair of model.sidePairs){assert.equal(pair.totalHeight,6);assert.equal(pair.bands.length,8);assert.equal(pair.bands.filter(b=>b.role==='white').length,4);}
 for(const layer of model.layers){const trace=traceSeedConductors(layer);assert.deepEqual(trace.counts,{bottomSleeves:4,conductors:8,rooted:8,coveredEdges:30,totalEdges:30});}
 assert.equal(buildBranchingSeed().audit.depth,8);assert.equal(buildBranchingSeed().sidePairs.length,64);
});
test('reference is eight unique retained three-bit routes, all on the unit octahedral edge graph',()=>{
 assert.equal(reference.strands.length,8);assert.equal(new Set(reference.strands.map(s=>s.id)).size,8);
 assert.equal(new Set(reference.strands.map(s=>JSON.stringify(s.guide))).size,8);
 assert.equal(reference.edges.length,12);
 for(const edge of reference.edges){
  assert.equal(edge.strandIds.length,2);assert.equal(new Set(edge.strandIds).size,2);
  assert.equal(edge.guide[0].reduce((sum,x,i)=>sum+(x-edge.guide[1][i])**2,0),2);
 }
 for(const s of reference.strands){
  assert.equal(s.guide.length,4);assert.equal(s.edgeIds.length,3);
  assert.deepEqual(Object.keys(s.polarities),['t','p','e']);
  assert.deepEqual(s.guide[0],reference.envelope[1]);assert.deepEqual(s.guide.at(-1),reference.envelope[0]);
  const target=reference.strands[s.outputSlot];assert.equal(target.polarities.t,s.polarities.t);
  assert.equal(['p','e'].filter(k=>target.polarities[k]!==s.polarities[k]).length,1);
 }
});
test('eight-by-eight routing matrix is bijective, reversible, and a controlled four-cycle',()=>{
 const P=reference.permutation,n=8;assert.equal(P.length,n);assert.deepEqual(reference.matrixBasis,reference.strands.map(s=>s.id));
 for(let i=0;i<n;i++){
  assert.equal(P[i].reduce((a,b)=>a+b,0),1);assert.equal(P.reduce((a,r)=>a+r[i],0),1);
  assert(P[i].every(v=>v===0||v===1));assert.equal(P[reference.strands[i].outputSlot][i],1);
  let j=i;for(let k=0;k<4;k++)j=reference.strands[j].outputSlot;assert.equal(j,i);
  const twice=reference.strands[reference.strands[i].outputSlot].outputSlot;assert.notEqual(twice,i);
  for(const bit of ['p','e'])assert.notEqual(reference.strands[twice].polarities[bit],reference.strands[i].polarities[bit]);
 }
});
test('Be reference is independent of selected layer paths and continuation rule; both panels use eight columns',()=>{
 const one=buildSulfurRouteComparison(model,{rule:'same-colour',visibleLayers:[true,false,false,false,false,false,false,false]}),all=buildSulfurRouteComparison(model,{rule:'cross-colour'});
 assert.equal(one.reference.length,8);assert.equal(one.combined.length,8);assert.equal(all.counts.sourceCopies,64);
 assert.deepEqual(one.reference,all.reference);assert(one.reference.every(s=>s.id.startsWith('be8:wire:')));
 assert.equal(one.correspondenceEstablished,false);
 const top=projectComparisonColumns(one.reference),bottom=projectComparisonColumns(one.combined);
 assert.deepEqual(top.map(s=>s.x),bottom.map(s=>s.x));
 for(const s of [...top,...bottom])for(const path of s.paths)for(const p of path.coordinates)assert(p.every(Number.isFinite));
 assert.equal(buildSulfurRouteComparison(model,{rule:'pending'}).combined.length,0);
});
