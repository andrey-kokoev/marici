import {test} from 'node:test';
import assert from 'node:assert/strict';
import {cellulationWindow,buildRepeatingCellulation} from '../research/realization-tower/repeating-cellulation.mjs';
test('regular FCC tetrahedra and whole octahedra tile without interior gaps or diagonals',()=>{
 const spec=cellulationWindow(1,[0,0,0],0),m=buildRepeatingCellulation(spec);
 assert.equal(m.source,'repeating-fcc');assert(m.cells.length>51);
 for(const e of m.edges){const [a,b]=e.vertices;assert(Math.abs(Math.hypot(...a.map((x,i)=>x-b[i]))-1)<1e-10);}
 for(const c of m.cells){assert.equal(c.vertices.length,c.kind==='tetrahedron'?4:6);assert.equal(c.faces.length,c.kind==='tetrahedron'?4:8);}
 const interior=m.faces.filter(f=>f.vertices.every(p=>p.every(v=>Math.abs(v)<1.5)));assert(interior.length>0);assert(interior.every(f=>f.owners.length===2));
 const larger=buildRepeatingCellulation({...spec,cellSize:2});assert.deepEqual(larger.cells.map(c=>c.id),m.cells.map(c=>c.id));
 assert.deepEqual(larger.cells[0].vertices,m.cells[0].vertices.map(p=>p.map(x=>x*2)));
 const translated=buildRepeatingCellulation({...spec,origin:[20,-20,10]});assert.equal(translated.cells.length,m.cells.length);
 assert.deepEqual(translated.cells[0].vertices,m.cells[0].vertices.map(p=>p.map((x,i)=>x+[20,-20,10][i]/Math.SQRT2)));
});
test('window follows the camera with a bounded allocation; size inputs are validated',()=>{
 assert.notDeepEqual(cellulationWindow(1,[100,0,0],3).origin,[0,0,0]);assert.equal(cellulationWindow(.5,[0,0,0],1e6).extent,12);
 for(const size of [0,-1,NaN,Infinity,3])assert.throws(()=>cellulationWindow(size));
});
