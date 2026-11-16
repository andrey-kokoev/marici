// Boundary of the canonical esd_7(Delta^3) Freudenthal census.
// Source: research/voevodsky/checkers/check_esd7_explicit_analytical_census.py
const permutations = [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]];
export const order = 7;
const corners = [[0,-0.5,0],[0,0.5,0],[-0.5,0,1/Math.sqrt(2)],[0.5,0,1/Math.sqrt(2)]];
export function buildShell() {
  const faces = new Map();
  const key = p => p.join(',');
  const bary = p => [p[0],p[1]-p[0],p[2]-p[1],order-p[2]];
  let tetrahedronCount = 0;
  for(let a=0;a<=order;a++)for(let b=0;b<=order;b++)for(let c=0;c<=order;c++)for(const permutation of permutations) {
    const p=[a,b,c],tet=[p.slice()];
    for(const axis of permutation){p[axis]++;tet.push(p.slice());}
    if(!tet.every(v=>0<=v[0]&&v[0]<=v[1]&&v[1]<=v[2]&&v[2]<=order))continue;
    tetrahedronCount++;
    for(let omit=0;omit<4;omit++) {
      const points=tet.filter((_,i)=>i!==omit),id=points.map(key).sort().join('|');
      const face=faces.get(id);
      if(face)face.incidence++;else faces.set(id,{points,incidence:1});
    }
  }
  const boundary=[...faces.values()].filter(f=>f.incidence===1),vertices=[],lookup=new Map();
  const index=p=>{
    const id=key(p);if(lookup.has(id))return lookup.get(id);
    const weights=bary(p),position=[0,1,2].map(axis=>weights.reduce((s,n,i)=>s+n*corners[i][axis],0));
    position[2]-=order/(2*Math.sqrt(2));
    const i=vertices.length;lookup.set(id,i);vertices.push({cumulative:p,barycentric:weights,position});return i;
  };
  const triangles=boundary.map(f=>f.points.map(index));
  const edges=new Map();
  for(const triangle of triangles)for(const [a,b] of [[0,1],[1,2],[2,0]]) {
    const pair=[triangle[a],triangle[b]].sort((x,y)=>x-y);edges.set(pair.join(','),pair);
  }
  return {order,vertices,triangles,edges:[...edges.values()],tetrahedronCount};
}
