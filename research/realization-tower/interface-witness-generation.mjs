// Local geometric experiment: full relative barycentric dual incidence,
// followed by a declared face-cone realization. No species or target counts.
// Input: tetrahedra in integer affine coordinates of dimension 3 or 4;
// first three coordinates must be an affine chart (as for sum-one A3).
const ix=[0,1,2,3];
const combinations=(xs,n)=>n===0?[[]]:xs.flatMap((x,i)=>combinations(xs.slice(i+1),n-1).map(t=>[x,...t]));
const canonical=xs=>[...xs].sort().join('|');
const mean=vs=>vs[0].map((_,j)=>vs.reduce((s,p)=>s+p[j]/vs.length,0));
const det=(a,b,c)=>a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]);
const volume6=vs=>Math.abs(det(...vs.slice(1).map(v=>v.slice(0,3).map((x,j)=>x-vs[0][j]))));
const gcd=(a,b)=>b?gcd(b,a%b):Math.abs(a);
function plane(vs){
 // All realization vertices are integer or quarter-integer. Work in x'=4x.
 const [a,b,c]=vs.map(v=>v.slice(0,3).map(x=>4*x));
 const u=b.map((x,j)=>x-a[j]),v=c.map((x,j)=>x-a[j]);
 let n=[u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]];
 let row=[...n,-n.reduce((s,x,j)=>s+x*a[j],0)];
 if(!row.some(x=>x!==0))throw Error('Degenerate face');
 if(!row.every(Number.isSafeInteger))throw Error('Unsafe exact plane arithmetic');
 const divisor=row.reduce((g,x)=>gcd(g,Math.abs(x)),0);
 row=row.map(x=>x/divisor);
 if(row.find(x=>x!==0)<0)row=row.map(x=>-x);
 return row.join(',');
}
function complex(tetrahedra,points){
 const faces=new Map();
 for(const t of tetrahedra)for(let size=1;size<=4;size++)for(const vs of combinations(t.vertices,size)){
  const id=canonical(vs);
  if(!faces.has(id))faces.set(id,{id,dimension:size-1,vertices:[...vs].sort(),owners:[]});
  faces.get(id).owners.push(t.id);
 }
 const rows=[...faces.values()];
 const boundary=rows.filter(f=>f.dimension===2&&f.owners.length===1);
 const planes=[...new Set(rows.filter(f=>f.dimension===2).map(f=>plane(f.vertices.map(v=>points[v]))))].sort();
 return {rows,boundary,counts:ix.map(d=>rows.filter(f=>f.dimension===d).length),planes};
}
export function generateInterfaceWitnesses(input){
 if(!input.length||new Set(input.map(t=>t.id)).size!==input.length)throw Error('Distinct nonempty source cells required');
 const points={},tetrahedra=[],seen=new Set();
 for(const t of input){
  if(t.vertices.length!==4||!t.vertices.every(v=>[3,4].includes(v.length)&&v.length===t.vertices[0].length&&v.every(Number.isSafeInteger)))throw Error('Integer tetrahedral source coordinates required');
  if(volume6(t.vertices)===0)throw Error('Degenerate source cell');
  const vertices=t.vertices.map(v=>{const id=`v:${v.join(',')}`;points[id]=[...v];return id;});
  const id=canonical(vertices);if(seen.has(id))throw Error('Repeated geometric source cell');seen.add(id);
  tetrahedra.push({id:t.id,vertices});
 }
 const source=complex(tetrahedra,points);
 if(source.rows.some(f=>f.dimension===2&&f.owners.length>2))throw Error('Nonmanifold face');
 // A relative dual block for EVERY primal face. Its simplices are coface
 // flags starting at that face. Boundary blocks are truncated, not discarded.
 const dualBlocks=source.rows.map(f=>{
  function extend(chain){
   const last=chain.at(-1);if(last.dimension===3)return [chain.map(x=>x.id)];
   return source.rows.filter(g=>g.dimension===last.dimension+1&&last.vertices.every(v=>g.vertices.includes(v))).flatMap(g=>extend([...chain,g]));
  }
  return {primalFace:f.id,dimension:3-f.dimension,onBoundary:source.boundary.some(b=>f.vertices.every(v=>b.vertices.includes(v))),maximalFlags:extend([f]),owners:[...f.owners]};
 });
 const dualVertices=source.rows.map(f=>({id:f.id,point:mean(f.vertices.map(v=>points[v]))}));
 const dualEdges=source.rows.filter(f=>f.dimension===2&&f.owners.length===2).map(f=>({primalFace:f.id,owners:[...f.owners],path:[...f.owners.slice(0,1).map(id=>canonical(tetrahedra.find(t=>t.id===id).vertices)),f.id,...f.owners.slice(1).map(id=>canonical(tetrahedra.find(t=>t.id===id).vertices))]}));
 const refined=[],coneByFace=new Map(),sourceVolumes={};
 for(const t of tetrahedra){
  const center=`center:${t.id}`;points[center]=mean(t.vertices.map(v=>points[v]));
  sourceVolumes[t.id]=volume6(t.vertices.map(v=>points[v]));
  for(const vs of combinations(t.vertices,3)){
   const face=canonical(vs),cell={id:`cone:${t.id}:${face}`,parent:t.id,sourceFace:face,vertices:[center,...vs]};
   refined.push(cell);if(!coneByFace.has(face))coneByFace.set(face,[]);coneByFace.get(face).push(cell.id);
  }
 }
 const witnesses=dualEdges.map(e=>({id:`witness:${e.primalFace}`,dualPath:e.path,parents:e.owners,sourceFace:e.primalFace,cells:coneByFace.get(e.primalFace),type:null}));
 const used=new Set(witnesses.flatMap(w=>w.cells));
 const residual=refined.filter(t=>!used.has(t.id)).map(t=>t.id);
 const output=complex(refined,points);
 const refinedVolumes={};for(const c of refined)refinedVolumes[c.parent]=(refinedVolumes[c.parent]??0)+volume6(c.vertices.map(v=>points[v]));
 if(Object.keys(sourceVolumes).some(id=>sourceVolumes[id]!==refinedVolumes[id]))throw Error('Parent volume not preserved');
 if(source.boundary.map(f=>f.id).sort().join(';')!==output.boundary.map(f=>f.id).sort().join(';'))throw Error('Outer boundary changed');
 // A shared-face witness is geometrically two-sided only if its parent
 // centers lie on opposite sides. Reject folded/overlapping source contacts.
 for(const w of witnesses){
  const vs=source.rows.find(f=>f.id===w.sourceFace).vertices.map(v=>points[v].slice(0,3));
  const side=id=>det(vs[1].map((x,j)=>x-vs[0][j]),vs[2].map((x,j)=>x-vs[0][j]),points[`center:${id}`].slice(0,3).map((x,j)=>x-vs[0][j]));
  if(side(w.parents[0])*side(w.parents[1])>=0)throw Error('Witness parents must occupy opposite half-spaces');
 }
 return {
  policy:'Full relative coface dual; realize each shared-face dual connection by its two incident face cones; retain every other cone',
  source:input.map(t=>({id:t.id,vertices:t.vertices.map(v=>[...v]),role:t.role??null})),
  points,dualVertices,dualBlocks,dualEdges,refinedCells:refined,witnesses,residualCells:residual,
  counts:{before:source.counts,after:output.counts,planesBefore:source.planes.length,planesAfter:output.planes.length,dualBlocks:ix.map(d=>dualBlocks.filter(b=>b.dimension===d).length),sharedInterfaceWitnesses:witnesses.length,witnessTetrahedra:used.size,residualTetrahedra:residual.length},
  planeConvention:'Distinct affine supporting planes of triangular cells, not parallel-plane families or proposed realization/proof slices',
  sourceVolumes,refinedVolumes,boundaryPreserved:true,expandsOuterBody:false,
  limitation:'This is a declared subdivision/dual-thickening policy. It does not derive Witness Generation selection, P/N/E filler types, esd7, or Pb-208.'
 };
}
