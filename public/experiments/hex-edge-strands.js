// Classic script so the experiment continues to work from file:// URLs.
// Enumerate actual directed growth paths; never infer paths from a target count.
function calculateSeedStrands(simplex) {
  const outgoing=new Map([...simplex.vertices.keys()].map(id=>[id,[]]));
  for(const edge of simplex.edges.values()) {
    let a=simplex.vertices.get(edge.a),b=simplex.vertices.get(edge.b);
    if((b.x-a.x)*simplex.direction.dx+3*(b.y-a.y)*simplex.direction.dy<0) [a,b]=[b,a];
    outgoing.get(a.id).push({vertex:b,edge:edge.id,role:simplexEdgeRole(a,b,simplex.direction)});
  }
  const strands=[];
  function visit(vertices,edges,choices) {
    const next=outgoing.get(vertices.at(-1).id).sort((a,b)=>a.role.localeCompare(b.role)||a.vertex.id.localeCompare(b.vertex.id));
    if(!next.length) {
      const id='S'+choices.join('');
      strands.push({id,choices:[...choices],seedVertices:vertices,seedEdges:edges,traces:[{history:[],vertices,edges}]});
      return;
    }
    for(const arm of next)visit([...vertices,arm.vertex],[...edges,arm.edge],next.length>1?[...choices,arm.role==='left'?'L':'R']:choices);
  }
  const origin=simplex.vertices.get(`v(${simplex.origin.x},${simplex.origin.y})`);
  visit([origin],[],[]);
  return strands;
}
function cloneStrandTraces(strands,transform,operation) {
  return strands.map(strand=>({...strand,traces:[...strand.traces,...strand.traces.map(trace=>{
    const vertices=trace.vertices.map(transform),edges=vertices.slice(1).map((v,i)=>{
      const [a,b]=[vertices[i],v].sort((a,b)=>a.x-b.x||a.y-b.y);
      return `e[${a.x},${a.y}|${b.x},${b.y}]`;
    });
    return {history:[...trace.history,operation],vertices,edges};
  })]}));
}
function auditStrands(scene) {
  const strands=scene.strands||[],memberships=new Map();
  for(const strand of strands)for(const trace of strand.traces)for(const edge of trace.edges) {
    if(!scene.edges.has(edge))throw Error(`Strand ${strand.id} leaves the process graph: ${edge}`);
    if(!memberships.has(edge))memberships.set(edge,new Set());memberships.get(edge).add(strand.id);
  }
  return {strands:strands.length,traceCopies:strands.reduce((n,s)=>n+s.traces.length,0),
    seedTerminals:new Set(strands.map(s=>s.seedVertices.at(-1).id)).size,
    edges:memberships.size,unassignedEdges:[...scene.edges.keys()].filter(id=>!memberships.has(id)),memberships};
}
