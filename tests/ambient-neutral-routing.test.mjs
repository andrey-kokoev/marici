import test from 'node:test';import assert from 'node:assert/strict';
import {auditAmbientNeutralRouting,compareRouteTraces} from '../research/strominger/ambient-neutral-routing.mjs';
import {singleOctahedralProcess} from '../research/realization-tower/single-octahedral-process.mjs';
for(const radius of [0,1,2,3])test(`ambient subtraction radius ${radius} preserves every matched trace`,()=>{
 const a=auditAmbientNeutralRouting(radius),n=6*(2*radius+1)**2;assert.equal(a.localChannels,n);assert.equal(a.ambientMatchedChannels,n);assert.equal(a.channelsExtendingAtBothEnds,n);assert.equal(a.addedOrChangedChannels,0);assert.equal(a.removedOrChangedChannels,0);assert.equal(a.referenceOccupiedPECells,0);assert.equal(a.peCouplingDefined,false);assert.equal(a.localizedNeutronCount,null);assert.equal(new Set(a.ambientMatchedPathIds).size,n);
});
test('edge-seven result is stable under enlarging the ambient search window again',()=>{
 const {extraShell:a,...one}=auditAmbientNeutralRouting(3,1),{extraShell:b,...two}=auditAmbientNeutralRouting(3,2);assert.deepEqual(one,two);
});
test('trace comparison detects changes, accepts reversal, rejects silent merging',()=>{
 const p={passIds:['a','b','c']};assert.deepEqual(compareRouteTraces([p],[{passIds:['c','b','a']}]),{unchanged:1,addedOrChanged:0,removedOrChanged:0});assert.deepEqual(compareRouteTraces([p],[{passIds:['a','d','c']}]),{unchanged:0,addedOrChanged:1,removedOrChanged:1});assert.throws(()=>compareRouteTraces([p,p],[p]),/Duplicate/);
});
test('response-only viewer filter hides ambient routes without removing cells or claiming zero neutrons',()=>{
 const p=singleOctahedralProcess(7,3,{nTubeAxis:'response'});assert.equal(p.interfaceGuides.length,0);assert.equal(p.retainedBodies.length,679);assert.equal(p.ambientNeutralAudit.ambientMatchedChannels,294);assert.equal(p.ambientNeutralAudit.localizedNeutronCount,null);assert.equal(p.inventory.rows[0].neutron,231);assert.equal(p.emptyRegionAudit.enclosedRegions,85);
});
