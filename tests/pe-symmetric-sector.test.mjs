import test from 'node:test';import assert from 'node:assert/strict';
import {buildPESymmetricSector,dualPoint} from '../research/strominger/pe-symmetric-sector.mjs';
import {nativeFaceRole} from '../research/realization-tower/native-face-role.mjs';
import {buildFoldedFibration} from '../research/realization-tower/fibration-folded-process.mjs';
import definition from '../research/strominger/fibration-steps-v1.json' with {type:'json'};
const key=vs=>vs.map(p=>p.join(',')).sort().join('|'),opposite={proton:'electron',electron:'proton',neutron:'neutron'};
test('reference really has P-only corner splitting and a 7P/6E native edge strip',()=>{
 const corners=definition.steps[0].assignments;assert.equal(corners.filter(c=>c.role==='proton').length,2);assert.equal(corners.filter(c=>c.role==='electron').length,1);
 const m=buildFoldedFibration(),faces=new Map();for(const c of m.geometry)for(const f of c.faces){const k=key(f);if(!faces.has(k))faces.set(k,{vertices:f,owners:[]});faces.get(k).owners.push(c.id);}
 const strip=[...faces.values()].filter(f=>f.owners.length===1&&f.vertices.every(p=>p[0]===2&&p[1]>=1));assert.equal(strip.length,13);assert.equal(strip.filter(f=>nativeFaceRole(f.vertices)==='proton').length,7);assert.equal(strip.filter(f=>nativeFaceRole(f.vertices)==='electron').length,6);
 // This is a geometric triangle count, independent of growth/corner labels.
});
for(const radius of [0,1,2,3])test(`symmetric native sector radius ${radius}: duality, closure, volume and all edge strips`,()=>{
 const s=buildPESymmetricSector(radius),n=s.edgeUnits,a=s.audit,pairs=new Map(s.dualPairs),faces=new Map(s.faces.map(f=>[f.id,f]));
 assert.equal(a.wholeCells.proton,2*(n**3-n)/3);assert.equal(a.wholeCells.electron,a.wholeCells.proton);assert.equal(a.wholeCells.neutron,(2*n**3+n)/3);assert.equal(a.surfaceCells.proton,a.surfaceCells.electron);assert.equal(a.surfaceFaces.proton,4*n*n);assert.equal(a.surfaceFaces.electron,4*n*n);assert.equal(a.nonmanifoldFaces,0);
 assert.equal(a.wholeCells.proton+a.wholeCells.electron+4*a.wholeCells.neutron,4*n**3);
 for(const c of s.cells){assert.equal(pairs.get(pairs.get(c.id)),c.id);assert.equal(c.faces.length,c.kind==='octahedron'?8:4);for(const p of c.vertices){assert.equal(p.reduce((a,b)=>a+b,0),1);assert.ok(p.every(Number.isInteger));assert.deepEqual(dualPoint(dualPoint(p)),p);assert.ok(p.every((x,i)=>x>=s.lower[i]&&x<=s.upper[i]));}}
 for(const f of s.faces){const dual=faces.get(key(f.vertices.map(dualPoint)));assert.ok(dual);assert.equal(dual.role,opposite[f.role]);assert.deepEqual([...dual.owners].sort(),f.owners.map(id=>pairs.get(id)).sort());}
 const edges=new Map(),vertices=new Set();for(const f of s.boundary){assert.ok([0,1,2,3].some(i=>f.vertices.every(p=>p[i]===s.lower[i])||f.vertices.every(p=>p[i]===s.upper[i])));for(const p of f.vertices)vertices.add(p.join(','));for(let i=0;i<3;i++){const k=key([f.vertices[i],f.vertices[(i+1)%3]]);edges.set(k,(edges.get(k)??0)+1);}}assert.ok([...edges.values()].every(n=>n===2));assert.equal(vertices.size-edges.size+s.boundary.length,2);
 const reached=new Set([s.cells[0].id]);for(let changed=true;changed;){changed=false;for(const f of s.faces)if(f.owners.some(id=>reached.has(id)))for(const id of f.owners)if(!reached.has(id)){reached.add(id);changed=true;}}assert.equal(reached.size,s.cells.length);
 assert.equal(s.edgeStrips.length,12);for(const e of s.edgeStrips){assert.deepEqual([e.upper.proton,e.upper.electron],[n-1,n]);assert.deepEqual([e.lower.proton,e.lower.electron],[n,n-1]);assert.deepEqual([e.combined.proton,e.combined.electron],[2*n-1,2*n-1]);}
});
