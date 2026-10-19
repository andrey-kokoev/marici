import * as M from './model.mjs';

// Isometric unfolding of TWO original pentachoron facets along their common face.
// This is not one global3D projection/isometry of the complete4-simplex.
export const sharedFace=['M0','C1','M1'];
const facet=Object.fromEntries(M.facet.map(n=>[n,M.outer[n].slice(0,3)]));
const subtract=(a,b)=>a.map((x,i)=>x-b[i]);
const dot=(a,b)=>a.reduce((sum,x,i)=>sum+x*b[i],0);
const [a,b,c]=sharedFace.map(n=>facet[n]),u=subtract(b,a),v=subtract(c,a);
const normal=[u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]];
const factor=2*dot(subtract(facet.C0,a),normal)/dot(normal,normal);
export const points={...facet,C2:facet.C0.map((x,i)=>x-factor*normal[i])};
export const bodies=[
  {id:'proton',name:'Proton · CMC[M]',notation:'C₀ M₀ C₁ [M₁]',nodes:['C0','M0','C1','M1'],window:['C0','M0','C1'],continuation:'M1',omittedSourceVertex:'C2',color:0x6baec8},
  {id:'neutron',name:'Neutron · MCM[C]',notation:'M₀ C₁ M₁ [C₂]',nodes:['M0','C1','M1','C2'],window:['M0','C1','M1'],continuation:'C2',omittedSourceVertex:'C0',color:0xd7ae77},
];
export const meta={
  title:'CMC[M] → MCM[C] · tetrahedral carriers',badge:'3D · two tetrahedral carriers',
  description:'Proton C₀ M₀ C₁ [M₁] and neutron M₀ C₁ M₁ [C₂]: two regular tetrahedra sharing the MCM face. Brackets mark each fourth continuation vertex.',
  centerTitle:'C₂ · retained fifth vertex, unfolded',formula:'P: C₀ M₀ C₁ [M₁] · N: M₀ C₁ M₁ [C₂]',
  note:'Two source facets unfolded into 3D. This preserves each tetrahedron’s edge lengths, not the complete five-vertex metric.',
  context:'Carrier wireframes',footer:'Proton CMC[M] · neutron MCM[C] · shared MCM face',
};
export function orientedVolume(nodes,coordinates=points) {
  const [a,...rest]=nodes.map(n=>coordinates[n]),[u,v,w]=rest.map(p=>p.map((x,i)=>x-a[i]));
  return (u[0]*(v[1]*w[2]-v[2]*w[1])-u[1]*(v[0]*w[2]-v[2]*w[0])+u[2]*(v[0]*w[1]-v[1]*w[0]))/6;
}
const bodyEdges=bs=>[...new Map(bs.flatMap(b=>b.nodes.flatMap((a,i)=>b.nodes.slice(i+1).map(c=>[a,c].sort()))).map(e=>[e.join('|'),e])).values()];
export const edges=bodyEdges(bodies);
export const sharedFaces=[sharedFace];

// Trial extension, NOT another vertex of the original five-vertex source.
// Reflect the neutron's opposite vertex M0 through the proposed electron face.
export const electronFace=['M1','C1','C2'];
const [e0,e1,e2]=electronFace.map(n=>points[n]),eu=subtract(e1,e0),ev=subtract(e2,e0);
const en=[eu[1]*ev[2]-eu[2]*ev[1],eu[2]*ev[0]-eu[0]*ev[2],eu[0]*ev[1]-eu[1]*ev[0]];
const ef=2*dot(subtract(points.M0,e0),en)/dot(en,en);
const M2=points.M0.map((x,i)=>x-ef*en[i]);
const trialBodies=[...bodies,{id:'electron',name:'Electron · MCC[M]',notation:'M₁ C₁ C₂ [M₂]',nodes:[...electronFace,'M2'],window:electronFace,continuation:'M2',color:0xf19ad0}];
export const trial={
  points:{...points,M2},bodies:trialBodies,edges:bodyEdges(trialBodies),sharedFace,sharedFaces:[sharedFace,electronFace],
  extension:{id:'M2',role:'M',originalSourceVertex:false,construction:'Reflect M0 across the neutron face M1/C1/C2',sourceFace:electronFace,oppositeVertex:'M0'},
  meta:{...meta,title:'CMC[M] → MCM[C] → MCC[M]',badge:'3D · three tetrahedral carriers',
    description:'Electron M₁ C₁ C₂ [M₂] joins the neutron across the MCC face. M₂ is a distinct fourth vertex; the proton and neutron retain their geometry.',
    formula:'P: C₀ M₀ C₁ [M₁] · N: M₀ C₁ M₁ [C₂] · E: M₁ C₁ C₂ [M₂]',
    note:'M₂ is the reflection of M₀ across the M₁ C₁ C₂ face. The three regular tetrahedra have disjoint interiors. M₂ extends the five-vertex geometry; it is not a vertex of the pentachoron.',
    footer:'Three face-attached tetrahedra · six distinct vertices · shared MCM and MCC faces'},
};
