// Period covers of the existing candidate, not an edge-five seam prescription.
import assert from 'node:assert/strict';
import {isSulfurPeriod,sulfurPeriodGenerators} from '../realization-tower/sulfur-32-wiring.mjs';
import {faceKey} from './native-axis-port-graph.mjs';
const anchor=vs=>[0,1,2,3].map(i=>Math.min(...vs.map(v=>v[i])));
export const mod5=n=>((n%5)+5)%5;
export function periodCoordinates(t){
 assert(isSulfurPeriod(t));const a=t.slice(0,3).map(x=>(t[3]-x)/4);
 assert(a.every(Number.isInteger));assert.deepEqual(t.map(x=>x||0),[0,1,2,3].map(i=>a.reduce((s,x,j)=>s+x*sulfurPeriodGenerators[j][i],0)));
 return a;
}
export function fiveCoverCharacters(){
 const out=[];for(let a=0;a<5;a++)for(let b=0;b<5;b++)for(let c=0;c<5;c++){
  const v=[a,b,c];if(v.find(x=>x!==0)===1)out.push(v);
 }return out;
}
export const characterValue=(v,a)=>mod5(v.reduce((s,x,i)=>s+x*a[i],0));
export function projectNativeWindow(sector,bulk,base){
 const cells=sector.cells.map(c=>{
  const a=anchor(c.vertices),matches=base.groups.flatMap(g=>{
   if(g.role!==c.role)return [];
   const t=anchor(g.representative.vertices).map((x,i)=>x-a[i]);
   return isSulfurPeriod(t)&&faceKey(c.vertices.map(v=>v.map((x,i)=>x+t[i])))===faceKey(g.representative.vertices)
    ?[{physicalCell:c.id,role:c.role,baseCell:g.id,translation:t,periodCoordinates:periodCoordinates(t)}]:[];
  });assert.equal(matches.length,1);return matches[0];
 });
 const byCell=new Map(cells.map(c=>[c.physicalCell,c])),basePorts=new Map(base.ports.map(p=>[p.id,p]));
 const ports=bulk.ports.map(p=>{
  const c=byCell.get(p.cell),q=c.baseCell+'/port/'+faceKey(p.vertices.map(v=>v.map((x,i)=>x+c.translation[i])));
  assert(basePorts.has(q));assert.equal(basePorts.get(q).axis,p.axis);
  return {physicalPort:p.id,physicalCell:p.cell,basePort:q,periodCoordinates:c.periodCoordinates};
 });return {cells,ports};
}
export function buildFivePeriodCover(base,character){
 assert(fiveCoverCharacters().some(v=>JSON.stringify(v)===JSON.stringify(character)),'Character must be a normalized nonzero F5 covector');
 const prefix='c5:'+character.join(',')+':',lift=(id,s)=>prefix+id+'@'+mod5(s),chi=t=>characterValue(character,periodCoordinates(t));
 const groups=base.groups.flatMap(g=>Array.from({length:5},(_,sheet)=>({id:lift(g.id,sheet),baseCell:g.id,role:g.role,sheet})));
 const ports=base.ports.flatMap(p=>Array.from({length:5},(_,sheet)=>({id:lift(p.id,sheet),basePort:p.id,cell:lift(p.cell,sheet),role:p.role,axis:p.axis,sheet})));
 const edges=base.edges.flatMap(e=>Array.from({length:5},(_,sheet)=>({id:lift(e.id,sheet),baseEdge:e.id,kind:e.kind,
  from:lift(e.from,sheet),to:lift(e.to,sheet+chi(e.transport)),transport:e.transport,sheetShift:chi(e.transport)})));
 const byPort=new Map(ports.map(p=>[p.id,p])),adj=new Map(ports.map(p=>[p.id,[]]));
 for(const e of edges){adj.get(e.from).push(e);adj.get(e.to).push(e);}
 for(const p of ports)assert.equal(adj.get(p.id).length,p.role==='neutron'?2:1);
 const unseen=new Set(adj.keys()),wires=[];
 while(unseen.size){
  const component=[unseen.values().next().value];unseen.delete(component[0]);
  for(let i=0;i<component.length;i++)for(const e of adj.get(component[i])){const q=e.from===component[i]?e.to:e.from;if(unseen.delete(q))component.push(q);}
  const endpoints=component.filter(p=>byPort.get(p).role!=='neutron');assert.equal(endpoints.length,2);
  const start=endpoints.find(p=>byPort.get(p).role==='proton'),end=endpoints.find(p=>byPort.get(p).role==='electron');assert(start&&end);
  const path=[start],edgePath=[],transports=[];let previous=null;
  while(path.at(-1)!==end){
   const here=path.at(-1),es=adj.get(here).filter(e=>e.id!==previous);assert.equal(es.length,1);const e=es[0];
   previous=e.id;edgePath.push(e.id);transports.push(e.transport.map(x=>(e.from===here?x:-x)||0));path.push(e.from===here?e.to:e.from);assert(path.length<=component.length);
  }
  assert.equal(path.length,component.length);const axis=byPort.get(start).axis;assert(path.every(p=>byPort.get(p).axis===axis));
  const ns=[...new Set(path.map(p=>byPort.get(p)).filter(p=>p.role==='neutron').map(p=>p.cell))];assert.equal(ns.length,1);
  const source=byPort.get(start).cell,target=byPort.get(end).cell;
  wires.push({id:source+'/wire:'+axis,axis,source,target,channel:ns[0],ports:path,edges:edgePath,transports,
   periodShift:[0,1,2,3].map(i=>transports.reduce((s,t)=>s+t[i],0))});
 }
 for(const g of groups)for(let axis=0;axis<4;axis++)assert.equal(wires.filter(w=>w.axis===axis&&({proton:w.source,electron:w.target,neutron:w.channel})[g.role]===g.id).length,1);
 // Connectedness refers to the whole-cell adjacency complex, not to the disjoint wires.
 const cellAdj=new Map(groups.map(g=>[g.id,[]]));for(const e of edges.filter(e=>e.kind==='shared-quotient-face')){
  const a=byPort.get(e.from).cell,b=byPort.get(e.to).cell;cellAdj.get(a).push(b);cellAdj.get(b).push(a);
 }
 const todo=[groups[0].id],seen=new Set(todo);for(let i=0;i<todo.length;i++)for(const n of cellAdj.get(todo[i]))if(!seen.has(n)){seen.add(n);todo.push(n);}
 assert.equal(seen.size,groups.length);
 return {schema:'sulfur.five-period-cover.v1',character,groups,ports,edges,wires,
  counts:{cellFibres:groups.length,ports:ports.length,edges:edges.length,wires:wires.length,connectedCellComplex:true},
  scope:'Abstract five-sheeted period cover of the existing candidate. Base-frame transports retained; no edge-five fundamental domain or physical identification asserted.'};
}
