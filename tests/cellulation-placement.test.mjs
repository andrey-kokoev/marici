import {test} from 'node:test';
import assert from 'node:assert/strict';
import * as T from 'three';
import {cellulationStartTranslation} from '../research/realization-tower/cellulation-placement.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
test('placement is exactly eight cell lengths along camera screen-up',()=>{
 for(const q of [new T.Quaternion(),new T.Quaternion().setFromEuler(new T.Euler(.7,-.3,1.2))]){
  const delta=new T.Vector3(...cellulationStartTranslation(q.toArray())),screen=delta.clone().applyQuaternion(q.clone().invert());
  assert(Math.abs(delta.length()-8)<1e-12);assert(Math.abs(screen.x)<1e-12);assert(Math.abs(screen.y-8)<1e-12);assert(Math.abs(screen.z)<1e-12);
 }
 assert.equal(normalizeSceneSettings().appearance.cellulationTranslation,null);
 assert.deepEqual(normalizeSceneSettings({appearance:{cellulationTranslation:[0,8,0]}}).appearance.cellulationTranslation,[0,8,0]);
 assert.equal(normalizeSceneSettings({appearance:{cellulationTranslation:[0,NaN,0]}}).appearance.cellulationTranslation,null);
});
