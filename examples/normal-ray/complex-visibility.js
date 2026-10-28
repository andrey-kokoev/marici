import {separateBeltGeometry} from './belt-geometry-layout.js';
import {expandBeltWiring} from './belt-wiring-layout.js';
import {beltLayerCount} from '../../research/realization-tower/belt-layer-model.mjs';
import {esd7NodePlanes,esd7PlaneOf} from './esd7-node-planes.js';
const pointKey=p=>p.map(x=>x.toFixed(7)).join(',');
const center=b=>b.vertices[0].map((_,i)=>b.vertices.reduce((s,p)=>s+p[i]/b.vertices.length,0));
// Mutually exclusive belt presentation; construction records remain untouched.
export function filterBeltView(proc,mode='wiring',options={}){
 if(!proc.centralBeltAudit)return proc;
 const removed=new Set(proc.parentCutAudit?.removedCellIds??[]),removedVisible=[...(proc.retainedBodies??[]),...(proc.emptyBodies??[])].filter(b=>removed.has(b.id));
 const geometry=mode==='geometry';let result=geometry?{...proc,attachmentBodies:[],terminalBundles:[],beltGraphLinks:[]}:{...proc};
 if(proc.parentCutAudit){result.parentCutAudit={...proc.parentCutAudit,visibleCutCount:removedVisible.length};result.preCutRetainedCount=proc.retainedBodies?.length??0;for(const field of ['retainedBodies','emptyBodies','presentationWireframes','conflictBodies','contextBodies'])if(result[field])result[field]=result[field].filter(b=>!removed.has(b.id));if(result.presentationLabels)result.presentationLabels=result.presentationLabels.filter(p=>!removed.has(p.cell));result.interfaceGuides=[];if(result.complexVisibilityAudit)result.complexVisibilityAudit={...result.complexVisibilityAudit,visibleParentCells:(result.retainedBodies?.length??0)+(result.emptyBodies?.length??0)};}
 if(proc.parentTipReplacementAudit){
  const ids=new Set(proc.parentTipReplacementAudit.cellIds),replacements=removedVisible.filter(b=>ids.has(b.id)).map(b=>({...b,role:'electron',seedLabel:'E',color:0xa82664,tipReplacement:{from:'neutron',to:'electron'}}));
  result.retainedBodies=[...result.retainedBodies,...replacements];result.presentationLabels=[...(result.presentationLabels??[]),...replacements.map(b=>({cell:b.id,role:'electron',text:'E',point:center(b)}))];
  result.parentCutAudit={...result.parentCutAudit,visibleReplacementCount:replacements.length};
  if(result.complexVisibilityAudit)result.complexVisibilityAudit={...result.complexVisibilityAudit,visibleParentCells:result.retainedBodies.length+(result.emptyBodies?.length??0)};
 }
 result=geometry?separateBeltGeometry(result):expandBeltWiring(result,options);
 result.beltViewAudit={mode:geometry?'geometry':'wiring',surfaceVisible:Boolean(result.beltSurface),arrowCount:(result.attachmentBodies??[]).filter(b=>b.beltPort).length,terminalCount:result.terminalBundles?.length??0,linkCount:result.nativeWiringGraph?.links.length??result.beltGraphLinks?.length??0};return result;
}
// Render-only filtering: no mutation of construction state or particle accounting.
export function filterComplexVisibility(proc,visibility={},beltLayers=[],esd7Planes={}){
 const visible={original:true,clone:true,belt:true,...visibility},layerCount=proc.centralBeltAudit?.layers.length??beltLayerCount;
 const parents=[...(proc.retainedBodies??[]),...(proc.emptyBodies??[])],beltIds=new Set((proc.attachmentBodies??[]).map(b=>b.id));
 const terminals=new Map((proc.terminalBundles??[]).map(b=>[b.id,b.beltTerminal]));
 const layerOf=new Map((proc.attachmentBodies??[]).map(b=>[b.id,b.beltPort?.layer]));
 const showId=id=>{if(terminals.has(id)){const t=terminals.get(id);return visible.belt&&visible[t.copy]&&beltLayers[t.layer-1]!==false;}if(beltIds.has(id))return visible.belt&&beltLayers[layerOf.get(id)-1]!==false;const plane=esd7PlaneOf.get(id);if(plane)return visible[plane.copy]&&esd7Planes[plane.copy]?.[plane.index]!==false;return true;};
 const atPoint=new Map(parents.map(b=>[pointKey(center(b)),b.id]));
 for(const b of proc.attachmentBodies??[])atPoint.set(pointKey(center(b)),b.id);
 const result={...proc};if(!visible.belt&&proc.beltSurface)result.beltSurface=null;
 for(const field of ['retainedBodies','emptyBodies','presentationWireframes','conflictBodies','contextBodies','attachmentBodies','terminalBundles'])if(proc[field])result[field]=proc[field].filter(b=>showId(b.id));
 if(proc.beltGraphLinks)result.beltGraphLinks=proc.beltGraphLinks.filter(e=>showId(e.from)&&showId(e.to));
 if(proc.presentationLabels)result.presentationLabels=proc.presentationLabels.filter(p=>showId(p.cell));
 if(proc.interfaceGuides)result.interfaceGuides=proc.interfaceGuides.filter(g=>{
  const ids=g.points.map(p=>atPoint.get(pointKey(p)));
  return ids.every(id=>id?showId(id):visible.original&&visible.clone&&visible.belt);
 });
 result.complexVisibilityAudit={...visible,esd7Planes:Object.fromEntries(['original','clone'].map(copy=>[copy,esd7NodePlanes.map(p=>esd7Planes[copy]?.[p.index]!==false)])),beltLayers:Array.from({length:layerCount},(_,i)=>beltLayers[i]!==false),visibleBeltLayerCounts:Array.from({length:layerCount},(_,i)=>(result.attachmentBodies??[]).filter(b=>b.beltPort?.layer===i+1).length),visibleParentCells:(result.retainedBodies?.length??0)+(result.emptyBodies?.length??0),visibleBeltCells:result.attachmentBodies?.length??0,visibleTerminalBundles:result.terminalBundles?.length??0};
 return result;
}
