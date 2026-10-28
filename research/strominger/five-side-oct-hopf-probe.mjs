// Explicit reference hypothesis only. No identification with native P/E
// contents, no routing/group selection, and no changes to the viewer.
const axes=[[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]];
const pointKey=p=>p.join(','),faceKey=vs=>vs.map(pointKey).sort().join('|');
function vector(v,n){if(v.length!==n||v.some(x=>!Number.isFinite(x)))throw Error('Invalid finite vector');}
function unit(v,n){vector(v,n);if(Math.abs(v.reduce((s,x)=>s+x*x,0)-1)>1e-9)throw Error('Expected a unit vector');}
export function nativeToOrthogonal(q,centre){return axes.map(a=>a.reduce((s,x,i)=>s+x*(q[i]-centre[i]),0)/2);}
export function orthogonalToNative(x,centre){return centre.map((c,i)=>c+axes.reduce((s,a,j)=>s+a[i]*x[j],0)/2);}

// Radial homeomorphism int(|x|_1 <= R) -> R^3, then inverse stereographic
// projection to S^3. The entire boundary maps to one point: an ADDED quotient.
export function octahedronToSpinor(x,R){
 vector(x,3);if(!Number.isFinite(R)||!(R>0))throw Error('Positive radius required');
 const l1=x.reduce((s,x)=>s+Math.abs(x),0);if(l1>R+1e-9)throw Error('Point outside octahedron');
 const d=Math.max(0,R-l1),r2=x.reduce((s,x)=>s+x*x,0),den=d*d+r2;
 return [...x.map(x=>2*d*x/den),(r2-d*d)/den];
}
export function spinorToOctahedron(q,R){
 unit(q,4);if(!Number.isFinite(R)||!(R>0))throw Error('Positive radius required');
 const den=1-q[3]+q.slice(0,3).reduce((s,x)=>s+Math.abs(x),0);
 if(den<1e-14)return null; // the collapsed boundary class, not a chosen vertex
 return q.slice(0,3).map(x=>R*x/den);
}
// q=(Re z0, Im z0, Re z1, Im z1); these are NOT native P/E records.
export function hopfProjection(q){
 unit(q,4);const [a,b,c,d]=q;
 return [2*(a*c+b*d),2*(b*c-a*d),a*a+b*b-c*c-d*d];
}
export function commonPhase(q,theta){
 unit(q,4);if(!Number.isFinite(theta))throw Error('Finite phase required');const c=Math.cos(theta),s=Math.sin(theta);
 return [q[0]*c-q[1]*s,q[0]*s+q[1]*c,q[2]*c-q[3]*s,q[2]*s+q[3]*c];
}
export function hopfSection(n,patch){
 unit(n,3);const [x,y,z]=n;
 if(patch==='north'){if(1+z<1e-12)throw Error('North section singular at south pole');const d=Math.sqrt(2*(1+z));return [d/2,0,x/d,-y/d];}
 if(patch==='south'){if(1-z<1e-12)throw Error('South section singular at north pole');const d=Math.sqrt(2*(1-z));return [x/d,y/d,d/2,0];}
 throw Error('Unknown Hopf patch');
}
export function sampledTransitionDegree(samples=256){
 if(!Number.isInteger(samples)||samples<8)throw Error('At least eight transition samples required');
 const phases=[];
 for(let i=0;i<=samples;i++){
  const phi=2*Math.PI*i/samples,n=[Math.cos(phi),Math.sin(phi),0],a=hopfSection(n,'north'),b=hopfSection(n,'south');
  const re=a[0]*b[0]+a[1]*b[1]+a[2]*b[2]+a[3]*b[3],im=a[0]*b[1]-a[1]*b[0]+a[2]*b[3]-a[3]*b[2];phases.push(Math.atan2(im,re));
 }
 let winding=0;for(let i=1;i<phases.length;i++)winding+=Math.atan2(Math.sin(phases[i]-phases[i-1]),Math.cos(phases[i]-phases[i-1]));
 return winding/(2*Math.PI);
}
export function spinorDirectionFrame(q){
 unit(q,4);const [a,b,c,d]=q,w=[-c,d,a,-b],iw=[-d,-c,b,a];
 const derivative=v=>[v[0]*c+a*v[2]+v[1]*d+b*v[3],v[1]*c+b*v[2]-v[0]*d-a*v[3],a*v[0]+b*v[1]-c*v[2]-d*v[3]];
 return {normal:hopfProjection(q),x:derivative(w),y:derivative(iw).map(x=>-x)};
}
export function sampledFrameTransitionDegree(samples=256){
 if(!Number.isInteger(samples)||samples<8)throw Error('At least eight transition samples required');
 const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);let last=0,total=0;
 for(let i=0;i<=samples;i++){
  const phi=2*Math.PI*i/samples,n=[Math.cos(phi),Math.sin(phi),0],a=spinorDirectionFrame(hopfSection(n,'north')),b=spinorDirectionFrame(hopfSection(n,'south'));
  const angle=Math.atan2(dot(b.x,a.y),dot(b.x,a.x));if(i)total+=Math.atan2(Math.sin(angle-last),Math.cos(angle-last));last=angle;
 }
 return total/(2*Math.PI);
}
function rank(columns){
 const basis=new Map();for(let bits of columns)while(bits){const p=bits.toString(2).length-1;if(basis.has(p))bits^=basis.get(p);else{basis.set(p,bits);break;}}return basis.size;
}
function homology(chains){
 const indices=chains.map(cs=>new Map(cs.map((c,i)=>[c.id,i]))),matrices=chains.map((cs,d)=>d===0?[]:cs.map(c=>c.boundary.reduce((bits,id)=>indices[d-1].has(id)?bits^(1n<<BigInt(indices[d-1].get(id))):bits,0n)));
 for(let d=2;d<chains.length;d++)for(const column of matrices[d]){
  let result=0n;for(let i=0;i<chains[d-1].length;i++)if(column&(1n<<BigInt(i)))result^=matrices[d-1][i];if(result)throw Error('Boundary squared is nonzero');
 }
 const ranks=matrices.map(rank),counts=chains.map(cs=>cs.length);
 return {cellCounts:counts,boundaryRanks:ranks,betti:counts.map((n,d)=>n-ranks[d]-(ranks[d+1]??0)),euler:counts.reduce((s,n,d)=>s+(d%2?-n:n),0)};
}
export function nativeVertexLinks(sector){
 const points=new Map(sector.cells.flatMap(c=>c.vertices.map(p=>[pointKey(p),p]))),boundary=new Set(sector.boundary.flatMap(f=>f.vertices.map(pointKey)));
 return [...points].map(([id,point])=>{
  const cells=sector.cells.filter(c=>c.vertices.some(p=>pointKey(p)===id)),faces=sector.faces.filter(f=>f.vertices.some(p=>pointKey(p)===id)),rays=new Map();
  for(const f of faces)for(const p of f.vertices)if(pointKey(p)!==id)rays.set(pointKey(p),p);
  const chains=[[...rays.keys()].map(id=>({id,boundary:[]})),faces.map(f=>({id:f.id,boundary:f.vertices.filter(p=>pointKey(p)!==id).map(pointKey)})),cells.map(c=>({id:c.id,boundary:faces.filter(f=>f.owners.includes(c.id)).map(f=>f.id)}))];
  return {id,point,boundary:boundary.has(id),cells:cells.map(c=>c.id),roles:{P:cells.filter(c=>c.role==='proton').length,N:cells.filter(c=>c.role==='neutron').length,E:cells.filter(c=>c.role==='electron').length},rays:[...rays.values()],homology:homology(chains)};
 });
}
// Interpret a formal comparison cycle as an integer 2-chain in the dual of
// its native vertex link. This is a sphere-sweep witness, not a Hopf lift.
export function comparisonSphereSweep(sector,overlap){
 const cells=new Map(sector.cells.map(c=>[c.id,c])),mean=c=>[0,1,2,3].map(i=>c.vertices.reduce((s,p)=>s+p[i],0)/c.vertices.length);
 const a=mean(cells.get(overlap.source)),b=mean(cells.get(overlap.target)),point=a.map((x,i)=>(x+b[i])/2),id=pointKey(point),link=nativeVertexLinks(sector).find(l=>l.id===id);
 if(!link||link.boundary)throw Error('Residual diagram is not at an interior vertex');
 const used=new Set(overlap.paths.flatMap(p=>p.cells));if(used.size!==link.cells.length||link.cells.some(c=>!used.has(c)))throw Error('Diagram is not the full vertex star');
 const dualFaces=new Map();
 for(const ray of link.rays){
  const edge=[point,ray],owns=link.cells.filter(c=>cells.get(c).vertices.some(p=>pointKey(p)===pointKey(ray))),adj=new Map(owns.map(c=>[c,[]]));
  for(const f of sector.faces)if(edge.every(p=>f.vertices.some(q=>pointKey(p)===pointKey(q)))){
   if(f.owners.length!==2)throw Error('Open dual link');adj.get(f.owners[0]).push(f.owners[1]);adj.get(f.owners[1]).push(f.owners[0]);
  }
  if(owns.length!==4||[...adj.values()].some(ns=>ns.length!==2))throw Error('Expected a four-cell native edge ring');
  const ring=[[...owns].sort()[0]];ring.push([...adj.get(ring[0])].sort()[0]);
  while(ring.length<4)ring.push(adj.get(ring.at(-1)).find(n=>n!==ring.at(-2)));
  if(!adj.get(ring.at(-1)).includes(ring[0])||new Set(ring).size!==4)throw Error('Broken dual quadrilateral');
  dualFaces.set(faceKey(edge),ring);
 }
 const cyclic=(a,b)=>a.some((_,offset)=>a.every((x,i)=>x===b[(i+offset)%b.length]));
 const paths=new Map(overlap.paths.map(p=>[p.id,p])),sweeps=[];let generator=null;
 for(const cycle of overlap.cycleBasis){
  const coefficients=new Map([...dualFaces.keys()].map(k=>[k,0]));
  for(const step of cycle.steps){
   const move=overlap.moves[step.edge],p=paths.get(step.from),q=paths.get(step.to),i=move.position,quad=[p.cells[i-1],p.cells[i],p.cells[i+1],q.cells[i]];
   const common=cells.get(quad[0]).vertices.filter(v=>quad.every(c=>cells.get(c).vertices.some(w=>pointKey(w)===pointKey(v))));
   if(common.length!==2||!common.some(p=>pointKey(p)===id))throw Error('Comparison does not bound a native edge ring');
   const k=faceKey(common),ring=dualFaces.get(k),sign=cyclic(quad,ring)?1:cyclic(quad,[...ring].reverse())?-1:0;
   if(!sign)throw Error('Comparison has wrong cyclic incidence');coefficients.set(k,coefficients.get(k)+sign);
  }
  const boundary=new Map();for(const [k,n] of coefficients){const ring=dualFaces.get(k);for(let i=0;i<4;i++){const a=ring[i],b=ring[(i+1)%4],e=[a,b].sort().join('|');boundary.set(e,(boundary.get(e)??0)+n*(a<b?1:-1));}}
  if([...boundary.values()].some(Boolean))throw Error('Sphere sweep is not a closed integer chain');
  const values=[...coefficients.values()];let degree=0;
  if(values.some(Boolean)){
   if(values.some(n=>Math.abs(n)!==1))throw Error('Basis cycle does not sweep the link once');
   if(!generator)generator=values;
   degree=values[0]/generator[0];if(values.some((n,i)=>n!==degree*generator[i]))throw Error('Inconsistent fundamental sphere orientation');
  }
  sweeps.push({steps:cycle.steps.length,degreeRelativeToFirstSweep:degree,coefficients:Object.fromEntries(coefficients)});
 }
 if(!generator)throw Error('No sphere generator represented');
 return {vertex:id,cellIds:link.cells,link:link.homology,roles:link.roles,dualFaces:Object.fromEntries(dualFaces),sweeps,scope:'Exact integer sphere-sweep witness in the native link. No circle action, phase transport or Hopf/Chern class has been inferred.'};
}

export function carrierHomologyMod2(sector){
 const vertices=new Map(),edges=new Map();
 for(const f of sector.faces){
  for(const p of f.vertices)vertices.set(pointKey(p),{id:pointKey(p),boundary:[]});
  for(let i=0;i<3;i++)for(let j=i+1;j<3;j++){const ps=[f.vertices[i],f.vertices[j]];edges.set(faceKey(ps),{id:faceKey(ps),boundary:ps.map(pointKey)});}
 }
 const faces=sector.faces.map(f=>({id:f.id,boundary:[[0,1],[0,2],[1,2]].map(([i,j])=>faceKey([f.vertices[i],f.vertices[j]]))}));
 const cells=sector.cells.map(c=>({id:c.id,boundary:c.faces.map(faceKey)}));
 const boundaryIds=[new Set(),new Set(),new Set(sector.boundary.map(f=>f.id)),new Set()];
 for(const f of sector.boundary){for(const p of f.vertices)boundaryIds[0].add(pointKey(p));for(const [i,j] of [[0,1],[0,2],[1,2]])boundaryIds[1].add(faceKey([f.vertices[i],f.vertices[j]]));}
 const chains=[[...vertices.values()],[...edges.values()],faces,cells];
 return {coefficients:'F2',carrier:homology(chains),boundary:homology(chains.slice(0,3).map((cs,d)=>cs.filter(c=>boundaryIds[d].has(c.id)))),relativeToBoundary:homology(chains.map((cs,d)=>cs.filter(c=>!boundaryIds[d].has(c.id)))),scope:'Cellular homology diagnostic. The original solid is not closed; collapsing its boundary is an extra operation, not performed by this computation.'};
}
