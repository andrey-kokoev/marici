import {cells} from './normal-ray-model.mjs';
const same=(a,b)=>a.every((x,i)=>x===b[i]);

// These are the explicitly identified k=7 patches, not a general surface
// closure rule. Locate them by face/layer and retain their support witnesses.
export function identifiedSurfaceNeutrons(k,assignments){
 if(k!==7)return [];
 const roles=new Map(assignments.map(a=>[a.cell,a.role])),pending=new Map();
 for(const [coordinate,layerCoordinate,minimum] of [[1,2,-3],[1,0,-3],[1,3,-2],[3,1,-2],[3,0,-3],[3,2,-3]]){
  const faces=cells.map(c=>({cell:c.id,face:c.vertices.filter(p=>p[coordinate]===2)})).filter(c=>c.face.length===3);
  for(const c of faces){
   if(roles.has(c.cell)||Math.min(...c.face.map(p=>p[layerCoordinate]))!==minimum)continue;
   const supports=faces.filter(d=>d.cell!==c.cell&&roles.has(d.cell)&&c.face.filter(p=>d.face.some(q=>same(p,q))).length===2).map(d=>({cell:d.cell,role:roles.get(d.cell)}));
   if(!supports.some(s=>s.role==='neutron')||!supports.some(s=>s.role==='electron'||s.role==='proton'))continue;
   pending.set(c.cell,{cell:c.cell,coordinate,layerCoordinate,minimum,supports});
  }
 }
 return [...pending.values()].sort((a,b)=>a.cell-b.cell);
}
