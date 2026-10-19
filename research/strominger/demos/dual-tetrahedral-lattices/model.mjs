// Declared reciprocal tetrahedral network. Coordinates are a drawing/checking
// chart, not an identification of physical space or nuclear particle positions.
export const directions=[[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]];
const shifts=[[0,0,0],[-1,0,0],[0,-1,0],[0,0,-1]];
export const id=(family,index)=>`${family}:${index.join(',')}`;
export function site(family,index){
 const [i,j,k]=index,offset=family==='B'?1:0;
 return {id:id(family,index),family,index:[...index],point:[2*(j+k)+offset,2*(i+k)+offset,2*(i+j)+offset]};
}
export function neighbors(s){
 const sign=s.family==='A'?1:-1,other=s.family==='A'?'B':'A';
 return shifts.map(d=>site(other,s.index.map((x,i)=>x+sign*d[i])));
}
export function dual(s){return site(s.family==='A'?'B':'A',s.index.map(x=>-x));}
export function tetrahedron(center){
 const vertices=neighbors(center);
 return {id:(center.family==='B'?'P@':'N@')+center.id,kind:center.family==='B'?'P':'N',center,vertexFamily:center.family==='B'?'A':'B',vertices};
}
export function barycenter(vertices){return [0,1,2].map(i=>vertices.reduce((s,v)=>s+v.point[i],0)/vertices.length);}
export function squared(a,b){return a.reduce((s,x,i)=>s+(x-b[i])**2,0);}
export function determinant(a,b,c){return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]);}
export function volume6(t){const p=t.vertices.map(v=>v.point),d=p.slice(1).map(v=>v.map((x,i)=>x-p[0][i]));return determinant(...d);}
export function pair(){return [tetrahedron(site('B',[0,0,0])),tetrahedron(site('A',[0,0,0]))];}
export function patch(radius=4.5){
 const cells=[];
 for(let i=-4;i<=4;i++)for(let j=-4;j<=4;j++)for(let k=-4;k<=4;k++)for(const family of ['A','B']){
  const center=site(family,[i,j,k]);
  if(center.point.reduce((s,x)=>s+x*x,0)<=radius*radius)cells.push(tetrahedron(center));
 }
 return cells;
}
export function periodicGraph(size=4){
 const mod=x=>((x%size)+size)%size,vertices=[],edges=[];
 for(let i=0;i<size;i++)for(let j=0;j<size;j++)for(let k=0;k<size;k++)for(const family of ['A','B'])vertices.push(site(family,[i,j,k]));
 for(const s of vertices.filter(v=>v.family==='A'))for(const n of neighbors(s)){
  const wrapped=n.index.map(mod),deck=n.index.map((x,i)=>(x-wrapped[i])/size);
  edges.push({source:s.id,target:id('B',wrapped),unwrappedTarget:n,deckTranslation:deck});
 }
 return {size,vertices,edges};
}
export function shortestCycle(graph){
 const adjacency=new Map(graph.vertices.map(v=>[v.id,[]]));
 for(const e of graph.edges){adjacency.get(e.source).push(e.target);adjacency.get(e.target).push(e.source);}
 let best=Infinity;
 for(const root of adjacency.keys()){
  const distances=new Map([[root,0]]),parent=new Map(),queue=[root];
  for(let q=0;q<queue.length;q++){
   const u=queue[q];
   for(const v of adjacency.get(u)){
    if(!distances.has(v)){distances.set(v,distances.get(u)+1);parent.set(v,u);queue.push(v);}
    else if(parent.get(u)!==v&&parent.get(v)!==u)best=Math.min(best,distances.get(u)+distances.get(v)+1);
   }
  }
 }
 return best;
}
export function elementaryLoop(){return [site('A',[0,0,0]),site('B',[0,0,0]),site('A',[1,0,0]),site('B',[1,-1,0]),site('A',[1,-1,0]),site('B',[0,-1,0])];}
export const scope='P/N label whole tetrahedra, not lattice vertices. Reciprocal barycentric selected tetrahedra are not asserted to be conventional cell-dual tilings. No nuclear force, occupied sites, physical charge, coherence maps or isotope stability is inferred.';
