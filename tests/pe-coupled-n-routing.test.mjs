import test from 'node:test';import assert from 'node:assert/strict';
import {probePECoupledNRouting} from '../research/strominger/pe-coupled-n-routing.mjs';
import {singleOctahedralProcess} from '../research/realization-tower/single-octahedral-process.mjs';
for(const [r,changed,pairs]of [[0,0,0],[1,36,18],[2,120,60],[3,252,126]])test(`P/E-coupled routing radius ${r}: reversible, dual, no merging`,()=>{
 const p=probePECoupledNRouting(r),a=p.audit;assert.equal(a.changedOpenChannels,changed);assert.equal(a.reroutedBoundaryPairs,changed);assert.equal(a.dualResponsePairs,pairs);assert.equal(a.selfDualResponses,0);assert.equal(a.closedLoops,0);assert.equal(a.branchingJunctions,0);assert.equal(a.dualityVerified,true);assert.equal(a.localizedNeutronCount,null);assert.equal(a.positiveSwitches,a.negativeSwitches);assert.equal(a.openChannels,a.ambientOpenChannels);
 for(const m of p.localRouting.values()){assert.equal(m.size,12);for(const[x,y]of m){assert.notEqual(x,y);assert.equal(m.get(y),x);}}
 const passes=p.paths.flatMap(path=>path.passes.map(p=>p.id));assert.equal(passes.length,a.localPasses);assert.equal(new Set(passes).size,passes.length);assert.equal(new Set(p.paths.flatMap(path=>[path.fromPort,path.toPort])).size,2*a.openChannels);assert.equal(new Set(p.dualPairs.flat()).size,changed);
});
test('response survives a larger ambient boundary and vanishes when P/E occupancy is removed',()=>{
 const a=probePECoupledNRouting(3).audit,b=probePECoupledNRouting(3,3).audit,off=probePECoupledNRouting(3,2,{occupied:false}).audit;
 for(const k of['coupledNCells','positiveSwitches','negativeSwitches','changedOpenChannels','reroutedBoundaryPairs','closedLoops','dualResponsePairs'])assert.equal(a[k],b[k]);assert.equal(off.coupledNCells,0);assert.equal(off.changedOpenChannels,0);assert.equal(off.dualResponsePairs,0);assert.equal(off.closedLoops,0);
});
test('viewer exposes actual response polylines while preserving cell and void counts',()=>{
 const p=singleOctahedralProcess(7,3,{nTubeAxis:'coupled'});assert.equal(p.interfaceGuides.length,252);assert.ok(p.interfaceGuides.some(g=>g.points.length>2));assert.equal(p.retainedBodies.length,679);assert.equal(p.emptyRegionAudit.enclosedRegions,85);assert.equal(p.peCoupledRoutingAudit.dualResponsePairs,126);assert.equal(p.peCoupledRoutingAudit.localizedNeutronCount,null);
});
