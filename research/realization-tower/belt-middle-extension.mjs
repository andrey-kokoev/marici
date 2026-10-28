import {nativeFaceRole} from './native-face-role.mjs';
const add=(a,b)=>a.map((v,i)=>v+b[i]),sub=(a,b)=>a.map((v,i)=>v-b[i]),mul=(a,s)=>a.map(v=>v*s),dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],mean=ps=>ps[0].map((_,i)=>ps.reduce((s,p)=>s+p[i]/ps.length,0)),key=v=>v.join(','),faceKey=vs=>vs.map(key).sort().join('|');
// Three overlapping native blocks, deduplicated as whole cells. The two end
// blocks advance by complementary FCC steps u and -v, u+v = the pole vector.
// The middle block fixes one explicit stagger phase; no fitted prism or split
// octahedron is introduced. This is not a new native field-transport map.
export function extendBeltMiddle(surface){
 if(!surface.axisAlignment)throw Error('Align the belt pole axis before extending');
 const c=surface.cellulation,centre=c.nativeCentre,pole=surface.nativeVertices[surface.axisAlignment.poleIndex],d=sub(pole,centre),positive=d.flatMap((v,i)=>v===1?[i]:[]),negative=d.flatMap((v,i)=>v===-1?[i]:[]);
 if(positive.length!==2||negative.length!==2)throw Error('Expected native opposite-vertex axis');
 const u=[0,0,0,0];u[positive[0]]=1;u[negative[0]]=-1;const v=sub(d,u),nativeMid=mul(sub(u,v),.5);
 const indexAt=q=>c.nativeVertices.findIndex(p=>key(p)===key(q)),origin=c.vertices[indexAt(centre)],U=sub(c.vertices[indexAt(add(centre,u))],origin),V=sub(c.vertices[indexAt(add(centre,v))],origin),mid=mul(sub(U,V),.5);
 const blocks=[{name:'middle',shift:[0,0,0,0],world:[0,0,0]},{name:'upper',shift:u,world:U},{name:'lower',shift:mul(v,-1),world:mul(V,-1)}],sourceFaces=new Map(c.faces.map(f=>[f.id,f])),cellMap=new Map(),vertexMap=new Map(),nativeVertices=[],vertices=[];
 const vertex=(native,world)=>{const k=key(native);if(!vertexMap.has(k)){vertexMap.set(k,vertices.length);nativeVertices.push(native);vertices.push(world);}return vertexMap.get(k);};
 for(const block of blocks)for(const source of c.cells){
  const ns=source.indices.map(i=>add(c.nativeVertices[i],block.shift)),k=faceKey(ns),witness={block:block.name,sourceGeometry:source.sourceGeometry,translation:block.shift};
  if(cellMap.has(k)){cellMap.get(k).witnesses.push(witness);continue;}
  const indices=source.indices.map((i,j)=>vertex(ns[j],sub(add(c.vertices[i],block.world),mid))),local=new Map(source.indices.map((i,j)=>[i,indices[j]]));
  cellMap.set(k,{id:`belt:extended:cell:${cellMap.size}`,kind:source.kind,indices,witnesses:[witness],triangles:source.faces.map(id=>sourceFaces.get(id).indices.map(i=>local.get(i)))});
 }
 const cells=[...cellMap.values()],faceMap=new Map();
 for(const cell of cells)for(const indices of cell.triangles){const k=[...indices].sort((a,b)=>a-b).join(':');if(!faceMap.has(k))faceMap.set(k,{id:`belt:extended:cell-face:${faceMap.size}`,indices,owners:[]});faceMap.get(k).owners.push(cell.id);}
 const allFaces=[...faceMap.values()];if(allFaces.some(f=>f.owners.length>2))throw Error('Nonmanifold native extension');
 for(const f of allFaces){const ns=f.indices.map(i=>nativeVertices[i]),sum=ns[0].reduce((s,_,i)=>s+Math.max(...ns.map(v=>v[i])),0);if(sum!==2&&sum!==3)throw Error('Non-native triangle');f.colorRole=nativeFaceRole(ns);f.colorRule='native-tetrahedral-orientation';}
 const boundary=allFaces.filter(f=>f.owners.length===1),boundaryIds=[...new Set(boundary.flatMap(f=>f.indices))],boundaryIndex=new Map(boundaryIds.map((v,i)=>[v,i]));
 const faces=boundary.map((f,i)=>{let indices=f.indices;const [a,b,c]=indices.map(i=>vertices[i]),centre=mean(indices.map(i=>vertices[i])),owner=cells.find(c=>c.id===f.owners[0]),inside=mean(owner.indices.map(i=>vertices[i]));if(dot(cross(sub(b,a),sub(c,a)),sub(centre,inside))<0)indices=[indices[0],indices[2],indices[1]];const id=`belt:extended:face:${i}`;f.surfaceFace=id;return {...f,id,indices:indices.map(i=>boundaryIndex.get(i)),centre,slot:null,patch:null};});
 const edgesOf=fs=>{const edges=new Map();for(const f of fs)for(let i=0;i<3;i++){const indices=[f.indices[i],f.indices[(i+1)%3]].sort((a,b)=>a-b),k=indices.join(':');if(!edges.has(k))edges.set(k,{indices,faces:[]});edges.get(k).faces.push(f.id);}return [...edges.values()];};
 const edges=edgesOf(faces),cellEdges=edgesOf(allFaces),publicCells=cells.map(({triangles,...cell})=>({...cell,faces:allFaces.filter(f=>f.owners.includes(cell.id)).map(f=>f.id)})),poles=[add(pole,u),sub(sub(mul(centre,2),pole),v)].map(q=>vertexMap.get(key(q)));
 if(cells.length!==34||faces.length!==64||edges.some(e=>e.faces.length!==2)||boundaryIds.length-edges.length+faces.length!==2)throw Error('Unexpected extended boundary');
 return {...surface,id:'belt:surface:native-middle-extension',notation:'native staggered two-band extension',vertices:boundaryIds.map(i=>vertices[i]),nativeVertices:boundaryIds.map(i=>nativeVertices[i]),faces,edges,patches:[],counts:{vertices:boundaryIds.length,edges:edges.length,faces:faces.length,euler:2},axisAlignment:{...surface.axisAlignment,poleIndex:boundaryIndex.get(poles[0])},extension:{kind:'staggered-native-middle',translations:blocks.map(b=>({name:b.name,translation:b.shift})),nativeMidpoint:add(centre,nativeMid),poleIndices:poles.map(i=>boundaryIndex.get(i)),addedBoundaryFaces:32,P:faces.filter(f=>f.colorRole==='proton').length,E:faces.filter(f=>f.colorRole==='electron').length,scope:'One explicit stagger phase, not a uniquely selected continuation. Geometry extension only; wiring remains a separate diagram.'},cellulation:{...c,vertices,nativeVertices,nativeCentre:add(centre,nativeMid),cells:publicCells,faces:allFaces,edges:cellEdges,source:'Integer sum-zero translations of whole native ESD7 template cells',counts:{vertices:vertices.length,edges:cellEdges.length,faces:allFaces.length,cells:cells.length,tetrahedra:cells.filter(c=>c.kind==='tetrahedron').length,octahedra:cells.filter(c=>c.kind==='octahedron').length,internalFaces:allFaces.length-faces.length},parentLatticeAttachment:{status:'tip-contact-only'}},scope:'Native whole-cell extension with 32 P and 32 E boundary faces. No combined particle inventory or field transport is inferred.'};
}
