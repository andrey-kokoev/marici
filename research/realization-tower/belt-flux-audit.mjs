// Geometric steady-flow audit, not a mechanical stability simulation.
// Node arrows are axial. Wires use a separately declared unit-momentum-per-
// flux convention to expose turning loads and angular transport across cuts.
const add=(a,b)=>a.map((v,i)=>v+b[i]),sub=(a,b)=>a.map((v,i)=>v-b[i]),mul=(a,s)=>a.map(v=>v*s),dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],unit=a=>mul(a,1/Math.hypot(...a));
const sum=vs=>vs.reduce(add,[0,0,0]),norm=Math.hypot;
export function deriveBeltFlux(model,sourceRate=1){
 if(!(sourceRate>0&&Number.isFinite(sourceRate)))throw Error('Expected positive source flux');
 const nodes=model.layers.flatMap(l=>l.nodes),last=model.layers.length,byId=new Map(nodes.map(n=>[n.id,n])),incoming=new Map(nodes.map(n=>[n.id,[]])),outgoing=new Map(nodes.map(n=>[n.id,[]]));
 for(const edge of model.links){if(!byId.has(edge.from)||!byId.has(edge.to))throw Error('Unknown endpoint');outgoing.get(edge.from).push(edge);incoming.get(edge.to).push(edge);}
 const pending=new Map(nodes.map(n=>[n.id,incoming.get(n.id).length])),queue=nodes.filter(n=>pending.get(n.id)===0).map(n=>n.id),edgeRates={},injection={},extraction={},nodeRates={};let visited=0;
 for(let i=0;i<queue.length;i++){
  const id=queue[i],node=byId.get(id),edges=outgoing.get(id),source=(node.layer===1&&node.direction==='E')||(node.layer===last&&node.direction==='P'),sink=(node.layer===1&&node.direction==='P')||(node.layer===last&&node.direction==='E');
  injection[id]=source?sourceRate:0;
  const rate=incoming.get(id).reduce((s,e)=>s+edgeRates[e.id],injection[id]);nodeRates[id]=rate;extraction[id]=sink?rate:0;
  if(sink&&edges.length)throw Error('Boundary sink has outgoing wiring');
  if(!sink&&!edges.length&&rate>0)throw Error('Internal dead end');
  for(const edge of edges){edgeRates[edge.id]=rate/edges.length;pending.set(edge.to,pending.get(edge.to)-1);if(pending.get(edge.to)===0)queue.push(edge.to);}
  visited++;
 }
 if(visited!==nodes.length)throw Error('Equal-split propagation requires an acyclic graph');
 return {sourceRate,edgeRates,injection,extraction,nodeRates};
}
// Diagnostic control only. Preserve geometry and branch counts, but attach each
// outer star satellite to the matching arm of the inner star on the primed side.
export function reflectedStarWiringControl(model){
 const copy=structuredClone(model),outer=copy.layers.at(-1),inner=copy.layers.at(-2),nodes=new Map(outer.nodes.map(n=>[n.id,n]));
 copy.links=copy.links.map(edge=>{
  const node=nodes.get(edge.outer);if(!node||!inner.nodes.some(n=>n.id===edge.inner))return edge;
  const slot=inner.starSlots[node.starCentre?3:node.arm],target=inner.nodes.find(n=>n.slot===slot);
  if(target.direction!==node.direction)throw Error('Control would cross transport directions');
  return {...edge,inner:target.id,from:edge.from===node.id?node.id:target.id,to:edge.to===node.id?node.id:target.id,bundle:{row:target.row,column:target.column}};
 });
 const links=new Map(copy.links.map(e=>[e.id,e]));for(const w of copy.wiring)w.branches=w.branches.map(e=>links.get(e.id));
 return copy;
}
function anisotropy(matrix){const [[a,b],[,d]]=matrix,trace=a+d;return {matrix,trace,relativeEigenvalueGap:trace>1e-14?Math.hypot(a-d,2*b)/trace:0};}
export function measureBeltFlux(model,flow){
 const nodes=model.layers.flatMap(l=>l.nodes),byId=new Map(nodes.map(n=>[n.id,n])),normal=unit(model.normal),seed=Math.abs(normal[0])<.8?[1,0,0]:[0,1,0],x=unit(cross(normal,seed)),y=cross(normal,x),origin=model.origin;
 const residual=new Map(nodes.map(n=>[n.id,(flow.injection[n.id]??0)-(flow.extraction[n.id]??0)])),reaction=new Map(nodes.map(n=>[n.id,mul(normal,(n.direction==='P'?1:-1)*((flow.injection[n.id]??0)-(flow.extraction[n.id]??0)))]));
 const segments=model.links.map(edge=>{
  const q=flow.edgeRates[edge.id];if(!(q>=0&&Number.isFinite(q)))throw Error('Missing or invalid edge flux');
  const a=byId.get(edge.from),b=byId.get(edge.to),u=unit(sub(b.position,a.position)),momentum=mul(u,q),mid=mul(add(a.position,b.position),.5);
  residual.set(a.id,residual.get(a.id)-q);residual.set(b.id,residual.get(b.id)+q);
  reaction.set(a.id,sub(reaction.get(a.id),momentum));reaction.set(b.id,add(reaction.get(b.id),momentum));
  return {edge,q,a,b,u,mid,momentum};
 });
 const layers=model.layers.map(layer=>{
  const totals={P:0,E:0},signedPosition=[0,0,0],matrix=[[0,0],[0,0]];
  for(const node of layer.nodes){const q=flow.nodeRates[node.id],r=sub(node.position,layer.center),sign=node.direction==='P'?1:-1;totals[node.direction]+=q;for(let j=0;j<3;j++)signedPosition[j]+=sign*q*r[j];const v=[dot(r,x),dot(r,y)];for(let a=0;a<2;a++)for(let b=0;b<2;b++)matrix[a][b]+=q*v[a]*v[b];}
  const force=sum(layer.nodes.map(n=>reaction.get(n.id))),torque=sum(layer.nodes.map(n=>cross(sub(n.position,origin),reaction.get(n.id))));
  return {label:layer.label,directionalFlux:totals,signedAxialFlux:totals.P-totals.E,axialArrowMoment:cross(signedPosition,normal),positionAnisotropy:anisotropy(matrix),turningReaction:force,turningMoment:torque,maxNodeTurningReaction:Math.max(...layer.nodes.map(n=>norm(...reaction.get(n.id))))};
 });
 const cuts=model.layers.slice(0,-1).map((layer,i)=>{
  const edges=segments.filter(s=>Math.min(s.a.layer,s.b.layer)===i+1&&Math.max(s.a.layer,s.b.layer)===i+2),totals={P:0,E:0},matrix=[[0,0],[0,0]];
  for(const s of edges){totals[s.edge.direction]+=s.q;const v=[dot(s.u,x),dot(s.u,y)];for(let a=0;a<2;a++)for(let b=0;b<2;b++)matrix[a][b]+=s.q*v[a]*v[b];}
  const vector=sum(edges.map(s=>s.momentum)),angular=sum(edges.map(s=>cross(sub(s.mid,origin),s.momentum))),axial=dot(vector,normal),axialAngular=dot(angular,normal);
  return {between:[layer.label,model.layers[i+1].label],directionalFlux:totals,vectorFlux:vector,transverseFlux:norm(...sub(vector,mul(normal,axial))),angularTransport:angular,axialAngularTransport:axialAngular,transverseAngularTransport:norm(...sub(angular,mul(normal,axialAngular))),tangentAnisotropy:anisotropy(matrix)};
 });
 const globalReaction=sum([...reaction.values()]),globalMoment=sum(nodes.map(n=>cross(sub(n.position,origin),reaction.get(n.id))));
 return {assumptions:{sourceRate:flow.sourceRate,split:'equal outgoing branches',arrow:'axial',wire:'unit momentum per flux along straight segment',scope:'steady geometric balance; no inertia, stiffness or time evolution'},totalInjection:Object.values(flow.injection).reduce((s,v)=>s+v,0),totalExtraction:Object.values(flow.extraction).reduce((s,v)=>s+v,0),maxConservationResidual:Math.max(...[...residual.values()].map(Math.abs)),layers,cuts,globalTurningReaction:globalReaction,globalTurningMoment:globalMoment,maxNodeTurningReaction:Math.max(...[...reaction.values()].map(v=>norm(...v)))};
}
