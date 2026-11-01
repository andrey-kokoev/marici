import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {completionTiming} from '../research/realization-tower/cellulation-completion.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
const key=points=>points.map(p=>p.join(',')).sort().join('|');
test('step 6 adds the missing white edge and exactly the other two faces',()=>{
 const model=buildCellulationStep(6),previous=buildCellulationStep(5),{arrow,faces}=model.completion;
 assert.deepEqual(model.cells,previous.cells);assert.deepEqual(arrow.from,model.witness.priorTurnMarkers[0].point);assert.deepEqual(arrow.to,model.witness.turnMarker.point);assert.equal(arrow.colour,0xffffff);
 assert.equal(faces.length,2);const red=model.witness.faces;assert(faces.every(f=>!red.some(g=>key(f)===key(g))));assert.deepEqual([...faces,...red].map(key).sort(),model.cells[0].faces.map(key).sort());
 const oldEdges=[...model.arrows.map(a=>[a.from,a.to]),...model.witness.returnPath.slice(0,-1).map((p,i)=>[p,model.witness.returnPath[i+1]])];
 assert(!oldEdges.some(e=>key(e)===key([arrow.from,arrow.to])));assert.equal(new Set([...oldEdges,[arrow.from,arrow.to]].map(key)).size,6);
});
test('arrow first, then red candidates fill, then white faces; Replay restores the candidates',()=>{
 const {hold,edge,vertices,total}=completionTiming,group=createCellulation(buildCellulationStep(6)),animate=group.userData.animate,audit=group.userData.audit.animation;
 for(const time of [0,hold,hold+edge-1]){animate(time,{});assert.equal(audit.redFaceCount,2);assert.equal(audit.whiteFaceCount,0);assert(audit.turnMarkers.every(m=>m.outlineVisible&&!m.solidVisible));}
 animate(hold+edge+vertices/2,{});assert(audit.turnMarkers.every(m=>m.fillProgress===.5));assert.equal(audit.whiteFaceCount,0);assert.equal(audit.arrowProgress,1);
 animate(hold+edge+vertices,{});assert(audit.turnMarkers.every(m=>m.fillProgress===1&&!m.outlineVisible));assert.equal(audit.whiteFaceCount,0);
 assert.equal(animate(total,{faceOpacity:.4}),false);assert.equal(audit.redFaceCount,2);assert.equal(audit.whiteFaceCount,2);assert(Math.abs(audit.whiteFaceOpacity-.22)<1e-12);
 animate(total,{edgesOnly:true});assert.equal(audit.whiteFaceCount,0);assert.equal(audit.redFaceCount,0);
 animate(0,{});assert.equal(audit.redFaceCount,2);assert.equal(audit.whiteFaceCount,0);assert.equal(audit.arrowProgress,0);assert(audit.turnMarkers.every(m=>m.outlineVisible&&!m.solidVisible));
 group.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});
});
