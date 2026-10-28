import definition from '../strominger/fibration-steps-v1.json' with {type:'json'};
import {cells,seed} from './normal-ray-model.mjs';
import {fibrationClonePoint,fibrationDisplayEnvelope} from './fibration12-process.mjs';
import {validateFibrationDefinition,describeFibrationStep,executeCornerStep,executePairedLayerStep} from './fibration-step-machine.mjs';
export const fibrationDefinition=validateFibrationDefinition(definition);
export const fibrationRestartStages=Object.freeze(definition.steps.map(describeFibrationStep));
const centroid=vertices=>vertices[0].map((_,i)=>vertices.reduce((s,v)=>s+v[i]/vertices.length,0));
const faceKey=vertices=>vertices.map(v=>v.map(x=>Number(x.toFixed(8))).join(',')).sort().join('|');
const near=(a,b)=>a.every((x,i)=>Math.abs(x-b[i])<1e-9);
const corners=fibrationDisplayEnvelope.slice(0,4);
// Compatibility inspection helpers delegate to the same step executor.
export function firstSurfaceLayer(){return surfaceLayer(1);}
export function surfaceLayer(layer,copy='clone'){
 if(!['clone','original'].includes(copy))throw Error('Invalid copy');
 const step=definition.steps.find(s=>s.operation==='fill-paired-surface-layer'&&s.layer===layer);
 if(!step)throw Error('Undefined layer');
 return executePairedLayerStep(step,definition.pairings[step.pairing]).filter(f=>f.copy===copy);
}
export function fibrationRestartProcess(k,step){
 if(!Number.isInteger(k)||k<1||k>7||!Number.isInteger(step)||step<0||step>=definition.steps.length)throw Error('Invalid restarted fibration step');
 const activeSteps=definition.steps.slice(0,step+1),bindings=executeCornerStep(activeSteps[0]);
 const retainedBodies=[],labels=[];
 for(const binding of bindings)for(const copy of binding.copies){
  const transform=copy==='clone'?fibrationClonePoint:p=>p;
  const matches=cells.filter(c=>c.vertices.some(v=>near(transform(v),binding.point)));
  if(matches.length!==1)throw Error(`Expected one corner cell for ${binding.text} in ${copy}`);
  const source=matches[0],vertices=source.vertices.map(transform),id=`${copy}-${source.id}`;
  retainedBodies.push({id,role:binding.role,components:[vertices],round:0,copy,sourceCell:source.id,vertexLabel:binding.text});
  labels.push({cell:id,point:centroid(vertices),text:binding.text,role:binding.role});
 }
 const surfaceAssignments=activeSteps.slice(1).flatMap(s=>executePairedLayerStep(s,definition.pairings[s.pairing]));
 const groups=new Map();
 for(const a of surfaceAssignments){const key=`${a.copy}-${a.sourceCell}`;if(!groups.has(key))groups.set(key,[]);groups.get(key).push(a);}
 for(const [id,faces] of groups){
  const {sourceCell,copy,layer}=faces[0],cell=cells.find(c=>c.id===sourceCell);
  const transform=copy==='clone'?fibrationClonePoint:p=>p;
  const faceRoles=Object.fromEntries(faces.map(f=>[faceKey(f.vertices),f.role]));
  const existing=retainedBodies.find(b=>b.id===id);
  if(existing)existing.faceRoles=faceRoles;
  else retainedBodies.push({id,components:[cell.vertices.map(transform)],round:layer,copy,sourceCell,color:0x89949e,opacity:.2,faceRoles});
 }
 for(const a of surfaceAssignments)labels.push({cell:`surface-${a.copy}-${a.layer}-${a.run}-${a.index}`,point:centroid(a.vertices),text:a.type,role:a.role});
 const mixedCells=[...groups].filter(([,faces])=>new Set(faces.map(a=>a.type)).size>1).map(([id])=>id);
 const layerSteps=activeSteps.filter(s=>s.operation==='fill-paired-surface-layer');
 return {k:7,step,end:seed,assignments:[],retainedBodies,presentationLabels:labels,
 presentationAudit:{nativeGeometry:true,fixedCellSize:true,nativeRealization:true},
 fibrationAudit:{restart:true,definitionPath:'research/strominger/fibration-steps-v1.json',layerSteps,proposedLayers:layerSteps.filter(s=>s.provisionalRuns.length).map(s=>s.layer),userStep:step+1,surfaceAssignments,mixedCells,layerCount:6,filledLayers:layerSteps.length,layerOrigins:['V5','V2'],pairings:definition.pairings,vertexBindings:bindings,bodyCount:retainedBodies.length,pathCount:0,pathOccurrences:0,paths:[],displaySiteCount:labels.length,gluedClone:{entry:corners[1],exit:fibrationClonePoint(corners[1]),entireSubdivisionTransported:true}},
 firstRay:null,rays:[],faceNeighbors:[],faceVertexComparisons:[],neutronNeighbors:[],surfaceNeutronNeighbors:[],closureRounds:[],nextClosure:[],diamonds:[],conflicts:[],interfaceGuides:[],
 summary:`Step ${step+1} — ${fibrationRestartStages[step]}`,history:activeSteps.map((s,i)=>({step:i+1,definition:s,operation:describeFibrationStep(s)})),canAdvance:step<definition.steps.length-1};
}
