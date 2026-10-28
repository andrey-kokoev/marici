// Experimental connection choice: shortest-geodesic Hopf/Pancharatnam
// transport between cell-centre directions at each interior vertex.
// NOT a source-derived operation on P/E contents or retained histories.
import {nativeVertexLinks,nativeToOrthogonal,hopfSection,commonPhase} from './five-side-oct-hopf-probe.mjs';
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
export const wrapPhase=x=>Math.atan2(Math.sin(x),Math.cos(x));
export function overlapPhase(a,b){
 const re=dot(a,b),im=a[0]*b[1]-a[1]*b[0]+a[2]*b[3]-a[3]*b[2];
 if(Math.hypot(re,im)<1e-10)throw Error('Antipodal directions: geodesic transport is ambiguous');
 return Math.atan2(im,re);
}
export function solidAngle(ring){
 let sum=0;const a=ring[0];for(let i=1;i<ring.length-1;i++){
  const b=ring[i],c=ring[i+1];sum+=2*Math.atan2(dot(a,cross(b,c)),1+dot(a,b)+dot(b,c)+dot(c,a));
 }return sum;
}
export function loopPhase(star,ring){
 return wrapPhase(ring.reduce((s,id,i)=>s+overlapPhase(star.spinors.get(id),star.spinors.get(ring[(i+1)%ring.length])),0));
}
export function buildLocalHopfTrial(sector,{gauge=()=>0}={}){
 const cells=new Map(sector.cells.map(c=>[c.id,c])),stars=[];
 for(const link of nativeVertexLinks(sector).filter(l=>!l.boundary)){
  const directions=new Map(),spinors=new Map();
  for(const id of link.cells){
   const c=cells.get(id),centre=link.point.map((_,i)=>c.vertices.reduce((s,p)=>s+p[i],0)/c.vertices.length),x=nativeToOrthogonal(centre,link.point),n=x.map(v=>v/Math.hypot(...x));
   directions.set(id,n);spinors.set(id,commonPhase(hopfSection(n,n[2]>-.9?'north':'south'),gauge(link.id,id)));
  }
  const star={vertex:link.id,point:link.point,cells:link.cells,directions,spinors,faces:[]};
  for(const ray of link.rays){
   const contains=(face,p)=>face.vertices.some(q=>q.every((x,i)=>x===p[i]));
   const faces=sector.faces.filter(f=>contains(f,link.point)&&contains(f,ray)),adj=new Map();
   for(const f of faces){if(f.owners.length!==2)throw Error('Open interior edge ring');const [a,b]=f.owners;for(const [x,y]of [[a,b],[b,a]]){if(!adj.has(x))adj.set(x,[]);adj.get(x).push(y);}}
   if(adj.size!==4||[...adj.values()].some(ns=>ns.length!==2))throw Error('Expected quadrilateral');
   const ring=[[...adj.keys()].sort()[0]];ring.push([...adj.get(ring[0])].sort()[0]);while(ring.length<4)ring.push(adj.get(ring.at(-1)).find(x=>x!==ring.at(-2)));
   if(new Set(ring).size!==4||!adj.get(ring.at(-1)).includes(ring[0]))throw Error('Broken ring');
   if(solidAngle(ring.map(id=>directions.get(id)))<0)ring.reverse();
   const area=solidAngle(ring.map(id=>directions.get(id))),phase=loopPhase(star,ring);
   star.faces.push({ray:ray.join(','),ring,area,phase});
  }
  star.totalArea=star.faces.reduce((s,f)=>s+f.area,0);
  // Retain individual face logs. Their total is not reduced modulo 2*pi.
  star.phaseSum=star.faces.reduce((s,f)=>s+f.phase,0);star.charge=star.phaseSum/(2*Math.PI);
  stars.push(star);
 }
 const byVertex=new Map(stars.map(s=>[s.vertex,s])),overlaps=[];
 for(const a of stars)for(const face of a.faces){
  const b=byVertex.get(face.ray);if(!b||a.vertex>=b.vertex)continue;
  if(face.ring.some(id=>!b.spinors.has(id)))throw Error('Shared edge does not share its four comparison cells');
  const phaseA=loopPhase(a,face.ring),phaseB=loopPhase(b,face.ring);
  overlaps.push({vertices:[a.vertex,b.vertex],ring:face.ring,phaseA,phaseB,mismatch:wrapPhase(phaseA-phaseB),conjugatedMismatch:wrapPhase(phaseA+phaseB)});
 }
 const neighbours=new Map(stars.map(s=>[s.vertex,new Set()]));for(const o of overlaps){const [a,b]=o.vertices;neighbours.get(a).add(b);neighbours.get(b).add(a);}
 const triangles=[];for(const [a,ns] of neighbours)for(const b of ns)if(a<b)for(const c of neighbours.get(b))if(b<c&&ns.has(c))triangles.push([a,b,c]);
 return {stars,overlaps,triangles};
}
