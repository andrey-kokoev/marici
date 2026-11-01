import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildSulfurIncomingBundle} from '../research/realization-tower/sulfur-32-incoming-bundle.mjs';
import {buildSulfurLocalTransitions} from '../research/realization-tower/sulfur-local-transition.mjs';
import {buildRouteBlindGeometry,predictBlindDepartures,fitAngularCompletion} from '../research/realization-tower/sulfur-route-blind.mjs';
import {runBlindProbe,predictHeldOutMotif} from '../scripts/lib/sulfur-route-blind-probe.mjs';
const probe=runBlindProbe(),geometry=buildRouteBlindGeometry(1),profile='plane + fitted angular signature';
const sub=(a,b)=>a.map((x,i)=>x-b[i]),add=(a,b)=>a.map((x,i)=>x+b[i]),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
test('candidate geometry contains every unit native edge, not merely occupied reference edges',()=>{
 assert.deepEqual(geometry.audit,{cells:51,vertices:44,edges:168,boundaryEdges:108});
 const points=[...geometry.vertices.values()];let count=0;
 for(let i=0;i<points.length;i++)for(let j=i+1;j<points.length;j++)if(dot(sub(points[i],points[j]),sub(points[i],points[j]))===2){
  count++;assert(geometry.edges.has([points[i].join(','),points[j].join(',')].sort().join('|')));
 }
 assert.equal(count,168);
});
test('the original plane-only rule fails uniqueness for all sixteen cases',()=>{
 assert.deepEqual(probe.totals['plane only'],{uniqueCorrect:0,ambiguousWithTruth:16,rejected:0,totalCandidates:48});
 for(const r of probe.results){assert.equal(r.prediction.candidates.length,6);assert.equal(r.scores['plane only'].candidates,3);}
 assert.equal(probe.totals['plane + equatorial phase'].uniqueCorrect,8);
 assert.equal(probe.totals['plane + equatorial phase + nearest centre'].rejected,4);
});
test('angular completion predicts all actual exits with both target-carrier records withheld',()=>{
 assert.deepEqual(probe.totals[profile],{uniqueCorrect:16,ambiguousWithTruth:0,rejected:0,totalCandidates:16});
 for(const r of probe.results){
  assert.equal(r.trainingMotifs.length,7);assert(!r.trainingMotifs.includes(r.motif));
  assert.deepEqual(r.angularModel.bySign['-'].axisCosine,{bits:['a','b','p','e'],coefficient:.5});
  assert.deepEqual(r.angularModel.bySign['-'].transverseCosine,{bits:['a','b','p','e'],coefficient:1});
  assert.deepEqual(r.angularModel.bySign['+'].axisCosine,{bits:[],coefficient:-.5});
  assert.deepEqual(r.angularModel.bySign['+'].transverseCosine,{bits:[],coefficient:1/3});
  assert.deepEqual(r.prediction.profiles[profile][0].point,r.expected.point);
 }
});
test('deleting every target successor and output-port field leaves predictions unchanged',()=>{
 const reference=buildSulfurIncomingBundle(),motifs=buildSulfurLocalTransitions(reference).motifs;
 for(const m of motifs){
  const blind=structuredClone(m);delete blind.outputs;delete blind.observedPermutation;
  for(const row of blind.rows){delete row.next;delete row.outgoingEdge;delete row.output;}
  const predictions=predictHeldOutMotif(geometry,motifs,blind,reference.axis);
  for(const r of predictions)assert.deepEqual(r.prediction,probe.results.find(x=>x.strandId===r.strandId).prediction);
 }
});
test('the completed choice does not use equatorial phase, candidate ordering or sector truncation',()=>{
 const larger=buildRouteBlindGeometry(2);
 for(const neighbors of larger.adjacency.values())neighbors.reverse();
 for(const r of probe.results){
  assert.equal(larger.adjacency.get(r.query.head.join(',')).length,12);
  const changed={...r.query,flowAxis:[1,-1,0,0]};
  const result=predictBlindDepartures(larger,changed,r.rule,r.angularModel).profiles[profile];
  assert.equal(result.length,1);assert.equal(result[0].edge,r.expected.edge);
 }
});
test('all 48 compatible native frames and 16 polarity tuples admit exactly one completed departure',()=>{
 const larger=buildRouteBlindGeometry(2),sample=probe.results[0],head=[1,0,0,0],roots=[];
 for(let i=0;i<4;i++)for(let j=0;j<4;j++)if(i!==j)roots.push([0,1,2,3].map(k=>Number(k===i)-Number(k===j)));
 let count=0,frames=0;
 for(const axis of roots)for(const oblique of roots)if(dot(axis,oblique)===-1){
  frames++;
  for(let mask=0;mask<16;mask++){
   const polarities=Object.fromEntries(['a','b','p','e'].map((b,i)=>[b,mask&(1<<i)?'-':'+']));
   const sign=polarities[sample.rule.selectorByA[polarities.a]],tail=sub(head,axis),planeWitness=add(tail,oblique);
   const query={tail,head,planeWitness,previous:sign===polarities.b?planeWitness:sub(tail,axis),polarities,flowAxis:[-.5,-.5,.5,.5]};
   const candidates=predictBlindDepartures(larger,query,sample.rule,sample.angularModel).profiles[profile];
   assert.equal(candidates.length,1);const departure=sub(candidates[0].point,head);
   if(sign==='-'){
    const parity=Object.values(polarities).reduce((p,s)=>p*(s==='+'?1:-1),1);
    assert.deepEqual(departure,add(axis,oblique).map(x=>parity*x||0));
   }else{assert.equal(dot(axis,departure),-1);assert.equal(dot(oblique,departure),1);}
   count++;
  }
 }
 assert.equal(frames,48);assert.equal(count,768);
 // This proves existence/uniqueness in the finite direction set, not that
 // these synthetic cases have physically or globally validated routes.
});
test('future-port injection and underdetermined angular calibration are rejected',()=>{
 const r=probe.results[0];
 assert.throws(()=>predictBlindDepartures(geometry,{...r.query,expectedNext:r.expected.point},r.rule),/Unexpected query field/);
 assert.throws(()=>fitAngularCompletion([{sign:'+',polarities:r.query.polarities,axisCosine:-.5,transverseCosine:1/3},{sign:'-',polarities:r.query.polarities,axisCosine:.5,transverseCosine:1}]),/ambiguous or inconsistent/);
 assert.equal(probe.sourceRoutesUnchanged,true);
});
