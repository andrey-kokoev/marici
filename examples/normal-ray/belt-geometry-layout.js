import {buildParentCellulations} from './parent-cellulation.js';
import {extendBeltMiddle} from '../../research/realization-tower/belt-middle-extension.mjs';
import {alignBeltInnerAxis} from './belt-axis-alignment.js';
import {worldPoint} from '../../research/realization-tower/normal-ray-model.mjs';
import {beltViewerPoint} from '../../research/realization-tower/neutron-belt-process.mjs';
import {nativeOctahedralBeltMetrics} from '../../research/realization-tower/belt-octahedral-surface.mjs';
export const geometryParentShift=1.5*Math.SQRT2*nativeOctahedralBeltMetrics.unitEdge;
export const geometryBeltSurface=(surface,layout)=>extendBeltMiddle(alignBeltInnerAxis(surface,layout));
export function geometryParentPoint(p,copy,layout){
 const shift=geometryParentShift*(copy==='original'?1:-1);
 return beltViewerPoint(worldPoint(p).map((v,i)=>v+shift*layout.normal[i]));
}
export function separateBeltGeometry(proc){
 const result={...proc},move=(p,copy)=>geometryParentPoint(p,copy,proc.centralBeltAudit);
 for(const field of ['retainedBodies','emptyBodies','presentationWireframes','conflictBodies','contextBodies'])if(proc[field])result[field]=proc[field].map(b=>{
  const point=p=>move(p,b.id.split(':')[0]);return {...b,insideNSector:true,neutralWire:b.role==='neutron',...(b.point?{point:point(b.point)}:{}),vertices:b.vertices?.map(point),faces:b.faces?.map(f=>f.map(point)),components:b.components?.map(f=>f.map(point))};
 });
 result.presentationLabels=proc.presentationLabels?.filter(l=>l.role!=='neutron').map(l=>({...l,point:l.cell.startsWith('belt:')?l.point:move(l.point,l.cell.split(':')[0])}));
 result.parentCellulations=buildParentCellulations(result);
 result.presentationLabels=result.presentationLabels?.filter(l=>proc.parentTipReplacementAudit?.cellIds.includes(l.cell)||l.cell.startsWith('belt:'));
 result.parentEdgeRays=[];
 if(proc.beltSurface)result.beltSurface=geometryBeltSurface(proc.beltSurface,proc.centralBeltAudit);
 result.geometryLayoutAudit={kind:'tip-contact',cellUnitsPerParent:1.5*Math.SQRT2,unitEdge:nativeOctahedralBeltMetrics.unitEdge,parentShift:geometryParentShift,beltAxisAlignment:result.beltSurface?.axisAlignment??null,beltExtension:result.beltSurface?.extension??null,scope:'E replacement tips touch the opposite belt vertices after rigid axis alignment. Vertex contact, not shared-face gluing; native records unchanged.'};
 return result;
}
