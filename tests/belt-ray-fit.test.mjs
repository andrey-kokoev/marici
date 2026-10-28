import test from 'node:test';import assert from 'node:assert/strict';
import {presentCentralBelt,centralParentPoint} from '../research/realization-tower/central-belt-layout.mjs';
import {doubleEsd7RuleProcess} from '../research/realization-tower/double-esd7-process.mjs';
import {filterBeltView} from '../examples/normal-ray/complex-visibility.js';
import {worldPoint} from '../research/realization-tower/normal-ray-model.mjs';
import {fitBeltInsideRays} from '../research/realization-tower/belt-ray-fit.mjs';
test('two-unit separation cannot enclose the belt under rotation; sqrt(6) separation admits its original pose',()=>{
 const source=presentCentralBelt(doubleEsd7RuleProcess(7,[])),p=filterBeltView(source,'geometry'),origin=worldPoint(p.centralBeltAudit.origin),axis=p.centralBeltAudit.normal,unit=p.beltSurface.cellulation.unitEdge,rays=source.parentCutAudit.caps.flatMap(cap=>cap.cutFace.map(v=>{const sign=cap.copy==='original'?1:-1,tip=origin.map((v,i)=>v+sign*2*unit*axis[i]),start=worldPoint(centralParentPoint(v,cap.copy)).map((v,i)=>v+sign*2*unit*axis[i]);return {copy:cap.copy,points:[start,start.map((v,i)=>v+5*(tip[i]-v))]};}));
 const snapshot=JSON.stringify(p),fit=fitBeltInsideRays(source.beltSurface,rays,origin,axis);
 assert.equal(fit.status,'rotation-obstructed');assert.ok(Math.abs(fit.rotationObstruction.beltInradius/unit-Math.sqrt(2/3))<1e-12);assert.ok(Math.abs(fit.rotationObstruction.enclosureClearance/unit-2/3)<1e-12);
 const shifted=rays.map(r=>({...r,points:r.points.map(p=>p.map((v,i)=>v+(r.copy==='original'?1:-1)*(Math.sqrt(6)-2)*unit*axis[i]))}));
 const possible=fitBeltInsideRays(source.beltSurface,shifted,origin,axis);assert.equal(possible.status,'fits');assert.equal(possible.degrees,0);assert.ok(possible.initialClearance>=-1e-12);assert.equal(JSON.stringify(p),snapshot);
});
