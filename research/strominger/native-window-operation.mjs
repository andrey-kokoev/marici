// Restrict the globally presented Z^3 period cover; do not close the window.
import assert from 'node:assert/strict';
import {sulfurPeriodGenerators,groupSulfurPayloads} from '../realization-tower/sulfur-32-wiring.mjs';
import {periodCoordinates} from './sulfur-period-covers.mjs';
import {faceKey} from './native-axis-port-graph.mjs';
export const periodVector=a=>[0,1,2,3].map(i=>a.reduce((s,x,j)=>s+x*sulfurPeriodGenerators[j][i],0));
export function nativeWindowWires(base,sector,projection){
 const byPort=new Map(base.ports.map(p=>[p.id,p])),byCell=new Map(base.groups.map(g=>[g.id,g]));
 // All translates of each source wire are defined by these integer offsets.
 const templates=base.wires.map(w=>{
  const offsets=[[0,0,0]];for(const t of w.transports){const d=periodCoordinates(t);offsets.push(offsets.at(-1).map((x,i)=>x+d[i]));}
  return {wire:w,offsets};
 });
 const templateAt=new Map(templates.flatMap(t=>t.wire.ports.map((p,i)=>[p,{template:t,index:i}]))),wires=new Map();
 for(const p of projection.ports){
  const {template:t,index}=templateAt.get(p.basePort),start=p.periodCoordinates.map((x,i)=>x-t.offsets[index][i]);
  const id=JSON.stringify([t.wire.id,start]);if(wires.has(id))continue;
  const vertices=t.wire.ports.map((q,i)=>{
   const bp=byPort.get(q),g=byCell.get(bp.cell),sheet=start.map((x,j)=>x+t.offsets[i][j]),translation=periodVector(sheet);
   const nativeBase=g.representative.id.split(':')[1].split(',').map(Number),cell=g.role+':'+nativeBase.map((x,j)=>x-translation[j]).join(',');
   const vs=bp.vertices.map(v=>v.map((x,j)=>x-translation[j]));
   return {id:cell+'@'+faceKey(vs),cell,vertices:vs,basePort:q,integerSheet:sheet,role:bp.role,axis:bp.axis};
  });
  const edges=[];for(let i=0;i<vertices.length-1;i++){
   const a=vertices[i],b=vertices[i+1],kind=a.cell===b.cell?'axis-continuity':'shared-native-face';
   if(kind==='shared-native-face')assert.equal(faceKey(a.vertices),faceKey(b.vertices));
   else assert.equal(a.role,'neutron');
   edges.push({from:a.id,to:b.id,kind});
  }
  wires.set(id,{id,axis:t.wire.axis,source:vertices[0].cell,target:vertices.at(-1).cell,
   channel:vertices.find(p=>p.role==='neutron').cell,ports:vertices.map(p=>p.id),portWitnesses:vertices,
   edges,transports:edges.map(()=>[0,0,0,0]),periodShift:[0,0,0,0],baseWire:t.wire.id,integerSheet:start});
 }
 const inside=new Set(sector.cells.map(c=>c.id));
 return {schema:'native.window-operation.v1',wires:[...wires.values()],insideCells:[...inside],
  sourceCells:sector.cells.filter(c=>c.role==='proton').map(c=>c.id),targetCells:sector.cells.filter(c=>c.role==='electron').map(c=>c.id),
  sourceBoundaryWires:[...wires.values()].filter(w=>!inside.has(w.source)).map(w=>w.id),
  targetBoundaryWires:[...wires.values()].filter(w=>!inside.has(w.target)).map(w=>w.id)};
}
const sortedRows=rows=>[...rows].sort((a,b)=>a.wire.localeCompare(b.wire));
export function nativeWindowProfile(model,rows,direction){
 assert(['P|E','E|P'].includes(direction));assert.equal(rows.length,model.wires.length);
 const byWire=new Map(rows.map(r=>[r.wire,r]));assert.equal(byWire.size,model.wires.length);assert(model.wires.every(w=>byWire.has(w.id)));
 const inside=new Set(model.insideCells),endpoint=direction==='P|E'?'source':'target';
 const internal=model.wires.filter(w=>inside.has(w[endpoint])),external=model.wires.filter(w=>!inside.has(w[endpoint]));
 const cells=groupSulfurPayloads({wires:internal},internal.map(w=>byWire.get(w.id)),direction).sort((a,b)=>a.cell.localeCompare(b.cell));
 assert(cells.every(c=>c.slots.flat().length===4&&c.slots.flat().every(Boolean)));
 return {direction,cells,boundary:sortedRows(external.map(w=>structuredClone(byWire.get(w.id))))};
}
export function restoreNativeWindowProfile(model,profile){
 const rows=sortedRows([...profile.cells.flatMap(c=>c.slots.flat()),...profile.boundary]);
 const expected=nativeWindowProfile(model,rows,profile.direction);
 assert.deepEqual({...profile,cells:[...profile.cells].sort((a,b)=>a.cell.localeCompare(b.cell)),boundary:sortedRows(profile.boundary)},expected,'Profile lost labels, slots, or boundary contents');
 return rows;
}
// Canonical pullback-state subspace: contents agree on every integer translate
// of a base wire. This is an explicit restriction, not a law of all lifted states.
export function completePeriodicWindowProfile(model,cells,direction){
 assert(['P|E','E|P'].includes(direction));const endpoint=direction==='P|E'?'source':'target';
 const expected=new Set(direction==='P|E'?model.sourceCells:model.targetCells),seen=new Set(),contents=new Map(),byWire=new Map(model.wires.map(w=>[w.id,w]));
 for(const cell of cells){
  assert(expected.has(cell.cell)&&!seen.has(cell.cell));seen.add(cell.cell);
  assert.equal(cell.slots.length,2);assert(cell.slots.every(row=>row.length===2));
  for(const [axis,row] of cell.slots.flat().entries()){
   const w=byWire.get(row.wire);assert(w&&w.axis===axis&&w[endpoint]===cell.cell);
   const {wire,...content}=row;
   if(contents.has(w.baseWire))assert.deepEqual(content,contents.get(w.baseWire),'Nonperiodic contents on repeated base wire');
   else contents.set(w.baseWire,structuredClone(content));
  }
 }
 assert.equal(seen.size,expected.size);assert(model.wires.every(w=>contents.has(w.baseWire)),'Internal views do not determine all base wires');
 const complete=nativeWindowProfile(model,model.wires.map(w=>({wire:w.id,...structuredClone(contents.get(w.baseWire))})),direction);
 assert.deepEqual([...cells].sort((a,b)=>a.cell.localeCompare(b.cell)),complete.cells,'Periodic completion changed original view');
 return complete;
}
export function applyNativeWindowOperation(model,profile){
 const rows=restoreNativeWindowProfile(model,profile);
 return nativeWindowProfile(model,rows,profile.direction==='P|E'?'E|P':'P|E');
}
