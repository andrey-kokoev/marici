// Regular square-projection tetrahedral lifts with explicit contact constraints.
// Wrapper transport is not a geometric equality constraint.
export function solveTetrahedralDepths(full,{tolerance=1e-8,maxCells=16,allowContactTranslation=false}={}){
 if(full.mode!=='direct')throw Error('Direct-contact depth constraints only; mediator extent is unspecified');
 if(!Number.isFinite(tolerance)||tolerance<=0||tolerance>1e-3)throw Error('Invalid geometric tolerance');
 const model=full.model,spaces=model.spaces,vertices=new Map(model.topology.vertices.map(v=>[v.id,v])),ports=new Map();
 if(!Number.isInteger(maxCells)||maxCells<1||maxCells>20||spaces.length>maxCells)throw Error('Depth enumeration bound exceeded or invalid');
 const cells=spaces.map((s,index)=>{
  const p=Object.fromEntries(Object.entries(s.ports).map(([name,id])=>[name,vertices.get(id)?.position]));
  if(Object.values(p).some(v=>!Array.isArray(v)||v.length!==2||!v.every(Number.isFinite)))throw Error('Missing square projection');
  const center=[(p.L[0]+p.R[0])/2,(p.T[1]+p.B[1])/2],radius=(p.R[0]-p.L[0])/2;
  const expected={T:[center[0],center[1]-radius],R:[center[0]+radius,center[1]],B:[center[0],center[1]+radius],L:[center[0]-radius,center[1]]};
  if(radius<=0||Object.keys(p).some(k=>p[k].some((x,i)=>Math.abs(x-expected[k][i])>tolerance)))throw Error('Regular lift requires an axis-aligned square projection');
  const cell={id:s.cell,space:s.id,index,center,radius,height:radius/Math.sqrt(2),positions:p};
  for(const [name,id] of Object.entries(s.ports))ports.set(id,{cell,index,name,parity:['T','B'].includes(name)?1:-1});
  return cell;
 });
 const constraints=[],seenSupports=new Set();
 for(const e of model.topology.edges)if(['neutron-space-contact','stacked-interface'].includes(e.kind)&&!seenSupports.has(e.support)){
  const a=ports.get(e.from),b=ports.get(e.to);if(!a||!b)throw Error('Contact is not between two cell ports');
  const pa=a.cell.positions[a.name],pb=b.cell.positions[b.name],projectionDelta=pa.map((x,i)=>x-pb[i]);
  if(projectionDelta.some(x=>Math.abs(x)>tolerance)&&!allowContactTranslation)throw Error(`Fixed projection prevents contact on ${e.support}: required relative translation ${JSON.stringify(projectionDelta)}`);
  seenSupports.add(e.support);constraints.push({support:e.support,from:e.from,to:e.to,a:a.index,b:b.index,fromPort:a.name,toPort:b.name,projectionDelta,fromHeight:a.parity*a.cell.height,toHeight:b.parity*b.cell.height});
 }
 if(!constraints.some(c=>full.interface.channelSupports.includes(c.support)))throw Error('Stacked contact is absent from geometric constraints');
 const adjacency=cells.map(()=>[]);constraints.forEach((c,i)=>{adjacency[c.a].push({constraint:i,other:c.b,orientation:1});adjacency[c.b].push({constraint:i,other:c.a,orientation:-1});});
 const solutions=[],rejections=[];let componentCount;
 for(let mask=0;mask<2**cells.length;mask++){
  const signs=cells.map((_,i)=>(mask>>i)&1?-1:1),offsets=new Map(),xyOffsets=new Map(),components=[],violations=[];
  for(let root=0;root<cells.length;root++)if(!offsets.has(root)){
   offsets.set(root,0);xyOffsets.set(root,[0,0]);const queue=[root];
   for(let i=0;i<queue.length;i++)for(const entry of adjacency[queue[i]]){
    const c=constraints[entry.constraint],delta=signs[c.a]*c.fromHeight-signs[c.b]*c.toHeight;
    const wanted=offsets.get(queue[i])+entry.orientation*delta;
    if(!offsets.has(entry.other)){offsets.set(entry.other,wanted);xyOffsets.set(entry.other,xyOffsets.get(queue[i]).map((x,k)=>x+entry.orientation*c.projectionDelta[k]));queue.push(entry.other);}
   }
   components.push(queue.map(i=>cells[i].id));
  }
  componentCount=components.length;
  for(const c of constraints){const residual=offsets.get(c.a)+signs[c.a]*c.fromHeight-offsets.get(c.b)-signs[c.b]*c.toHeight;const projectedResidual=xyOffsets.get(c.a).map((x,i)=>x+c.projectionDelta[i]-xyOffsets.get(c.b)[i]);if(Math.abs(residual)>tolerance||projectedResidual.some(x=>Math.abs(x)>tolerance))violations.push({support:c.support,residual,projectedResidual});}
  if(violations.length){rejections.push({mask,violations});continue;}
  const coordinates={};
  for(const cell of cells)coordinates[cell.id]=Object.fromEntries(Object.entries(cell.positions).map(([port,xy])=>[port,[...xy.map((x,i)=>x+xyOffsets.get(cell.index)[i]),offsets.get(cell.index)+signs[cell.index]*(['T','B'].includes(port)?1:-1)*cell.height]]));
  solutions.push({mask,signs:Object.fromEntries(cells.map(c=>[c.id,signs[c.index]])),centerDepths:Object.fromEntries(cells.map(c=>[c.id,offsets.get(c.index)])),projectedTranslations:Object.fromEntries(cells.map(c=>[c.id,xyOffsets.get(c.index)])),components,coordinates});
 }
 const relations=[];
 if(solutions.length)for(let i=0;i<cells.length;i++)for(let j=i+1;j<cells.length;j++){
  const products=new Set(solutions.map(s=>s.signs[cells[i].id]*s.signs[cells[j].id]));if(products.size===1)relations.push({cells:[cells[i].id,cells[j].id],relation:[...products][0]===1?'same-depth-sign':'opposite-depth-sign'});
 }
 return {definitionId:model.definitionId,allowContactTranslation,status:solutions.length?'realizable-under-regular-lift':'refuted-under-regular-lift',
  counts:{cells:cells.length,contactConstraints:constraints.length,signAssignments:2**cells.length,admissibleSignAssignments:solutions.length,geometricComponents:componentCount,relativeComponentDepthOffsets:Math.max(0,componentCount-1)},
  cells:cells.map(({index,positions,...c})=>c),constraints,relations,solutions,allPositiveControl:{admissible:solutions.some(s=>s.mask===0),violations:rejections.find(r=>r.mask===0)?.violations??[]},
  assumptions:['Every projected cell is lifted as a regular tetrahedron, with one binary depth sign.','Only explicit same-shell cell contacts and the direct stacked channel impose equality of 3D vertex positions.',allowContactTranslation?'Projected cell translations are explicitly permitted in the trial embedding, not changes to the drawing.':'Projected cell positions are held fixed.','Each disconnected geometric component has its first cell center depth fixed to zero as a coordinate gauge; relative component translations remain free.'],
  limits:['Wrapper attachments are transport interfaces, not geometrically realized rods or surfaces; they supply no missing depth constraints.','This checks vertex incidence and edge lengths, not nonintersection of volumes or full 3D packing.','Discrete solutions are label- and coordinate-dependent, not a count of physically inequivalent states.','No channel rotation, PE frame law, or neutron-loop transport is selected by this solver.']};
}
