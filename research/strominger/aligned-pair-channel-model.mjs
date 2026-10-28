import definition from './aligned-pair-channel-steps-v1.json' with {type:'json'};
import {makeRetainedContextBraid} from './retained-context-braid-model.mjs';
const copy=x=>structuredClone(x),same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const pairKey=(a,b)=>a<b?`${a}:${b}`:`${b}:${a}`;
function bank(values){if(!Array.isArray(values)||values.length!==8)throw Error('Eight retained reference values required');}
export function makeAlignedPairChannels(){
 const context=makeRetainedContextBraid(),references=context.references;
 if(references.length!==definition.channels.independentReferenceCount)throw Error('Reference source mismatch');
 const channels=[];
 for(let i=0;i<8;i++)for(let j=i+1;j<8;j++)channels.push({id:pairKey(i,j),slots:[i,j],references:[references[i],references[j]],direction:i^j});
 const rounds=definition.forward.directions.map((direction,index)=>({index:index+1,direction,channelIds:channels.filter(c=>c.direction===direction).map(c=>c.id)}));
 const byId=new Map(channels.map(c=>[c.id,c]));
 const stages=[...rounds.map(r=>({number:r.index,operation:'matching-projection',round:r.index,direction:r.direction,channelIds:r.channelIds})),...rounds.toReversed().map((r,i)=>({number:rounds.length+i+1,operation:'dual-pullback',round:r.index,direction:r.direction,channelIds:r.channelIds}))];
 function project(round,values){bank(values);return round.channelIds.map(id=>{const c=byId.get(id);return {channel:id,slots:[...c.slots],references:[...c.references],values:c.slots.map(i=>copy(values[i]))};});}
 function pullback(round,packets){
  if(packets.length!==round.channelIds.length)throw Error('Incomplete matching packet');
  const out=Array(8),seen=new Set();
  for(const packet of packets){
   const c=byId.get(packet.channel);
   if(!c||!round.channelIds.includes(c.id)||seen.has(c.id)||!same(packet.slots,c.slots)||!same(packet.references,c.references)||packet.values.length!==2)throw Error('Mismatched channel provenance');
   seen.add(c.id);c.slots.forEach((slot,i)=>{if(Object.hasOwn(out,slot))throw Error('Matching is not disjoint');out[slot]=copy(packet.values[i]);});
  }
  if(seen.size!==4||Object.keys(out).length!==8)throw Error('Matching does not cover all references');return out;
 }
 function glue(packets){
  if(packets.length!==channels.length)throw Error('Expected all twenty-eight pair channels');
  const out=Array(8),seen=new Set();
  for(const packet of packets){
   const c=byId.get(packet.channel);
   if(!c||seen.has(c.id)||!same(packet.slots,c.slots)||!same(packet.references,c.references)||packet.values.length!==2)throw Error('Mismatched channel provenance');
   seen.add(c.id);c.slots.forEach((slot,i)=>{if(Object.hasOwn(out,slot)&&!same(out[slot],packet.values[i]))throw Error(`Inconsistent shared reference ${slot}`);out[slot]=copy(packet.values[i]);});
  }
  return out;
 }
 function run(values,dual){
  bank(values);bank(dual);
  const atlas=[],records=[],pending=new Map();
  for(const stage of stages){
   const round=rounds[stage.round-1];
   if(stage.operation==='matching-projection'){
    const fieldPackets=project(round,values),dualPackets=project(round,dual);
    pending.set(round.index,{fieldPackets,dualPackets});atlas.push(...fieldPackets);
    records.push({...stage,fieldPackets,dualPackets});
   }else{
    const stored=pending.get(round.index);
    if(!stored)throw Error('Return without forward provenance');
    records.push({...stage,dualReturn:pullback(round,stored.dualPackets),retainedFieldRecovery:pullback(round,stored.fieldPackets)});
    pending.delete(round.index);
   }
  }
  const recovered=glue(atlas);
  if(!same(recovered,values)||pending.size)throw Error('Protocol failed retained recovery');
  return {channelCount:channels.length,stageCount:stages.length,activeChannelsPerStage:4,independentReferences:8,atlas,records,recovered,returns:records.filter(r=>r.operation==='dual-pullback').map(r=>r.dualReturn),sourceRetained:copy(values)};
 }
 function transportChannel(packet,p){
  const moved=packet.slots.map(i=>p[i]),flip=moved[0]>moved[1],slots=[...moved].sort((a,b)=>a-b);
  return {channel:pairKey(...slots),slots,references:slots.map(i=>references[i]),values:flip?copy(packet.values.toReversed()):copy(packet.values),orientation:flip?-1:1};
 }
 return {definition,references,context,channels,rounds,stages,project,pullback,glue,run,transportChannel};
}
