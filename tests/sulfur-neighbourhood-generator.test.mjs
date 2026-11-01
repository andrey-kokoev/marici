import {test} from 'node:test';
import assert from 'node:assert/strict';
import {runBlindProbe} from '../scripts/lib/sulfur-route-blind-probe.mjs';
import {buildRouteBlindGeometry} from '../research/realization-tower/sulfur-route-blind.mjs';
import {generateUpperNeighbourhood} from '../research/realization-tower/sulfur-neighbourhood-generator.mjs';
import {runNeighbourhoodProbe,queriesFromIncomingPrefixes} from '../scripts/lib/sulfur-neighbourhood-probe.mjs';
const probe=await runNeighbourhoodProbe(),geometry=buildRouteBlindGeometry(1);
test('four incoming-prefix neighbourhoods generate eight carriers and sixteen exact local passages',()=>{
 assert.deepEqual(probe.counts,{junctions:4,carriers:8,records:16,exactNeighbourhoods:16,preservedRecords:16,changedCarriersWhenBFlipped:16});
 for(const {query,result}of probe.predicted){
  assert.deepEqual(Object.keys(query).sort(),['arrivals','at']);assert.equal(result.status,'unique');
  assert.equal(result.groups.length,2);assert.equal(result.generated.length,4);
  for(const group of result.groups){
   assert.equal(group.unlabelledTemplateCarriers.length,2);assert.equal(group.carrierCandidates.length,1);
   assert.equal(group.generated.length,2);
  }
 }
 assert.equal(new Set(probe.comparisons.map(c=>c.id)).size,16);assert.equal(probe.sourceRoutesUnchanged,true);
});
test('frozen calibration exactly matches every prior-style held-out angular fit',()=>{
 const old=runBlindProbe();
 for(const r of old.results){
  assert.deepEqual(r.angularModel.bySign,probe.calibration.angularModel.bySign);
  for(const k of ['selectorByA','inputByAgreement','outputBySign'])assert.deepEqual(r.rule[k],probe.calibration.rule[k]);
 }
});
test('input order and opaque IDs do not select carriers or exits',()=>{
 for(const {query,result}of probe.predicted){
  const changed=structuredClone(query);changed.arrivals.reverse();
  for(const [i,a]of changed.arrivals.entries()){a.record.payload.originalId=a.record.id;a.record.id='opaque '+i;}
  const generated=generateUpperNeighbourhood(geometry,changed,probe.calibration).generated;
  for(const g of generated){
   const old=result.generated.find(x=>x.record.id===g.record.payload.originalId);assert.deepEqual(g.points,old.points);
   assert.deepEqual(g.record,changed.arrivals.find(a=>a.record.id===g.record.id).record);
  }
 }
});
test('erasing b leaves eight indistinguishable arrival pairs that require different carriers',()=>{
 assert.equal(probe.bAblation.length,8);
 for(const group of probe.bAblation){
  assert.equal(group.records.length,2);
  assert.deepEqual(group.records.map(r=>r.b).sort(),['+','-']);
  assert.equal(new Set(group.records.map(r=>r.generatedHead.join(','))).size,2);
 }
});
test('removing state or complement records exposes missing information instead of inventing a tie-break',()=>{
 const query=structuredClone(probe.predicted[0].query);delete query.arrivals[0].record.polarities.b;
 assert.throws(()=>generateUpperNeighbourhood(geometry,query,probe.calibration),/Missing incoming polarity/);
 const incomplete=structuredClone(probe.predicted[0].query);incomplete.arrivals.pop();
 const result=generateUpperNeighbourhood(geometry,incomplete,probe.calibration);
 assert.equal(result.status,'unresolved');assert.equal(result.inputRecords.length,3);
 assert(result.groups.some(g=>g.status==='unresolved'&&/complementary pair/.test(g.reason)));
});
test('unavailable native carriers remain unresolved and no edge is fabricated',()=>{
 const original=probe.predicted[0],blocked={...geometry,adjacency:new Map(geometry.adjacency)},heads=new Set(original.result.groups.map(g=>g.head.join(',')));
 blocked.adjacency.set(original.query.at.join(','),geometry.adjacency.get(original.query.at.join(',')).filter(n=>!heads.has(n.point.join(','))));
 const result=generateUpperNeighbourhood(blocked,original.query,probe.calibration);
 assert.equal(result.status,'unresolved');assert.equal(result.generated.length,0);assert.equal(result.inputRecords.length,4);
 assert(result.groups.every(g=>g.carrierCandidates.length===0));
});
test('prefix-only inputs are sufficient; future carrier and frame injection is rejected',()=>{
 for(const {query} of probe.predicted){
  const prefixes=query.arrivals.map(a=>({prefix:[a.previous,query.at],record:a.record}));
  assert.deepEqual(queriesFromIncomingPrefixes(prefixes),[query]);
  assert.throws(()=>generateUpperNeighbourhood(geometry,{...query,head:[0,0,0,1]},probe.calibration),/Unexpected query field/);
  assert.throws(()=>generateUpperNeighbourhood(geometry,{...query,planeWitness:query.arrivals[0].previous},probe.calibration),/Unexpected query field/);
 }
});
