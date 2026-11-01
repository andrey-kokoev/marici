import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {validateCellulationLoop} from '../research/realization-tower/cellulation-loop-validation.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
import {renderedCellulationArrows} from '../examples/normal-ray/cellulation-loop-validation.js';
const model=buildCellulationStep(20),root=createCellulation(model);root.userData.animate(Infinity,{});
const arrows=renderedCellulationArrows(root),anchors=root.userData.cellulationAnchors;
const report=(m=model,a=arrows,d=anchors)=>validateCellulationLoop(m,a,d);
test('current loop has closed equal sides and valid FCC cells, but two route conflicts and unassigned roles',()=>{
 const r=report();assert.equal(r.segments.length,32);assert(r.sides.every(s=>Math.abs(s.length-8)<1e-9));assert(r.joins.every(j=>j.gap===0&&j.markerIds.length===1));
 assert.equal(r.duplicateCells,0);assert.equal(r.invalidCells,0);assert.equal(r.roles,'unassigned');assert.equal(r.checks.find(c=>c.name==='Arrow geometry').status,'pass');
 assert.deepEqual(r.issues.map(i=>i.type),['reversed-arrow','opposing-arrows']);
 assert(r.issues[0].message.includes('(8,0,8) → (8,1,7)'));assert(r.issues[1].message.includes('(8,7,1) → (8,8,0)'));
 assert.deepEqual(r.joins.map(j=>j.status),['warning','warning','pass','pass']);
});
test('missing arrows, color changes and non-unit rendered arrows are detected',()=>{
 const first=arrows.find(a=>a.from.every(x=>Math.abs(x)<1e-9)&&a.color===0xff3030),same=a=>a.from.every((x,i)=>Math.abs(x-first.from[i])<1e-9)&&a.to.every((x,i)=>Math.abs(x-first.to[i])<1e-9);
 assert(report(model,arrows.filter(a=>!same(a))).issues.some(i=>i.type==='missing-arrow'));
 assert(report(model,arrows.map(a=>same(a)?{...a,color:0xffffff}:a)).issues.some(i=>i.type==='arrow-color'));
 assert(report(model,[...arrows,{from:[0,0,0],to:[.1,0,0],color:0xffffff}]).issues.some(i=>i.type==='invalid-arrow'));
});
test('cell duplicates, off-lattice cells, nonmanifold ownership, join gaps and duplicate dots are detected',()=>{
 assert.equal(report({...model,cells:[...model.cells,model.cells[0]]}).duplicateCells,1);
 const bad={...model.cells[0],vertices:model.cells[0].vertices.map((p,i)=>i===0?p.map(x=>x+.1):p)};
 assert.equal(report({...model,cells:[bad,...model.cells.slice(1)]}).invalidCells,1);
 assert(report({...model,faces:[{...model.faces[0],owners:['a','b','c']},...model.faces.slice(1)]}).issues.some(i=>i.type==='nonmanifold'));
 assert(report({...model,closingWhiteClone:{...model.closingWhiteClone,end:[0,0,.1]}}).issues.some(i=>i.type==='gap'));
 const seed=anchors.find(a=>a.id==='seed');assert(report(model,arrows,[...anchors,{...seed,id:'duplicate'}]).issues.some(i=>i.type==='join-vertex'));
});
test('arrow collection uses live transformed geometry, not just model arrow records',()=>{
 const copy=root.children[1];copy.matrix.elements[12]+=.1;copy.matrixWorldNeedsUpdate=true;
 const r=report(model,renderedCellulationArrows(root));assert(r.issues.some(i=>i.type==='invalid-arrow'));assert(r.issues.some(i=>i.type==='missing-arrow'));
 root.userData.animate(Infinity,{});
});
