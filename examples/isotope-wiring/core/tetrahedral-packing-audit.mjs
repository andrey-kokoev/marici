// Separating-axis test for two full-dimensional convex tetrahedra.
// All face normals and cross-products of edge directions are required.
const sub=(a,b)=>a.map((x,i)=>x-b[i]);
const dot=(a,b)=>a.reduce((sum,x,i)=>sum+x*b[i],0);
const cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
const edgeIndices=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]],faces=[[0,1,2],[0,1,3],[0,2,3],[1,2,3]];
function validate(points,tolerance){
 if(!Array.isArray(points)||points.length!==4||points.some(p=>!Array.isArray(p)||p.length!==3||p.some(x=>!Number.isFinite(x))))throw Error('Expected four finite 3D points');
 const scale=Math.max(...edgeIndices.map(([a,b])=>Math.hypot(...sub(points[a],points[b]))));
 if(!Number.isFinite(scale)||scale<=tolerance)throw Error('Degenerate tetrahedron');
 const scaled=points.map(p=>sub(p,points[0]).map(x=>x/scale));
 const volume6=Math.abs(dot(sub(scaled[1],scaled[0]),cross(sub(scaled[2],scaled[0]),sub(scaled[3],scaled[0]))));
 if(volume6<=1e-12)throw Error('Degenerate tetrahedron');
 return scaled;
}
export function classifyTetrahedronPair(first,second,{tolerance=1e-8}={}){
 if(!Number.isFinite(tolerance)||tolerance<=0)throw Error('Tolerance must be positive and finite');
 const a=validate(first,tolerance),b=validate(second,tolerance),directions=points=>edgeIndices.map(([i,j])=>sub(points[j],points[i]));
 const ea=directions(a),eb=directions(b),axes=[];
 for(const p of [a,b])for(const [i,j,k] of faces)axes.push(cross(sub(p[j],p[i]),sub(p[k],p[i])));
 for(const x of ea)for(const y of eb)axes.push(cross(x,y));
 let boundaryAxis=null,minimumOverlap=Infinity;
 // Translate projections to a common nearby origin for numerical stability.
 const origin=first[0],left=first.map(p=>sub(p,origin)),right=second.map(p=>sub(p,origin));
 for(const raw of axes){const n=Math.hypot(...raw);if(n<=1e-12)continue;const axis=raw.map(x=>x/n),pa=left.map(p=>dot(p,axis)),pb=right.map(p=>dot(p,axis));
  const overlap=Math.min(Math.max(...pa),Math.max(...pb))-Math.max(Math.min(...pa),Math.min(...pb));
  if(overlap < -tolerance)return {status:'disjoint',separatingAxis:axis,gap:-overlap};
  if(overlap<minimumOverlap)minimumOverlap=overlap;
  if(overlap<=tolerance)boundaryAxis=axis;
 }
 return boundaryAxis?{status:'boundary-contact',boundaryAxis,minimumOverlap}:{status:'volume-overlap',minimumOverlap};
}
export function auditTetrahedralPacking(depths,{tolerance=1e-8}={}){
 if(!depths.solutions.length)throw Error('No incidence-consistent embeddings to audit');
 const contactPairs=new Set(depths.constraints.map(c=>JSON.stringify([depths.cells[c.a].id,depths.cells[c.b].id].sort()))),results=[];
 for(const solution of depths.solutions){const pairs=[];
  for(let i=0;i<depths.cells.length;i++)for(let j=i+1;j<depths.cells.length;j++){
   const first=depths.cells[i].id,second=depths.cells[j].id,a=solution.coordinates[first],b=solution.coordinates[second],classification=classifyTetrahedronPair(Object.values(a),Object.values(b),{tolerance});
   const sharedVertices=[];for(const [p,u] of Object.entries(a))for(const [q,v] of Object.entries(b))if(Math.hypot(...sub(u,v))<=tolerance)sharedVertices.push([p,q]);
   const declared=contactPairs.has(JSON.stringify([first,second].sort()));
   pairs.push({cells:[first,second],...classification,declaredContact:declared,sharedVertices});
  }
  const violatedVertexConstraints=depths.constraints.filter(c=>Math.hypot(...sub(solution.coordinates[depths.cells[c.a].id][c.fromPort],solution.coordinates[depths.cells[c.b].id][c.toPort]))>tolerance).map(c=>c.support);
  const overlaps=pairs.filter(p=>p.status==='volume-overlap'),unexpected=pairs.filter(p=>p.status==='boundary-contact'&&!p.declaredContact),missing=pairs.filter(p=>p.declaredContact&&p.status!=='boundary-contact');
  results.push({mask:solution.mask,status:overlaps.length||unexpected.length||missing.length||violatedVertexConstraints.length?'refuted':'verified-for-cell-geometry',counts:{pairs:pairs.length,disjoint:pairs.filter(p=>p.status==='disjoint').length,boundaryContacts:pairs.filter(p=>p.status==='boundary-contact').length,volumeOverlaps:overlaps.length,unexpectedContacts:unexpected.length,missingContacts:missing.length,violatedVertexConstraints:violatedVertexConstraints.length},violatedVertexConstraints,pairs});
 }
 return {status:results.every(r=>r.status==='verified-for-cell-geometry')?'verified-for-cell-geometry':'refuted',tolerance,embeddings:results.length,results,
  scope:'Pairwise convex cell-volume and contact audit for the supplied, translated regular lifts. Wrapper surfaces, PE paths beyond cell supports, and frame laws are not realized.',
  limits:['Results use the reported component depth offsets; no new intercomponent positions are inferred.','Boundary contact is allowed only for a declared cell pair; coincidence alone does not create a new graph attachment.','The SAT classification is numerical with the stated absolute distance tolerance, not an exact geometric proof.','Surviving embeddings do not select a physical handedness or transport law.']};
}
