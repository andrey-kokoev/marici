import test from 'node:test';
import assert from 'node:assert/strict';
import {a4Cell,closedAtTriangle,geometryStudy,transportStudy,compose} from '../research/realization-tower/assembly-approaches.mjs';
const identity=[0,1,2,3,4],key=p=>p.join(','),sorted=ps=>ps.map(key).sort();
const permutations=xs=>xs.length?xs.flatMap((x,i)=>permutations(xs.filter((_,j)=>j!==i)).map(p=>[x,...p])):[[]];
test('marked simplex has four ports and the fixed A4 neighbor is rectified, not another regular simplex',()=>{
 const g=geometryStudy(),m=g.markedInterface;
 assert.equal(m.seed.q,1);assert.equal(m.seed.vertices.length,5);assert.equal(m.ports.length,4);
 assert.equal(m.continuation.q,2);assert.equal(m.continuation.vertices.length,10);assert.equal(m.sharedFacet.length,4);assert.equal(m.oppositeSection.length,6);
 assert.deepEqual(sorted(m.ports.map(p=>p.endpoint)),sorted(m.sharedFacet));
 for(const p of m.ports)assert.equal(p.endpoint.reduce((s,x,i)=>s+(x-p.apex[i])**2,0),2);
 assert(g.dual.negationMatches);assert.equal(g.dual.seed.q,4);assert.equal(g.dual.continuation.q,3);
 assert.throws(()=>a4Cell([0,0,0,0,0]));
});
test('all 15 nonempty subsets of the fixed triangle star have exactly one closed completion',()=>{
 const g=geometryStudy();assert.deepEqual(g.star.map(c=>c.q),[1,2,2,3]);assert.equal(g.triangle.length,3);assert.equal(g.interfaces.length,4);
 assert.equal(g.closedSubsets.length,1);assert.deepEqual(g.closedSubsets[0],g.star.map(c=>c.floor));
 assert(Math.abs(g.angleSum-2*Math.PI)<1e-12);
 for(let i=0;i<4;i++)assert(!closedAtTriangle(g.star.filter((_,j)=>i!==j),g.triangle));
 assert(!closedAtTriangle([g.star[0],g.star[0]],g.triangle),'Duplicated occupancy is not closure');
});
test('coordinate relabellings preserve the chamber construction, without cell-ID tie breaking',()=>{
 const g=geometryStudy();let count=0;
 for(const p of permutations(identity))for(const c of g.star){
  const relabel=v=>p.map(i=>v[i]);assert.deepEqual(sorted(a4Cell(relabel(c.floor)).vertices),sorted(c.vertices.map(relabel)));count++;
 }
 assert.equal(count,480);
});
test('actual He4 has four chart-simple exit paths; same endpoint does not identify their transport',()=>{
 const t=transportStudy();assert.equal(new Set(t.charts.map(c=>c.cell)).size,6);assert.equal(t.charts.length,10);assert.equal(t.paths.length,4);
 assert.deepEqual(t.paths.map(p=>p.origin),[0,1,3,4]);assert.equal(t.sameEndpointComparisons.length,2);
 assert(t.sameEndpointComparisons.every(c=>!c.sameCoefficients&&c.originDifference>0&&!c.nativeComparisonSupplied));
 for(const comparison of t.sameEndpointComparisons){const a=t.paths[comparison.fromPath],b=t.paths[comparison.toPath];assert.deepEqual(compose(comparison.coefficientComparison,a.permutation),b.permutation);}
 for(const p of t.paths){assert.equal(new Set(p.charts).size,p.charts.length);p.edges.forEach((e,i)=>{assert.equal(t.edges[e].from,p.charts[i]);assert.equal(t.edges[e].to,p.charts[i+1]);});}
});
test('electron comparison square has a coefficient solution but no admitted electron reader lift',()=>{
 const t=transportStudy(),s=t.electronSquare;
 assert.deepEqual(s.left,s.right);assert(s.nativeReaderRejected);assert(!s.nativeDirectEdgeExists);assert.equal(t.reverseElectronEdges,0);
 assert.notDeepEqual(t.algebra.DR,t.algebra.RD);assert.deepEqual(t.algebra.D2,identity);assert.deepEqual(t.algebra.commonFixedSlots,[]);
 assert.notDeepEqual(compose(t.algebra.R,t.algebra.C),s.right,'Copying the N reader map to E is not the derived square');
 assert.notDeepEqual(t.algebra.C,s.right,'An identity E edge cannot close the square');
 for(let i=0;i<5;i++){
  const basis=identity.map(j=>i===j?1:0),apply=(p,v)=>p.map(j=>v[j]);
  assert.deepEqual(apply(s.candidateMap,apply(t.algebra.C,basis)),apply(t.algebra.C,apply(t.algebra.R,basis)));
 }
 assert.deepEqual(t.readerRoundTrip.permutation,identity);assert.equal(t.readerRoundTrip.originAdvance,2);
});
