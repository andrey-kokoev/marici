// Full native bulk graph, before any periodic quotient or boundary sewing.
// Uses the same four coordinate-normal axes as sulfur-32-wiring.mjs.
import assert from 'node:assert/strict';
export const faceKey=vs=>vs.map(v=>v.join(',')).sort().join('|');
export function buildNativeAxisPortGraph(sector){
 const ports=[],facePorts=new Map(),byCell=new Map(),edges=[];
 for(const cell of sector.cells){
  const local=cell.faces.map(vertices=>{
   const axes=[0,1,2,3].filter(i=>vertices.every(v=>v[i]===vertices[0][i]));assert.equal(axes.length,1);
   const face=faceKey(vertices),p={id:cell.id+'@'+face,cell:cell.id,role:cell.role,axis:axes[0],face,vertices};
   ports.push(p);if(!facePorts.has(face))facePorts.set(face,[]);facePorts.get(face).push(p);return p;
  });byCell.set(cell.id,local);
 }
 assert.equal(facePorts.size,sector.faces.length,'Native face inventory changed');
 for(const f of sector.faces){
  const ps=facePorts.get(f.id);assert(ps,'Missing native face');
  assert.deepEqual(ps.map(p=>p.cell).sort(),[...f.owners].sort(),'Native face incidence was dropped or changed');
 }
 const connect=(a,b,kind)=>{assert.equal(a.axis,b.axis);edges.push({id:kind+':'+[a.id,b.id].sort().join('~'),from:a.id,to:b.id,axis:a.axis,kind});};
 for(const ps of facePorts.values()){
  assert(ps.length===1||ps.length===2);
  if(ps.length===2){assert(ps.some(p=>p.role==='neutron'));assert(ps.some(p=>p.role!=='neutron'));connect(ps[0],ps[1],'shared-native-face');}
 }
 for(const cell of sector.cells)for(let axis=0;axis<4;axis++){
  const ps=byCell.get(cell.id).filter(p=>p.axis===axis);assert.equal(ps.length,cell.role==='neutron'?2:1);
  if(cell.role==='neutron'){
   assert.deepEqual([...ps.flatMap(p=>p.vertices.map(v=>v.join(',')))].sort(),cell.vertices.map(v=>v.join(',')).sort(),'Opposite faces must partition the octahedron vertices');
   connect(ps[0],ps[1],'axis-continuity');
  }
 }
 const byPort=new Map(ports.map(p=>[p.id,p])),adj=new Map(ports.map(p=>[p.id,[]]));
 for(const e of edges){adj.get(e.from).push(e);adj.get(e.to).push(e);}
 assert([...adj.values()].every(es=>es.length<=2));
 const boundary=ports.filter(p=>facePorts.get(p.face).length===1),boundaryIds=new Set(boundary.map(p=>p.id));
 const unseen=new Set(ports.map(p=>p.id)),components=[];
 while(unseen.size){
  const todo=[unseen.values().next().value];unseen.delete(todo[0]);
  for(let i=0;i<todo.length;i++)for(const e of adj.get(todo[i])){const n=e.from===todo[i]?e.to:e.from;if(unseen.delete(n))todo.push(n);}
  const ps=todo.map(p=>byPort.get(p)),charged=ps.filter(p=>p.role!=='neutron'),open=ps.filter(p=>boundaryIds.has(p.id));
  assert.equal(new Set(ps.map(p=>p.axis)).size,1);
  const edgeIds=[...new Set(todo.flatMap(p=>adj.get(p).map(e=>e.id)))];assert.equal(edgeIds.length,todo.length-1,'No closed or branching component');
  const nCells=[...new Set(ps.filter(p=>p.role==='neutron').map(p=>p.cell))];assert(nCells.length<=1);
  let kind;
  if(open.length===0){assert.equal(charged.length,2);assert.deepEqual(charged.map(p=>p.role).sort(),['electron','proton']);kind='complete-PNE';}
  else if(charged.length===1)kind=nCells.length?'open-N-half':'open-charged-port';
  else{assert.equal(charged.length,0);kind='open-N-only';}
  components.push({id:'component:'+components.length,axis:ps[0].axis,kind,ports:todo,edges:edgeIds,
   chargedPorts:charged.map(p=>p.id),boundaryPorts:open.map(p=>p.id),neutronCells:nCells});
 }
 const counts={cells:sector.cells.length,ports:ports.length,sharedFaces:edges.filter(e=>e.kind==='shared-native-face').length,
  axisContinuities:edges.filter(e=>e.kind==='axis-continuity').length,physicalBoundaryPorts:boundary.length,components:components.length,
  kinds:Object.fromEntries([...new Set(components.map(c=>c.kind))].map(k=>[k,components.filter(c=>c.kind===k).length]))};
 return {schema:'native.axis-port-bulk.v1',ports,edges,boundaryPorts:boundary.map(p=>p.id),components,counts};
}
