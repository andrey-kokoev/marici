import test from 'node:test';
import assert from 'node:assert/strict';
import {processes,processState} from '../research/realization-tower/normal-ray-processes.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
test('pair contexts are an isolated 28-position process',()=>{
 assert.ok(processes.some(p=>p.id==='pair-context-7x4'));
 const old=processState('fibration-12x12',7,0);
 for(let i=0;i<28;i++){
  const s=processState('pair-context-7x4',7,i);
  assert.equal(s.pairContextAudit.position,i+1);assert.equal(s.pairContextAudit.depth,Math.floor(i/7)+1);
  assert.equal(s.canAdvance,i<27);assert.equal(s.history.length,i+1);
  assert.deepEqual(Object.keys(s.pairContextAudit.bank),['aa','ab','ba','bb']);
  assert.equal(s.pairContextAudit.confirmation,'confirmed');assert.equal(s.pairContextAudit.actionHistory.length,2*(Math.floor(i/7)+1));
  assert.equal(s.assignments.length,0);assert.ok(s.retainedBodies.length>=3);
 }
 assert.deepEqual(processState('fibration-12x12',7,0),old);
 assert.throws(()=>processState('pair-context-7x4',7,28));
});
test('saved progress retains the new process independently and clamps its depth',()=>{
 const s=normalizeSceneSettings({process:{id:'pair-context-7x4',k:2,step:99,progress:{'fibration-12x12':{k:7,step:2}}}});
 assert.equal(s.process.k,7);assert.equal(s.process.step,27);assert.equal(s.process.progress['fibration-12x12'].step,2);
});
