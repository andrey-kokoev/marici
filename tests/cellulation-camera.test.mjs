import {test} from 'node:test';
import assert from 'node:assert/strict';
import * as T from 'three';
import {cellulationResetPose} from '../research/realization-tower/cellulation-camera.mjs';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
test('reset gives an exactly vertical vertex normal and horizontal opposite face',()=>{
 for(const size of [.5,1,2]){
  const pose=cellulationResetPose(1,size),camera=new T.OrthographicCamera(-2,2,2,-2,.01,100);
  camera.up.fromArray(pose.up);camera.position.fromArray(pose.target).add(new T.Vector3(...pose.offset));camera.lookAt(new T.Vector3(...pose.target));camera.updateMatrixWorld();
  const screen=buildCellulationStep(1,size).cells[0].vertices.map(p=>new T.Vector3(...p).project(camera));
  const centroid=screen.reduce((s,p)=>s.add(p),new T.Vector3()).divideScalar(4);
  assert(Math.abs(centroid.x+.44)<1e-12);assert(Math.abs(centroid.y-.44)<1e-12);
  const arrow=buildCellulationStep(3,size).arrows[0],start=new T.Vector3(...arrow.from).project(camera),end=new T.Vector3(...arrow.to).project(camera);
  assert(end.x>start.x);assert(end.y<start.y); // screen-right and downward in the canonical view
  const witness=buildCellulationStep(4,size).witness,loop=[arrow.from,...witness.returnPath].map(p=>new T.Vector3(...p).project(camera));
  for(let i=0;i<2;i++){const a=loop[i+1].clone().sub(loop[i]),b=loop[i+2].clone().sub(loop[i+1]);assert(a.x*b.y-a.y*b.x<0);} // two right turns
  assert.deepEqual(witness.returnPath.at(-1),arrow.from);
  const base=screen.slice(1).reduce((s,p)=>s.add(p),new T.Vector3()).divideScalar(3);
  assert(Math.abs(screen[0].x-base.x)<1e-12);assert(screen[0].y>base.y);
  assert(screen.slice(1).every(p=>Math.abs(p.y-base.y)<1e-12));
  assert(Math.abs(new T.Vector3(...pose.up).dot(new T.Vector3(...pose.offset)))<1e-12);
 }
 for(const frustum of [[-4,4,3,-2],[-2,2,5,-3]]){
  const pose=cellulationResetPose(1,1,frustum),camera=new T.OrthographicCamera(...frustum,.01,100);
  camera.up.fromArray(pose.up);camera.position.fromArray(pose.target).add(new T.Vector3(...pose.offset));camera.lookAt(new T.Vector3(...pose.target));camera.updateMatrixWorld();
  const center=new T.Vector3(...[1,1,1].map(x=>x/(2*Math.SQRT2))).project(camera);
  assert(Math.abs(center.x+.44)<1e-12);assert(Math.abs(center.y-.44)<1e-12);
 }
 assert.deepEqual(cellulationResetPose(0).up,cellulationResetPose(1).up);
 assert.deepEqual(cellulationResetPose(0).target,[0,0,0]);
});
