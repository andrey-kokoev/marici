// Integer incidence first; Euclidean scale is applied only for display.
// Same planes as the reference: n_i.x = d(1 + 4k).
export const NORMALS = [[1,1,1],[-1,-1,1],[-1,1,-1],[1,-1,-1]];
export const DIRECTIONS = [];
for (let zero=0; zero<3; zero++) {
  const axes=[0,1,2].filter(i=>i!==zero);
  for (const a of [-1,1]) for (const b of [-1,1]) {
    const v=[0,0,0]; v[axes[0]]=a; v[axes[1]]=b; DIRECTIONS.push(v);
  }
}
export const key = v => v.join(',');
export function makeLattice(radius=3, distance=0.67) {
  if (!Number.isInteger(radius) || radius<1 || radius>6 || !Number.isFinite(distance) || distance<=0)
    throw new RangeError('radius must be 1..6 and distance positive');
  const vertices=[], lookup=new Map(), edges=[];
  for(let x=-radius;x<=radius;x++) for(let y=-radius;y<=radius;y++) for(let z=-radius;z<=radius;z++) {
    if ((x+y+z)%2!==0) continue;
    const index=[x,y,z], q=index.map(v=>2*v-1);
    const vertex={index,q,position:q.map(v=>v*Math.sqrt(3)*distance)};
    lookup.set(key(index),vertices.length); vertices.push(vertex);
  }
  vertices.forEach((v,i)=>DIRECTIONS.forEach(direction=>{
    const j=lookup.get(key(v.index.map((n,k)=>n+direction[k])));
    if(j!==undefined && i<j) edges.push([i,j]);
  }));
  // Include every plane containing a displayed vertex; finite circular patches
  // are visual aids, not a clipping or boundary condition for the lattice.
  const planes=NORMALS.flatMap((normal,family)=>{
    const levels=new Set(vertices.map(v=>(normal.reduce((s,n,k)=>s+n*v.q[k],0)-1)/4));
    return [...levels].sort((a,b)=>a-b).map(k=>({family,k,normal:normal.map(n=>n/Math.sqrt(3)),offset:distance*(1+4*k)}));
  });
  return {vertices,edges,planes,lookup,edgeLength:2*Math.sqrt(6)*distance};
}
export function neighbours(lattice,index) {
  return DIRECTIONS.map(d=>lattice.lookup.get(key(index.map((v,k)=>v+d[k])))).filter(i=>i!==undefined);
}
