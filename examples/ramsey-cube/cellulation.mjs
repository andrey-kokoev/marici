// Complete (unclipped) Delaunay cells at a site in the viewer's [0,8]^3 FCC patch.
const inside=p=>p.every(x=>x>=0&&x<=8)
const near=(p,q)=>p.reduce((s,x,i)=>s+(x-q[i])**2,0)===2
function poly(kind,points){
  const edges=[],faces=[]
  for(let i=0;i<points.length;i++)for(let j=0;j<i;j++)if(near(points[i],points[j])){
    edges.push([points[i],points[j]])
    for(let k=0;k<j;k++)if(near(points[k],points[i])&&near(points[k],points[j]))faces.push([points[i],points[j],points[k]])
  }
  return {kind,points,edges,faces}
}
export function cellsAt(p){
  const cells=[]
  for(const dx of [-1,0])for(const dy of [-1,0])for(const dz of [-1,0]){
    const lo=p.map((x,i)=>x+[dx,dy,dz][i]),points=[]
    for(let i=0;i<8;i++){const q=lo.map((x,j)=>x+(i>>j&1));if(q.reduce((a,b)=>a+b,0)%2===0)points.push(q)}
    if(points.every(inside))cells.push(poly('tetrahedron',points))
  }
  for(let d=0;d<3;d++)for(const s of [-1,1]){
    const center=p.map((x,j)=>x+(j===d?s:0)),points=[]
    for(let i=0;i<3;i++)for(const sign of [-1,1])points.push(center.map((x,j)=>x+(i===j?sign:0)))
    if(points.every(inside))cells.push(poly('octahedron',points))
  }
  return cells
}

// Nested FCC solids grown from a fixed apex. Grade = number of elementary
// nearest-neighbour segments on each macro edge, not a graph-theoretic rank.
const cache=new Map()
export function gradedSolid(shape,g){
  if(!['tetrahedron','octahedron'].includes(shape)||!Number.isInteger(g)||g<1||g>(shape==='tetrahedron'?8:4))throw Error('invalid solid or grade')
  const id=shape+g;if(cache.has(id))return cache.get(id)
  const tet=shape==='tetrahedron',inside=([x,y,z])=>tet? x+y>=z&&x+z>=y&&y+z>=x&&x+y+z<=2*g : Math.abs(x-4)+Math.abs(y-4)+Math.abs(z-g)<=g
  const hull=tet?[[0,0,0],[g,g,0],[g,0,g],[0,g,g]]:[[4-g,4,g],[4+g,4,g],[4,4-g,g],[4,4+g,g],[4,4,0],[4,4,2*g]]
  const bars=[],mesh=new Map(),counts={tetrahedron:0,octahedron:0}
  for(let i=0;i<hull.length;i++)for(let j=0;j<i;j++)if(hull[i].reduce((s,x,k)=>s+(x-hull[j][k])**2,0)===2*g*g)bars.push([hull[i],hull[j]])
  for(let x=0;x<=8;x++)for(let y=0;y<=8;y++)for(let z=0;z<=8;z++){
    if((x+y+z)%2||!inside([x,y,z]))continue
    for(const c of cellsAt([x,y,z])){const keys=c.points.map(q=>q.join(','));if(keys.sort()[0]!==[x,y,z].join(',')||!c.points.every(inside))continue
      counts[c.kind]++;for(const e of c.edges)mesh.set(e.map(q=>q.join(',')).sort().join(';'),e)
    }
  }
  const solid={inside,bars,edges:[...mesh.values()],counts};cache.set(id,solid);return solid
}
