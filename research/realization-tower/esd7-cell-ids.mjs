import {buildFoldedFibration} from './fibration-folded-process.mjs';
import {geometricCellLayer} from './cell-fibration-cut.mjs';
const center=g=>g.vertices[0].map((_,i)=>g.vertices.reduce((s,v)=>s+v[i],0)/g.vertices.length);
// Full-carrier numbering from the proton vertex V2. Finish each geometric
// layer before the next; within a layer, traverse lattice coordinates V1,V3,V4.
export function makeEsd7CellIds(geometry){
 if(geometry.length!==175)throw Error('Number the complete 175-cell ESD7 carrier');
 const ordered=geometry.map(g=>({g,layer:geometricCellLayer(g,2),center:center(g)}));
 ordered.sort((a,b)=>{
  if(a.layer!==b.layer)return a.layer-b.layer;
  for(const axis of [0,2,3])if(a.center[axis]!==b.center[axis])return a.center[axis]-b.center[axis];
  return 0;
 });
 const ids=new Map(ordered.map(({g},i)=>[g.id,i+1]));
 if(ids.size!==geometry.length)throw Error('Unique ESD7 geometry required');
 return ids;
}
const ids=makeEsd7CellIds(buildFoldedFibration().geometry);
const geometryIds=new Map([...ids].map(([geometryId,id])=>[id,geometryId]));
export const esd7CellId=geometryId=>ids.get(geometryId)??geometryId;
export const esd7GeometryId=id=>geometryIds.get(id);
