import {geometricCellLayer} from './cell-fibration-cut.mjs';
const key=ps=>ps.map(p=>p.map(x=>Number(x.toFixed(8))).join(',')).sort().join('|');
export function innerLayerHexReflection(geometry,assigned,corners){
 const occupied=new Map(assigned.map(g=>[g.id,g])),agreed=[];
 for(const source of corners){
  const others=corners.filter(c=>c!==source);
  const axis=source.point.findIndex((x,i)=>others.every(c=>c.point[i]===others[0].point[i]&&c.point[i]!==x));
  const unit=(others[0].point[axis]-source.point[axis])/7;
  // Layer 2's inward boundary, not any exterior carrier face.
  const plane=source.point[axis]+3*unit;
  const triangles=geometry.filter(g=>geometricCellLayer(g,source.vertex)===2).flatMap(cell=>cell.faces.filter(f=>f.every(p=>Math.abs(p[axis]-plane)<1e-8)).map(triangle=>({cell,triangle})));
  const points=new Map(triangles.flatMap(t=>t.triangle.map(p=>[key([p]),p])));
  const hexagons=[...points].map(([pointKey,hexCenter])=>({hexCenter,six:triangles.filter(t=>t.triangle.some(p=>key([p])===pointKey))})).filter(h=>h.six.length===6);
  if(hexagons.length!==1)throw Error('Unique inward layer-2 hexagon required');
  const {hexCenter,six}=hexagons[0],empty=six.filter(t=>!occupied.has(t.cell.id));
  if(empty.length!==3||six.filter(t=>occupied.has(t.cell.id)).length!==3)throw Error('Inner hexagon requires three filled and three empty cells');
  for(const gap of empty){
   const reflected=key(gap.triangle.map(p=>p.map((x,i)=>2*hexCenter[i]-x)));
   const opposite=six.find(t=>key(t.triangle)===reflected),other=occupied.get(opposite?.cell.id);
   if(!other||gap.cell.kind!=='octahedron')throw Error('Opposite filled triangle and native octahedral gap required');
   const witness={view:'inside-layer-2',source:source.vertex,face:others.map(c=>c.vertex),axis,plane,hexCenter,triangle:gap.triangle,oppositeTriangle:opposite.triangle,oppositeCell:other.id,role:other.role,assignedRole:['electron','proton'].includes(other.role)?'neutron':other.role};
   agreed.push({cell:gap.cell,source:source.vertex,hexWitnesses:[witness],role:witness.assignedRole,reason:['electron','proton'].includes(other.role)?'inner-opposite-EP-to-N':'inner-opposite'});
  }
 }
 if(new Set(agreed.map(g=>g.cell.id)).size!==agreed.length)throw Error('Inner hexagons must fill distinct whole cells');
 return {agreed,unresolved:[]};
}
