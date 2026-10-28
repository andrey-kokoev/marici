import {test} from 'node:test';
import assert from 'node:assert/strict';
import {makeLattice,neighbours,NORMALS,DIRECTIONS} from '../examples/realization-lattice/geometry.js';
test('four equivalent normals, twelve symmetric local directions',()=>{
  for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)assert.equal(NORMALS[i].reduce((s,x,k)=>s+x*NORMALS[j][k],0),-1);
  assert.equal(new Set(DIRECTIONS.map(v=>v.join(','))).size,12);
  for(const n of NORMALS){const dots=DIRECTIONS.map(d=>d.reduce((s,x,k)=>s+x*n[k],0));assert.deepEqual([dots.filter(v=>v<0).length,dots.filter(v=>v===0).length,dots.filter(v=>v>0).length],[3,6,3]);}
});
test('same four plane families, equal edges and twelve interior neighbours',()=>{
  for(const r of [1,2,3,6])for(const d of [0.2,0.67,1.5]){
    const l=makeLattice(r,d);assert.equal(neighbours(l,[0,0,0]).length,12);
    for(const v of l.vertices)for(const n of NORMALS)assert((n.reduce((s,x,k)=>s+x*v.q[k],0)-1)%4===0);
    const seen=new Set();
    for(const [a,b] of l.edges){assert(a<b);assert(!seen.has(`${a},${b}`));seen.add(`${a},${b}`);
      const delta=l.vertices[a].position.map((x,k)=>x-l.vertices[b].position[k]);assert(Math.abs(Math.hypot(...delta)-l.edgeLength)<1e-10);
      const shared=NORMALS.filter(n=>n.reduce((s,x,k)=>s+x*(l.vertices[a].q[k]-l.vertices[b].q[k]),0)===0);assert.equal(shared.length,2);
    }
    assert(l.planes.every(p=>Number.isInteger(p.k)));
  }
});
test('bounds and scale are explicit',()=>{
  for(const args of [[0,1],[7,1],[2.5,1],[2,0],[2,NaN]])assert.throws(()=>makeLattice(...args),RangeError);
  const a=makeLattice(2,0.5),b=makeLattice(2,1);assert.deepEqual(a.edges,b.edges);
  a.vertices.forEach((v,i)=>v.position.forEach((x,k)=>assert.equal(b.vertices[i].position[k],2*x)));
});
