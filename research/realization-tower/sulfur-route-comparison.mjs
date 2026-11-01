import {buildSulfurIncomingBundle} from './sulfur-32-incoming-bundle.mjs';
import {buildBeryllium8Reference} from './beryllium-8-reference.mjs';
import {traceSeedConductors} from './seed-retained-conductors.mjs';
export const comparisonRules=['pending','same-colour','cross-colour'];
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
export function buildSulfurRouteComparison(seed,{visibleLayers=Array(8).fill(true),rule='pending',reference=seed.audit.depth===4?buildBeryllium8Reference():buildSulfurIncomingBundle()}={}){
 if(!comparisonRules.includes(rule))throw Error('Unknown comparison rule');
 const u=[.5,-.5,.5,-.5],v=[.5,-.5,-.5,.5];
 const referenceColumns=reference.strands.map((s,column)=>({column,id:s.id,label:(reference.labelOrder??['a','b','p','e']).map(b=>s.polarities[b]).join(''),
  polarities:{...s.polarities},polarityDirection:s.polarityDirection??0,routeDirection:s.routeDirection??0,colours:s.colors,inputSlot:s.inputSlot??column,outputSlot:s.outputSlot,edgeIds:[...s.edgeIds],guide:s.guide.map(p=>[...p]),
  paths:[{points:s.guide.map(p=>[dot(p,u)+.35*dot(p,v),-dot(p,reference.axis)])}]}));
 const selected=seed.layers.flatMap((layer,index)=>visibleLayers[index]!==false?[{layer,index}]:[]),identities=new Map();
 if(rule!=='pending')for(const {layer,index} of selected){
  const trace=traceSeedConductors(layer,{interiorRouting:rule});
  for(const strand of trace.strands){
   if(!identities.has(strand.id))identities.set(strand.id,{id:strand.id,pairIndex:strand.pairIndex,colour:strand.colour,paths:new Map(),copies:[]});
   const item=identities.get(strand.id),points=strand.guide.map(p=>[p[0],-p[1]]);
   // Directed full paths, deduplicated only WITHIN one retained template ID.
   // Distinct strand IDs are never merged because their geometry happens to match.
   const key=JSON.stringify(points.map(p=>p.map(x=>Math.round(x*1e9)/1e9)));
   if(!item.paths.has(key))item.paths.set(key,{points,sourceLayers:[]});
   item.paths.get(key).sourceLayers.push(index+1);
   item.copies.push({layer:index+1,word:strand.word,edges:[...strand.edgeIds],canonicalEdges:[...strand.canonicalEdges]});
  }
 }
 const combinedColumns=[...identities.values()].sort((a,b)=>a.pairIndex-b.pairIndex||(a.colour==='red'?-1:1)).map((s,column)=>({
  ...s,column,label:`${s.pairIndex+1}${s.colour==='red'?'R':'B'}`,paths:[...s.paths.values()],colours:[s.colour==='red'?0xff4545:0x438bff]}));
 return {reference:referenceColumns,combined:combinedColumns,rule,sourceLayers:selected.map(s=>s.index+1),
  status:!selected.length?'no-visible-layers':rule==='pending'?'rule-pending':'candidate',
  correspondenceEstablished:false,alignment:'ordinal comparison positions only; source IDs have not been assigned native identities',
  counts:{referenceStrands:referenceColumns.length,combinedStrands:combinedColumns.length,sourceCopies:combinedColumns.reduce((n,s)=>n+s.copies.length,0),projectedPaths:combinedColumns.reduce((n,s)=>n+s.paths.length,0)}};
}
// Each column shows a complete route in its own miniature projection. The
// common column grid is comparison alignment, not a fabricated identity map.
export function projectComparisonColumns(columns,slotCount=columns.length||16){
 const points=columns.flatMap(c=>c.paths.flatMap(p=>p.points));if(!points.length)return [];
 const xmin=Math.min(...points.map(p=>p[0])),xmax=Math.max(...points.map(p=>p[0])),ymin=Math.min(...points.map(p=>p[1])),ymax=Math.max(...points.map(p=>p[1]));
 const width=600/slotCount;
 return columns.map(c=>({...c,x:20+(c.column+.5)*width,paths:c.paths.map(path=>{
  const coordinates=path.points.map(p=>[20+(c.column+.5)*width+((p[0]-xmin)/(xmax-xmin||1)-.5)*width*.75,32+(p[1]-ymin)/(ymax-ymin||1)*144]);
  const polarity=c.polarityDirection||c.routeDirection||0;
  const polarityArrows=[];
  if(polarity)for(let i=1;i<coordinates.length;i++){
   const a=coordinates[i-1],b=coordinates[i],delta=b.map((x,j)=>x-a[j]),length=Math.hypot(...delta);
   if(length>1e-9){
    const centre=a.map((x,j)=>(x+b[j])/2),unit=delta.map(x=>x/length*polarity);
    polarityArrows.push({segment:i-1,centre,angle:Math.atan2(unit[1],unit[0])*180/Math.PI,direction:polarity,kind:c.polarityDirection?'polarity':'route'});
   }
  }
  return {...path,coordinates,svg:coordinates.map(p=>p.join(',')).join(' '),polarityArrows};
 })}));
}
