import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildSulfurIncomingBundle} from '../research/realization-tower/sulfur-32-incoming-bundle.mjs';
import {buildSulfurLocalTransitions,learnLocalRule,enterLocalCarrier,leaveLocalCarrier,compareHexLocalStars} from '../research/realization-tower/sulfur-local-transition.mjs';
const source=buildSulfurIncomingBundle(),before=JSON.stringify(source),model=buildSulfurLocalTransitions(source),rule=learnLocalRule(model.motifs);
test('extract eight reference motifs covering all sixteen strands without changing routes',()=>{
 assert.equal(model.motifs.length,8);assert.equal(model.coverage.passages,16);
 assert.deepEqual(model.coverage.strandIds.toSorted(),source.strands.map(s=>s.id).sort());
 assert.equal(JSON.stringify(source),before);assert.equal(model.candidates.length,16);
 assert.deepEqual(rule.selectorByA,{'+':'p','-':'e'});assert.deepEqual(rule.parityByHeldSign,{'+':1,'-':0});
});
test('one-bit carrier reproduces actual reference exits and reverses all sixteen records losslessly',()=>{
 const seen=new Set();
 for(const motif of model.motifs)for(const row of motif.rows){
  const strand=source.strands.find(s=>s.id===row.strandId),i=strand.edgeIds.indexOf(motif.id);
  const packet={strandId:strand.id,polarities:structuredClone(strand.polarities),colour:strand.label,opaquePayload:{token:row.strandId,nested:[1,-3,null,{phase:[2,-5]}]},port:strand.edgeIds[i-1]};
  const snapshot=structuredClone(packet),carrier=enterLocalCarrier(motif,packet,rule),result=leaveLocalCarrier(motif,carrier,rule);
  assert.equal(result.port,strand.edgeIds[i+1]);assert.equal(carrier.payload.port,undefined);
  assert.deepEqual(result,{...snapshot,port:strand.edgeIds[i+1]});assert.deepEqual(packet,snapshot);
  const reverse=leaveLocalCarrier(motif,enterLocalCarrier(motif,result,rule,'reverse'),rule);
  assert.deepEqual(reverse,snapshot);seen.add(result.strandId);
  const anonymous={...snapshot,strandId:'opaque unrelated ID'};
  assert.equal(leaveLocalCarrier(motif,enterLocalCarrier(motif,anonymous,rule),rule).port,result.port);
 }
 assert.equal(seen.size,16);
});
test('the same rule predicts each held-out motif rather than memorizing its strand IDs',()=>{
 for(const held of model.motifs){
  const learned=learnLocalRule(model.motifs.filter(m=>m.id!==held.id));
  assert.equal(learned.selectorByA[held.context.a],held.selector);
  for(const row of held.rows){
   const packet={strandId:row.strandId,polarities:row.polarities,port:row.incomingEdge};
   assert.equal(leaveLocalCarrier(held,enterLocalCarrier(held,packet,learned),learned).port,row.outgoingEdge);
  }
 }
});
test('invalid ingress, inconsistent payload and erased carrier state are rejected',()=>{
 const m=model.motifs[0],r=m.rows[0],packet={strandId:r.strandId,polarities:r.polarities,port:r.incomingEdge};
 assert.throws(()=>enterLocalCarrier(m,{...packet,port:'not a port'},rule));
 assert.throws(()=>enterLocalCarrier(m,{...packet,polarities:{...r.polarities,[m.selector]:'-'}},rule));
 const carrier=enterLocalCarrier(m,packet,rule);delete carrier.slot;assert.throws(()=>leaveLocalCarrier(m,carrier,rule));
 assert.throws(()=>enterLocalCarrier(m,packet,{parityByHeldSign:{}}));
 const bad=structuredClone(model.motifs);bad[0].rows[0].output^=1;assert.throws(()=>learnLocalRule(bad));
});
test('direct rigid star identification is obstructed; history and colour states are retained',()=>{
 const comparison=compareHexLocalStars(model);
 assert.equal(comparison.allHexStars120,true);assert.equal(comparison.patterns.length,4);
 assert.equal(comparison.referenceCandidates,16);assert.deepEqual(comparison.rigidStarMatches,[]);
 for(const m of model.motifs){
  assert.deepEqual(m.geometry.tail.cosines,[-1,-.5,.5]);
  assert(Math.abs(m.geometry.head.gramDeterminant-.5)<1e-12);
 }
 assert.equal(JSON.stringify(source),before);
});
