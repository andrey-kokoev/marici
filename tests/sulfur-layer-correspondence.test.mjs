import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildBranchingSeed} from '../research/realization-tower/branching-seed.mjs';
import {traceSeedConductors} from '../research/realization-tower/seed-retained-conductors.mjs';
import {buildSulfurIncomingBundle} from '../research/realization-tower/sulfur-32-incoming-bundle.mjs';
import {checkRouteBundleCapacity} from '../research/realization-tower/route-bundle-invariants.mjs';
const seed=buildBranchingSeed(),source=traceSeedConductors(seed.layers[0]),native=buildSulfurIncomingBundle();
const sourceEdges=trace=>trace.memberships.map(e=>({id:e.edge,strands:e.strands}));
const targetEdges=native.edges.map(e=>({id:e.id,strands:e.strandIds}));
test('bottom sleeves give sixteen distinct actual root-to-boundary conductor paths covering the whole layer',()=>{
 assert.deepEqual(source.counts,{bottomSleeves:8,conductors:16,rooted:16,coveredEdges:108,totalEdges:108});
 assert.equal(new Set(source.strands.map(s=>s.edgeIds.join('|'))).size,16);
 for(const s of source.strands){
  assert(seed.layers[0].routes.some(r=>JSON.stringify(r.edges)===JSON.stringify(s.edgeIds)));
  assert.equal(s.edgeIds.length,16);assert(s.events.every(e=>e.kind==='sole-boundary-trunk'));
  assert(s.word.split('').slice(1).filter((c,i)=>c!==s.word[i]).length<=1);
 }
 for(const sleeve of source.bottomSleeves)assert.equal(source.memberships.find(e=>e.edge===sleeve).strands.length,2);
 for(const node of seed.layers[0].nodes){
  const into=source.memberships.filter(e=>e.to===node.id).reduce((n,e)=>n+e.strands.length,0),out=source.memberships.filter(e=>e.from===node.id).reduce((n,e)=>n+e.strands.length,0);
  if(into&&out)assert.equal(into,out);
 }
});
test('all reflected layers transport the same sixteen template identities and full edge ancestry',()=>{
 for(const layer of seed.layers){
  const trace=traceSeedConductors(layer);assert.deepEqual(trace.counts,source.counts);
  for(const s of trace.strands)assert.deepEqual(s.canonicalEdges,source.strands.find(p=>p.id===s.id).canonicalEdges);
 }
});
test('sixteen paths and full edge coverage do not uniquely determine sleeve routing',()=>{
 const other=traceSeedConductors(seed.layers[0],{interiorRouting:'cross-colour'});
 assert.deepEqual(other.counts,source.counts);
 assert(other.strands.some(s=>s.word!==source.strands.find(p=>p.id===s.id).word));
 for(const s of other.strands)assert(seed.layers[0].routes.some(r=>JSON.stringify(r.edges)===JSON.stringify(s.edgeIds)));
 assert.equal(checkRouteBundleCapacity(sourceEdges(other),targetEdges).source.bySize[4],2);
});
test('native shared-route bundles obstruct a fixed route-preserving relabelling, not just a path-length match',()=>{
 const check=checkRouteBundleCapacity(sourceEdges(source),targetEdges);
 assert.equal(check.source.bySize[4],2);assert.equal(check.target.bySize[4],10);
 assert.equal(check.source.bySize[2],23);assert.equal(check.target.bySize[2],32);
 assert.equal(check.necessaryConditionsSatisfied,false);
 assert.deepEqual(check.obstructions,[{size:2,availableSourceGroups:23,requiredTargetGroups:32},{size:4,availableSourceGroups:2,requiredTargetGroups:10}]);
});
test('the obstruction survives arbitrary ID renaming and subdivision; the checker admits its positive control',()=>{
 const edges=sourceEdges(source),renamed=edges.flatMap((e,i)=>[0,1].map(j=>({id:`split:${i}:${j}`,strands:e.strands.map(s=>'opaque '+source.strands.findIndex(r=>r.id===s))})));
 const self=checkRouteBundleCapacity(edges,renamed);assert.equal(self.necessaryConditionsSatisfied,true);
 const failed=checkRouteBundleCapacity(renamed,targetEdges);assert.equal(failed.necessaryConditionsSatisfied,false);
 assert.deepEqual(failed.source.bySize,self.source.bySize);
});
