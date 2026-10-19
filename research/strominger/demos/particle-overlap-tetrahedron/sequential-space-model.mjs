import {makeLatticeItem,acrossFace,itemKey} from './lattice-items.mjs';
const mean=points=>points.reduce((a,p)=>a.map((x,i)=>x+p[i]/points.length),[0,0,0,0]);
const sub=(a,b)=>a.map((x,i)=>x-b[i]),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
function normal(item,face){const n=sub(mean(face),item.center),length=Math.sqrt(dot(n,n));return n.map(x=>x/length);}
const faceContinuationRule=Object.freeze({
 name:'inner-center entry, then spatial face continuation',
 principle:'Enter the seed at its center from the inner dimension. Only after a spatial face crossing, continue as straight as possible relative to that incoming face normal. Commit only a unique maximum; otherwise stop.',
 qualification:'Center entry is not an incoming spatial face and supplies no spatial normal by itself. Subsequent normal continuation remains a kinematic proposal, not a derived particle law. Neither particle counts, coordinate ordering nor future layouts select a face.',
 element:'One complete tetrahedral or octahedral lattice item per successful step; an octahedron retains its four primitive cells.',
});
export const sequentialRule=Object.freeze({
 name:'entry–exit centerline continuation',
 principle:'Enter the first cell at its center from the inner dimension; exit the specified last cell at its center into the next realization. Follow their straight segment, admitting only the next full-face neighbor, one item per step.',
 qualification:'A boundary-conditioned kinematic proposal, not a derived particle law. The last cell must be supplied. Edge/vertex crossings remain explicit ambiguities, not coordinate-order choices or general construction obstructions.',
 element:'One complete tetrahedral or octahedral lattice item per successful step.',
});
export function createSequentialConstruction(options={}){
 if(options.incomingFace!=null)throw RangeError('Seed entry is at its center from the inner dimension, not through a spatial face');
 const supplied=options.seed??makeLatticeItem('tetrahedron',[0,0,0,0]);
 const seed=makeLatticeItem(supplied.kind,supplied.origin,supplied.inverted),last=options.exitCell?makeLatticeItem(options.exitCell.kind,options.exitCell.origin,options.exitCell.inverted):null;
 const identity=Object.freeze({...options.identity??{id:'id'}}),placed=[seed],events=[],occupied=new Set([seed.key]);
 const entry={kind:'inner-center',source:'inner-dimension',point:[...seed.center]},direction=last?sub(last.center,seed.center):null;
 let parameter=0,incoming=null;
 function inspect(){
  if(!last)return {status:'needs-exit',reason:'Last cell and its next-realization exit are not specified',candidates:[]};
  const current=placed.at(-1);
  if(current.key===last.key)return {status:'complete',reason:'Identity reaches the last cell center and exits into the next realization',candidates:[]};
  const crossings=[];
  for(const face of current.faces){
   const n=sub(mean(face),current.center),denominator=dot(n,direction);if(denominator<=1e-12)continue;
   const t=dot(n,sub(mean(face),seed.center))/denominator;
   if(t<=parameter+1e-12||t>1+1e-12)continue;
   crossings.push({face,parameter:t});
  }
  if(!crossings.length)return {status:'blocked',reason:'The endpoint segment has no forward boundary crossing',candidates:[]};
  const first=Math.min(...crossings.map(c=>c.parameter));
  const candidates=crossings.filter(c=>Math.abs(c.parameter-first)<1e-12).map(c=>({...c,item:acrossFace(current,c.face)}));
  if(candidates.some(c=>occupied.has(c.item.key)))return {status:'blocked',reason:'The endpoint segment would revisit an occupied item',candidates:[]};
  return {status:candidates.length===1?'ready':'ambiguous',reason:candidates.length===1?'Unique next full-face crossing toward the exit':'The specified segment crosses an edge or vertex; this path needs an additional rule',candidates};
 }
 function snapshot(){
  const decision=inspect(),reached=decision.status==='complete';
  return {identity,entry:structuredClone(entry),exit:last?{kind:'next-center',target:'next-realization',cellKey:last.key,point:[...last.center],reached,identity:reached?identity:null}:null,rule:sequentialRule,...structuredClone(decision),items:structuredClone(placed),incomingFace:structuredClone(incoming),events:structuredClone(events),added:events.length,parameter:reached?1:parameter};
 }
 function step(){
  const decision=inspect();if(decision.status!=='ready')return {...snapshot(),committed:false};
  const {face,item,parameter:t}=decision.candidates[0];
  events.push({number:events.length+1,from:placed.at(-1).key,to:item.key,face:structuredClone(face),priorItemCount:placed.length,identityId:identity.id,parameter:t});
  placed.push(item);occupied.add(item.key);incoming=structuredClone(face);parameter=t;
  return {...snapshot(),committed:true};
 }
 return {snapshot,step};
}
// Separate API for an already face-entered spatial element, not seed admission.
export function resumeFaceContinuation({item,incomingFace,identity}={}){
 if(!item||!incomingFace)throw RangeError('Spatial continuation requires an item and incoming face');
 return createCursor({seed:item,incomingFace,identity,entryKind:'spatial-face'});
}
function createCursor({seed=makeLatticeItem('tetrahedron',[0,0,0,0]),incomingFace=null,identity={id:'id'},entryKind}){
 // Reconstruct geometry rather than accepting a supplied final layout.
 seed=makeLatticeItem(seed.kind,seed.origin,seed.inverted);
 if(incomingFace&&!seed.faces.some(f=>itemKey(f)===itemKey(incomingFace)))throw RangeError('Incoming face is not a boundary face of the current item');
 const entry=entryKind==='inner-center'?{kind:entryKind,source:'inner-dimension',point:[...seed.center]}:{kind:entryKind,source:'spatial-neighbor',face:structuredClone(incomingFace)};
 const carriedIdentity=Object.freeze({...identity}),placed=[seed],occupied=new Set([seed.key]),events=[];
 let incoming=incomingFace?structuredClone(incomingFace):null;
 function inspect(){
  const current=placed.at(-1),direction=incoming?normal(current,incoming).map(x=>-x):null;
  const free=current.faces.filter(f=>!incoming||itemKey(f)!==itemKey(incoming)).map(face=>({face,item:acrossFace(current,face),score:direction?dot(normal(current,face),direction):0})).filter(c=>!occupied.has(c.item.key));
  if(!free.length)return {status:'blocked',reason:'No free face at the active element',candidates:[]};
  const best=Math.max(...free.map(c=>c.score));
  if(direction&&best<=1e-12)return {status:'blocked',reason:'No forward face at the active element',candidates:[]};
  const candidates=free.filter(c=>Math.abs(c.score-best)<1e-12);
  return {status:candidates.length===1?'ready':'ambiguous',reason:candidates.length===1?'Unique face-normal continuation':direction?'Several equally straight continuations':'Inner-center entry supplies no spatial direction distinguishing the exposed faces',candidates};
 }
 function snapshot(){return {identity:carriedIdentity,entry:structuredClone(entry),rule:faceContinuationRule,...structuredClone(inspect()),items:structuredClone(placed),incomingFace:structuredClone(incoming),events:structuredClone(events),added:events.length};}
 function step(){
  const decision=inspect();
  if(decision.status!=='ready')return {...snapshot(),committed:false};
  const {face,item}=decision.candidates[0],from=placed.at(-1);
  // Only this one item is committed. The next face is inspected, not committed.
  events.push({number:events.length+1,from:from.key,to:item.key,face:structuredClone(face),priorItemCount:placed.length,identityId:carriedIdentity.id});
  placed.push(item);occupied.add(item.key);incoming=structuredClone(face);
  return {...snapshot(),committed:true};
 }
 return {snapshot,step};
}
