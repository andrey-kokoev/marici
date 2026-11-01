import {packCellulation} from './cellulation-geometry.mjs';
const pointKey=p=>p.join(','),cellKey=c=>c.vertices.map(p=>p.map(x=>Math.round(x*Math.SQRT2)).join(',')).sort().join('|');
const world=p=>p.map(x=>x/Math.SQRT2);
function tetrahedron(base){
 const vertices=[0,1].flatMap(x=>[0,1].flatMap(y=>[0,1].map(z=>[base[0]+x,base[1]+y,base[2]+z]))).filter(p=>(p[0]+p[1]+p[2])%2===0);
 const points=vertices.map(world);return {id:`t:${base}`,kind:'tetrahedron',vertices:points,faces:points.map((_,i)=>points.filter((_,j)=>i!==j))};
}
function octahedron(center){
 const pairs=[0,1,2].map(axis=>[-1,1].map(sign=>world(center.map((v,i)=>v+(i===axis?sign:0)))));
 return {id:`o:${center}`,kind:'octahedron',vertices:pairs.flat(),faces:pairs[0].flatMap(a=>pairs[1].flatMap(b=>pairs[2].map(c=>[a,b,c])))};
}
function neighbors(cell){
 const result=[];
 for(const face of cell.faces){
  const f=face.map(p=>p.map(x=>Math.round(x*Math.SQRT2))),keys=f.map(pointKey);
  const lo=[0,1,2].map(i=>Math.max(...f.map(p=>p[i]))-1),hi=[0,1,2].map(i=>Math.min(...f.map(p=>p[i])));
  for(let x=lo[0];x<=hi[0];x++)for(let y=lo[1];y<=hi[1];y++)for(let z=lo[2];z<=hi[2];z++){
   const candidate=tetrahedron([x,y,z]),vertices=new Set(candidate.vertices.map(p=>pointKey(p.map(v=>Math.round(v*Math.SQRT2)))));
   if(keys.every(k=>vertices.has(k)))result.push(candidate);
  }
  for(let axis=0;axis<3;axis++)for(const sign of [-1,1]){
   const center=f[0].map((v,i)=>v+(i===axis?sign:0));
   if(f.every(p=>p.reduce((sum,v,i)=>sum+Math.abs(v-center[i]),0)===1))result.push(octahedron(center));
  }
 }
 return result;
}
// Background context only: four whole cells incident to a unit FCC edge.
export function cellulationEdgeContext(from,to,cellSize=1){
 const [a,b]=[from,to].map(p=>p.map(x=>Math.round(x*Math.SQRT2/cellSize))),keys=[pointKey(a),pointKey(b)],result=[];
 const lo=a.map((x,i)=>Math.max(x,b[i])-1),hi=a.map((x,i)=>Math.min(x,b[i]));
 for(let x=lo[0];x<=hi[0];x++)for(let y=lo[1];y<=hi[1];y++)for(let z=lo[2];z<=hi[2];z++){
  const c=tetrahedron([x,y,z]),vertices=new Set(c.vertices.map(p=>pointKey(p.map(v=>Math.round(v*Math.SQRT2)))));
  if(keys.every(k=>vertices.has(k)))result.push(c);
 }
 for(let axis=0;axis<3;axis++)for(const sign of [-1,1]){
  const center=a.map((x,i)=>x+(i===axis?sign:0));
  if(b.reduce((sum,x,i)=>sum+Math.abs(x-center[i]),0)===1)result.push(octahedron(center));
 }
 return result.map(c=>({...c,vertices:c.vertices.map(p=>p.map(x=>x*cellSize)),faces:c.faces.map(f=>f.map(p=>p.map(x=>x*cellSize)))}));
}
export function cellulationIncidentEdges(edges,point){
 return edges.filter(e=>e.vertices.some(p=>p.every((v,i)=>Math.abs(v-point[i])<1e-7)));
}
// Whole cells within two face-adjacency hops; independent of camera and zoom.
export function buildCellulationNeighborhood(placed,layers=2){
 if(!Number.isInteger(layers)||layers<0||layers>2)throw Error('Expected zero, one or two layers');
 const seen=new Map(placed.map(c=>[cellKey(c),c]));let frontier=[...seen.values()];
 for(let layer=0;layer<layers;layer++){
  const next=[];for(const cell of frontier)for(const candidate of neighbors(cell)){
   const key=cellKey(candidate);if(seen.has(key))continue;seen.set(key,candidate);next.push(candidate);
  }frontier=next;
 }
 return {...packCellulation([...seen.values()],'cellulation-neighborhood'),cellSize:1,layers,placedCells:placed.length};
}
