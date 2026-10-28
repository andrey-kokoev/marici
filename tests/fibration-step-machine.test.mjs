import test from 'node:test';
import assert from 'node:assert/strict';
import {fibrationDefinition,fibrationRestartStages,fibrationRestartProcess} from '../research/realization-tower/fibration-restart-process.mjs';
import {validateFibrationDefinition,describeFibrationStep,executePairedLayerStep} from '../research/realization-tower/fibration-step-machine.mjs';
test('every surface occurrence has exactly one type-preserving paired occurrence',()=>{
 for(const step of fibrationDefinition.steps.slice(1)){
  const faces=executePairedLayerStep(step,fibrationDefinition.pairings[step.pairing]);
  for(const canonical of faces.filter(f=>f.copy==='clone')){
   const pair=faces.filter(f=>f.canonicalId===canonical.canonicalId);
   assert.equal(pair.length,2);assert.deepEqual(new Set(pair.map(f=>f.copy)),new Set(['original','clone']));
   assert.equal(pair[0].type,pair[1].type);assert.equal(pair[0].role,pair[1].role);
   const original=pair.find(f=>f.copy==='original');
   assert.equal(original.index,canonical.index);
  }
 }
});
test('changing a step once changes both faces and generated summary, without copy-specific data',()=>{
 const definition=structuredClone(fibrationDefinition),step=definition.steps[5];
 step.words[1]='P'+step.words[1].slice(1);
 validateFibrationDefinition(definition);
 const faces=executePairedLayerStep(step,definition.pairings[step.pairing]);
 const pair=faces.filter(f=>f.canonicalId==='layer-5:2:1');
 assert.equal(pair.length,2);assert.ok(pair.every(f=>f.type==='P'&&f.role==='proton'));
 assert.match(describeFibrationStep(step),new RegExp(step.words[1]));
 assert.ok(!Object.hasOwn(step,'originalWords')&&!Object.hasOwn(step,'cloneWords'));
});
test('rendered steps and summaries come from executable definitions',()=>{
 assert.deepEqual(fibrationRestartStages,fibrationDefinition.steps.map(describeFibrationStep));
 const state=fibrationRestartProcess(7,5);
 assert.deepEqual(state.fibrationAudit.layerSteps,fibrationDefinition.steps.slice(1,6));
 assert.deepEqual(state.fibrationAudit.proposedLayers,[5]);
 const invalid=structuredClone(fibrationDefinition);invalid.steps[3].words[0]='NN';
 assert.throws(()=>validateFibrationDefinition(invalid),/word/);
});
