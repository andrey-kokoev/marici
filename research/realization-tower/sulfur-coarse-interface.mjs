// Layer-side coarse geometry and causal subchannel audit. No native routes.
import {auditLayerHistory,encodeHistoryBit} from './sulfur-layer-history.mjs';
const sub=(a,b)=>a.map((x,i)=>x-b[i]);
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const require=(ok,message)=>{if(!ok)throw Error(message);};
export function coarsenWhiteBranchLayer(layer){
 const positions=new Map(layer.nodes.map(n=>[n.id,n.point])),edges=[];
 for(const white of layer.edges.filter(e=>e.role==='white'))for(const branch of layer.edges.filter(e=>e.from===white.to&&e.role!=='white')){
  edges.push({from:white.from,to:branch.to,colour:branch.role,constituents:[white.id,branch.id],points:[positions.get(white.from),positions.get(branch.to)]});
 }
 const nodes=[...new Set(edges.flatMap(e=>[e.from,e.to]))].map(id=>({id,point:positions.get(id),incoming:edges.filter(e=>e.to===id),outgoing:edges.filter(e=>e.from===id)}));
 return {nodes,edges,scope:'White-edge contraction with white-tail vertex positions; metric on coarse endpoint chords, not an isometry of the original two-edge paths'};
}
export function auditReturnInterface(layer){
 const history=auditLayerHistory(layer),coarse=coarsenWhiteBranchLayer(layer),anchor=history.interfaces[0];
 require(anchor,'No first two-history merge');
 const white=history.whiteRecords.find(w=>w.edge===anchor.whiteEdge),start=coarse.nodes.find(n=>n.id===white.from);
 const step=(node,colour)=>{const edge=node.outgoing.find(e=>e.colour===colour);require(edge,'Missing coarse branch');return coarse.nodes.find(n=>n.id===edge.to);};
 const rb=step(step(start,'red'),'blue'),br=step(step(start,'blue'),'red');
 require(rb.id===br.id,'Two unlike choices do not form a return diamond');
 const end=rb,target=history.whiteRecords.find(w=>w.from===end.id);
 require(target.depth===white.depth+2,'Wrong return depth');
 const atDepth=history.whiteRecords.filter(w=>w.depth===target.depth);
 const visits=r=>r.path.includes(anchor.whiteEdge);
 const selected=target.records.filter(visits),bypass=target.records.filter(r=>!visits(r));
 const escaping=atDepth.filter(w=>w.from!==end.id).flatMap(w=>w.records.filter(visits).map(r=>({word:r.word,end:w.from})));
 const originalEdges=new Map(layer.edges.map(e=>[e.id,e]));
 const fullWords=layer.routes.map(r=>r.edges.map(id=>originalEdges.get(id).role).filter(c=>c!=='white').map(c=>c==='red'?'R':'B').join(''));
 const selectedStates=selected.map(r=>{
  const retainedColour=r.word[white.depth-1]==='R'?'red':'blue',portColour=originalEdges.get(r.arrival).role;
  const completions=fullWords.filter(w=>w.startsWith(r.word)),next={red:0,blue:0};
  for(const w of completions)next[w[target.depth]==='R'?'red':'blue']++;
  return {word:r.word,portColour,retainedColour,candidateB:encodeHistoryBit(retainedColour),completions:r.completions,nextChoices:next};
 });
 const arms=end.incoming.map(e=>sub(e.points[0],end.point)),out=end.outgoing.map(e=>sub(e.points[1],end.point));
 return {layer:layer.id,anchor:{whiteEdge:anchor.whiteEdge,vertex:start.id,depth:white.depth},
  target:{whiteEdge:target.edge,vertex:end.id,depth:target.depth,point:end.point,incoming:end.incoming,outgoing:end.outgoing},
  metric:{armSquaredLengths:arms.map(a=>dot(a,a)),incomingCosine:dot(arms[0],arms[1])/Math.sqrt(dot(arms[0],arms[0])*dot(arms[1],arms[1])),outgoingAreStraightContinuations:out.every(d=>arms.some(a=>d.every((x,i)=>Math.abs(x+a[i])<1e-10)))},
  selectedStates,bypass:bypass.map(r=>r.word),escaping,
  counts:{allArrivals:target.records.length,selectedArrivals:selected.length,bypassingArrivals:bypass.length,escapingAnchorHistories:escaping.length},
  closedChannel:escaping.length===0&&bypass.length===0,scope:'Selected classes are conditioned on a past anchor visit; all bypass and escape classes remain present'};
}
// Construct a plane similarity from two specified port correspondences.
// This does not choose those correspondences or assign native state labels.
export function planeSimilarity(sourceOrigin,sourcePorts,targetOrigin,targetPorts){
 const s=sourcePorts.map(p=>sub(p,sourceOrigin)),t=targetPorts.map(p=>sub(p,targetOrigin));
 const g=s.map(a=>s.map(b=>dot(a,b))),h=t.map(a=>t.map(b=>dot(a,b))),det=g[0][0]*g[1][1]-g[0][1]**2;
 require(det>1e-12,'Degenerate source frame');const scaleSquared=h[0][0]/g[0][0];
 require(g.every((row,i)=>row.every((x,j)=>Math.abs(h[i][j]-scaleSquared*x)<1e-10)),'Port frames are not similar');
 const map=point=>{
  const v=sub(point,sourceOrigin),v0=dot(v,s[0]),v1=dot(v,s[1]);
  const a=(g[1][1]*v0-g[0][1]*v1)/det,b=(g[0][0]*v1-g[0][1]*v0)/det;
  require(v.every((x,i)=>Math.abs(x-a*s[0][i]-b*s[1][i])<1e-9),'Point is outside source plane');
  return targetOrigin.map((x,i)=>x+a*t[0][i]+b*t[1][i]);
 };
 return {scaleSquared,map};
}
