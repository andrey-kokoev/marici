import {buildBeryllium8Reference} from './beryllium-8-reference.mjs';
const key=p=>p.join(','),edgeKey=(a,b)=>[key(a),key(b)].sort().join('|');
// Trial only: replace the mixed strands' rim passes by explicitly retained
// passages through one central sleeve. Preserve all eight endpoint matches.
export function buildBeryllium9Reference({centralSleeve=true}={}){
 const reference=buildBeryllium8Reference();
 if(!centralSleeve)return {...reference,kind:'be9-reference-clone',sleeve:null};
 const centre=reference.envelope[0].map((_,i)=>reference.envelope.reduce((n,p)=>n+p[i],0)/reference.envelope.length);
 const strands=reference.strands.map(s=>{
  if(!s.polarityDirection)return s;
  const guide=[s.guide[0],s.guide[1],[...centre],s.guide[2],s.guide[3]];
  return {...s,guide,sourceEdgeIds:[...s.edgeIds],throughSleeve:true,edgeIds:guide.slice(1).map((p,i)=>edgeKey(guide[i],p))};
 });
 const selected=strands.filter(s=>s.throughSleeve),groupBy=field=>[...new Set(selected.map(s=>s[field]))].sort().map(port=>({port,strandIds:selected.filter(s=>s[field]===port).map(s=>s.id)}));
 const sleeve={id:'be9:central-neutron-sleeve',point:centre,radius:.2,strandIds:selected.map(s=>s.id),incomingPairs:groupBy('entryPort'),outgoingPairs:groupBy('exitPort'),
  passages:selected.map(s=>({strandId:s.id,entryPort:s.entryPort,exitPort:s.exitPort,inputSlot:s.inputSlot,outputSlot:s.outputSlot}))};
 const edges=new Map();
 for(const s of strands)for(let i=0;i<s.edgeIds.length;i++){
  const id=s.edgeIds[i];if(!edges.has(id))edges.set(id,{id,guide:s.guide.slice(i,i+2),sleeveLink:s.guide.slice(i,i+2).some(p=>key(p)===key(centre)),strandIds:[]});
  edges.get(id).strandIds.push(s.id);
 }
 return {...reference,kind:'be9-central-sleeve-candidate',strands,edges:[...edges.values()],sleeve,
  audit:{...reference.audit,routingEdges:edges.size,interiorLinks:[...edges.values()].filter(e=>e.sleeveLink).length,centralSleeves:1,sleeveStrands:selected.length,
   routingStatus:'trial: four mixed identities pass through a central sleeve, retaining their original output slots',
   scope:'Two incoming pairs and two outgoing pairs, with four explicit identity-preserving passages. Other four native routes and the eight-slot permutation are unchanged.'}};
}
