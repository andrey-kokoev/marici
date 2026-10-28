import {cells} from './normal-ray-model.mjs';
import {fibrationClonePoint,fibrationDisplayEnvelope} from './fibration12-process.mjs';
const roles={P:'proton',N:'neutron',E:'electron'};
const centroid=vertices=>vertices[0].map((_,i)=>vertices.reduce((s,v)=>s+v[i]/vertices.length,0));
const faceKey=face=>face.map(v=>v.map(x=>Number(x.toFixed(8))).join(',')).sort().join('|');
const tip=fibrationDisplayEnvelope[1],oppositeTip=fibrationDisplayEnvelope[5];
const seamPoint=tip.map((x,i)=>(x+oppositeTip[i])/2),normal=oppositeTip.map((x,i)=>x-tip[i]);
const normal2=normal.reduce((s,x)=>s+x*x,0);
export function reflectAcrossFibrationSeam(point){
 const scale=2*point.reduce((s,x,i)=>s+(x-seamPoint[i])*normal[i],0)/normal2;
 return point.map((x,i)=>{const value=x-scale*normal[i];return Math.abs(value)<1e-12?0:value;});
}
// Resolve reflected surface triangles to existing native cells, rather than
// assuming that the tetrahedral interior subdivision has mirror symmetry.
const nativeSurfaceFaces=new Map();
for(const cell of cells)for(const axis of [0,2,3]){
 const face=cell.vertices.filter(v=>v[axis]===2);
 if(face.length===3){const key=faceKey(face);if(nativeSurfaceFaces.has(key))throw Error('Ambiguous native surface face');nativeSurfaceFaces.set(key,{cell,face});}
}
export function validateFibrationDefinition(definition){
 if(definition.schemaVersion!==1||definition.carrier!=='face-glued-esd7-pair')throw Error('Unsupported fibration definition');
 if(definition.steps[0]?.operation!=='assign-corners')throw Error('Expected corner initialization');
 const ids=new Set();
 definition.steps.forEach((step,index)=>{
  if(ids.has(step.id))throw Error('Duplicate step id');ids.add(step.id);
  if(index===0){
   if(step.assignments.length!==5||new Set(step.assignments.map(a=>a.vertex)).size!==5)throw Error('Expected five vertex assignments');
   for(const a of step.assignments)if(!/^V[1-5]$/.test(a.vertex)||!Object.values(roles).includes(a.role))throw Error('Invalid corner assignment');
   return;
  }
  const pairing=definition.pairings[step.pairing];
  if(step.operation!=='fill-paired-surface-layer'||step.layer!==index||step.layer>6)throw Error('Invalid layer step');
  if(!pairing?.preserveParticleTypes||pairing.operation!=='reflect-across-shared-face'||pairing.fixedVertices?.join(',')!=='V1,V3,V4'||pairing.faces.length!==3)throw Error('Missing type-preserving face pairing');
  if(step.words.length!==3||!step.words.some(w=>w!==null)||step.words.some(w=>w!==null&&(typeof w!=='string'||w.length!==2*step.layer+1||!/^[PNE]+$/.test(w))))throw Error('Layer word does not fit its surface');
  for(const f of pairing.faces)if(![0,2,3].includes(f.sourcePlane)||![0,2,3].includes(f.towardAxis)||f.sourcePlane===f.towardAxis)throw Error('Invalid face transport');
  if(!step.provisionalRuns.every(n=>[1,2,3].includes(n)))throw Error('Invalid provisional run');
 });
 return definition;
}
export function describeFibrationStep(step){
 if(step.operation==='assign-corners')return step.assignments.map(a=>`${a.label} at ${a.vertex}`).join('; ')+'.';
 return `Layer ${step.layer}: ${step.words.map(w=>w??'unassigned').join(' | ')}. Both V₅ and V₂.${step.provisionalRuns.length?` Runs ${step.provisionalRuns.join(', ')} provisional.`:''}`;
}
export function executeCornerStep(step){
 if(step.operation!=='assign-corners')throw Error('Expected assign-corners');
 const vertices=[...fibrationDisplayEnvelope.slice(0,4),fibrationDisplayEnvelope[5]];
 return step.assignments.map(a=>({text:a.label,role:a.role,point:vertices[Number(a.vertex.slice(1))-1],copies:a.vertex==='V2'?['original']:a.vertex==='V5'?['clone']:['original','clone']}));
}
// One operation creates BOTH sides. Particle types are read exactly once from
// the canonical words, then transported with their face correspondence.
export function executePairedLayerStep(step,pairing){
 if(step.operation!=='fill-paired-surface-layer')throw Error('Expected paired layer operation');
 const {layer}=step;
 const slab=cells.filter(c=>Math.min(...c.vertices.map(v=>v[1]+5))===layer&&Math.max(...c.vertices.map(v=>v[1]+5))===layer+1);
 const canonical=[],paired=[];
 pairing.faces.forEach((side,run)=>{
  const word=step.words[run];
  if(word===null)return;
  const entries=slab.map(cell=>({cell,face:cell.vertices.filter(v=>v[side.sourcePlane]===2)})).filter(e=>e.face.length===3);
  entries.sort((a,b)=>centroid(b.face)[side.towardAxis]-centroid(a.face)[side.towardAxis]);
  if(entries.length!==word.length)throw Error('Surface triangle count does not match step word');
  entries.forEach((entry,index)=>{
   const type=word[index],canonicalId=`${step.id}:${run+1}:${index+1}`;
   const shared={canonicalId,type,sourceType:type,role:roles[type],layer,run:run+1};
   const vertices=entry.face.map(fibrationClonePoint);
   canonical.push({...shared,sourceCell:entry.cell.id,vertices,copy:'clone',face:side.canonical,index:index+1});
   const reflected=vertices.map(reflectAcrossFibrationSeam),target=nativeSurfaceFaces.get(faceKey(reflected));
   if(!target)throw Error('Reflected surface triangle is not a native face');
   paired.push({...shared,sourceCell:target.cell.id,vertices:target.face,copy:'original',face:side.paired,index:index+1});
  });
 });
 paired.sort((a,b)=>a.run-b.run||a.index-b.index);
 return [...canonical,...paired];
}
