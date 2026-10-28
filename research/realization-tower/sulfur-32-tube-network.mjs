const pointKey=p=>p.map(x=>Math.round(x*1e9)/1e9).join(',');
const portKey=(edge,p)=>`${edge.id}@${pointKey(p)}`;

// Continue a bundle only when every retained strand makes the same passage.
// Merely touching at a honeycomb vertex does not imply a tube junction.
export function buildSulfurTubeNetwork(model){
 const edges=[...model.edges].sort((a,b)=>a.id.localeCompare(b.id)),nodes=new Map(),wires=new Map(model.strands.map(s=>[s.id,s]));
 const signature=e=>[...e.strandIds].sort().join('|');
 for(const edge of edges)for(const p of edge.guide){const k=pointKey(p);if(!nodes.has(k))nodes.set(k,[]);nodes.get(k).push(edge);}
 const consecutive=(a,b)=>a.strandIds.every(id=>{
  const wire=wires.get(id),i=wire.edgeIds.indexOf(a.id),j=wire.edgeIds.indexOf(b.id);
  return i>=0&&j>=0&&(Math.abs(i-j)===1||(wire.closed&&Math.abs(i-j)===wire.edgeIds.length-1));
 });
 const candidates=new Map();
 for(const edge of edges)for(const p of edge.guide){
  const next=nodes.get(pointKey(p)).filter(e=>e.id!==edge.id&&signature(e)===signature(edge)&&consecutive(edge,e));
  if(next.length===1)candidates.set(portKey(edge,p),next[0]);
 }
 const continuation=new Map();
 for(const edge of edges)for(const p of edge.guide){const next=candidates.get(portKey(edge,p));if(next&&candidates.get(portKey(next,p))?.id===edge.id)continuation.set(portKey(edge,p),next);}
 const used=new Set(),segments=[];
 const trace=(first,start)=>{
  const path=[start],chain=[];let edge=first,point=start,closed=false;
  while(true){
   if(used.has(edge.id))throw Error('Tube continuation reuses an occupied edge');
   used.add(edge.id);chain.push(edge);
   point=edge.guide.find(p=>pointKey(p)!==pointKey(point));path.push(point);
   const next=continuation.get(portKey(edge,point));if(!next)break;
   if(next.id===first.id&&pointKey(point)===pointKey(start)){closed=true;break;}
   edge=next;
  }
  const sourceCells=[...new Set(chain.flatMap(e=>e.carrierCells))].sort();
  segments.push({id:`tube:${chain.map(e=>e.id).sort().join(';')}`,points:path,closed,edgeIds:chain.map(e=>e.id),strandIds:[...first.strandIds],sourceCells,nGroups:model.channelGroups.filter(g=>g.members.some(c=>sourceCells.includes(c))).map(g=>g.id)});
 };
 for(const edge of edges){
  if(used.has(edge.id))continue;
  const start=[...edge.guide].sort((a,b)=>pointKey(a).localeCompare(pointKey(b))).find(p=>!continuation.has(portKey(edge,p)));
  if(start)trace(edge,start);
 }
 for(const edge of edges)if(!used.has(edge.id))trace(edge,[...edge.guide].sort((a,b)=>pointKey(a).localeCompare(pointKey(b)))[0]);
 if(used.size!==edges.length)throw Error('Incomplete tube edge coverage');
 const endpointNodes=new Map(),byEdge=new Map(edges.map(e=>[e.id,e]));
 for(const segment of segments)if(!segment.closed)for(const end of ['start','end']){
  const first=end==='start',point=first?segment.points[0]:segment.points.at(-1),k=pointKey(point);
  if(!endpointNodes.has(k))endpointNodes.set(k,[]);
  endpointNodes.get(k).push({segmentId:segment.id,end,point,edgeId:first?segment.edgeIds[0]:segment.edgeIds.at(-1)});
 }
 const joins=(a,b)=>{
  const ea=byEdge.get(a.edgeId),eb=byEdge.get(b.edgeId);
  return ea.strandIds.filter(id=>eb.strandIds.includes(id)).some(id=>{const w=wires.get(id);return Math.abs(w.edgeIds.indexOf(ea.id)-w.edgeIds.indexOf(eb.id))===1;});
 };
 const junctions=[];
 for(const ports of endpointNodes.values()){
  const remaining=new Set(ports);
  while(remaining.size){
   const component=[remaining.values().next().value];remaining.delete(component[0]);
   for(let i=0;i<component.length;i++)for(const other of remaining)if(joins(component[i],other)){remaining.delete(other);component.push(other);}
   if(component.length>1)junctions.push({id:`junction:${pointKey(component[0].point)}:${component.map(p=>p.edgeId).sort().join(';')}`,point:component[0].point,ports:component});
  }
 }
 const identities=model.channelGroups.map(group=>{
  const owned=edges.filter(e=>e.carrierCells.some(c=>group.members.includes(c))),remaining=new Set(owned.map(e=>e.id)),components=[];
  while(remaining.size){
   const queue=[owned.find(e=>remaining.has(e.id))],component=[];remaining.delete(queue[0].id);
   for(let i=0;i<queue.length;i++){
    const edge=queue[i];component.push(edge.id);
    for(const next of owned)if(remaining.has(next.id)&&next.guide.some(p=>edge.guide.some(q=>pointKey(p)===pointKey(q)))){remaining.delete(next.id);queue.push(next);}
   }
   components.push(component.sort());
  }
  const edgeIds=owned.map(e=>e.id),segmentIds=segments.filter(s=>s.edgeIds.some(id=>edgeIds.includes(id))).map(s=>s.id);
  return {id:group.id,label:group.label??group.id,members:[...group.members],edgeIds,segmentIds,components,sharedSegmentIds:segments.filter(s=>segmentIds.includes(s.id)&&s.nGroups.length>1).map(s=>s.id)};
 });
 return {segments,identities,junctions,audit:{nativeEdges:edges.length,continuousSegments:segments.length,internalJoins:continuation.size/2,closedSegments:segments.filter(s=>s.closed).length}};
}
