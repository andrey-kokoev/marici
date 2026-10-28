import test from 'node:test';import assert from 'node:assert/strict';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
test('nine native belt planes persist separately from legacy six port layers',()=>{
 const legacy=normalizeSceneSettings({appearance:{beltLayers:Array(6).fill(false)}});assert.deepEqual(legacy.appearance.nativeBeltLayers,Array(9).fill(true));
 const mask=[false,true,false,true,true,false,true,true,false],saved=normalizeSceneSettings({appearance:{nativeBeltLayers:mask}});assert.deepEqual(saved.appearance.nativeBeltLayers,mask);assert.deepEqual(normalizeSceneSettings(JSON.parse(JSON.stringify(saved))).appearance.nativeBeltLayers,mask);
});
