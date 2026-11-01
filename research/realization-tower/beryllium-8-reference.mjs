import {singleOctahedralEnvelope} from './single-octahedral-process.mjs';
const key=p=>p.join(','),edgeKey=(a,b)=>[key(a),key(b)].sort().join('|');
// Independent eight-route candidate on a unit native octahedral edge graph.
// Four entry ports are labelled (p,e). t retains the choice of adjacent rim
// port: + follows the cyclic order, - follows its inverse. No source-layer
// routes, visibility, continuation rule, or fitted path subset is consulted.
export function buildBeryllium8Reference(){
 const envelope=singleOctahedralEnvelope(0),tip=envelope[1],exitTip=envelope[0];
 const axis=[-.5,-.5,.5,.5],entryVertices=[3,4,5,2];
 // Gray order (++,+-,--,-+) follows adjacent vertices, never opposite tips.
 const rimOrder=[0,1,3,2],styles=[{label:'white',colors:[0xffffff]},{label:'white-red',colors:[0xffffff,0xff3030]},{label:'white-red',colors:[0xffffff,0xff3030]},{label:'blue',colors:[0x168fff]}];
 const strands=[];
 for(let pe=0;pe<4;pe++)for(let turn=0;turn<2;turn++){
  const t=turn===0?'+':'-',p=pe<2?'+':'-',e=pe%2===0?'+':'-',sign=turn===0?1:-1;
  const target=rimOrder[(rimOrder.indexOf(pe)+sign+4)%4];
  const guide=[tip,envelope[entryVertices[pe]],envelope[entryVertices[target]],exitTip].map(p=>[...p]);
  strands.push({id:`be8:wire:${t}${p}${e}`,polarities:{t,p,e},...styles[pe],polarityDirection:pe===1?1:pe===2?-1:0,routeDirection:pe===0||pe===3?1:0,inputSlot:2*pe+turn,outputSlot:2*target+turn,
   entryPort:pe,exitPort:target,turn:sign,guide,edgeIds:guide.slice(1).map((p,i)=>edgeKey(guide[i],p))});
 }
 const edges=new Map();
 for(const s of strands)for(let i=0;i<s.edgeIds.length;i++){
  const id=s.edgeIds[i];if(!edges.has(id))edges.set(id,{id,guide:s.guide.slice(i,i+2),strandIds:[]});
  edges.get(id).strandIds.push(s.id);
 }
 const permutation=Array.from({length:strands.length},()=>Array(strands.length).fill(0));
 for(const s of strands)permutation[s.outputSlot][s.inputSlot]=1;
 return {kind:'be8-octahedral-turn-candidate',labelOrder:['t','p','e'],axis,envelope,strands,edges:[...edges.values()],permutation,matrixBasis:strands.map(s=>s.id),
  audit:{strands:strands.length,nativeEdges:edges.size,entryPorts:4,turnChoices:2,outputSlots:new Set(strands.map(s=>s.outputSlot)).size,
   routingStatus:'candidate: four-port rim shift controlled by retained turn t; inverse shift recovers each input',
   scope:'Eight retained (t,p,e) routes on the unit octahedral carrier; not a selected subset of Su-32 or of the layer paths.'}};
}
