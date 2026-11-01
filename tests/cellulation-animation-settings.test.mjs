import {test} from 'node:test';
import assert from 'node:assert/strict';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
test('Animate starts off on every load, even if the saved session had it on',()=>{
 for(const saved of [undefined,false,true]){
  const settings=normalizeSceneSettings({appearance:{cellulationStep:7,cellulationAnimate:saved}});
  assert.equal(settings.appearance.cellulationAnimate,false);assert.equal(settings.appearance.cellulationStep,7);
 }
});
