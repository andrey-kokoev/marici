// Checker/calibration harness. Unlike the solver, this module may read routes.
import {buildSulfurIncomingBundle} from '../../research/realization-tower/sulfur-32-incoming-bundle.mjs';
import {buildSulfurLocalTransitions} from '../../research/realization-tower/sulfur-local-transition.mjs';
import {learnGeometricLocalRule} from '../../research/realization-tower/sulfur-local-geometry.mjs';
import {buildRouteBlindGeometry,predictBlindDepartures,departureAngles,fitAngularCompletion} from '../../research/realization-tower/sulfur-route-blind.mjs';
const sub=(a,b)=>a.map((x,i)=>x-b[i]);
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
export function incomingQuery(motif,row,flowAxis){
 const axis=sub(motif.head,motif.tail);
 const witnesses=motif.inputs.filter(p=>{const v=sub(p.point,motif.tail);return dot(axis,axis)*dot(v,v)-dot(axis,v)**2>1e-10;});
 if(witnesses.length!==1)throw Error('Incoming prefixes do not determine a unique plane witness');
 return structuredClone({tail:motif.tail,head:motif.head,previous:row.previous,planeWitness:witnesses[0].point,polarities:row.polarities,flowAxis});
}
export function predictHeldOutMotif(geometry,motifs,heldOut,flowAxis){
 const training=motifs.filter(m=>m.id!==heldOut.id),rule=learnGeometricLocalRule(training);
 const observations=training.flatMap(m=>m.rows.map(row=>{
  const query=incomingQuery(m,row,flowAxis),sign=query.polarities[rule.selectorByA[query.polarities.a]];
  return {polarities:query.polarities,sign,...departureAngles(query,row.next)};
 }));
 const angularModel=fitAngularCompletion(observations);
 return heldOut.rows.map(row=>{
  const query=incomingQuery(heldOut,row,flowAxis);
  return {motif:heldOut.number,strandId:row.strandId,query,trainingMotifs:training.map(m=>m.number),rule,angularModel,prediction:predictBlindDepartures(geometry,query,rule,angularModel)};
 });
}
export function runBlindProbe(){
 const reference=buildSulfurIncomingBundle(),before=JSON.stringify(reference),model=buildSulfurLocalTransitions(reference),geometry=buildRouteBlindGeometry(1);
 // All target predictions are completed before target exits are compared.
 const predictions=model.motifs.flatMap(m=>predictHeldOutMotif(geometry,model.motifs,m,reference.axis));
 const totals={};
 const results=predictions.map(result=>{
  const strand=reference.strands.find(s=>s.id===result.strandId),motif=model.motifs.find(m=>m.number===result.motif),i=strand.edgeIds.indexOf(motif.id);
  const expected={edge:strand.edgeIds[i+1],point:strand.guide[i+2]},scores={};
  for(const [name,candidates]of Object.entries(result.prediction.profiles)){
   const hit=candidates.some(c=>c.edge===expected.edge),status=hit?(candidates.length===1?'uniqueCorrect':'ambiguousWithTruth'):'rejected';
   totals[name]??={uniqueCorrect:0,ambiguousWithTruth:0,rejected:0,totalCandidates:0};totals[name][status]++;totals[name].totalCandidates+=candidates.length;
   scores[name]={status,candidates:candidates.length};
  }
  return {...result,expected,scores};
 });
 if(JSON.stringify(reference)!==before)throw Error('Reference mutated');
 return {schema:'sulfur-route-blind-probe.v1',geometry:geometry.audit,referenceScope:reference.audit.routingStatus,sourceRoutesUnchanged:true,
  conditions:'Known upper carrier, incoming frame from observed prefixes, and full incoming polarity state. All candidate exits generated from whole-cell geometry. Each calibration excludes both records of the target carrier.',
  calibrationCaveat:'Angular completion is a candidate refinement formulated during this investigation; leave-one-carrier-out checks are within-reference checks, not an independent test of discovery or a derivation from layer reflections.',totals,results};
}
