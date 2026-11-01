import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep,cellulationSteps} from '../research/realization-tower/cellulation-steps.mjs';
import {buildRepeatingCellulation,cellulationWindow} from '../research/realization-tower/repeating-cellulation.mjs';
test('step 1 is exactly one regular unit tetrahedron already belonging to the lattice',()=>{
 assert.equal(cellulationSteps.length,26);
 const model=buildCellulationStep();assert.equal(model.step,1);assert.equal(model.cells.length,1);assert.equal(model.cells[0].vertices.length,4);assert.equal(model.faces.length,4);assert.equal(model.edges.length,6);assert.equal(model.fade,undefined);
 for(const {vertices:[a,b]} of model.edges)assert(Math.abs(Math.hypot(...a.map((x,i)=>x-b[i]))-1)<1e-12);
 const lattice=buildRepeatingCellulation(cellulationWindow(1,[0,0,0],0));assert.deepEqual(model.cells[0],lattice.cells.find(c=>c.id==='t:0,0,0'));
 const scaled=buildCellulationStep(1,2);assert.deepEqual(scaled.cells[0].vertices,model.cells[0].vertices.map(p=>p.map(x=>x*2)));
 assert.equal(model.markedVertex,null);
 const second=buildCellulationStep(2);assert.deepEqual(second.cells,model.cells);assert.deepEqual(second.faces,model.faces);assert.deepEqual(second.markedVertex,model.cells[0].vertices[0]);
 const third=buildCellulationStep(3);assert.deepEqual(third.cells,model.cells);assert.deepEqual(third.markedVertex,second.markedVertex);assert.equal(third.arrows.length,1);assert.deepEqual(third.arrows[0],{from:model.cells[0].vertices[0],to:model.cells[0].vertices[2],colour:0xff3030});assert.deepEqual(second.arrows,[]);
 const fourth=buildCellulationStep(4);assert.deepEqual(fourth.cells,model.cells);assert.deepEqual(fourth.witness.proposedVertex,third.arrows[0].to);assert.deepEqual(fourth.witness.returnPath,[model.cells[0].vertices[2],model.cells[0].vertices[1],model.cells[0].vertices[0]]);
 assert.deepEqual(fourth.witness.faces,[]);
 const fifth=buildCellulationStep(5);assert.deepEqual(fifth.cells,model.cells);assert.deepEqual(fifth.witness.returnPath,[model.cells[0].vertices[0],model.cells[0].vertices[3],model.cells[0].vertices[2]]);
 assert.throws(()=>buildCellulationStep(27));assert.throws(()=>buildCellulationStep(1,NaN));
});
