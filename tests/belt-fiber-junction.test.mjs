import test from 'node:test';import assert from 'node:assert/strict';
import {splitFiberJunction,joinFiberJunction,advanceFiberJunction,fiberJunctionNorm} from '../research/realization-tower/belt-fiber-junction.mjs';
import {buildBeltLayers} from '../research/realization-tower/belt-layer-model.mjs';
const near=(a,b,tolerance=1e-10)=>{assert.equal(a.flat().length,b.flat().length);a.flat().forEach((v,i)=>assert.ok(Math.abs(v-b.flat()[i])<tolerance));};
test('all full-fiber components survive the orthonormal junction and inverse',()=>{
 for(const inputs of [[[1],[0],[0]],[[1,2,-3],[4,-5,6],[-7,8,9]],[[2,3],[2,3],[2,3]]]){
  const snapshot=JSON.stringify(inputs),state=splitFiberJunction(inputs);near(joinFiberJunction(state),inputs);assert.ok(Math.abs(fiberJunctionNorm(state)-inputs.flat().reduce((s,x)=>s+x*x,0))<1e-10);assert.equal(JSON.stringify(inputs),snapshot);
  near(joinFiberJunction(advanceFiberJunction(advanceFiberJunction(state),-2*Math.PI/3)),inputs);
 }
 assert.throws(()=>splitFiberJunction([[1],[2,3],[4]]));assert.throws(()=>splitFiberJunction([[NaN],[1],[2]]));
});
test('common mode stays fixed and differences remain bounded, without decay',()=>{
 let state=splitFiberJunction([[1,2],[3,5],[-2,8]]),initial=structuredClone(state),norm=fiberJunctionNorm(state),contrastNorm=state.contrasts.flat().reduce((s,x)=>s+x*x,0);
 for(let i=0;i<3000;i++){state=advanceFiberJunction(state);near([state.common],[initial.common]);assert.ok(Math.abs(fiberJunctionNorm(state)-norm)<1e-8);assert.ok(Math.abs(state.contrasts.flat().reduce((s,x)=>s+x*x,0)-contrastNorm)<1e-8);}
 near(joinFiberJunction(state),joinFiberJunction(initial),1e-8);
});
test('120-degree contrast rotation is precisely cyclic routing in the original fiber basis',()=>{
 const inputs=[[1,2],[3,4],[5,6]],state=splitFiberJunction(inputs);
 near(joinFiberJunction(advanceFiberJunction(state)),[inputs[2],inputs[0],inputs[1]]);
 near(joinFiberJunction(advanceFiberJunction(advanceFiberJunction(advanceFiberJunction(state)))),inputs);
 const loss=splitFiberJunction([[1],[-1],[0]]);near([loss.common],[[0]]);assert.ok(fiberJunctionNorm(loss)>0,'common-mode-only projection would erase a nonzero state');
});
test('trial is attached to all six central three-input junctions without changing wiring',()=>{
 const m=buildBeltLayers({origin:[0,0,0],x:[1,0,0],y:[0,1,0],normal:[0,0,1]});assert.equal(m.links.length,74);assert.equal(m.fiberJunctions.length,6);
 for(const j of m.fiberJunctions){assert.equal(j.inputs.length,3);assert.equal(new Set(j.inputs).size,3);assert.equal(j.status,'trial');assert.equal(j.retainedModes.length,3);for(const from of j.inputs)assert.ok(m.links.some(e=>e.from===from&&e.to===j.target));}
});
