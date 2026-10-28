import {singleOctahedralEnvelope} from './single-octahedral-process.mjs';
const tips=singleOctahedralEnvelope(1),origin=tips[0].map((x,i)=>(x+tips[1][i])/2);
const axes=[0,2,4].map(j=>tips[j].map((x,i)=>(x-origin[i])/3));
export const junctionCoordinates=p=>axes.map(a=>a.reduce((s,x,i)=>s+x*(p[i]-origin[i]),0));
export const junctionPlanes=[[0,1],[1,2],[2,0]].flatMap(([i,j])=>[-1,1].flatMap(a=>[-1,1].map(b=>({i,j,a,b}))));
// Three pairwise intersections of the perpendicular square-tube envelopes.
// Their union includes the triple overlap, but also reaches its blocked approaches.
export const junctionOverlapVolumes=[[0,1],[1,2],[2,0]].map(pair=>pair.flatMap(i=>junctionPlanes.slice(i*4,i*4+4)));
export function junctionPlaneDistance(p,plane){const q=junctionCoordinates(p);return plane.a*q[plane.i]+plane.b*q[plane.j]-1;}
const eps=1e-9;
const distance2=(a,b)=>a.reduce((s,x,i)=>s+(x-b[i])**2,0);
export function polygonArea(polygon){
 let area=0;for(let i=1;i<polygon.length-1;i++){
  const a=polygon[i].map((x,j)=>x-polygon[0][j]),b=polygon[i+1].map((x,j)=>x-polygon[0][j]);
  const aa=a.reduce((s,x)=>s+x*x,0),bb=b.reduce((s,x)=>s+x*x,0),ab=a.reduce((s,x,j)=>s+x*b[j],0);
  area+=Math.sqrt(Math.max(0,aa*bb-ab*ab))/2;
 }return area;
}
function clean(points){
 const p=points.filter((v,i)=>!i||distance2(v,points[i-1])>eps*eps);
 if(p.length>1&&distance2(p[0],p.at(-1))<=eps*eps)p.pop();
 return p.length>=3&&polygonArea(p)>eps?p:[];
}
function split(polygon,plane){
 const ds=polygon.map(p=>junctionPlaneDistance(p,plane));
 if(ds.every(d=>d<=eps))return {inside:polygon,outside:[]};
 if(ds.every(d=>d>=-eps))return {inside:[],outside:polygon};
 const inside=[],outside=[];
 for(let i=0;i<polygon.length;i++){
  const p=polygon[i],q=polygon[(i+1)%polygon.length],d=ds[i],e=ds[(i+1)%polygon.length];
  if(d<=eps)inside.push(p);if(d>=-eps)outside.push(p);
  if((d>eps&&e< -eps)||(d< -eps&&e>eps)){
   const t=d/(d-e),hit=p.map((x,j)=>x+t*(q[j]-x));inside.push(hit);outside.push(hit);
  }
 }
 return {inside:clean(inside),outside:clean(outside)};
}
function subtractConvex(polygon,planes){
 let candidate=polygon;const patches=[];
 for(const plane of planes){
  if(!candidate.length)break;
  const {inside,outside}=split(candidate,plane);if(outside.length)patches.push(outside);candidate=inside;
 }
 return patches;
}
// Remove internal walls throughout every pairwise overlap (including the triple
// overlap). No new faces or caps: exterior tube walls stay outside these volumes.
export function subtractTubesJunction(polygon){
 return junctionOverlapVolumes.reduce((patches,planes)=>patches.flatMap(p=>subtractConvex(p,planes)),[polygon]);
}
