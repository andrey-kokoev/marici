// Geometric probe only. k counts planes parallel to the seed's opposite face.
import {lattice,worldPoint} from '../strominger/demos/particle-overlap-tetrahedron/simplex-model.mjs';
export const apex=[-5,2,2,2];
export const addressAt=t=>[-5+t,2-t/3,2-t/3,2-t/3];
const sub=(a,b)=>a.map((x,i)=>x-b[i]);
const det=(a,b,c)=>a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]);
const p=worldPoint(apex),d=sub(worldPoint(addressAt(1)),p),eps=1e-9;
export const cells=lattice.cells.map((ids,id)=>{
 const vertices=ids.map(i=>lattice.nodes[i].address),v=vertices.map(worldPoint),basis=v.slice(1).map(q=>sub(q,v[0])),den=det(...basis);
 function bary(q){const r=sub(q,v[0]),b=[det(r,basis[1],basis[2])/den,det(basis[0],r,basis[2])/den,det(basis[0],basis[1],r)/den];return [1-b.reduce((s,x)=>s+x,0),...b];}
 const a=bary(p),b=bary(p.map((x,i)=>x+d[i])).map((x,i)=>x-a[i]);let lo=0,hi=7,valid=true;
 for(let i=0;i<4;i++){if(Math.abs(b[i])<eps){if(a[i]<-eps)valid=false;}else if(b[i]>0)lo=Math.max(lo,-a[i]/b[i]);else hi=Math.min(hi,-a[i]/b[i]);}
 const interval=valid&&hi>=lo-eps?[Math.max(0,lo),Math.min(7,hi)]:null;
 return {id,vertices,interval};
});
export const seed=cells.find(c=>c.vertices.some(v=>v.every((x,i)=>x===apex[i])));
if(!seed)throw Error('Missing corner seed');
export function slice(k){
 if(!Number.isInteger(k)||k<1||k>7)throw Error('Plane index must be 1..7');
 const polygons=new Map();let cutCells=0;
 for(const cell of cells){
  const points=[];
  for(let i=0;i<4;i++){
   const a=cell.vertices[i],da=a[0]-(-5+k);if(Math.abs(da)<eps)points.push(a);
   for(let j=i+1;j<4;j++){const b=cell.vertices[j],db=b[0]-(-5+k);if(da*db<0){const t=da/(da-db);points.push(a.map((x,n)=>x+t*(b[n]-x)));}}
  }
  const unique=[...new Map(points.map(p=>[p.map(x=>x.toFixed(9)).join(','),p])).values()];
  if(unique.length<3)continue;cutCells++;
  const center=unique[0].map((_,i)=>unique.reduce((s,p)=>s+p[i]/unique.length,0));
  // Coordinates q1,q2 are affine coordinates on the slice plane.
  unique.sort((a,b)=>Math.atan2(a[2]-center[2],a[1]-center[1])-Math.atan2(b[2]-center[2],b[1]-center[1]));
  const key=unique.map(p=>p.map(x=>x.toFixed(9)).join(',')).sort().join('|');polygons.set(key,unique);
 }
 const traversed=cells.filter(c=>c.interval&&Math.min(k,c.interval[1])-Math.max(0,c.interval[0])>eps).map(c=>c.id);
 const atStop=cells.filter(c=>c.interval&&c.interval[0]<=k+eps&&c.interval[1]>=k-eps).map(c=>c.id);
 return {k,point:addressAt(k),polygons:[...polygons.values()],cutCells,traversed,atStop};
}
export const faceEvents=[...new Set(cells.flatMap(c=>c.interval??[]).filter(t=>t>eps&&t<=7+eps).map(t=>Number(t.toFixed(9))))].sort((a,b)=>a-b);
export {lattice,worldPoint};
