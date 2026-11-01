import {blueClonePoint} from './cellulation-blue-clone.mjs';
const dot=(a,b)=>a.reduce((sum,x,i)=>sum+x*b[i],0),sub=(a,b)=>a.map((x,i)=>x-b[i]);
const cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
export function buildShellFace(previous,index){
 let loop=previous;while(!loop.closingWhiteClone)loop=loop.previous;
 const blue=loop.previous.blueClone,size=previous.cellSize,lattice=p=>p.map(x=>Math.round(x*Math.SQRT2/size));
 const corners=[blue.sourceStart,blue.sourceEnd,blue.attachment,blue.end].map(lattice);
 const triples=[[0,1,2],[0,3,1],[0,2,3],[1,3,2]],planes=triples.map(ids=>{
  const vertices=ids.map(i=>corners[i]),opposite=corners.find((_,i)=>!ids.includes(i));let normal=cross(sub(vertices[1],vertices[0]),sub(vertices[2],vertices[0]));
  if(dot(normal,sub(opposite,vertices[0]))>0)normal=normal.map(x=>-x);
  const length=Math.hypot(...normal);normal=normal.map(x=>x/length);
  return {vertices,normal,distance:p=>dot(normal,sub(p,vertices[0]))};
 });
 const plane=planes[index],inside=p=>planes.every(f=>f.distance(p)<1e-7),on=p=>Math.abs(plane.distance(p))<1e-7;
 const lo=[0,1,2].map(i=>Math.min(...corners.map(p=>p[i]))),hi=[0,1,2].map(i=>Math.max(...corners.map(p=>p[i]))),candidates=[];
 for(let x=lo[0];x<hi[0];x++)for(let y=lo[1];y<hi[1];y++)for(let z=lo[2];z<hi[2];z++){
  const vertices=[0,1].flatMap(dx=>[0,1].flatMap(dy=>[0,1].map(dz=>[x+dx,y+dy,z+dz]))).filter(p=>p.reduce((a,b)=>a+b,0)%2===0);
  if(vertices.every(inside))candidates.push({id:`shell:t:${x},${y},${z}`,kind:'tetrahedron',vertices,faces:vertices.map((_,i)=>vertices.filter((_,j)=>i!==j))});
 }
 for(let x=lo[0];x<=hi[0];x++)for(let y=lo[1];y<=hi[1];y++)for(let z=lo[2];z<=hi[2];z++){
  if((x+y+z)%2===0)continue;
  const pairs=[0,1,2].map(axis=>[-1,1].map(sign=>[x,y,z].map((v,i)=>v+(i===axis?sign:0)))),vertices=pairs.flat();
  if(vertices.every(inside))candidates.push({id:`shell:o:${x},${y},${z}`,kind:'octahedron',vertices,faces:pairs[0].flatMap(a=>pairs[1].flatMap(b=>pairs[2].map(c=>[a,b,c])))});
 }
 const world=p=>p.map(x=>x*size/Math.SQRT2),key=vertices=>vertices.map(p=>p.join(',')).sort().join('|');
 const supporting=candidates.filter(c=>c.faces.some(f=>f.every(on))),existing=new Set(previous.cells.map(c=>key(c.vertices.map(lattice))));
 const newCells=supporting.filter(c=>!existing.has(key(c.vertices))).map(c=>({...c,vertices:c.vertices.map(world),faces:c.faces.map(f=>f.map(world))}));
 const triangles=supporting.flatMap(c=>c.faces.filter(f=>f.every(on))).map(f=>f.map(world));
 const existingFaces=new Set(previous.faces.map(f=>key(f.vertices.map(lattice))));
 // Boundary readings only: do not assign particle roles or impose a color on
 // internal shared interfaces. Match actual seed face planes, not row parity.
 let seed=blue.source;while(seed.step!==6)seed=seed.previous;
 const faceNormal=f=>{const n=cross(sub(f[1],f[0]),sub(f[2],f[0])),length=Math.hypot(...n);return n.map(x=>x/length);};
 const seedFaces=seed.witness.faces.flatMap((face,i)=>[
  {id:`red-seed:face:${i}`,colour:seed.arrows[0].colour,normal:faceNormal(face)},
  {id:`blue-seed:face:${i}`,colour:blue.colour,normal:faceNormal(face.map(p=>blueClonePoint(blue,p)))}
 ]);
 const boundaryReadings=newCells.flatMap(cell=>cell.faces.filter(face=>planes.some(p=>face.every(v=>Math.abs(p.distance(lattice(v)))<1e-7))).map(face=>{
  const normal=faceNormal(face),matches=seedFaces.filter(s=>Math.abs(dot(s.normal,normal))>1-1e-7);
  if(matches.length!==1)throw Error('Shell boundary face must match exactly one retained colored seed orientation');
  const source=matches[0];return {vertices:face,owner:cell.id,kind:cell.kind,colour:cell.kind==='octahedron'?0xffffff:source.colour,source:cell.kind==='octahedron'?'white-octahedral-filler':source.id};
 }));
 return {seedFaces,boundaryReadings,index,corners:plane.vertices,normal:plane.normal,triangles,newTriangles:triangles.filter(f=>!existingFaces.has(key(f.map(lattice)))),newCells,supportingCells:supporting.length,interiorCellsExcluded:candidates.filter(c=>!c.faces.some(f=>planes.some(p=>f.every(v=>Math.abs(p.distance(v))<1e-7)))).length};
}
