// Conditional upper-neighbourhood generator. No reference routes, target
// carrier list, supplied frame, coordinate ordering, or strand-ID routing.
import {predictBlindDepartures} from './sulfur-route-blind.mjs';
const key=p=>p.join(',');
const sub=(a,b)=>a.map((x,i)=>x-b[i]);
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const require=(ok,message)=>{if(!ok)throw Error(message);};
export function generateUpperNeighbourhood(geometry,query,calibration){
 require(Object.keys(query).every(k=>['at','arrivals'].includes(k)),'Unexpected query field: no future carrier or frame may be supplied');
 const {at,arrivals}=query,{rule,angularModel}=calibration;
 require(Array.isArray(at)&&at.length===4&&geometry.vertices.has(key(at)),'Unknown arrival vertex');
 require(Array.isArray(arrivals)&&arrivals.length>0,'No arriving records');
 const ids=new Set(),groups=new Map();
 for(const arrival of arrivals){
  require(Object.keys(arrival).every(k=>['previous','record'].includes(k)),'Unexpected arrival field');
  const {previous,record}=arrival;
  require(Array.isArray(previous)&&previous.length===4&&geometry.adjacency.get(key(at)).some(n=>key(n.point)===key(previous)),'Arrival is not a native edge');
  require(typeof record?.id==='string'&&!ids.has(record.id),'Missing or duplicate identity');ids.add(record.id);
  for(const b of ['a','b','p','e'])require(['+','-'].includes(record.polarities?.[b]),'Missing incoming polarity state');
  const p=record.polarities,selector=rule.selectorByA[p.a];require(['p','e'].includes(selector),'Unknown active polarity');
  const held=selector==='p'?'e':'p',context={a:p.a,b:p.b,[held]:p[held]},groupKey=JSON.stringify([selector,p.a,p.b,p[held]]);
  if(!groups.has(groupKey))groups.set(groupKey,{selector,context,arrivals:[]});
  groups.get(groupKey).arrivals.push(arrival);
 }
 const results=[];
 for(const group of groups.values()){
  const members=group.arrivals,base={selector:group.selector,context:group.context,arrivalIds:members.map(a=>a.record.id)};
  if(members.length!==2||new Set(members.map(a=>a.record.polarities[group.selector])).size!==2){
   results.push({...base,status:'unresolved',reason:'Need exactly one complementary pair in this retained context',carrierCandidates:[],generated:[]});continue;
  }
  const tagged=members.map(a=>({...a,arm:sub(a.previous,at),kind:rule.inputByAgreement[String(a.record.polarities[group.selector]===a.record.polarities.b)]}));
  const straight=tagged.filter(a=>a.kind==='straight'),oblique=tagged.filter(a=>a.kind==='oblique');
  require(straight.length===1&&oblique.length===1,'Calibrated rule does not distinguish the two incoming roles');
  const incident=geometry.adjacency.get(key(at));
  const unlabelled=incident.filter(n=>{
   const d=sub(n.point,at),products=tagged.map(a=>dot(d,a.arm)).sort((a,b)=>a-b);
   return products[0]===-2&&products[1]===-1;
  });
  const candidates=incident.filter(n=>{
   const d=sub(n.point,at);return dot(d,straight[0].arm)===-2&&dot(d,oblique[0].arm)===-1;
  });
  const evidence={...base,unlabelledTemplateCarriers:unlabelled.map(n=>n.point),carrierCandidates:candidates.map(n=>n.point),generated:[]};
  if(candidates.length!==1){results.push({...evidence,status:'unresolved',reason:'Carrier absent or ambiguous'});continue;}
  const head=candidates[0].point,planeWitness=oblique[0].previous;
  const continuations=tagged.map(a=>{
   // The adapter's flow axis serves diagnostic profiles only. The successful
   // angular profile uses neither a global flow axis nor equatorial phase.
   const input={tail:at,head,previous:a.previous,planeWitness,polarities:a.record.polarities,flowAxis:sub(head,at)};
   const possible=predictBlindDepartures(geometry,input,rule,angularModel).profiles['plane + fitted angular signature'];
   return {arrival:a,possible};
  });
  if(continuations.some(c=>c.possible.length!==1)){
   results.push({...evidence,head,planeWitness,status:'unresolved',reason:'Departure absent or ambiguous',departures:continuations.map(c=>({id:c.arrival.record.id,candidates:c.possible}))});continue;
  }
  const generated=continuations.map(({arrival,possible})=>({record:structuredClone(arrival.record),points:[arrival.previous,at,head,possible[0].point].map(p=>[...p])}));
  results.push({...evidence,head:[...head],planeWitness:[...planeWitness],status:'unique',generated});
 }
 return {status:results.every(g=>g.status==='unique')?'unique':'unresolved',at:[...at],groups:results,
  inputRecords:structuredClone(arrivals.map(a=>a.record)),generated:results.flatMap(g=>g.generated),
  scope:'conditional on the calibrated upper-junction template and incoming a,b,p,e labels; b is an existing reference route-choice label, not a geometry-derived bit'};
}
