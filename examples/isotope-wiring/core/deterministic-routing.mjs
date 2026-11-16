// Trial rotation-system routing, not a derived frame-transport law.
// A routing state includes an outgoing edge and a handedness (+1 or -1).
export function buildDeterministicRouting(binding){
 const {vertices,edges}=binding.topology,vertexMap=new Map(vertices.map(v=>[v.id,v])),edgeMap=new Map(edges.map(e=>[e.id,e])),ports=new Map(vertices.map(v=>[v.id,[]]));
 if(vertexMap.size!==vertices.length||edgeMap.size!==edges.length)throw Error('Duplicate graph IDs');
 for(const e of edges){const r=edgeMap.get(e.reverse);if(!ports.has(e.from)||!ports.has(e.to)||!r||r.from!==e.to||r.to!==e.from||r.reverse!==e.id||r.support!==e.support)throw Error('Invalid reverse incidence');ports.get(e.from).push(e);}
 const order=[];
 for(const [id,rows] of ports){
  const p=vertexMap.get(id).position;if(!Array.isArray(p)||p.length!==2||!p.every(Number.isFinite))throw Error('Explicit finite projection coordinates required');
  const angle=e=>{const q=vertexMap.get(e.to).position;return Math.atan2(-(q[1]-p[1]),q[0]-p[0]);};
  rows.sort((a,b)=>angle(a)-angle(b));
  // No identifier-based tie breaking: coincident projected rays need another rule.
  for(let i=0;i<rows.length;i++)for(let j=i+1;j<rows.length;j++)if(Math.abs(angle(rows[i])-angle(rows[j]))<1e-12)throw Error(`Ambiguous cyclic order at ${id}`);
  order.push({vertex:id,outgoing:rows.map(e=>e.id)});
 }
 const key=s=>JSON.stringify([s.edge,s.hand]);
 const reverse=s=>({edge:edgeMap.get(s.edge).reverse,hand:-s.hand});
 function next(s){
  if(![1,-1].includes(s.hand)||!edgeMap.has(s.edge))throw Error('Invalid routing state');
  const e=edgeMap.get(s.edge),at=ports.get(e.to),i=at.findIndex(r=>r.id===e.reverse);
  return {edge:at[(i+s.hand+at.length)%at.length].id,hand:s.hand};
 }
 const states=edges.flatMap(e=>[1,-1].map(hand=>({edge:e.id,hand}))),predecessors=new Map(),transitions=[];
 let backtracks=0;
 for(const s of states){const n=next(s),k=key(n);predecessors.set(k,(predecessors.get(k)||0)+1);transitions.push({from:s,to:n});if(n.edge===edgeMap.get(s.edge).reverse)backtracks++;
  // If e -> f is allowed, reverse(f) -> reverse(e) must also be allowed.
  if(key(next(reverse(n)))!==key(reverse(s)))throw Error('Routing fails reversal');
 }
 if(predecessors.size!==states.length||[...predecessors.values()].some(n=>n!==1))throw Error('Routing is not a permutation');
 const seen=new Set(),cycles=[],stateCycles=new Map();
 for(const start of states){if(seen.has(key(start)))continue;const cycle=[];let s=start;
  do{if(seen.has(key(s)))throw Error('Cycle merged before returning');seen.add(key(s));stateCycles.set(key(s),cycles.length);cycle.push(s);s=next(s);}while(key(s)!==key(start));
  cycles.push({id:`route:${cycles.length}`,states:cycle,length:cycle.length});
 }
 const routes=[];
 for(const b of binding.peBindings){
  const declared=binding.topology.walks.find(w=>w.id===b.pair);if(!declared)throw Error('Missing PE departure binding');
  for(const hand of [1,-1]){
   const start={edge:declared.edges[0],hand},steps=[];let s=start;
   do{steps.push(s.edge);s=next(s);}while(key(s)!==key(start));
   if(edgeMap.get(steps[0]).from!==b.vertex||edgeMap.get(steps.at(-1)).to!==b.vertex)throw Error('PE route is not based at its PE vertex');
   const reversed=[...steps].reverse().map(id=>edgeMap.get(id).reverse);let rs={edge:reversed[0],hand:-hand};
   for(const expected of reversed){if(rs.edge!==expected)throw Error('Reverse roundtrip differs');rs=next(rs);}
   if(rs.edge!==reversed[0]||rs.hand!==-hand)throw Error('Reverse state did not return');
   routes.push({pair:b.pair,base:b.vertex,hand,departure:start.edge,cycle:stateCycles.get(key(start)),edges:steps,reverseEdges:reversed,reverseHand:-hand,firstVertexReturn:steps.findIndex(id=>edgeMap.get(id).to===b.vertex)+1,fullStateReturn:steps.length});
  }
 }
 return {definitionId:binding.definitionId,status:'verified-for-declared-rule',rule:'Next port in cyclic projected order after the reversed arrival leg; handedness +1 or -1. Reverse traversal flips handedness.',
  assumptions:['Screen y is inverted when defining counterclockwise port order.','Projected cyclic port order is a chosen rotation system, not inferred tetrahedral depth.','State includes incoming/outgoing incidence and handedness, not just a PE vertex.'],
  counts:{vertices:vertices.length,directedEdges:edges.length,routingStates:states.length,cycles:cycles.length,PEOccurrences:binding.peBindings.length,PETrials:routes.length,immediateBacktracks:backtracks,oddDegreeVertices:order.filter(v=>v.outgoing.length%2===1).length},
  order,transitions,cycles,PEroutes:routes,
  checks:{oneSuccessorPerState:true,onePredecessorPerState:true,reversalCompatible:true,allStatesPeriodic:true,allPETrialsReturn:true},
  frameReturn:'unknown: routing handedness is not an SO(3) frame; no transport law was added',
  limitation:'Uniqueness is conditional on the declared departure and handedness. Multiple possible routing rules and initial PE states remain; periodicity follows from the finite permutation.'};
}
