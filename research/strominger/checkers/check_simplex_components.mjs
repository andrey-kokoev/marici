import assert from 'node:assert/strict';
import {lattice,surfaceLayers,edges,faces} from '../demos/particle-overlap-tetrahedron/simplex-model.mjs';
const {assembly,cells,nodes}=lattice;
assert.deepEqual(assembly.layers.map(l=>l.items.length),[1,4,44,126]);
assert.equal(assembly.items[0].id,'layer0-item1');assert.deepEqual(assembly.items[0].children,[0]);
assert.equal(assembly.items[0].inverted,false);
assert.deepEqual(assembly.components[0].addresses,[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]);
assert.equal(assembly.items.length,175);
assert.deepEqual(assembly.items.flatMap(item=>item.children),assembly.components.map(c=>c.id));
for(const [layer,row] of assembly.layers.entries())for(const [index,item] of row.items.entries()){
 assert.equal(item.id,`layer${layer}-item${index+1}`);assert.equal(item.layer,layer);
 assert.equal(item.children.length,item.kind==='octahedron'?4:1);
 for(const id of item.children){assert.equal(assembly.components[id].layer,layer);assert.equal(assembly.components[id].itemId,item.id);assert.equal(surfaceLayers.cellLayers[id],4-layer);}
}
assert.deepEqual(assembly.layers.map(l=>l.items.filter(i=>i.kind==='octahedron').length),[0,4,0,52]);
assert.equal(assembly.components.filter(c=>c.primitive==='regular').length,119);
assert.equal(assembly.components.filter(c=>c.primitive==='splitOctahedron').length,224);
assert.equal(assembly.groups.length,56);
assert.equal(new Set(cells.map(c=>[...c].sort((a,b)=>a-b).join(','))).size,343);
const claimed=new Set();
for(const group of assembly.groups){
 assert.equal(group.children.length,4);
 const vertexSet=new Set(),incidence=new Map();
 for(const id of group.children){
  assert.ok(!claimed.has(id));claimed.add(id);
  assert.equal(assembly.components[id].parent,group.id);
  assert.equal(assembly.components[id].primitive,'splitOctahedron');
  cells[id].forEach(v=>vertexSet.add(v));
  for(const face of faces){const key=face.map(i=>cells[id][i]).sort((a,b)=>a-b).join(',');incidence.set(key,(incidence.get(key)||0)+1);}
 }
 assert.equal(vertexSet.size,6);
 assert.equal([...incidence.values()].filter(n=>n===1).length,8);
 assert.equal([...incidence.values()].filter(n=>n===2).length,4);
}
assert.equal(claimed.size,224);
for(const component of assembly.components){
 if(component.primitive==='regular')assert.equal(component.parent,null);
 const spectrum=edges.map(([i,j])=>component.addresses[i].reduce((s,x,k)=>s+(x-component.addresses[j][k])**2,0)).sort((a,b)=>a-b);
 assert.deepEqual(spectrum,component.primitive==='regular'?[2,2,2,2,2,2]:[2,2,2,2,2,4]);
}
const sub=(a,b)=>a.map((x,i)=>x-b[i]);
const cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const tets=cells.map(c=>c.map(id=>nodes[id].address.slice(0,3)));
const boxes=tets.map(t=>[0,1,2].map(i=>[Math.min(...t.map(p=>p[i])),Math.max(...t.map(p=>p[i]))]));
// Separating-axis theorem for every pair of convex tetrahedra, in exact
// integer affine coordinates. Touching faces/edges/vertices are permitted;
// positive-volume overlap and containment are not.
function interiorsDisjoint(a,b){
 const axes=[];
 for(const t of [a,b])for(const [i,j,k] of faces)axes.push(cross(sub(t[j],t[i]),sub(t[k],t[i])));
 for(const [i,j] of edges)for(const [k,l] of edges)axes.push(cross(sub(a[j],a[i]),sub(b[l],b[k])));
 return axes.some(axis=>{
  if(axis.every(x=>x===0))return false;
  const pa=a.map(p=>dot(p,axis)),pb=b.map(p=>dot(p,axis));
  return Math.max(...pa)<=Math.min(...pb)||Math.max(...pb)<=Math.min(...pa);
 });
}
let pairCount=0,volume6=0;
for(let i=0;i<tets.length;i++){
 const [a,b,c,d]=tets[i];
 const v=Math.abs(dot(sub(b,a),cross(sub(c,a),sub(d,a))));assert.equal(v,1);volume6+=v;
 for(let j=i+1;j<tets.length;j++){pairCount++;if(boxes[i].some(([min,max],k)=>max<=boxes[j][k][0]||boxes[j][k][1]<=min))continue;assert.ok(interiorsDisjoint(tets[i],tets[j]),`Overlapping or subsumed cells ${i}/${j}`);}
}
assert.equal(volume6,7**3);
assert.ok(nodes.every(n=>n.address.every(Number.isInteger)&&n.address.reduce((s,x)=>s+x,0)===1));
assert.equal(nodes.length,120);
assert.ok(nodes.every(n=>n.address.every(x=>x>=-5&&x<=2)));
const faceIncidence=new Map();
for(const c of cells)for(const f of faces){const key=f.map(i=>c[i]).sort((a,b)=>a-b).join(',');faceIncidence.set(key,(faceIncidence.get(key)||0)+1);}
assert.ok([...faceIncidence.values()].every(n=>n===1||n===2));
const boundary=[...faceIncidence].filter(([,n])=>n===1).map(([key])=>key.split(',').map(Number));
assert.equal(boundary.length,196);
for(const face of boundary)assert.ok([0,1,2,3].some(axis=>face.every(id=>nodes[id].address[axis]===2)),'Every boundary triangle belongs to a flat envelope face');
const boundaryEdges=new Map(),boundaryVertices=new Set();
for(const f of boundary){f.forEach(v=>boundaryVertices.add(v));for(const [i,j] of [[0,1],[0,2],[1,2]]){const k=[f[i],f[j]].sort((a,b)=>a-b).join(',');boundaryEdges.set(k,(boundaryEdges.get(k)||0)+1);}}
assert.ok([...boundaryEdges.values()].every(n=>n===2));
assert.equal(boundaryVertices.size-boundaryEdges.size+boundary.length,2);
const seen=new Set([0]),queue=[0];
for(let i=0;i<queue.length;i++)for(let j=0;j<boundary.length;j++)if(!seen.has(j)&&boundary[queue[i]].filter(v=>boundary[j].includes(v)).length===2){seen.add(j);queue.push(j);}
assert.equal(seen.size,boundary.length); // one closed surface, no enclosed cavities
const centroid=cells.reduce((s,c)=>s.map((x,i)=>x+c.reduce((sum,id)=>sum+nodes[id].address[i]/4,0)/cells.length),[0,0,0,0]);
assert.ok(centroid.every(x=>Math.abs(x-.25)<1e-10)); // seed center = total volume center
export const assemblyVerification={regular:119,splitOctahedron:224,octahedronGroups:56,pairsChecked:pairCount,overlaps:0,duplicateCells:0,volumeMatches:true,uprightSeed:true,closedBoundaryFaces:196};
console.log('PASS component assembly:',JSON.stringify(assemblyVerification));
