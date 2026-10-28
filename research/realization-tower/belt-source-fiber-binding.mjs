// Candidate presentation adapter for the prior twelve-sector marked table.
// No physical P/E, field-map or parent-face binding is inferred from this codec.
export const sectorRows=()=>Array.from({length:4},(_,s)=>Array.from({length:4},(_,t)=>({label:4*s+t,source:s,target:t})).filter(r=>r.source!==r.target)).flat();
export function bindSourceFibers(rows,layer,{marking=[0,1,2,3],history=[]}={}){
 if(!['star-array','tube-ports'].includes(layer.kind)||marking.length!==4||new Set(marking).size!==4)throw Error('Expected four marked endpoints and retained outer star addresses');
 if(rows.length!==12||new Set(rows.map(r=>r.label)).size!==12||new Set(rows.map(r=>`${marking.indexOf(r.source)}:${marking.indexOf(r.target)}`)).size!==12)throw Error('Expected twelve distinct directed sector occurrences');
 const satellites=rows.map(row=>{const s=marking.indexOf(row.source),t=marking.indexOf(row.target);if(s<0||t<0||s===t)throw Error('Invalid marked sector');const arm=(s^t)-1,node=layer.nodes.find(n=>!n.starCentre&&n.group===s&&n.arm===arm);if(!node)throw Error('Missing satellite');return {node:node.id,star:s,arm,row:structuredClone(row)};});
 const centres=marking.map((endpoint,star)=>({node:layer.nodes.find(n=>n.starCentre&&n.group===star).id,endpoint,sourceRows:satellites.filter(r=>r.row.source===endpoint).map(r=>r.row.label),targetRows:satellites.filter(r=>r.row.target===endpoint).map(r=>r.row.label)}));
 return {status:'candidate-labelled-presentation',selector:'source',marking:[...marking],armConvention:'source-index XOR target-index minus one',history:structuredClone(history),satellites,centres,scope:'Centres retain fiber keys and row references, not new rows or a summed field. Source/target groupings are distinct.'};
}
export function restoreSourceFibers(binding){
 if(binding.selector!=='source')throw Error('Missing source-column marker');
 return binding.satellites.map(s=>structuredClone(s.row));
}
export function auditSourceFiberRouting(model,sourceIndex,targetIndex){
 const source=model.layers[sourceIndex],target=model.layers[targetIndex],binding=bindSourceFibers(sectorRows(),source),outgoing=new Map(model.layers.flatMap(l=>l.nodes).map(n=>[n.id,[]]));for(const edge of model.links)outgoing.get(edge.from).push(edge.to);
 const sinks=target.nodes.filter(n=>n.starCentre).sort((a,b)=>a.group-b.group),sinkIndex=new Map(sinks.map((n,i)=>[n.id,i]));
 function terminalShares(id,active=new Set()){
  if(active.has(id))throw Error('Cyclic routing not admitted by this audit');if(sinkIndex.has(id)){const result=[0,0,0,0];result[sinkIndex.get(id)]=1;return result;}
  const next=outgoing.get(id);if(!next?.length)throw Error('Unexpected terminal');const seen=new Set(active).add(id),result=[0,0,0,0];for(const child of next){const v=terminalShares(child,seen);v.forEach((x,i)=>result[i]+=x/next.length);}return result;
 }
 const rows=binding.satellites.map(s=>{const shares=terminalShares(s.node),intendedStar=s.row.target;return {...s,equalSplitShares:shares,intendedStar,intendedReachable:shares[intendedStar]>0,exclusiveTarget:shares.every((q,i)=>Math.abs(q-(i===intendedStar?1:0))<1e-12)};});
 return {sourceLayer:source.label,targetLayer:target.label,binding,rows,equalSplitTransfer:sinks.map((_,i)=>rows.map(r=>r.equalSplitShares[i])),addressedTargetTransfer:sinks.map((_,i)=>rows.map(r=>r.intendedStar===i?1:0)),addressedSinkFlux:sinks.map((_,i)=>rows.filter(r=>r.intendedStar===i).length),allIntendedTargetsReachable:rows.every(r=>r.intendedReachable),equalSplittingRespectsTargets:rows.every(r=>r.exclusiveTarget),scope:'Equal-split columns trace one normalized source at a time. Addressed target matrix is a candidate demultiplexer, not installed transport.'};
}
