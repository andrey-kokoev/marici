import {lattice} from '../strominger/demos/particle-overlap-tetrahedron/simplex-model.mjs';
import {itemKey} from '../strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs';
const keys=new Set(lattice.cells.map(c=>itemKey(c.map(i=>lattice.nodes[i].address))));
function permutations(xs){return xs.length?xs.flatMap((x,i)=>permutations(xs.filter((_,j)=>i!==j)).map(rest=>[x,...rest])):[[]];}
export const corners=[0,1,2,3].map(axis=>lattice.nodes.reduce((best,n)=>n.address[axis]<best[axis]?n.address:best,lattice.nodes[0].address));
export function cornerPlacement(bodies,corner){
 const proton=bodies.find(b=>b.species==='proton');
 for(const permutation of permutations([0,1,2,3]))for(const sign of [1,-1])for(const anchor of proton.vertices){
  const shift=corner.map((x,i)=>x-sign*anchor[permutation[i]]);
  const transform=p=>p.map((_,i)=>sign*p[permutation[i]]+shift[i]);
  const placed=bodies.map(b=>({...b,vertices:b.vertices.map(transform)}));
  if(placed.every(b=>keys.has(itemKey(b.vertices))))return {bodies:placed,corner,transform:{permutation,sign,shift}};
 }
 return null;
}
