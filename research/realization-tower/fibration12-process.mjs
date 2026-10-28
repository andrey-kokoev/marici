import attempt from '../strominger/pe-surface-filler-attempt-v1.json' with {type:'json'};
import {seed} from './normal-ray-model.mjs';
export const fibration12Stages=Object.freeze(attempt.construction_steps.map(s=>s.operation));
const roles={P:'proton',E:'electron',N:'neutron'};
const colors={P:0x1265a8,E:0xa82664,N:0xe5eaf0};
const names=['P','E','N1','N2'];
const corners=Object.fromEntries(names.map((name,i)=>[name,[0,1,2,3].map(j=>i===j?-5:2)]));
const binding={N_P:'N1',N_E:'N2'};
const seamCenter=corners.P.map((_,i)=>(corners.P[i]+corners.N1[i]+corners.N2[i])/3);
const axis=corners.P.map((x,i)=>x-seamCenter[i]);
const axisNorm2=axis.reduce((s,x)=>s+x*x,0);
// Proper half-turn in the sum-one affine 3-space: P is fixed, N1/N2 exchange.
// Transport the entire subdivision, not only its outer envelope.
export function fibrationClonePoint(point){
 const delta=point.map((x,i)=>x-seamCenter[i]);
 const factor=2*delta.reduce((s,x,i)=>s+x*axis[i],0)/axisNorm2;
 return delta.map((x,i)=>{const value=seamCenter[i]+factor*axis[i]-x;return Math.abs(value)<1e-12?0:value;});
}
export const fibrationDisplayEnvelope=[...Object.values(corners),...Object.values(corners).map(fibrationClonePoint)];
export function fibration12Process(k,step){
 if(!Number.isInteger(k)||k<1||k>7||!Number.isInteger(step)||step<0||step>=fibration12Stages.length)throw Error('Invalid fibration step');
 const sites=new Map(),paths=[],guides=[];
 function mark(point,type,record){
  const key=point.join(',');if(!sites.has(key))sites.set(key,{point,types:[],records:[]});
  const s=sites.get(key);if(!s.types.includes(type))s.types.push(type);s.records.push(record);
 }
 for(const name of names)mark(corners[name],name[0],{kind:'corner',vertex:name});
 for(const s of attempt.construction_steps.slice(0,step+1))for(const [index,p] of (s.paths??[]).entries()){
  const from=binding[p.origin]??p.origin,to=binding[p.toward]??p.toward;
  const a=corners[from],b=corners[to],points=[a],id=`step${s.step}-path${index}`;
  for(let j=1;j<=p.step_count;j++){
   const point=a.map((x,i)=>x+(b[i]-x)*j/7);points.push(point);
   mark(point,p.word[j-1],{kind:'path-step',path:id,step:j,type:p.word[j-1]});
   guides.push({id:`${id}-${j}`,points:[points[j-1],point],color:colors[p.word[j-1]]});
  }
  paths.push({id,constructionStep:s.step,from,to,word:p.word,points});
 }
 const labels=[...sites.values()].map((s,i)=>({cell:`site-${i}`,point:s.point,role:roles[s.types[0]],text:s.types.join('/')}));
 // Retain both copies; merge coincident seam markers for drawing only.
 const displaySites=new Map();
 for(const [copy,transform] of [['original',p=>p],['clone',fibrationClonePoint]])for(const label of labels){
  const point=transform(label.point),key=point.map(x=>x.toFixed(8)).join(',');
  const isExit=copy==='clone'&&label.point.every((x,i)=>x===corners.E[i]);
  const text=isExit?'E′':label.text;
  if(!displaySites.has(key))displaySites.set(key,{...label,cell:`${copy}-${label.cell}`,point,text});
  else {const prior=displaySites.get(key);if(prior.text!==text)prior.text=[...new Set([...prior.text.split('/'),...text.split('/')])].join('/');}
 }
 const displayLabels=[...displaySites.values()];
 const cloneGuides=guides.map(g=>({...g,id:`clone-${g.id}`,points:g.points.map(fibrationClonePoint)}));
 const repeated=paths.filter((p,i)=>paths.slice(0,i).some(q=>q.from===p.from&&q.to===p.to));
 return {k:7,step,end:seed,assignments:[],retainedBodies:[],presentationLabels:displayLabels,presentationPoints:displayLabels,interfaceGuides:[...guides,...cloneGuides],
 firstRay:null,rays:[],faceNeighbors:[],faceVertexComparisons:[],neutronNeighbors:[],surfaceNeutronNeighbors:[],closureRounds:[],nextClosure:[],diamonds:[],conflicts:[],
 presentationAudit:{nativeGeometry:true,fixedCellSize:true,nativeRealization:false},
 fibrationAudit:{gluedClone:{entry:corners.E,exit:fibrationClonePoint(corners.E),sharedFace:['P','N1','N2'],rotation:'Half-turn about the P-to-N1/N2-midpoint axis',vertexIdentification:{P:'P',N1:'N2',N2:'N1'},entireSubdivisionTransported:true},displaySiteCount:displayLabels.length,userStep:step+1,paths,sites:[...sites.values()],pathCount:paths.length,pathOccurrences:paths.reduce((n,p)=>n+p.word.length,0),distinctDirectedRoutes:new Set(paths.map(p=>`${p.from}->${p.to}`)).size,repeatedRouteCount:repeated.length,multiTypedSites:[...sites.values()].filter(s=>s.types.length>1).length,cornerBinding:corners,respectiveNBinding:binding,interpretation:'Three elementary edge intervals per path. Letters mark successive lattice sites; no tetrahedral cell filling or all-to-all 144-comparison table is inferred.'},
 history:attempt.construction_steps.slice(0,step+1),summary:`Step ${step+1} — ${fibration12Stages[step]}`,canAdvance:step<fibration12Stages.length-1};
}
