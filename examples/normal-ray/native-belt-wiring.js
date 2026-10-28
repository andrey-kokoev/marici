import {worldPoint} from '../../research/realization-tower/normal-ray-model.mjs';
import {beltViewerPoint} from '../../research/realization-tower/neutron-belt-process.mjs';
import {geometryBeltSurface,separateBeltGeometry,geometryParentShift} from './belt-geometry-layout.js';
const mean=ps=>ps[0].map((_,i)=>ps.reduce((s,p)=>s+p[i]/ps.length,0)),key=p=>p.map(v=>Number(v.toFixed(8))).join(','),roles=['proton','neutron','electron'];
export const nativeWiringScale=Object.freeze({axial:2.5,transverse:1.8,gap:.8});
export function wiringParentPoint(p,copy,layout){
 const shift=geometryParentShift*nativeWiringScale.axial+nativeWiringScale.gap;
 return beltViewerPoint(worldPoint(p).map((v,i)=>v+(copy==='original'?1:-1)*shift*layout.normal[i]));
}
function planesOf(surface,layout){
 if(!surface)return [];
 const origin=worldPoint(layout.origin),projection=p=>p.reduce((s,v,i)=>s+(v-origin[i])*layout.normal[i],0),levels=new Map();
 for(const cell of surface.cellulation.cells){const level=Number(projection(mean(cell.indices.map(i=>surface.cellulation.vertices[i]))).toFixed(8));if(!levels.has(level))levels.set(level,[]);levels.get(level).push(cell.id);}
 return [...levels].sort((a,b)=>b[0]-a[0]).map(([position,cellIds],index)=>({index,position,cellIds,count:cellIds.length,label:`${index+1} (${cellIds.length})`}));
}
export function nativeBeltPlanes(proc){return proc.beltSurface?planesOf(geometryBeltSurface(proc.beltSurface,proc.centralBeltAudit),proc.centralBeltAudit):[];}
export function expandBeltWiring(proc,{nativeBeltLayers=[]}={}){
 const geometry=separateBeltGeometry(proc),layout=proc.centralBeltAudit,origin=worldPoint(layout.origin),normal=layout.normal,scale=nativeWiringScale,planes=planesOf(geometry.beltSurface,layout),layerOf=new Map(planes.flatMap(p=>p.cellIds.map(id=>[id,p.index])));
 const pose=(p,shape)=>{
  if(shape!=='belt')return p.map((v,i)=>v+(shape==='original'?1:-1)*(geometryParentShift*(scale.axial-1)+scale.gap)*normal[i]);
  const d=p.map((v,i)=>v-origin[i]),z=d.reduce((s,v,i)=>s+v*normal[i],0);return origin.map((v,i)=>v+scale.transverse*d[i]+(scale.axial-scale.transverse)*z*normal[i]);
 };
 const sources=[...geometry.parentCellulations.map(p=>({...p,shape:p.copy})),...(geometry.beltSurface?[{...geometry.beltSurface.cellulation,shape:'belt'}]:[])],nodes=[],links=[],raw=new Map();
 for(const source of sources){
  for(const cell of source.cells){
   if(source.shape==='belt'&&nativeBeltLayers[layerOf.get(cell.id)]===false)continue;
   const fs=source.faces.filter(f=>f.owners.includes(cell.id)),role=cell.role??(cell.kind==='octahedron'?'neutron':fs[0].colorRole),points=cell.indices.map(i=>source.vertices[i]),vertices=points.map(p=>beltViewerPoint(pose(p,source.shape))),point=mean(vertices);
   const body={id:cell.id,kind:cell.kind,role,point,vertices,faces:fs.map(f=>f.indices.map(i=>beltViewerPoint(pose(source.vertices[i],source.shape)))),components:[],nativeWiring:{shape:source.shape,layerIndex:layerOf.get(cell.id)??null,sourceGeometry:cell.sourceGeometry??null,sourceWitnesses:cell.witnesses??null,scope:'One whole native cell; node role from tetrahedral orientation or octahedral filler, with E-tip overrides.'}};
   nodes.push({id:cell.id,body,position:point});raw.set(cell.id,{points,shape:source.shape});
  }
  for(const face of source.faces)if(face.owners.length===2)links.push({id:`native-face:${source.shape}:${face.id}`,from:face.owners[0],to:face.owners[1],kind:'native-face',directed:false,sharedFace:face.id,shape:source.shape});
 }
 // Only the two actual E-tip/belt-pole vertex contacts are added. They are
 // explicitly not shared-facet links, directed transport or terminal bundles.
 for(const id of proc.parentTipReplacementAudit?.cellIds??[]){const parent=raw.get(id);if(!parent)continue;const vertices=new Set(parent.points.map(key));for(const [beltId,cell]of raw)if(cell.shape==='belt'){const shared=cell.points.filter(p=>vertices.has(key(p)));if(shared.length)links.push({id:`native-tip:${id}:${beltId}`,from:id,to:beltId,kind:'native-tip-contact',directed:false,sharedVertices:shared,shape:'contact'});}}
 const visibleLinks=links.filter(e=>raw.has(e.from)&&raw.has(e.to)),parents=nodes.filter(n=>n.body.nativeWiring.shape!=='belt').map(n=>n.body),belt=nodes.filter(n=>n.body.nativeWiring.shape==='belt').map(n=>n.body),counts=bs=>Object.fromEntries(roles.map(role=>[role,bs.filter(b=>b.role===role).length]));
 const audit={kind:'native-cell-dual',nodeCount:nodes.length,parentNodes:parents.length,beltNodes:belt.length,terminalBundleNodes:0,nodeRoles:counts([...parents,...belt]),parentRoles:counts(parents),beltRoles:counts(belt),sharedFaceLinks:visibleLinks.filter(e=>e.kind==='native-face').length,tipContactLinks:visibleLinks.filter(e=>e.kind==='native-tip-contact').length,directedLinks:0,planes:planes.map(p=>({...p,visible:nativeBeltLayers[p.index]!==false})),scope:'Actual current cellulation. Shared-face adjacency plus explicitly marked vertex contacts; no directed transport law inferred.'};
 return {...proc,complexVisibilityAudit:{...proc.complexVisibilityAudit,visibleParentCells:parents.length,visibleBeltCells:belt.length,visibleTerminalBundles:0,visibleBeltLayerCounts:planes.map(p=>nativeBeltLayers[p.index]===false?0:p.count),nativeBeltPlanes:planes.map(p=>nativeBeltLayers[p.index]!==false)},retainedBodies:parents,emptyBodies:[],presentationWireframes:[],conflictBodies:[],contextBodies:[],attachmentBodies:belt,terminalBundles:[],beltSurface:null,beltGraphLinks:[],interfaceGuides:[],presentationLabels:[],parentCellulations:undefined,nativeWiringGraph:{nodes,links:visibleLinks},nativeWiringAudit:audit,wiringLayoutAudit:{kind:'exploded-native-cell-dual',axialScale:scale.axial,transverseScale:scale.transverse,terminalGap:scale.gap,parentShift:geometryParentShift*scale.axial+scale.gap,scope:'Display expansion only; connectivity is built in the actual Geometry-view pose before expansion.'}};
}
export function nativeWiringInventory(proc){
 const a=expandBeltWiring(proc).nativeWiringAudit,row=(id,label,counts)=>({id,label,...counts,total:roles.reduce((s,r)=>s+counts[r],0)}),rows=[row('parents-exposed','Parents',a.parentRoles),row('belt-faces','Belt',a.beltRoles),row('combined','Combined total',a.nodeRoles)];
 return {rows,displayRows:rows,unit:'nodes',unassigned:0,scope:'One node per whole native cell. This is not the exposed-face count shown in Geometry view.'};
}
