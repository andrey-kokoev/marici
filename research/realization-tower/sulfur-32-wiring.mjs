import {buildPESymmetricSector} from '../strominger/pe-symmetric-sector.mjs';
const mod4=x=>((x%4)+4)%4;
const key=vs=>vs.map(v=>v.join(',')).sort().join('|');
const anchor=vs=>[0,1,2,3].map(i=>Math.min(...vs.map(v=>v[i])));
const centre=vs=>vs[0].map((_,i)=>vs.reduce((s,v)=>s+v[i],0)/vs.length);
export const sulfurPeriodGenerators=[0,1,2,3].map(i=>[0,1,2,3].map(j=>1-4*Number(i===j)));
export function isSulfurPeriod(t){return t.every(Number.isInteger)&&t.reduce((a,b)=>a+b,0)===0&&t.every(x=>mod4(x)===mod4(t[3]));}
function shapeClass(vs){const a=anchor(vs);return JSON.stringify([a.slice(0,3).map(x=>mod4(x-a[3])),vs.map(v=>v.map((x,i)=>x-a[i])).sort((a,b)=>a.join(',').localeCompare(b.join(',')))]);}
function require(condition,message){if(!condition)throw Error(message);}
function axisOf(vs){const axes=[0,1,2,3].filter(i=>vs.every(v=>v[i]===vs[0][i]));require(axes.length===1,'Face must have exactly one coordinate normal');return axes[0];}

export function buildSulfur32Wiring(){
 const sector=buildPESymmetricSector(1),cellClasses=new Map(),sourceToGroup=new Map();
 for(const cell of sector.cells){
  const k=cell.role+':'+shapeClass(cell.vertices);
  if(!cellClasses.has(k))cellClasses.set(k,{id:'s32:cell:'+cell.id,role:cell.role,members:[],representative:cell});
  const group=cellClasses.get(k),a=anchor(cell.vertices),b=anchor(group.representative.vertices),translation=a.map((x,i)=>b[i]-x);
  require(isSulfurPeriod(translation),'Invalid cell lift translation');
  require(key(cell.vertices.map(v=>v.map((x,i)=>x+translation[i])))===key(group.representative.vertices),'Cell lift does not recover representative');
  group.members.push({id:cell.id,translation,vertices:cell.vertices,faces:cell.faces});sourceToGroup.set(cell.id,group.id);
 }
 const groups=[...cellClasses.values()],byGroup=new Map(groups.map(g=>[g.id,g])),faceClasses=new Map(),ports=new Map();
 const roleCounts={};for(const g of groups){roleCounts[g.role]=(roleCounts[g.role]??0)+1;g.label=({proton:'P',neutron:'N',electron:'E'})[g.role]+roleCounts[g.role];}
 for(const cell of sector.cells)for(const [faceIndex,vertices] of cell.faces.entries()){
  const fk=shapeClass(vertices),axis=axisOf(vertices),group=byGroup.get(sourceToGroup.get(cell.id)),lift=group.members.find(m=>m.id===cell.id),translated=vertices.map(v=>v.map((x,i)=>x+lift.translation[i]));
  if(!faceClasses.has(fk))faceClasses.set(fk,{id:'s32:face:'+faceClasses.size,axis,ports:[]});
  const face=faceClasses.get(fk),id=group.id+'/port/'+key(translated);
  if(!ports.has(id)){ports.set(id,{id,cell:group.id,role:group.role,face:face.id,axis,vertices:translated,lifts:[]});face.ports.push(id);}
  ports.get(id).lifts.push({cell:cell.id,faceIndex,vertices,translation:lift.translation});
 }
 const faces=[...faceClasses.values()],adj=new Map([...ports.keys()].map(id=>[id,[]])),edges=[];
 const connect=(a,b,kind,transport=[0,0,0,0])=>{const e={id:'s32:edge:'+edges.length,from:a,to:b,kind,transport};edges.push(e);adj.get(a).push(e);adj.get(b).push(e);};
 for(const face of faces){
  require(face.ports.length===2,'Nonclosed or nonmanifold quotient face');
  const [a,b]=face.ports.map(id=>ports.get(id).vertices),aa=anchor(a),bb=anchor(b),translation=aa.map((x,i)=>bb[i]-x);
  require(isSulfurPeriod(translation)&&key(a.map(v=>v.map((x,i)=>x+translation[i])))===key(b),'Face comparison is not an exact period translation');
  face.translation=translation;connect(...face.ports,'shared-quotient-face',translation);
 }
 const channels=groups.filter(g=>g.role==='neutron').map(g=>({id:g.id,members:g.members,slots:Array(4).fill(null)}));
 for(const channel of channels)for(let axis=0;axis<4;axis++){
  const ps=[...ports.values()].filter(p=>p.cell===channel.id&&p.axis===axis);
  require(ps.length===2,'N channel needs two opposite ports per axis');connect(ps[0].id,ps[1].id,'axis-continuity');
 }
 // Solve components of the complete constraint graph; only then orient them.
 const unseen=new Set(ports.keys()),components=[];
 while(unseen.size){const todo=[unseen.values().next().value],component=[];unseen.delete(todo[0]);
  for(let i=0;i<todo.length;i++){const id=todo[i];component.push(id);for(const e of adj.get(id)){const next=e.from===id?e.to:e.from;if(unseen.delete(next))todo.push(next);}}
  components.push(component);
 }
 const wires=components.map(component=>{
  const endpoints=component.filter(id=>ports.get(id).role!=='neutron');
  require(endpoints.length===2,'Closed or branching component has no unique two-ended wire');
  const start=endpoints.find(id=>ports.get(id).role==='proton'),end=endpoints.find(id=>ports.get(id).role==='electron');require(start&&end,'Wire endpoints must be P and E');
  const axis=ports.get(start).axis;require(component.every(id=>ports.get(id).axis===axis),'Wire changes coordinate axis');
  const path=[start],edgePath=[],transports=[];let previous=null;
  while(path.at(-1)!==end){const here=path.at(-1),nextEdges=adj.get(here).filter(e=>e.id!==previous);require(nextEdges.length===1,'Wire branches');const edge=nextEdges[0];previous=edge.id;edgePath.push(edge.id);transports.push(edge.transport.map(x=>x===0?0:edge.from===here?x:-x));path.push(edge.from===here?edge.to:edge.from);require(path.length<=component.length,'Wire cycles');}
  require(path.length===component.length,'Unretained component ports');
  const nCells=[...new Set(path.map(id=>ports.get(id)).filter(p=>p.role==='neutron').map(p=>p.cell))];require(nCells.length===1,'Wire does not pass through exactly one N channel');
  return {id:ports.get(start).cell+'/wire:'+axis,axis,slot:[axis>>1,axis&1],source:ports.get(start).cell,target:ports.get(end).cell,channel:nCells[0],ports:path,edges:edgePath,transports,periodShift:[0,1,2,3].map(i=>transports.reduce((s,t)=>s+t[i],0))};
 }).sort((a,b)=>a.id.localeCompare(b.id));
 const grid=values=>[values.slice(0,2),values.slice(2,4)];
 for(const channel of channels){for(const wire of wires.filter(w=>w.channel===channel.id)){require(!channel.slots[wire.axis],'Duplicate channel slot');channel.slots[wire.axis]=wire.id;}require(channel.slots.every(Boolean),'Incomplete channel');channel.entry=grid(channel.slots);channel.exit=grid(channel.slots);}
 const sourceFibers=groups.filter(g=>g.role==='proton').map(g=>({cell:g.id,slots:[0,1,2,3].map(axis=>wires.filter(w=>w.source===g.id&&w.axis===axis).map(w=>w.id))}));
 const targetFibers=groups.filter(g=>g.role==='electron').map(g=>({cell:g.id,slots:[0,1,2,3].map(axis=>wires.filter(w=>w.target===g.id&&w.axis===axis).map(w=>w.id))}));
 require([...sourceFibers,...targetFibers].every(f=>f.slots.every(s=>s.length===1)),'Endpoint is not 2-by-2');
 const sourceShapes=new Map(sector.cells.map(c=>[key(c.vertices),c.id])),dualGroups={};
 for(const group of groups){const images=group.members.map(m=>sourceToGroup.get(sourceShapes.get(key(m.vertices.map(q=>q.map((x,i)=>2*sector.centre[i]-x))))));require(images.every(id=>id===images[0]),'Dual does not descend to group');dualGroups[group.id]=images[0];}
 const dualWires={};for(const w of wires){const d=wires.filter(v=>v.axis===w.axis&&v.source===dualGroups[w.target]&&v.target===dualGroups[w.source]&&v.channel===dualGroups[w.channel]);require(d.length===1,'Dual wire is ambiguous or missing');dualWires[w.id]=d[0].id;}
 const seamGuides=[],seamLinks=[];
 for(const face of faces){const [a,b]=face.ports.map(id=>ports.get(id));if(a.lifts.some(x=>b.lifts.some(y=>key(x.vertices)===key(y.vertices))))continue;
  const x=a.lifts[0],y=b.lifts[0];seamGuides.push({id:face.id,points:[centre(x.vertices),centre(y.vertices)],color:0xe1bc65,connector:true,overlay:true});
  seamLinks.push({from:x.cell,to:y.cell,kind:'periodic-seam',directed:false});
 }
 const vertexClasses=new Set(),edgeClasses=new Set();
 for(const port of ports.values()){for(const v of port.vertices)vertexClasses.add(shapeClass([v]));for(let i=0;i<3;i++)for(let j=i+1;j<3;j++)edgeClasses.add(shapeClass([port.vertices[i],port.vertices[j]]));}
 const pairLinks=channels.filter(c=>c.members.length===2).map(c=>({from:c.members[0].id,to:c.members[1].id,kind:'retained-tip-pair',directed:false}));
 return {schema:'sulfur-32.global-wiring.v1',closure:'A3 / span_Z(1-4e_i)',generators:sulfurPeriodGenerators,groups,faces,ports:[...ports.values()],edges,wires,channels,sourceFibers,targetFibers,dualGroups,dualWires,seamGuides,seamLinks,pairLinks,
  counts:{sourceCells:sector.cells.length,cellFibers:groups.length,NChannels:channels.length,PSourceFibers:sourceFibers.length,ETargetFibers:targetFibers.length,wires:wires.length,quotientFaces:faces.length,quotientEdges:edgeClasses.size,quotientVertices:vertexClasses.size,periodicSeams:seamLinks.length,tipPairs:pairLinks.length},
  scope:'Candidate global periodic closure. All geometric lifts retained. Coordinate axes index the 2-by-2 ports; no transformation of wire payloads or physical sulfur identification is inferred.'};
}

export function presentSulfurWires(model,direction='P|E'){
 if(!['P|E','E|P'].includes(direction))throw Error('Unknown wiring direction');
 return model.wires.map(w=>direction==='P|E'?structuredClone(w):{...structuredClone(w),source:w.target,target:w.source,ports:[...w.ports].reverse(),edges:[...w.edges].reverse(),transports:w.transports.toReversed().map(t=>t.map(x=>x===0?0:-x)),periodShift:w.periodShift.map(x=>x===0?0:-x)});
}
export function groupSulfurPayloads(model,rows,direction='P|E'){
 require(rows.length===model.wires.length&&new Set(rows.map(r=>r.wire)).size===rows.length,'Every wire payload must be retained exactly once');
 const values=new Map(rows.map(r=>[r.wire,r])),fibers=new Map();
 for(const wire of presentSulfurWires(model,direction)){require(values.has(wire.id),'Missing wire payload');if(!fibers.has(wire.source))fibers.set(wire.source,{cell:wire.source,slots:[null,null,null,null]});fibers.get(wire.source).slots[wire.axis]=structuredClone(values.get(wire.id));}
 return [...fibers.values()].map(f=>({...f,slots:[f.slots.slice(0,2),f.slots.slice(2,4)]}));
}
export function restoreSulfurPayloads(fibers){return fibers.flatMap(f=>f.slots.flat()).map(r=>structuredClone(r)).sort((a,b)=>a.wire.localeCompare(b.wire));}
