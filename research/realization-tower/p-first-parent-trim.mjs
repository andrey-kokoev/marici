import {buildFoldedFibration} from './fibration-folded-process.mjs';
import {nativeFaceRole} from './native-face-role.mjs';
const model=buildFoldedFibration(),sources=new Map(model.geometry.map(c=>[c.id,c])),native=new Map(model.occurrences.map(o=>[o.id,sources.get(o.sourceGeometry)]));
// Whole-cell approximation to moving each q_i <= 2 boundary to q_i <= 1.5.
// Use original local coordinates on BOTH copies, not their displayed poses.
// Boundary ties: remove P; retain N/E. Explicit E contact tips are exceptions.
export function trimParentHalfStep(proc){
 if(!proc.centralBeltAudit)throw Error('Parent trim requires the separated belt assembly');
 const protectedIds=new Set(proc.parentTipReplacementAudit?.cellIds??[]),all=[...new Map([...(proc.emptyBodies??[]),...(proc.retainedBodies??[])].map(b=>[b.id,b])).values()],removed=new Set(),decisions=[];
 for(const body of all){const source=native.get(body.id);if(!source)continue;
  const centre=source.vertices[0].map((_,i)=>source.vertices.reduce((s,p)=>s+p[i]/source.vertices.length,0)),depth=2-Math.max(...centre),role=protectedIds.has(body.id)?'electron':source.kind==='octahedron'?'neutron':nativeFaceRole(source.faces[0]),protect=protectedIds.has(body.id),remove=!protect&&(depth<.5||(depth===.5&&role==='proton'));
  if(remove)removed.add(body.id);decisions.push({id:body.id,copy:body.id.split(':')[0],role,depth,protectedTip:protect,remove});
 }
 const result={...proc};for(const field of ['retainedBodies','emptyBodies','presentationWireframes','conflictBodies','contextBodies'])if(proc[field])result[field]=proc[field].filter(b=>!removed.has(b.id));
 result.presentationLabels=proc.presentationLabels?.filter(l=>!removed.has(l.cell));
 const counts=xs=>Object.fromEntries(['proton','neutron','electron'].map(role=>[role,xs.filter(c=>c.role===role).length]));
 result.parentTrimAudit={kind:'p-first-half-step',threshold:.5,coordinateRule:'max(local cell centre q_i) <= 1.5; P excluded on ties',wholeCells:true,protectedTipIds:[...protectedIds],removedIds:[...removed],removed:counts(decisions.filter(c=>c.remove)),remaining:counts(decisions.filter(c=>!c.remove)),perCopy:['original','clone'].map(copy=>({copy,removed:counts(decisions.filter(c=>c.copy===copy&&c.remove)),remaining:counts(decisions.filter(c=>c.copy===copy&&!c.remove))})),scope:'Experimental cell-centre boundary erosion, not a proved duality half-cycle or exact geometric clipping. Two E-tip contact cells explicitly exempted.'};
 return result;
}
