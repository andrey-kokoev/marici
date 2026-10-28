import test from 'node:test';
import assert from 'node:assert/strict';
import {fibrationRestartProcess} from '../research/realization-tower/fibration-restart-process.mjs';
import {cells} from '../research/realization-tower/normal-ray-model.mjs';
import {processState} from '../research/realization-tower/normal-ray-processes.mjs';
test('legacy word fixture retains native corner cells at five vertices' ,()=>{
 const p=fibrationRestartProcess(7,0);
 assert.equal(processState('fibration-12x12',7,0).fibrationAudit.generated,true);
 assert.equal(p.fibrationAudit.vertexLabels,undefined);
 assert.equal(p.retainedBodies.length,8);assert.equal(p.presentationPoints,undefined);
 assert.equal(p.interfaceGuides.length,0);assert.equal(p.canAdvance,true);
 assert.deepEqual(p.fibrationAudit.vertexBindings.map(b=>b.text),['+P','−P','+N','E','−N']);
 assert.equal(new Set(p.retainedBodies.map(b=>b.id)).size,8);
 for(const b of p.retainedBodies){
  const vertices=b.components[0];assert.equal(vertices.length,4);
  // Cells are transported without changing any edge length.
  const original=cells.find(c=>c.id===b.sourceCell).vertices;
  const d2=(vs,i,j)=>vs[i].reduce((s,x,k)=>s+(x-vs[j][k])**2,0);
  for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)assert.ok(Math.abs(d2(vertices,i,j)-d2(original,i,j))<1e-9);
 }
 assert.throws(()=>fibrationRestartProcess(7,7));
});
test('Layer 1 colors nine outer triangles on six native cells in perimeter order',()=>{
 const p=fibrationRestartProcess(7,1),a=p.fibrationAudit.surfaceAssignments.filter(f=>f.copy==='clone');
 assert.equal(a.length,9);assert.equal(new Set(a.map(f=>f.sourceCell)).size,6);
 assert.equal(a.map(f=>f.type).join(''),'NPNNPEEPN');
 assert.equal(p.retainedBodies.length,20);assert.equal(p.canAdvance,true);
 assert.equal(p.fibrationAudit.mixedCells.length,0);
 assert.equal(a[0].sourceCell,a[8].sourceCell);
 assert.equal(a[0].type,a[8].type);
 assert.equal(a[5].sourceCell,a[6].sourceCell);
 assert.equal(a[5].type,a[6].type);
 assert.equal(a[6].type,'E');
 assert.equal(a[8].type,'N');
 for(const f of a){const body=p.retainedBodies.find(b=>b.sourceCell===f.sourceCell&&b.copy==='clone');assert.ok(f.vertices.every(v=>body.components[0].some(w=>v.every((x,i)=>Math.abs(x-w[i])<1e-9))));}
 for(let run=0;run<3;run++)for(let i=0;i<2;i++){
  const a0=a[run*3+i].vertices,a1=a[run*3+i+1].vertices;
  assert.equal(a0.filter(v=>a1.some(w=>v.every((x,j)=>Math.abs(x-w[j])<1e-9))).length,2);
 }
});
