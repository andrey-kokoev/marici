// Compare a common-center sign inversion to the source reciprocal-center incidence.
import fs from 'node:fs';
import assert from 'node:assert/strict';
import {site,neighbors,dual,barycenter} from '../../strominger/demos/dual-tetrahedral-lattices/model.mjs';
const data=JSON.parse(fs.readFileSync(new URL('../../voevodsky/results/esd7_explicit_analytical_census.json',import.meta.url),'utf8'));
const co=new Map(data.vertices.map(v=>[v.id,v.barycentric]));const tet=data.tetrahedra.find(t=>t.id==='T184');
const imb=([a,b,c,d])=>[a+b-c-d,a+c-b-d,a+d-b-c];const add=(a,b)=>a.map((v,i)=>v+b[i]);const neg=a=>a.map(v=>-v);const key=a=>a.join(',');const keys=a=>a.map(key).sort();
const plus=tet.vertices.map(id=>imb(co.get(id)));const A=site('A',[0,0,0]),B=site('B',[0,0,0]);const left=neighbors(B),right=neighbors(A);
assert.deepEqual(keys(plus.map(v=>add(B.point,v))),keys(left.map(s=>s.point)));
assert.deepEqual(keys(plus.map(v=>add(A.point,neg(v)))),keys(right.map(s=>s.point)));
assert.deepEqual(barycenter(left),B.point);assert.deepEqual(barycenter(right),A.point);
const edge=(a,b)=>neighbors(a).some(n=>n.id===b.id);let links=0;
for(const l of left)for(const r of right){assert.equal(edge(l,r),l.id===A.id||r.id===B.id);links+=+edge(l,r)}
const dualMid=A.point.map((v,i)=>(v+B.point[i])/2);for(const l of left){assert.deepEqual(dual(l).point,dualMid.map((m,i)=>2*m-l.point[i]));assert(edge(dual(B),dual(l)))}
// A points necessarily all-even with coordinate sum divisible by 4; B points all odd.
for(const x of plus.map(v=>add(B.point,neg(v))))assert(x.every(i=>i%2===0)&&x.reduce((a,b)=>a+b,0)%4!==0);
assert.equal(links,7);console.log('T184 relative corners',keys(plus),'center of source shell',B.point,'dual shell center',A.point,'fixed inversion point',dualMid,'cross-family links',links,'of 16; partner corners at unchanged center: 0 lattice sites');
