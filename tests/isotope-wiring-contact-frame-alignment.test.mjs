import test from 'node:test';
import assert from 'node:assert/strict';
import {solveContactFrameAlignment} from '../examples/isotope-wiring/core/contact-frame-alignment.mjs';
const axis=[0,0,1],reference=[1,0,0],source={axis,reference},I=[[1,0,0],[0,1,0],[0,0,1]];
const apply=(m,v)=>m.map(row=>row.reduce((sum,x,i)=>sum+x*v[i],0));
const close=(a,b)=>a.every((x,i)=>Math.abs(x-b[i])<1e-9);
test('point contact does not select a rotation and axis alignment retains twist freedom',()=>{
 assert.equal(solveContactFrameAlignment().status,'unknown');const r=solveContactFrameAlignment({source:{axis},target:{axis}});assert.equal(r.status,'underdetermined');assert.match(r.freedom,/SO\(2\)/);assert.equal(r.rotation,undefined);assert.equal(solveContactFrameAlignment({source,target:{axis}}).status,'underdetermined');
});
test('identical axes allow distinct rotations when transverse references differ',()=>{
 const aligned=solveContactFrameAlignment({source,target:source}),twisted=solveContactFrameAlignment({source,target:{axis,reference:[0,1,0]}});assert.equal(aligned.status,'verified');assert.equal(twisted.status,'verified');assert.deepEqual(aligned.rotation,I);assert.notDeepEqual(aligned.rotation,twisted.rotation);assert.deepEqual(apply(twisted.rotation,axis),axis);assert.deepEqual(apply(twisted.rotation,reference),[0,1,0]);
});
test('general oriented frames map all axes, not just their normal',()=>{
 const r=solveContactFrameAlignment({source:{axis:[1,2,3],reference:[2,-1,4]},target:{axis:[-2,3,1],reference:[4,1,-2]}});assert.equal(r.status,'verified');for(let i=0;i<3;i++){const a=r.source.frame.map(row=>row[i]),b=r.target.frame.map(row=>row[i]);assert(close(apply(r.rotation,a),b));assert(close(apply(r.reverseRotation,b),a));}
});
test('normalization and transverse projection do not infer extra constraints',()=>{
 const r=solveContactFrameAlignment({source:{axis:[0,0,1e200],reference:[1e200,0,1e200]},target:source});assert.equal(r.status,'verified');assert.deepEqual(r.rotation,I);
});
test('invalid or degenerate frames fail rather than silently supplying a roll reference',()=>{
 for(const bad of [{axis:[0,0,0],reference},{axis,reference:[0,0,2]},{axis,reference:[0,0,0]},{axis:[NaN,0,1],reference},{axis:[0,1],reference}])assert.equal(solveContactFrameAlignment({source:bad,target:source}).status,'refuted');assert.throws(()=>solveContactFrameAlignment({tolerance:0}),/Tolerance/);
});
