import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
import {renderedCellulationWitnessInput} from '../examples/normal-ray/cellulation-loop-validation.js';
import {auditShellCellOrders,auditShellFaceOrders,advanceShellWitnessState,shellSemanticOutcome,compareShellOutcomes} from '../research/realization-tower/cellulation-shell-confluence.mjs';
import {buildShellWitnessPlan} from '../research/realization-tower/cellulation-shell-witness.mjs';
const model=buildCellulationStep(23),previous=createCellulation(model.previous);previous.userData.animate(Infinity,{});
const input=renderedCellulationWitnessInput(previous);

test('a legal adjacent cell swap changes dot 422 from red to white, with a different normal',()=>{
 const report=auditShellCellOrders(model,input,{randomTrials:4});assert.equal(report.status,'order-dependent');assert.equal(report.incompleteSchedules,0);
 const witness=report.adjacentWitness;assert(witness);assert.deepEqual(witness.cells,['shell:t:3,1,2','shell:t:3,2,1']);assert.deepEqual(witness.prefix,['shell:t:2,1,1']);
 assert.deepEqual(witness.firstDifference,{field:'dots.colour',key:'4,2,2',left:0xff3030,right:0xffffff});
 assert(witness.differences.some(d=>d.field==='dots.normal'));assert.equal(report.octahedralArrivalOrders.tested,24);assert.equal(report.octahedralArrivalOrders.conflicting,0);
 const byId=new Map(model.shellFace.newCells.map(c=>[c.id,c]));
 const left=createCellulation(model),right=createCellulation({...model,shellFace:{...model.shellFace,newCells:witness.rightOrder.map(id=>byId.get(id))}});
 for(const g of [left,right])g.userData.animate(Infinity,{});
 assert.deepEqual(right.userData.witnessPlan.cells.map(c=>c.cell.id),witness.rightOrder);
 const dot=g=>g.children.find(o=>o.userData.witnessDotId==='shell:4,2,2'&&o.geometry.type==='SphereGeometry');
 assert.equal(dot(left).material.color.getHex(),0xff3030);assert.equal(dot(right).material.color.getHex(),0xffffff);
 const anchor=g=>g.userData.cellulationAnchors.find(a=>a.id==='shell:4,2,2');assert.notDeepEqual(anchor(left).normal,anchor(right).normal);assert.deepEqual(anchor(left).point,anchor(right).point);
});
test('all macro-face orders complete, but changing face order can change directed arrows without changing geometry',()=>{
 const report=auditShellFaceOrders(model.previous,input);assert.equal(report.completed,24);assert.deepEqual(report.incomplete,[]);assert.equal(report.status,'order-dependent');
 assert(report.differingTrialsByField.arrows>0);assert(report.differingTrialsByField['dots.colour']>0);
 for(const field of ['cells','faces','faceOwnership','dots.id'])assert.equal(report.differingTrialsByField[field]??0,0);
 assert.deepEqual(report.examples[0].order,[0,2,1,3]);
});
test('semantic comparison ignores serialization order but detects arrow, face and ownership changes',()=>{
 const plan=buildShellWitnessPlan(model,input),state=advanceShellWitnessState(input,plan),a=shellSemanticOutcome(state);
 const b=shellSemanticOutcome({...state,arrows:[...state.arrows].reverse(),anchors:[...state.anchors].reverse(),faces:[...state.faces].reverse(),cells:[...state.cells].reverse()});assert.deepEqual(compareShellOutcomes(a,b),[]);
 const changed=structuredClone(a);changed.arrows.pop();changed.faces[0][1].colour=0x123456;changed.faceOwnership[0][1]=['wrong-owner'];
 const differences=compareShellOutcomes(a,changed);for(const field of ['arrows','faces','faceOwnership'])assert(differences.some(d=>d.field===field));
 assert.throws(()=>buildShellWitnessPlan(model,input,{octahedronOrder:[0,0,2,3]}));
});
test('pure final-state projection agrees with rendered dot colors/normals and directed arrows',()=>{
 const root=createCellulation(model);root.userData.animate(Infinity,{});
 const predicted=shellSemanticOutcome(advanceShellWitnessState(input,root.userData.witnessPlan)),actual=shellSemanticOutcome(renderedCellulationWitnessInput(root));
 for(const field of ['arrows','dots','cells','faceOwnership'])assert.deepEqual(actual[field],predicted[field]);
});
