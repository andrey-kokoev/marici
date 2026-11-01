import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildBranchingSeed} from '../research/realization-tower/branching-seed.mjs';
import {buildSulfurIncomingBundle} from '../research/realization-tower/sulfur-32-incoming-bundle.mjs';
import {buildSulfurRouteComparison,projectComparisonColumns} from '../research/realization-tower/sulfur-route-comparison.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
import {createBranchingSeed} from '../examples/normal-ray/branching-seed-renderer.js';
const seed=buildBranchingSeed(),reference=buildSulfurIncomingBundle(),mask=ids=>Array.from({length:8},(_,i)=>ids.includes(i+1));
const build=(ids,rule='same-colour')=>buildSulfurRouteComparison(seed,{reference,visibleLayers:mask(ids),rule});
test('reference retains exactly the existing sixteen native identities, complete guides and output permutation',()=>{
 const c=build([1]);assert.equal(c.reference.length,16);
 for(const [i,s]of c.reference.entries()){
  assert.equal(s.id,reference.strands[i].id);assert.deepEqual(s.guide,reference.strands[i].guide);assert.deepEqual(s.edgeIds,reference.strands[i].edgeIds);assert.equal(s.outputSlot,reference.strands[i].outputSlot);
 }
 assert.deepEqual(c.reference,build([2,7,8],'cross-colour').reference);assert.equal(c.correspondenceEstablished,false);
});
test('pending rule and no selected layers produce no invented combined paths',()=>{
 assert.equal(build([1],'pending').status,'rule-pending');assert.deepEqual(build([1],'pending').combined,[]);
 assert.equal(build([]).status,'no-visible-layers');assert.deepEqual(build([]).combined,[]);
 assert.throws(()=>build([1],'fabricated-rule'));
});
test('combined preserves sixteen source identities while deduplicating only their full directed projected copies',()=>{
 for(const [ids,copies,paths]of [[[1],16,16],[[1,7],32,32],[[1,2,3,4,5,6,7,8],128,64]]){
  const c=build(ids);assert.deepEqual(c.counts,{referenceStrands:16,combinedStrands:16,sourceCopies:copies,projectedPaths:paths});
  assert.deepEqual(c.sourceLayers,ids);assert.equal(new Set(c.combined.map(s=>s.id)).size,16);
  for(const s of c.combined){
   assert(!s.id.startsWith('wire:'));assert.deepEqual(s.paths.flatMap(p=>p.sourceLayers).sort((a,b)=>a-b),ids);
   for(const copy of s.copies)assert(seed.layers[copy.layer-1].routes.some(r=>JSON.stringify(r.edges)===JSON.stringify(copy.edges)));
  }
 }
});
test('rule changes real routes rather than reference labels; spacing and by-layer display do not affect calculation',()=>{
 const a=build([1]),b=build([1],'cross-colour');assert(a.combined.some((s,i)=>s.copies[0].word!==b.combined[i].copies[0].word));
 const changed=buildSulfurRouteComparison(buildBranchingSeed({seedLayerGap:6,seedPairsByLayer:false}),{reference,visibleLayers:mask([1]),rule:'same-colour'});
 assert.deepEqual(a,changed);
});
test('both panels use the same sixteen column positions, with finite actual-path projections',()=>{
 const c=build([1,2,7,8]),a=projectComparisonColumns(c.reference),b=projectComparisonColumns(c.combined);
 assert.deepEqual(a.map(s=>s.x),b.map(s=>s.x));
 for(const s of [...a,...b])for(const path of s.paths)for(const [x,y]of path.coordinates){assert(Number.isFinite(x)&&Number.isFinite(y));assert(x>=s.x-18&&x<=s.x+18);assert(y>=32&&y<=176);}
});
test('comparison no longer adds fabricated pair banks or camera bounds to the 3D seed',()=>{
 const g=createBranchingSeed(seed,{seedPairsByLayer:false,seedPairsCombined:true,seedVisibleLayers:mask([1])});
 assert.equal(g.userData.audit.sidePairs,0);assert.equal(g.userData.audit.combinedDisplay,'separate route-comparison panel');
 assert(!g.children.some(o=>o.userData.combinedPath||o.userData.combinedSleeve));
 assert.deepEqual(buildBranchingSeed({seedPairsCombined:true}).envelope,buildBranchingSeed({seedPairsCombined:false}).envelope);
 g.traverse(o=>{o.geometry?.dispose();if(o.material)(Array.isArray(o.material)?o.material:[o.material]).forEach(m=>m.dispose());});
});
test('independent reference and combined toggles and explicit rule survive settings normalization',()=>{
 const defaults=normalizeSceneSettings({}).appearance;assert.equal(defaults.seedShowReference,false);assert.equal(defaults.seedComparisonRule,'pending');
 for(const ref of [false,true])for(const combined of [false,true])for(const rule of ['pending','same-colour','cross-colour']){
  const a=normalizeSceneSettings({appearance:{seedShowReference:ref,seedPairsCombined:combined,seedComparisonRule:rule}}).appearance;
  assert.equal(a.seedShowReference,ref);assert.equal(a.seedPairsCombined,combined);assert.equal(a.seedComparisonRule,rule);
 }
 assert.equal(normalizeSceneSettings({appearance:{seedComparisonRule:'unknown'}}).appearance.seedComparisonRule,'pending');
});
