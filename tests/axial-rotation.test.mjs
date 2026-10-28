import test from 'node:test';import assert from 'node:assert/strict';import {Quaternion,Vector3} from 'three';
import {protonRotationLine,locksAllowAxialRotation} from '../examples/normal-ray/axial-rotation.js';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
test('axial rotation fixes both proton endpoints in glued and separated views',()=>{
 for(const separated of [false,true]){const line=protonRotationLine(separated),q=new Quaternion().setFromAxisAngle(line.axis,.7);assert.ok(Math.abs(line.axis.length()-1)<1e-12);assert.ok(line.plus.clone().sub(line.minus).dot(line.axis)>0);
  for(const p of [line.minus,line.plus])assert.ok(p.clone().sub(line.pivot).applyQuaternion(q).add(line.pivot).distanceTo(p)<1e-10);
  assert.ok(locksAllowAxialRotation(line,[line.minus,line.plus]));const off=new Vector3(1,0,0);if(Math.abs(off.dot(line.axis))>.9)off.set(0,1,0);assert.equal(locksAllowAxialRotation(line,[line.pivot.clone().add(off)]),false);
 }
});
test('axial preference normalizes and persists alongside existing spin settings',()=>{
 assert.equal(normalizeSceneSettings({}).motion.axialRotation,false);const saved=normalizeSceneSettings({motion:{spin:true,axialRotation:true,speed:-2}});assert.deepEqual(saved.motion,{spin:true,axialRotation:true,speed:-2});assert.deepEqual(normalizeSceneSettings(JSON.parse(JSON.stringify(saved))).motion,saved.motion);
});
