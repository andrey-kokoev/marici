import {worldPoint} from './normal-ray-model.mjs';
const sub=(a,b)=>a.map((v,i)=>v-b[i]),add=(a,b)=>a.map((v,i)=>v+b[i]),mul=(a,s)=>a.map(v=>v*s),dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],unit=a=>mul(a,1/Math.hypot(...a)),mean=ps=>ps[0].map((_,i)=>ps.reduce((s,p)=>s+p[i]/ps.length,0)),key=vs=>vs.map(v=>v.map(q=>q.toFixed(8)).join(',')).sort().join('|');
// One whole tip cell removed from each displayed parent. Records are retained.
export function buildNCapDocking(parent,surface,basePoint){
 const caps=[];
 for(const [copy,label] of [['original','+N'],['clone','−N']]){
  const cap=parent.occurrences.find(c=>c.copy===copy&&c.boundary.includes(label));if(!cap||cap.vertices.length!==4)throw Error('N tip must be one native tetrahedron');
  const binding=parent.bindings.find(b=>b.text===label&&b.copies.includes(copy)),cutFace=cap.faces.find(f=>f.every(v=>key([v])!==key([binding.point]))),neighbor=parent.occurrences.find(c=>c.copy===copy&&c.id!==cap.id&&c.faces.some(f=>key(f)===key(cutFace)));
  if(!neighbor||neighbor.vertices.length!==6)throw Error('Expected whole octahedral neighbor behind N tip');
  const target=surface.faces.find(f=>f.patch===copy&&f.slot===3),src=cutFace.map(p=>worldPoint(basePoint(p,copy))),dst=target.indices.map(i=>surface.vertices[i]),sourceCentre=mean(src),targetCentre=mean(dst),tip=worldPoint(basePoint(binding.point,copy));
  const sourceNormal=unit(sub(tip,sourceCentre)),targetNormal=mul(unit(cross(sub(dst[1],dst[0]),sub(dst[2],dst[0]))),-1),sy=unit(sub(src[0],sourceCentre)),sx=cross(sy,sourceNormal);
  // Choose the least additional roll among the three exact triangle matchings.
  const first=[...dst].sort((a,b)=>dot(unit(sub(b,targetCentre)),sy)-dot(unit(sub(a,targetCentre)),sy))[0],ty=unit(sub(first,targetCentre)),tx=cross(ty,targetNormal);
  const transform=p=>{const d=sub(p,sourceCentre);return add(targetCentre,add(add(mul(tx,dot(d,sx)),mul(ty,dot(d,sy))),mul(targetNormal,dot(d,sourceNormal))));};
  const faceError=Math.max(...src.map(p=>Math.min(...dst.map(q=>Math.hypot(...sub(transform(p),q))))));if(faceError>1e-9)throw Error('N cut triangle failed exact rigid face matching');
  const remaining=parent.occurrences.filter(c=>c.copy===copy&&c.id!==cap.id),normal=mul(targetNormal,-1),clearance=Math.min(...remaining.flatMap(c=>c.vertices.map(p=>dot(sub(transform(worldPoint(basePoint(p,copy))),targetCentre),normal))));
  if(clearance < -1e-8)throw Error('Parent crosses belt attachment plane');
  caps.push({copy,label,cellId:cap.id,retainedCell:structuredClone(cap),neighborId:neighbor.id,cutFace,sourceCentre,targetCentre,targetFace:target.id,sourceNormal,targetNormal,faceError,clearance,transform});
 }
 return {caps,transform:(p,copy)=>caps.find(c=>c.copy===copy).transform(worldPoint(basePoint(p,copy))),audit:{status:'single-N-tip-cut-and-central-face-docked',removedCellIds:caps.map(c=>c.cellId),caps:caps.map(({transform,...c})=>c),scope:'Rigid unit-face docking with parents on opposite exterior half-spaces. Removed tip records retained. Thick belt borders mark the declared inside-N sector; no field law follows.'}};
}
