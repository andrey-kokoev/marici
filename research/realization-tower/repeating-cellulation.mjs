import {packCellulation} from './cellulation-geometry.mjs';
// The FCC honeycomb has no outer shape: even-parity integer vertices,
// one tetrahedron per unit cube and an octahedron at every odd-parity vertex.
// Only a camera-following, softly faded window is materialized.
export const cellulationEnvelope=[-3,3].flatMap(x=>[-3,3].flatMap(y=>[-3,3].map(z=>[x,y,z])));
export function cellulationWindow(cellSize=1,target=[0,0,0],viewRadius=3,view=null){
 if(!Number.isFinite(cellSize)||cellSize<.5||cellSize>2)throw Error('Cell size must be 0.5..2');
 if(target.length!==3||!target.every(Number.isFinite)||!Number.isFinite(viewRadius)||viewRadius<0)throw Error('Invalid viewing window');
 const spacing=cellSize/Math.SQRT2;
 const origin=target.map(x=>2*Math.round(x/spacing/2));
 if(view){
  const axes=[view.right,view.up,view.normal].map(a=>a.map(x=>Math.round(x*10000)/10000));
  const limits=[Math.ceil(view.halfWidth/spacing)+4,Math.ceil(view.halfHeight/spacing)+4,6];
  const extent=Math.ceil(Math.max(...[0,1,2].map(i=>axes.reduce((sum,a,j)=>sum+Math.abs(a[i])*limits[j],0))))+2;
  return {cellSize,origin,extent,viewport:{axes,limits}};
 }
 return {cellSize,origin,extent:Math.min(12,Math.max(4,Math.ceil(viewRadius/spacing)+3))};
}
export function buildRepeatingCellulation({cellSize,origin,extent,viewport}){
 const spacing=cellSize/Math.SQRT2,cells=[],world=p=>p.map(x=>x*spacing);
 const offsets=[0,1].flatMap(x=>[0,1].flatMap(y=>[0,1].map(z=>[x,y,z])));
 for(let x=origin[0]-extent;x<=origin[0]+extent;x++)for(let y=origin[1]-extent;y<=origin[1]+extent;y++){
  let low=-extent,high=extent;
  // Intersect each vertical lattice column with the camera-aligned slab.
  // This covers arbitrarily wide views without constructing a cubic volume.
  if(viewport)for(let i=0;i<3;i++){
   const [a,b,c]=viewport.axes[i],v=a*(x-origin[0])+b*(y-origin[1]),limit=viewport.limits[i];
   if(Math.abs(c)<1e-8){if(Math.abs(v)>limit){low=1;high=0;break;}}
   else {const u=(-limit-v)/c,w=(limit-v)/c;low=Math.max(low,Math.min(u,w));high=Math.min(high,Math.max(u,w));}
  }
  for(let z=origin[2]+Math.ceil(low);z<=origin[2]+Math.floor(high);z++){
  const base=[x,y,z],vertices=offsets.map(o=>o.map((v,i)=>v+base[i])).filter(p=>(p[0]+p[1]+p[2])%2===0).map(world);
  cells.push({id:`t:${base}`,kind:'tetrahedron',vertices,faces:vertices.map((_,i)=>vertices.filter((_,j)=>i!==j))});
  if((x+y+z)%2!==0){
   const pairs=[0,1,2].map(axis=>[-1,1].map(sign=>world(base.map((v,i)=>v+(i===axis?sign:0)))));
   cells.push({id:`o:${base}`,kind:'octahedron',vertices:pairs.flat(),faces:pairs[0].flatMap(a=>pairs[1].flatMap(b=>pairs[2].map(c=>[a,b,c])))});
  }
 }
 }
 return {...packCellulation(cells,'repeating-fcc'),cellSize,window:{origin:[...origin],extent,viewport},fade:{viewport:!!viewport,center:world(origin),radius:(extent-1)*spacing,width:2*spacing}};
}
