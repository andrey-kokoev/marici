import {buildOctahedralFullFibration} from './octahedral-full-fibration.mjs';
const key=vs=>vs.map(String).sort().join('|');
const centre=vs=>vs[0].map((_,i)=>vs.reduce((s,v)=>s+v[i]/vs.length,0));
const phase=q=>q.slice(0,3).map(x=>((x-q[3])%4+4)%4).join(',');
const distance=(a,b)=>a.reduce((s,x,i)=>s+(x-b[i])**2,0);

// UNVALIDATED CANDIDATE. This is bookkeeping over selected correspondences,
// not a coherence constructor or a native-realization certificate. See
// ../strominger/five-side-oct-routing-obligations-v1.md and its audit receipt.
// Route through actual cell ports and opposite N faces. No edge-coverage
// objective, shortest-path search, or filler geometry supplies connectivity.
export function buildOctahedralCoherentRouting(radius){
 const fibration=buildOctahedralFullFibration(radius),{sector}=fibration,cells=new Map(sector.cells.map(c=>[c.id,c]));
 const faces=new Map(sector.faces.map(f=>[f.id,f])),ports=new Map(),slots=[],slotByCellAxis=new Map(),chargedPorts=new Map();
 for(const c of sector.cells){
  const base=c.vertices[0].map((_,i)=>Math.max(...c.vertices.map(v=>v[i])));
  for(let axis=0;axis<4;axis++){
   const fs=c.faces.filter(f=>f.every(p=>p[axis]===f[0][axis])).sort((a,b)=>a[0][axis]-b[0][axis]);
   const ps=fs.map((vertices,i)=>{
    const port={id:`${c.id}/axis:${axis}/face:${i}`,cell:c.id,role:c.role,axis,face:key(vertices),vertices,point:centre(vertices)};ports.set(port.id,port);return port;
   });
   if(c.role==='neutron'){
    if(ps.length!==2)throw Error('N slot needs two opposite faces');
    const entry=ps[0],exit=ps[1],lateral=entry.vertices[0].map((x,i)=>x-entry.point[i]),norm=Math.hypot(...lateral);
    const point=t=>entry.point.map((x,i)=>x+t*(exit.point[i]-x)+.055*lateral[i]/norm);
    const slot={id:`${c.id}/slot:${axis}`,cell:c.id,axis,phase:phase(base),entry:entry.id,exit:exit.id,wireIds:[],points:[entry.point,point(1/3),point(2/3),exit.point]};
    slots.push(slot);slotByCellAxis.set(`${c.id}|${axis}`,slot);
   }else{if(ps.length!==1)throw Error('Charged cell needs one face per axis');chargedPorts.set(`${c.id}|${axis}`,ps[0]);}
  }
 }
 const links=new Map(),routes=[];
 const connect=(from,to,wireId,kind,points)=>{
  const id=`${kind}:${from}->${to}`;
  if(!links.has(id))links.set(id,{id,from,to,kind,axis:ports.get(from).axis,wireIds:[],points:points??[ports.get(from).point,ports.get(to).point]});
  const link=links.get(id);if(link.wireIds.includes(wireId))throw Error('Repeated wire on a connection');link.wireIds.push(wireId);return id;
 };
 const neighbour=port=>faces.get(port.face).owners.find(id=>id!==port.cell);
 let interiorAdmissions=0;
 for(const wire of fibration.wires){
  const source=chargedPorts.get(`${wire.source}|${wire.axis}`),target=chargedPorts.get(`${wire.target}|${wire.axis}`),sourceN=neighbour(source),targetN=neighbour(target);
  const chain=[...new Set([sourceN,targetN].filter(Boolean))].map(id=>slotByCellAxis.get(`${id}|${wire.axis}`));
  if(chain.some(s=>!s))throw Error('Shared face is not an N channel');
  // A boundary-to-boundary record must still enter a real filler channel.
  // Choose a retained lift of its existing Sulfur N phase, not a direct P/E bypass.
  let admission=false;
  if(!chain.length){
   const p=cells.get(wire.source),base=p.vertices[0].map((_,i)=>Math.max(...p.vertices.map(v=>v[i]))+Number(i===wire.axis));
   const candidates=slots.filter(s=>s.axis===wire.axis&&s.phase===phase(base));
   candidates.sort((a,b)=>distance(centre(cells.get(a.cell).vertices),centre(p.vertices))-distance(centre(cells.get(b.cell).vertices),centre(p.vertices))||a.id.localeCompare(b.id));
   if(!candidates.length)throw Error('No retained N lift for boundary wire');chain.push(candidates[0]);admission=true;interiorAdmissions++;
  }
  const path=[source.id],edgeIds=[];let previous=source.id;
  const join=next=>{
   const a=ports.get(previous),b=ports.get(next),native=a.face===b.face;
   if(native&&(!faces.get(a.face).owners.includes(a.cell)||!faces.get(a.face).owners.includes(b.cell)))throw Error('Invalid native interface');
   edgeIds.push(connect(previous,next,wire.id,native?'native-interface':'boundary-seam'));path.push(next);previous=next;
  };
  for(const slot of chain){
   join(slot.entry);slot.wireIds.push(wire.id);
   edgeIds.push(connect(slot.entry,slot.exit,wire.id,'N-interior',slot.points));path.push(slot.exit);previous=slot.exit;
  }
  join(target.id);
  routes.push({...wire,ports:path,links:edgeIds,slots:chain.map(s=>s.id),cells:chain.map(s=>s.cell),interiorAdmission:admission});
 }
 if(slots.some(s=>!s.wireIds.length))throw Error('Unwired filler slot');
 const neighbours=new Map(sector.cells.filter(c=>c.role==='neutron').map(c=>[c.id,new Set()]));
 for(const r of routes)for(let i=1;i<r.cells.length;i++){neighbours.get(r.cells[i-1]).add(r.cells[i]);neighbours.get(r.cells[i]).add(r.cells[i-1]);}
 const unseen=new Set(neighbours.keys()),coherenceGroups=[];
 while(unseen.size){const members=[unseen.values().next().value];unseen.delete(members[0]);for(let i=0;i<members.length;i++)for(const n of neighbours.get(members[i]))if(unseen.delete(n))members.push(n);
  const groupSlots=slots.filter(s=>members.includes(s.cell)),wireIds=[...new Set(groupSlots.flatMap(s=>s.wireIds))];
  coherenceGroups.push({id:`coherence:${coherenceGroups.length+1}`,members,slots:groupSlots.map(s=>s.id),wireIds,internalLinks:groupSlots.map(s=>`N-interior:${s.entry}->${s.exit}`)});
 }
 const result={fibration,ports:[...ports.values()],slots,routes,links:[...links.values()],coherenceGroups};
 result.audit=validateOctahedralCoherentRouting(result);
 return result;
}

export function validateOctahedralCoherentRouting(model){
 const expectedSlots=model.fibration.sector.cells.filter(c=>c.role==='neutron').flatMap(c=>[0,1,2,3].map(axis=>`${c.id}/slot:${axis}`));
 if(model.slots.map(s=>s.id).sort().join('|')!==expectedSlots.sort().join('|'))throw Error('Incomplete filler slot inventory');
 const ports=new Map(model.ports.map(p=>[p.id,p])),links=new Map(model.links.map(l=>[l.id,l])),byWire=new Map(model.fibration.wires.map(w=>[w.id,w]));
 if(new Set(model.routes.map(r=>r.id)).size!==byWire.size||model.routes.length!==byWire.size)throw Error('Lost or duplicated retained wire');
 const nativeFaces=new Map(model.fibration.sector.faces.map(f=>[f.id,f])),cells=new Map(model.fibration.sector.cells.map(c=>[c.id,c])),slots=new Map(model.slots.map(s=>[s.id,s]));
 const traversals=new Map(model.links.map(l=>[l.id,[]]));
 for(const r of model.routes){
  const w=byWire.get(r.id);if(!w||r.links.length!==r.ports.length-1)throw Error('Invalid retained route');
  if(ports.get(r.ports[0]).cell!==w.source||ports.get(r.ports.at(-1)).cell!==w.target)throw Error('Changed fibre correspondence');
  if(new Set(r.ports).size!==r.ports.length)throw Error('Route branches or revisits a port');
  let fillers=0;
  for(let i=0;i<r.links.length;i++){
   const l=links.get(r.links[i]);if(!l||l.from!==r.ports[i]||l.to!==r.ports[i+1]||l.axis!==w.axis)throw Error('Broken port continuation');
   traversals.get(l.id).push(w.id);if(l.kind==='N-interior')fillers++;
  }
  if(!fillers)throw Error('Wire bypasses filler coherence');
  const actualCells=r.links.map(id=>links.get(id)).filter(l=>l.kind==='N-interior').map(l=>ports.get(l.from).cell);
  if(actualCells.join('|')!==r.cells.join('|')||r.slots.map(id=>slots.get(id)?.cell).join('|')!==actualCells.join('|'))throw Error('Route does not follow its declared filler cells');
  const p=cells.get(w.source),expectedPhase=phase(p.vertices[0].map((_,i)=>Math.max(...p.vertices.map(v=>v[i]))+Number(i===w.axis)));
  if(r.slots.some(id=>slots.get(id).axis!==w.axis||slots.get(id).phase!==expectedPhase))throw Error('Wrong filler phase or coordinate slot');
  for(const [portId,cellId] of [[r.ports[0],actualCells[0]],[r.ports.at(-1),actualCells.at(-1)]]){const p=ports.get(portId),neighbour=nativeFaces.get(p.face).owners.find(id=>id!==p.cell);if(neighbour&&neighbour!==cellId)throw Error('Native face neighbour was bypassed');}
 }
 for(const l of model.links){const actual=traversals.get(l.id);if(!actual.length||new Set(l.wireIds).size!==l.wireIds.length||[...actual].sort().join('|')!==[...l.wireIds].sort().join('|'))throw Error('Connection copies or loses wire records');}
 for(const p of model.ports){
  const incoming=model.links.filter(l=>l.to===p.id).flatMap(l=>l.wireIds),outgoing=model.links.filter(l=>l.from===p.id).flatMap(l=>l.wireIds);
  if(new Set(incoming).size!==incoming.length||new Set(outgoing).size!==outgoing.length)throw Error('Broadcast at a port');
  if(p.role==='neutron'&&incoming.sort().join('|')!==outgoing.sort().join('|'))throw Error('Filler port is not conservative');
 }
 for(const s of model.slots){if(ports.get(s.entry)?.cell!==s.cell||ports.get(s.exit)?.cell!==s.cell||ports.get(s.entry).axis!==s.axis||ports.get(s.exit).axis!==s.axis||s.entry===s.exit)throw Error('Invalid internal slot ports');const l=model.links.find(l=>l.kind==='N-interior'&&l.from===s.entry&&l.to===s.exit);if(!l||!s.wireIds.length||[...s.wireIds].sort().join('|')!==[...l.wireIds].sort().join('|'))throw Error('Incomplete filler slot');}
 for(const g of model.coherenceGroups){
  const actualSlots=model.slots.filter(s=>g.members.includes(s.cell));
  if([...g.slots].sort().join('|')!==actualSlots.map(s=>s.id).sort().join('|')||[...g.wireIds].sort().join('|')!==[...new Set(actualSlots.flatMap(s=>s.wireIds))].sort().join('|'))throw Error('Coherence group lost its internal wiring');
 }
 for(const r of model.routes){const owners=model.coherenceGroups.filter(g=>g.wireIds.includes(r.id));if(owners.length!==1||r.cells.some(c=>!owners[0].members.includes(c)))throw Error('Broken coherence-group continuation');}
 const members=model.coherenceGroups.flatMap(g=>g.members),nativeN=model.fibration.sector.cells.filter(c=>c.role==='neutron').map(c=>c.id);
 if(new Set(members).size!==members.length||[...members].sort().join('|')!==nativeN.sort().join('|'))throw Error('Incomplete coherence-group partition');
 return {status:'coherent-port-routing',constructionAdmitted:false,coherenceEstablished:false,nativeRoutingEstablished:false,validationScope:'candidate bookkeeping only; legacy status string is not an admission',inputFibres:model.fibration.sourceFibers.length,outputFibres:model.fibration.targetFibers.length,slotWires:model.routes.length,geometricNCells:nativeN.length,coherenceGroups:model.coherenceGroups.length,internalChannels:model.slots.length,occupiedNativeFaces:new Set(model.ports.map(p=>p.face)).size,nativeInterfaces:model.links.filter(l=>l.kind==='native-interface').length,boundarySeams:model.links.filter(l=>l.kind==='boundary-seam').length,interiorAdmissions:model.routes.filter(r=>r.interiorAdmission).length,unwiredFillerSlots:0,copiedBranches:0,scope:'Explicit opposite-face filler channels and retained boundary seams. Boundary lift selection remains a declared convention; this is not a proof of a physical phase law.'};
}
