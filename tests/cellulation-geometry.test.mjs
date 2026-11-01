import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationGeometry} from '../research/realization-tower/cellulation-geometry.mjs';
import {buildFoldedFibration} from '../research/realization-tower/fibration-folded-process.mjs';
import {worldPoint} from '../research/realization-tower/normal-ray-model.mjs';
import {buildPESymmetricSector} from '../research/strominger/pe-symmetric-sector.mjs';
test('Su-32 uses its own complete edge-three octahedral carrier, not the 175-cell reference',()=>{
 const model=buildCellulationGeometry('sulfur-32'),native=buildPESymmetricSector(1);
 assert.equal(model.source,'sulfur-32');assert.equal(model.cells.length,51);
 assert.equal(model.cells.filter(c=>c.kind==='tetrahedron').length,32);assert.equal(model.cells.filter(c=>c.kind==='octahedron').length,19);
 for(const [i,c] of model.cells.entries()){assert.deepEqual(c.vertices,native.cells[i].vertices.map(worldPoint));assert.deepEqual(c.faces,native.cells[i].faces.map(f=>f.map(worldPoint)));}
 assert.equal(model.faces.length,native.faces.length);assert.equal(model.faces.filter(f=>f.owners.length===1).length,72);assert(model.faces.some(f=>f.owners.length===2));
 assert.equal(model.faces.reduce((n,f)=>n+f.owners.length,0),32*4+19*8);
});
const key=points=>points.map(p=>p.map(x=>Number(x.toFixed(8))).join(',')).sort().join('|');
test('cellulation reuses all 175 whole cells without particle or flow records',()=>{
 const model=buildCellulationGeometry(),source=buildFoldedFibration().geometry;
 assert.equal(model.cells.length,175);assert.equal(model.cells.filter(c=>c.kind==='tetrahedron').length,119);assert.equal(model.cells.filter(c=>c.kind==='octahedron').length,56);
 for(const [i,c] of model.cells.entries()){
  assert.deepEqual(c.vertices,source[i].vertices.map(worldPoint));assert.deepEqual(c.faces,source[i].faces.map(f=>f.map(worldPoint)));
  assert.deepEqual(Object.keys(c),['id','kind','vertices','faces']);
  const edges=new Map();for(const f of c.faces)for(let j=0;j<3;j++){const e=[f[j],f[(j+1)%3]];edges.set(key(e),e);}
  assert.equal(c.vertices.length,c.kind==='tetrahedron'?4:6);assert.equal(c.faces.length,c.kind==='tetrahedron'?4:8);assert.equal(edges.size,c.kind==='tetrahedron'?6:12);
  const lengths=[...edges.values()].map(([a,b])=>a.reduce((s,x,j)=>s+(x-b[j])**2,0));assert(lengths.every(x=>Math.abs(x-lengths[0])<1e-10));
 }
 assert.equal(new Set(model.faces.map(f=>key(f.vertices))).size,model.faces.length);
 assert.equal(new Set(model.edges.map(e=>key(e.vertices))).size,model.edges.length);
 assert(model.faces.every(f=>f.owners.length===1||f.owners.length===2));assert(model.faces.some(f=>f.owners.length===2));
 assert.equal(model.faces.reduce((sum,f)=>sum+f.owners.length,0),119*4+56*8);
});
