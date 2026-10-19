// Periodic quantum-test supports generated from the actual native octahedra.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {makeLatticeItem} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
const root=new URL('../../../',import.meta.url),out=new URL('../results/chamon-fcc-covers/',import.meta.url);
const F=b=>[b[1]+b[2],b[1]+b[3],b[2]+b[3]];
const lift=t=>[-(t[0]+t[1]+t[2])/2,(t[0]+t[1]-t[2])/2,(t[0]+t[2]-t[1])/2,(-t[0]+t[1]+t[2])/2];
const classes=[[0,0,0],[1,1,0],[1,0,1],[0,1,1]],mod=(x,m)=>(x%m+m)%m;
assert.deepEqual(makeLatticeItem('tetrahedron',[0,0,0,0]).vertices.map(F),classes);
const covers=[];
for(const lengths of [[2,2,2],[4,4,4],[6,6,6],[4,6,8]]){
 const qubits=[],centers=[];
 for(let x=0;x<lengths[0];x++)for(let y=0;y<lengths[1];y++)for(let z=0;z<lengths[2];z++)((x+y+z)%2?centers:qubits).push([x,y,z]);
 const indices=new Map(qubits.map((v,i)=>[v.join(','),i])),octahedra=[];
 for(const center of centers){
  const delta=lift(center.map(x=>x-1)),origin=delta.map((x,i)=>x-(i===0?1:0));
  assert(origin.every(Number.isInteger));
  const native=makeLatticeItem('octahedron',origin),vertices=native.vertices.map(F);
  assert.equal(vertices.length,6);assert.equal(native.faces.length,8);assert.equal(native.components.length,4);
  assert.deepEqual(vertices.reduce((s,v)=>s.map((x,i)=>x+v[i]),[0,0,0]).map(x=>x/6),center);
  const factors=[];
  for(let axis=0;axis<3;axis++)for(const side of [-1,1]){
   const point=center.map((x,i)=>x+(i===axis?side:0));assert(vertices.some(v=>String(v)===String(point)));
   const wrapped=point.map((x,i)=>mod(x,lengths[i])),deck=point.map((x,i)=>(x-wrapped[i])/lengths[i]);
   assert(deck.every(Number.isInteger));const qubit=indices.get(wrapped.join(','));assert(Number.isInteger(qubit));
   factors.push({pauli:'XYZ'[axis],unwrapped:point,wrapped,deck,qubit});
  }
  octahedra.push({center,classBits:center.map(x=>x%2),nativeOrigin:origin,nativeKey:native.key,factors});
 }
 assert.equal(qubits.length,lengths.reduce((a,b)=>a*b)/2);assert.equal(octahedra.length,qubits.length);
 covers.push({lengths,qubits,octahedra});
}
const report={schema:'marici.chamon-fcc-covers.v1',status:'pass',fccMap:'(b1+b2,b1+b3,b2+b3)',classes,covers,nativeGrammarChanged:false,sourceHashes:{}};
for(const path of ['research/strominger/checkers/export_chamon_fcc_covers.mjs','research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs','research/strominger/demos/particle-overlap-tetrahedron/simplex-components.mjs'])report.sourceHashes[path]=createHash('sha256').update(await readFile(new URL(path,root))).digest('hex');
await mkdir(out,{recursive:true});await writeFile(new URL('verification.json',out),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:'pass',covers:covers.map(c=>({lengths:c.lengths,spins:c.qubits.length}))}));
