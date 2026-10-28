import {cells} from './normal-ray-model.mjs';
const key=p=>p.join(',');
const shared=(a,b)=>a.filter(p=>b.some(q=>key(p)===key(q)));
const charged=role=>role==='electron'||role==='proton';

// Complete the short surface arcs where an incoming charged diamond meets
// an existing N-cell boundary. Never move/relabel the boundary or its diamond.
export function surfaceNeutronBoundaryGaps(k,assignments,rays){
 const roles=new Map(assignments.map(a=>[a.cell,a.role])),pending=new Map(),witnesses=[],seen=new Set();
 for(const ray of rays){
  const lastCharged=ray.surfaceCells.findLastIndex(c=>charged(roles.get(c.cell)));
  if(lastCharged<0||lastCharged+1>=ray.surfaceCells.length)continue;
  const start=ray.surfaceCells[lastCharged],boundary=ray.surfaceCells[lastCharged+1];
  if(roles.get(boundary.cell)!=='neutron')continue;
  const meeting=shared(start.face,boundary.face);if(meeting.length!==1)continue;
  const vertex=meeting[0],{coordinate,value}=ray;
  const faces=cells.filter(c=>c.vertices.every(p=>p[0]<=-5+k)).map(c=>({cell:c.id,face:c.vertices.filter(p=>p[coordinate]===value)})).filter(c=>c.face.length===3&&c.face.some(p=>key(p)===key(vertex)));
  function walk(path){
   const last=path.at(-1);
   if(last.cell===boundary.cell){
    if(path.length<3||path.length>4)return;
    const ids=path.map(c=>c.cell),gap=ids.slice(1,-1),fillCells=gap.filter(id=>!roles.has(id));
    const signature=`${coordinate}:${value}:`+ids.join(',');
    if(!fillCells.length||seen.has(signature))return;seen.add(signature);
    const witnessIndex=witnesses.length;
    witnesses.push({ray:ray.id,coordinate,value,vertex,source:start.cell,boundary:boundary.cell,path:ids,gap,fillCells});
    for(const cell of fillCells){if(!pending.has(cell))pending.set(cell,{cell,witnesses:[]});pending.get(cell).witnesses.push(witnessIndex);}
    return;
   }
   if(path.length>=4)return;
   for(const next of faces){
    if(path.some(c=>c.cell===next.cell)||shared(last.face,next.face).length!==2)continue;
    if(charged(roles.get(next.cell)))continue;
    walk([...path,next]);
   }
  }
  walk([start]);
 }
 return {cells:[...pending.values()].sort((a,b)=>a.cell-b.cell),witnesses};
}
