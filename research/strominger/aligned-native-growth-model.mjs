// Experimental attachment binding. No target words or layer layouts are inputs.
import {GenerativeAssemblyRules} from '../nima/generative-phase-assembly.mjs';
import {makeAlignedPairChannels} from './aligned-pair-channel-model.mjs';
import {permuteReference} from './retained-context-braid-model.mjs';
const marks=['C0','M0','C1','M1','C2'];
const copy=x=>structuredClone(x),equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const invert=p=>p.map((_,i)=>p.indexOf(i));
const apply=(v,p)=>p.map(i=>copy(v[i]));
export function runAlignedNativeGrowth(values,{frame=[0,1,2,3],dual=values}={}){
 const atlas=makeAlignedPairChannels();
 if(values.length!==8||dual.length!==8)throw Error('Complete retained banks required');
 const seedBindings=Object.fromEntries(marks.slice(0,4).map((m,i)=>[m,permuteReference(atlas.references[i],frame)]));
 const rules=new GenerativeAssemblyRules({seedBindings}),slot=new Map(atlas.references.map((v,i)=>[v,i])),p=atlas.context.permutation(frame);
 const rounds=atlas.rounds.map(round=>{
  const direction=p[0]^p[round.direction];
  if(!Array.from({length:8},(_,i)=>p[i]^p[i^round.direction]).every(d=>d===direction))throw Error('Frame does not preserve matchings');
  return {...atlas.rounds.find(r=>r.direction===direction),logicalStage:round.index};
 });
 let field=atlas.context.push(values,frame),current=rules.root,cumulative=Array.from({length:8},(_,i)=>i);
 const initial=copy(field),selected=[current],records=[],excluded=[];
 const occupied=new Set([rules.charts[rules.packets[current].chart].cell]);
 for(const round of rounds){
  const source=rules.packets[current],chart=rules.charts[source.chart],eligible=[];
  // A single frontier. Reader-only and reference-changing moves are not
  // silently converted to same-bank two-port attachments.
  for(const id of rules.outgoing(current)){
   const op=rules.operations[id],target=rules.charts[rules.packets[op.target].chart];
   let reason=null;
   if(chart.cell===target.cell)reason='reader-only move';
   else if(occupied.has(target.cell))reason='target already retained';
   else if(marks.some(m=>chart.aliases[m]!==target.aliases[m]))reason='reference-changing attachment needs a larger port map';
   else if(marks.some(m=>!slot.has(chart.aliases[m])))reason='reference outside retained bank';
   if(reason){excluded.push({stage:round.logicalStage,operation:op.kind,reason});continue;}
   const indices=marks.map(m=>slot.get(chart.aliases[m])),global=Array.from({length:8},(_,i)=>i);
   indices.forEach((to,i)=>global[to]=indices[op.permutation[i]]);
   const moved=global.map((from,to)=>({from,to})).filter(x=>x.from!==x.to);
   if(!moved.length||!moved.every(x=>(x.from^x.to)===round.direction))continue;
   rules.validateTransfer(op);eligible.push({op,global});
  }
  if(eligible.length>1)throw Error('Ambiguous native attachment; no target-fitting tie-breaker permitted');
  const before=copy(field),permutation=eligible[0]?.global??Array.from({length:8},(_,i)=>i),operation=eligible[0]?.op??null;
  const beforePermutation=[...cumulative];
  field=apply(field,permutation);cumulative=permutation.map(i=>cumulative[i]);
  if(operation){current=operation.target;selected.push(current);occupied.add(rules.charts[rules.packets[current].chart].cell);}
  records.push({stage:round.logicalStage,direction:round.direction,channelIds:round.channelIds,operation:operation?copy(operation):null,
   sourcePacket:source.id,targetPacket:current,before,after:copy(field),permutation,beforePermutation,afterPermutation:[...cumulative],
   packets:atlas.project(round,field).map(packet=>({...packet,occurrence:`stage-${round.logicalStage}`,initialSlots:packet.slots.map(i=>cumulative[i])}))});
 }
 const assembly=rules.inspect(selected);
 if(!assembly.valid||!assembly.certifiedExit)throw Error('Generated attachment chain did not pass native assembly inspection');
 let covector=atlas.context.push(dual,frame),recovered=copy(field);
 const terminalDual=copy(covector),returns=[];
 for(const record of records.toReversed()){
  const afterDual=copy(covector),inverse=invert(record.permutation);
  covector=apply(covector,inverse);recovered=apply(recovered,inverse);
  returns.push({stage:15-record.stage,forwardStage:record.stage,channelIds:record.channelIds,
   kind:'dual-pullback-not-native-growth',nativeOperation:record.operation?.kind??null,afterDual,beforeDual:copy(covector),recovered:copy(recovered)});
 }
 if(!equal(recovered,initial))throw Error('Full retained recovery failed');
 // Normalize every time-indexed endpoint back to the common initial bank.
 const normalized=Array(8);
 for(const record of records)for(const packet of record.packets)packet.initialSlots.forEach((i,j)=>{
  if(Object.hasOwn(normalized,i)&&!equal(normalized[i],packet.values[j]))throw Error('Transport-normalized channel disagreement');normalized[i]=copy(packet.values[j]);
 });
 if(!equal(normalized,initial))throw Error('Incomplete normalized channel atlas');
 return {frame,references:atlas.references,initial,final:field,terminalDual,initialDual:covector,recovered,normalized,records,returns,excluded,
  packets:selected.map(id=>copy(rules.packets[id])),charts:selected.map(id=>copy(rules.charts[rules.packets[id].chart])),
  bodies:selected.map(id=>copy(rules.geometry.cells[rules.charts[rules.packets[id].chart].cell].vertices)),assembly,
  channelCount:atlas.channels.length,stageCount:records.length+returns.length,
  policy:'Single frontier; append only unoccupied, unchanged-reference native face attachments whose coefficient support is in the active matching. At most one attachment per stage; ambiguity fails closed.'};
}
