// Conditional global reference, not native payload transport.
// Tensor-product line connection of one unit Hopf monopole at each interior
// vertex. Retain factor phases and solid-angle lifts; never infer flux from
// an exponential alone. No high-dimensional tensor state is materialized.
import {nativeToOrthogonal,hopfSection,commonPhase} from './five-side-oct-hopf-probe.mjs';
import {buildLocalHopfTrial,overlapPhase,solidAngle,wrapPhase} from './five-side-oct-local-hopf-trial.mjs';
const keyRing=ring=>[...ring].sort().join('|');
export function connectionMap(trial){return new Map(trial.edgePhases.map(e=>[e.endpoints.join('|'),e.phase]));}
export function pathPhase(connection,cells){
 let phase=0;for(let i=1;i<cells.length;i++){const [a,b]=[cells[i-1],cells[i]],value=connection.get([a,b].sort().join('|'));if(value===undefined)throw Error('Path leaves the retained native connection');phase+=(a<b?1:-1)*value;}return phase;
}
export function buildGlobalHopfTrial(sector,{gauge=()=>0}={}){
 const local=buildLocalHopfTrial(sector),centres=new Map(sector.cells.map(c=>[c.id,c.vertices[0].map((_,i)=>c.vertices.reduce((s,p)=>s+p[i],0)/c.vertices.length)]));
 const used=new Set(local.stars.flatMap(s=>s.cells)),factors=local.stars.map(source=>{
  const directions=new Map(),spinors=new Map();
  for(const id of used){const x=nativeToOrthogonal(centres.get(id),source.point),r=Math.hypot(...x);if(r<1e-10)throw Error('A comparison cell centre hits a monopole');const n=x.map(v=>v/r);directions.set(id,n);spinors.set(id,commonPhase(hopfSection(n,n[2]>-.9?'north':'south'),gauge(source.vertex,id)));}
  return {source:source.vertex,directions,spinors};
 });
 const edgePhases=new Map(),edgeKey=(a,b)=>[a,b].sort().join('|');
 const edgePhase=(a,b)=>{
  const key=edgeKey(a,b),sign=a<b?1:-1;
  if(!edgePhases.has(key)){const [x,y]=[a,b].sort(),contributions=factors.map(f=>({source:f.source,phase:overlapPhase(f.spinors.get(x),f.spinors.get(y))}));edgePhases.set(key,{endpoints:[x,y],contributions,phase:wrapPhase(contributions.reduce((s,c)=>s+c.phase,0))});}
  return sign*edgePhases.get(key).phase;
 };
 const faces=new Map(),starFlux=[];
 for(const star of local.stars){
  const fluxBySource=new Map(factors.map(f=>[f.source,0]));
  for(const face of star.faces){
   const id=keyRing(face.ring),contributions=factors.map(f=>({source:f.source,flux:-solidAngle(face.ring.map(c=>f.directions.get(c)))/2}));
   const flux=contributions.reduce((s,c)=>s+c.flux,0),loop=wrapPhase(face.ring.reduce((s,a,i)=>s+edgePhase(a,face.ring[(i+1)%4]),0));
   for(const c of contributions)fluxBySource.set(c.source,fluxBySource.get(c.source)+c.flux);
   const occurrence={star:star.vertex,ring:face.ring,contributions,flux,loop,phaseAgreementError:Math.abs(wrapPhase(loop-flux))};
   if(!faces.has(id))faces.set(id,{id,nativeEdge:[star.vertex,face.ray].sort(),occurrences:[]});faces.get(id).occurrences.push(occurrence);
  }
  starFlux.push({vertex:star.vertex,fluxBySource:Object.fromEntries(fluxBySource),flux:[...fluxBySource.values()].reduce((s,x)=>s+x,0)});
 }
 const faceList=[...faces.values()],shared=faceList.filter(f=>f.occurrences.length===2),boundary=faceList.filter(f=>f.occurrences.length===1);
 if(faceList.some(f=>f.occurrences.length>2))throw Error('Nonmanifold dual face');
 return {local,factors,edgePhases:[...edgePhases.values()],faces:faceList,starFlux,shared,boundary,boundaryFlux:boundary.reduce((s,f)=>s+f.occurrences[0].flux,0),scope:'Tensor-product connection on the union of interior-vertex dual cells minus their centres. The outer dual boundary is NOT the native octahedron boundary or its closure law.'};
}
