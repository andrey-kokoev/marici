import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {whiteRepeatAt,whiteRepeatDuration} from '../research/realization-tower/cellulation-white-repeat.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
const key=c=>c.vertices.map(p=>p.map(x=>Math.round(x*Math.SQRT2)).join(',')).sort().join('|');
test('five translated 12–17 blocks reuse the completed join and advance to (8,8,0)',()=>{
 const m=buildCellulationStep(18);assert.equal(m.whiteRepeats.length,5);assert.equal(m.cells.length,22);assert.equal(new Set(m.cells.map(key)).size,22);assert.deepEqual(m.cells.slice(0,17),m.previous.cells);
 const original12=buildCellulationStep(12).cells.at(-1);
 for(const [i,c] of m.whiteRepeats.entries()){
  assert.deepEqual(c.delta,[0,i+1,-i-1]);assert.deepEqual(c.stages.map(s=>s.step),[13,14,15,16,17]);
  const boundary={vertices:original12.vertices.map(p=>p.map((x,j)=>x+c.delta[j]/Math.SQRT2))};
  assert.equal(key(boundary),key(i===0?m.previous.cells.at(-1):m.whiteRepeats[i-1].stages.at(-1).cells[0]));
  assert.deepEqual(c.stages[0].directedArrow.euler,[-45,45,90]);assert.equal(c.stages.at(-1).solidClosure.faces.length,4);
 }
 assert.deepEqual(m.whiteRepeats.at(-1).stages[0].directedArrow.toLattice,[8,8,0]);assert.equal(whiteRepeatDuration,11600);
});
test('sequential playback keeps prior work, uniquely identified dots, and completed rectangles filled',()=>{
 const g=createCellulation(buildCellulationStep(18)),priorIds=g.children[0].userData.cellulationAnchors.map(a=>a.id);
 for(const elapsed of [0,500,1000,3650,6300,9600,11600,23200,Infinity]){
  g.userData.animate(elapsed,{});const f=whiteRepeatAt(elapsed),a=g.userData.audit.animation;assert.equal(a.completed,f.completed);assert.equal(a.step,f.step);
  assert.equal(g.children[0].userData.audit.animation.whiteRectangleCount,1);
  const ids=g.userData.cellulationAnchors.map(a=>a.id);assert.equal(new Set(ids).size,ids.length);for(const id of priorIds)assert(ids.includes(id));
  assert.equal(new Set(g.userData.cellulationCells.map(key)).size,g.userData.cellulationCells.length);
 }
 assert.equal(g.userData.cellulationCells.length,22);assert.equal(g.userData.cellulationAnchors.length,priorIds.length+15);assert.equal(g.userData.audit.animation.completed,5);
 assert.equal(g.userData.audit.animation.current.animation.filledDotCount,3);assert.equal(g.userData.audit.animation.current.animation.whiteRectangleCount,1);
 assert(g.userData.cellulationAnchors.some(a=>a.point.map(x=>Math.round(x*Math.SQRT2)).join(',')==='8,8,0'));
 g.userData.animate(0,{});assert.equal(g.userData.cellulationCells.length,17);assert.deepEqual(g.userData.cellulationAnchors.map(a=>a.id),priorIds);
});
