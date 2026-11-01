import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {buildCellulationNeighborhood,cellulationIncidentEdges} from '../research/realization-tower/cellulation-neighborhood.mjs';
const key=c=>c.vertices.map(p=>p.map(x=>Math.round(x*Math.SQRT2)).join(',')).sort().join('|');
test('two layers mean exactly two whole-cell face-adjacency hops',()=>{
 const seed=buildCellulationStep(1).cells;
 const zero=buildCellulationNeighborhood(seed,0),one=buildCellulationNeighborhood(seed,1),two=buildCellulationNeighborhood(seed,2);
 assert.equal(zero.cells.length,1);assert.equal(one.cells.length,5);assert.equal(two.cells.length,27);
 const expected=buildCellulationNeighborhood(one.cells,1);assert.deepEqual(new Set(two.cells.map(key)),new Set(expected.cells.map(key)));
 assert.equal(new Set(two.cells.map(key)).size,two.cells.length);assert(two.cells.every(c=>c.faces.length===(c.kind==='tetrahedron'?4:8)));
 for(const {vertices:[a,b]} of two.edges)assert(Math.abs(Math.hypot(...a.map((x,i)=>x-b[i]))-1)<1e-12);
 const larger=buildCellulationNeighborhood(two.cells,1);assert(larger.cells.some(c=>!new Set(two.cells.map(key)).has(key(c))));
});
test('hover selection returns only existing unit grid edges incident to the dot',()=>{
 const grid=buildCellulationNeighborhood(buildCellulationStep(2).cells),point=[0,0,0];
 const edges=cellulationIncidentEdges(grid.edges,point);assert.equal(edges.length,12);
 for(const e of edges){assert(grid.edges.includes(e));assert(e.vertices.some(p=>p.every(x=>x===0)));}
 assert.deepEqual(cellulationIncidentEdges(grid.edges,[100,100,100]),[]);
});
test('the completed chain needs only 169 background cells, independent of viewport size',()=>{
 const placed=buildCellulationStep(10).cells,result=buildCellulationNeighborhood(placed);
 assert.equal(result.layers,2);assert.equal(result.placedCells,15);assert.equal(result.cells.length,169);
 const keys=new Set(result.cells.map(key));for(const c of placed)assert(keys.has(key(c)));
});
