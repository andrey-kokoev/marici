import {test} from 'node:test';
import assert from 'node:assert/strict';
import {Quaternion,Vector3} from 'three';
import {orientationCompass} from '../examples/normal-ray/orientation-compass.js';
test('compass projects six signed directions and three coordinate planes into camera space',()=>{
 const c=orientationCompass();assert.equal(c.directions.length,6);assert.deepEqual(c.planes.map(p=>p.name).sort(),['XY','XZ','YZ']);
 const x=c.directions.find(d=>d.key==='+X'),y=c.directions.find(d=>d.key==='+Y');assert.equal(x.x,118);assert.equal(x.y,70);assert.equal(y.y,28);
 assert.notEqual(c.directions.find(d=>d.key==='+Z').labelX,c.directions.find(d=>d.key==='−Z').labelX);
 const q=new Quaternion().setFromAxisAngle(new Vector3(0,0,1),Math.PI/2),rotated=orientationCompass(q.toArray()),rx=rotated.directions.find(d=>d.key==='+X');
 assert(Math.abs(rx.x-76)<1e-10);assert(Math.abs(rx.y-112)<1e-10);assert.notEqual(rotated.planes.find(p=>p.name==='XY').points,c.planes.find(p=>p.name==='XY').points);
});
