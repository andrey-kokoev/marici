// Trace actual layer edges from the bottom sleeve ports; no native IDs,
// requested wire count, coordinate straightening, or selected route indices.
const require=(ok,message)=>{if(!ok)throw Error(message);};
export function traceSeedConductors(layer,{interiorRouting='same-colour'}={}){
 require(['same-colour','cross-colour'].includes(interiorRouting),'Unknown sleeve routing');
 const nodes=new Map(layer.nodes.map(n=>[n.id,n])),incoming=new Map(),outgoing=new Map();
 for(const e of layer.edges){
  if(!incoming.has(e.to))incoming.set(e.to,[]);incoming.get(e.to).push(e);
  if(!outgoing.has(e.from))outgoing.set(e.from,[]);outgoing.get(e.from).push(e);
 }
 const bottom=layer.edges.filter(w=>w.role==='white'&&(outgoing.get(w.to)??[]).length===2&&(outgoing.get(w.to)??[]).every(e=>!(outgoing.get(e.to)??[]).length))
  .sort((a,b)=>nodes.get(a.from).lattice[1]-nodes.get(b.from).lattice[1]);
 const strands=[];
 for(const [pairIndex,sleeve]of bottom.entries())for(const terminal of outgoing.get(sleeve.to)){
  let vertex=terminal.from,portRole=terminal.role;const reverse=[terminal],events=[],seen=new Set([terminal.to]);
  while(vertex!==layer.root){
   require(!seen.has(vertex),'Backward trace encountered a cycle');seen.add(vertex);
   const choices=incoming.get(vertex)??[];require(choices.length>0,'Trace terminated before the root');
   let chosen;
   if(choices.length===1){
    chosen=choices[0];
    if(chosen.role!=='white'&&chosen.role!==portRole){
     events.push({vertex,kind:'sole-boundary-trunk',fromRole:portRole,toRole:chosen.role,edge:chosen.id});portRole=chosen.role;
    }
   }else{
    const desired=interiorRouting==='same-colour'?portRole:portRole==='red'?'blue':'red';
    const matching=choices.filter(e=>e.role===desired);require(matching.length===1,'No unique requested incoming port');chosen=matching[0];
    if(desired!==portRole)events.push({vertex,kind:'cross-colour-sleeve',fromRole:portRole,toRole:desired,edge:chosen.id});
    portRole=desired;
   }
   reverse.push(chosen);vertex=chosen.from;
  }
  const edges=reverse.reverse(),guide=[nodes.get(edges[0].from).point,...edges.map(e=>nodes.get(e.to).point)];
  strands.push({id:`seed:pair:${pairIndex+1}:${terminal.role}`,pairIndex,colour:terminal.role,sleeve:sleeve.id,terminal:terminal.id,
   edgeIds:edges.map(e=>e.id),guide,word:edges.filter(e=>e.role!=='white').map(e=>e.role==='red'?'R':'B').join(''),
   canonicalEdges:edges.map(e=>`${nodes.get(e.from).lattice.join(',')}→${nodes.get(e.to).lattice.join(',')}`),events:events.reverse()});
 }
 const memberships=layer.edges.map(e=>({edge:e.id,role:e.role,from:e.from,to:e.to,strands:strands.filter(s=>s.edgeIds.includes(e.id)).map(s=>s.id)}));
 return {layer:layer.id,interiorRouting,root:layer.root,strands,memberships,bottomSleeves:bottom.map(e=>e.id),
  scope:'Candidate conductor lift with explicitly chosen sleeve routing; at a boundary follow the sole existing trunk. Conductor identity is distinct from trunk edge colour; conservation alone does not establish a native correspondence.',
  counts:{bottomSleeves:bottom.length,conductors:strands.length,rooted:strands.filter(s=>layer.edges.find(e=>e.id===s.edgeIds[0]).from===layer.root).length,
   coveredEdges:memberships.filter(e=>e.strands.length>0).length,totalEdges:layer.edges.length}};
}
