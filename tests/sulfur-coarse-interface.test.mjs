import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildBranchingSeed} from '../research/realization-tower/branching-seed.mjs';
import {coarsenWhiteBranchLayer,planeSimilarity} from '../research/realization-tower/sulfur-coarse-interface.mjs';
import {runCoarseInterfaceProbe} from '../scripts/lib/sulfur-coarse-interface-probe.mjs';
const probe=await runCoarseInterfaceProbe();
test('white contraction gives directed two-edge chords with 60-degree incoming arms',()=>{
 for(const layer of buildBranchingSeed().layers){
  const c=coarsenWhiteBranchLayer(layer);assert.equal(c.nodes.length,45);assert.equal(c.edges.length,72);
  for(const e of c.edges){const [w,b]=e.constituents.map(id=>layer.edges.find(x=>x.id===id));assert.equal(w.role,'white');assert.equal(w.to,b.from);assert.equal(w.from,e.from);assert.equal(b.to,e.to);}
 }
 for(const l of probe.layers){assert(l.metric.armSquaredLengths.every(x=>Math.abs(x-3)<1e-10));assert(Math.abs(l.metric.incomingCosine-.5)<1e-10);assert.equal(l.metric.outgoingAreStraightContinuations,true);}
});
test('either port assignment matches all four native joins, using incoming geometry only',()=>{
 assert.equal(probe.alignments.length,64);
 for(const a of probe.alignments){assert.equal(a.carrierHeadsMatch,true);assert(Math.abs(a.scaleSquared-2/3)<1e-10);}
 // A valid two-port map is not a selected, labelled wiring correspondence.
 assert.equal(probe.summary.unlabelledMetricAlignments,64);
});
test('the two-diamond return family has four states but is not a closed four-record channel',()=>{
 for(const l of probe.layers){
  assert.deepEqual(l.counts,{allArrivals:6,selectedArrivals:4,bypassingArrivals:2,escapingAnchorHistories:4});
  assert.equal(l.anchor.depth,2);assert.equal(l.target.depth,4);assert.equal(l.closedChannel,false);
  assert.deepEqual(l.selectedStates.map(r=>r.word).sort(),['BRBR','BRRB','RBBR','RBRB']);
  assert.deepEqual([...l.bypass].sort(),['BBRR','RRBB']);
  for(const colour of ['red','blue'])assert.deepEqual(l.selectedStates.filter(r=>r.portColour===colour).map(r=>r.candidateB).sort(),['+','-']);
 }
});
test('past history does not select a next branch in the existing layer route family',()=>{
 for(const l of probe.layers)for(const r of l.selectedStates){assert.deepEqual(r.nextChoices,{red:8,blue:8});assert.equal(r.completions,16);}
});
test('coarse planar compatibility does not conceal the eight nonplanar native exits',()=>{
 assert.equal(probe.summary.nativeDeparturesOutsideInputPlane,8);assert.equal(probe.summary.nativeDepartures,16);
 for(const d of probe.departures)assert(d.distanceSquaredFromInputPlane<1e-10||Math.abs(d.distanceSquaredFromInputPlane-4/3)<1e-10);
 const map=planeSimilarity([0,0,0],[[1,0,0],[0,1,0]],[0,0,0,0],[[1,0,0,0],[0,1,0,0]]);
 assert.throws(()=>map.map([0,0,1]),/outside source plane/);
 assert.throws(()=>planeSimilarity([0,0,0],[[1,0,0],[0,1,0]],[0,0,0],[[1,0,0],[1,1,0]]),/not similar/);
});
