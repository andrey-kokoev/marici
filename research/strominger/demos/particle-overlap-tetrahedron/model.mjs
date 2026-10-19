// Geometric placement proposed in the operator's overlapping-window model.
// Coordinates follow the existing regular pentachoron spin-interface source.
export const outer = {
  C0: [1, 1, 1, 0], M0: [1, -1, -1, 0],
  C1: [-1, 1, -1, 0], M1: [-1, -1, 1, 0],
  V4: [0, 0, 0, Math.sqrt(5)],
};
export const barycenter = Object.values(outer)[0].map((_, i) =>
  Object.values(outer).reduce((sum, v) => sum + v[i], 0) / 5);
export const points = { ...outer, C2: barycenter };
export const facet = ['C0', 'M0', 'C1', 'M1'];
export const names = { C0:'C₀', M0:'M₀', C1:'C₁', M1:'M₁', C2:'C₂', V4:'V₄' };
export const routes = [
  { id:'proton', name:'Proton', nodes:['C0','M0','C1'], color:0xf6b75a, css:'#f6b75a', start:0,
    detail:'Boundary triangle. Its last segment M₀ → C₁ is shared with the neutron window.' },
  { id:'neutron', name:'Neutron', nodes:['M0','C1','M1'], color:0x66cfff, css:'#66cfff', start:1,
    detail:'Adjacent boundary triangle. C₁ → M₁ is traversed back as M₁ → C₁ in the electron window.' },
  { id:'electron', name:'Electron', nodes:['M1','C1','C2'], color:0xf19ad0, css:'#f19ad0', start:3,
    detail:'Radial triangle. The shared edge returns to C₁, then the path reaches C₂, the pentachoron barycenter.' },
];
export const walk = ['C0','M0','C1','M1','C1','C2'];
export const facetEdges = facet.flatMap((a,i) => facet.slice(i+1).map(b => [a,b]));
export const facetFaces = [[0,1,2],[1,2,3],[0,2,3],[0,1,3]].map(ids => ids.map(i => facet[i]));
export function project4D(point, angle=35) {
  const r=angle*Math.PI/180;
  return [point[0], Math.cos(r)*point[1]-Math.sin(r)*point[3], point[2]];
}
export function pointOnWalk(progress, coordinates=points) {
  const t=Math.max(0,Math.min(5,progress));
  const step=Math.min(4,Math.floor(t)), f=t-step;
  return coordinates[walk[step]].map((v,i) => v+(coordinates[walk[step+1]][i]-v)*f);
}
export function distanceSquared(a,b) { return a.reduce((s,x,i)=>s+(x-b[i])**2,0); }
export function directedEdges(route) { return route.nodes.slice(0,-1).map((a,i)=>[a,route.nodes[i+1]]); }
export const placementScope='Display realizations of the same directed windows: Cartesian and hexagonal lattice incidence, five-vertex regular pentachoron, and the earlier facet/barycenter proposal. Coordinates and traversal progress are not physical configuration variables or time.';

export const carriers=['C0','M0','C1','M1','C2'];
// Operator-requested xz plane: x realization; z C/M codimension layer.
// y is unassigned and unused; M1 is directly above C1 along z.
export const lattice={C0:[-1,0,0],M0:[-1,0,1],C1:[0,0,0],M1:[0,0,1],C2:[1,0,0]};
// Separate simple-hexagonal realization: axial coefficients [q,h,r]
// multiply a, c, b respectively; the original Cartesian view is unchanged.
export const hexBasis={a:[1,0,0],b:[.5,0,Math.sqrt(3)/2],c:[0,1,0]};
export const tetraAxisLabels={X:'a₁',NX:'a₂',Z:'b₁',NZ:'b₂',Y:'c₁',NY:'c₂'};
export const tetraAxisDirections={X:hexBasis.a,NX:hexBasis.a.map(v=>-v),Z:hexBasis.b,NZ:hexBasis.b.map(v=>-v),Y:hexBasis.c,NY:hexBasis.c.map(v=>-v)};
export function hexPoint([q,h,r]) {return [q+r/2,h,r*Math.sqrt(3)/2];}
export const hex=Object.fromEntries(Object.entries(lattice).map(([n,p])=>[n,hexPoint(p)]));
export function triangularGrid(radius=12) {
  if(!Number.isInteger(radius)||radius<1)throw new RangeError('Positive integer grid radius required');
  const vertices=[],triangles=[],edgeMap=new Map(),size=2*radius+1;
  const index=(q,r)=>(q+radius)*size+r+radius;
  for(let q=-radius;q<=radius;q++)for(let r=-radius;r<=radius;r++)vertices.push(hexPoint([q,0,r]));
  for(let q=-radius;q<radius;q++)for(let r=-radius;r<radius;r++) {
    const a=index(q,r),b=index(q+1,r),c=index(q,r+1),d=index(q+1,r+1);
    triangles.push([a,b,c],[b,d,c]);
  }
  for(const cell of triangles)for(let i=0;i<3;i++) {
    const edge=[cell[i],cell[(i+1)%3]].sort((a,b)=>a-b);edgeMap.set(edge.join(','),edge);
  }
  return {radius,vertices,triangles,edges:[...edgeMap.values()]};
}
// Periodic Freudenthal triangulation in basis (a,-b,c). The 120°
// basal pair selects the unit equilateral diagonal on every c=0 face.
export function tetrahedralGrid(radius=3) {
  if(!Number.isInteger(radius)||radius<1)throw new RangeError('Positive integer grid radius required');
  const vertices=[],coefficients=[],tetrahedra=[],edgeMap=new Map(),faceMap=new Map(),size=2*radius+1;
  const index=(u,v,h)=>((u+radius)*size+v+radius)*size+h+radius;
  for(let u=-radius;u<=radius;u++)for(let v=-radius;v<=radius;v++)for(let h=-radius;h<=radius;h++) {
    vertices.push(hexPoint([u,h,-v]));coefficients.push([u,v,h]);
  }
  const permutations=[[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]];
  for(let u=-radius;u<radius;u++)for(let v=-radius;v<radius;v++)for(let h=-radius;h<radius;h++)for(const permutation of permutations) {
    const p=[u,v,h],cell=[index(...p)];
    for(const axis of permutation){p[axis]++;cell.push(index(...p));}
    const inversions=permutation.reduce((sum,x,i)=>sum+permutation.slice(i+1).filter(y=>x>y).length,0);
    if(inversions%2)[cell[1],cell[2]]=[cell[2],cell[1]];
    tetrahedra.push(cell);
    for(let i=0;i<4;i++)for(let j=i+1;j<4;j++) {
      const edge=[cell[i],cell[j]].sort((a,b)=>a-b);edgeMap.set(edge.join(','),edge);
    }
    for(let omitted=0;omitted<4;omitted++) {
      const face=cell.filter((_,i)=>i!==omitted).sort((a,b)=>a-b),key=face.join(',');
      const existing=faceMap.get(key);
      if(existing)existing.uses++;else faceMap.set(key,{vertices:face,uses:1});
    }
  }
  return {radius,vertices,coefficients,tetrahedra,edges:[...edgeMap.values()],faces:[...faceMap.values()]};
}
export function boundedTetrahedralGrid(radius=4) {
  if(!Number.isInteger(radius)||radius<1)throw new RangeError('Positive integer cutoff radius required');
  const source=tetrahedralGrid(Math.ceil(2*radius/Math.sqrt(3)));
  const selected=source.tetrahedra.filter(cell=>cell.every(i=>Math.hypot(...source.vertices[i])<=radius+1e-12));
  const used=[...new Set(selected.flat())],remap=new Map(used.map((id,i)=>[id,i]));
  const vertices=used.map(i=>source.vertices[i]),coefficients=used.map(i=>source.coefficients[i]);
  const tetrahedra=selected.map(cell=>cell.map(i=>remap.get(i))),edgeMap=new Map(),faceMap=new Map();
  for(const cell of tetrahedra) {
    for(let i=0;i<4;i++)for(let j=i+1;j<4;j++) {
      const edge=[cell[i],cell[j]].sort((a,b)=>a-b);edgeMap.set(edge.join(','),edge);
    }
    for(let omitted=0;omitted<4;omitted++) {
      const face=cell.filter((_,i)=>i!==omitted).sort((a,b)=>a-b),key=face.join(',');
      const existing=faceMap.get(key);
      if(existing)existing.uses++;else faceMap.set(key,{vertices:face,uses:1});
    }
  }
  return {radius,center:[0,0,0],vertices,coefficients,tetrahedra,edges:[...edgeMap.values()],faces:[...faceMap.values()]};
}
export function isLatticeView(view) {return view==='lattice'||view==='hex';}
// Here C2 is the fifth ORIGINAL vertex. The barycenter is not a sixth carrier.
export const pentachoron={C0:outer.C0,M0:outer.M0,C1:outer.C1,M1:outer.M1,C2:outer.V4};
const choose=(items,n)=>n===0?[[]]:items.flatMap((v,i)=>choose(items.slice(i+1),n-1).map(rest=>[v,...rest]));
// |sqrt(5) tan(angle)| < 1 puts the projected fifth vertex strictly inside the facet.
export const pentachoronProjectionRange={min:-20,max:20,default:0};
export const simplexEdges=choose(carriers,2);
export const simplexFaces=choose(carriers,3);
export const simplexCells=carriers.map(omitted=>({id:'omit-'+omitted,omitted,nodes:carriers.filter(n=>n!==omitted)}));
export const latticeAxes={x:'realization',y:'unassigned; all carriers at y=0',z:'codimension: C=0, M=1'};
export const hexAxes={a:'realization; a₁ positive, a₂ negative',b:'codimension: C=0, M=1; b₁ positive, b₂ negative',c:'normal; c₁ positive, c₂ negative; all carriers at c=0'};
export const views={
  hex:{title:'Tetrahedral lattice, shared walk',badge:'Orthographic · tetrahedral mesh',description:'One tetrahedral lattice, limited to a 4-unit radius around C₁. C₀–M₀–C₁ remains one elementary coordinate-grid triangle in the xz plane and a shared tetrahedron face. No separate plane lattice is drawn.',centerTitle:'C₂ · tetrahedral lattice endpoint',formula:'a₁/a₂: realization · b₁/b₂: codimension · c₁/c₂: normal',note:'All five carriers have y = 0. Each window is a unit equilateral face of the volume mesh. Off-plane tetrahedra are equal-volume but non-regular: regular tetrahedra alone cannot fill Euclidean 3D space.',context:'Tetrahedral lattice · radius 4',footer:'Single tetrahedral lattice · radius 4 about C₁ · unrestricted orbit'},
  lattice:{title:'Codimension layers, shared walk',badge:'Orthographic · 3D lattice',description:'The lattice lies in the xz plane: x is realization, z is codimension, and y is unused. M₀ and M₁ lie above the C spine along z.',centerTitle:'C₂ · lattice endpoint',formula:'z: C = 0, M = 1 · x: realization',note:'All five carriers have y = 0. M₀ = (−1, 0, 1); M₁ = (0, 0, 1). The y-axis remains unassigned.',context:'Codimension / realization grid',footer:'C layer: z = 0 · M layer: z = 1 · y: unused'}, 
  pentachoron:{title:'Five vertices, three faces',badge:'Orthographic · 4D → 3D',description:'All five carriers are original vertices of a regular pentachoron. Each particle window is one of its ten triangular faces.',centerTitle:'C₂ · fifth pentachoron vertex',formula:'5 vertices · 10 edges · 10 faces · 5 cells',note:'C₂ is the fifth 4D vertex, projected inside the outer tetrahedron. The 4D angle is limited to ±20° to keep it strictly inside; it is not the 4D barycenter.',context:'All 10 simplex edges',footer:'Regular 4-simplex · three original triangular faces'},
  barycenter:{title:'Facet and barycenter',badge:'Orthographic · 4D → 3D',description:'Earlier proposal: four carriers lie on a tetrahedral facet; C₂ is the pentachoron barycenter, distinct from its fifth vertex V₄.',centerTitle:'C₂ · pentachoron barycenter',formula:'b = (v₀ + v₁ + v₂ + v₃ + v₄) / 5',note:'The electron triangle reaches into the center. C₂ is the starting point of the next series.',context:'Fifth outer vertex & center line',footer:'Facet C₀ M₀ C₁ M₁ · radial triangle M₁ C₁ C₂'},
};
export function coordinatesFor(view) {
  if(view==='lattice')return lattice;
  if(view==='hex')return hex;
  if(view==='pentachoron')return pentachoron;
  if(view==='barycenter')return points;
  throw new Error('Unknown view: '+view);
}
// Rotate the orthonormal y-w plane, then orthogonally discard w.
// The lattice is already 3D; every view is subsequently rendered by an orthographic camera.
export function displayPoint(point,view,angle=view==='pentachoron'?pentachoronProjectionRange.default:35) {
  return isLatticeView(view)?point.slice():project4D(point,angle);
}
export function routeDetail(route,view) {
  if(view==='barycenter')return route.detail;
  const shared=route.id==='proton'?'Shares M₀ → C₁ with the neutron.':route.id==='neutron'?'Shares M₀ → C₁ with the proton; reaches M₁ along C₁ → M₁.':'Returns along M₁ → C₁, opposite to the neutron shared edge, then reaches C₂.';
  return (view==='hex'?'Elementary triangular lattice cell. ':view==='lattice'?'Codimension-layered lattice window. ':'Original triangular pentachoron face. ')+shared;
}
