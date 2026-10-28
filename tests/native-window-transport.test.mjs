import test from 'node:test';import assert from 'node:assert/strict';import fs from 'node:fs';
import {decodeChannel,encodeFixture} from '../research/strominger/checkers/native_retained_channel.mjs';
import {retainNativeWindow,restoreNativeWindow,transportNativeWindow,auditNativeWindowTransport} from '../research/strominger/native-window-transport.mjs';
const f=decodeChannel(encodeFixture(JSON.parse(fs.readFileSync(new URL('../research/strominger/results/joint-field-sewing-fixture.json',import.meta.url),'utf8'))));
const value=[[1,2],[3,-4],[5,6],[-7,8],[9,-10]];
test('three active values plus two retained complementary values recover every actual packet',()=>{
 for(const p of f.packets){const view=retainNativeWindow(f,p.id,value);assert.equal(view.active.length,3);assert.equal(view.complement.length,2);assert.deepEqual(restoreNativeWindow(f,view),value);assert.equal(view.fullFieldReference.dimension,44);assert.equal(view.fullFieldReference.framePacket,p.id);}
});
test('all 18 existing native interfaces commute with retained-window recovery on the whole five-slot basis',()=>{
 const audit=auditNativeWindowTransport(f);assert.equal(audit.status,'retained-window-transport-passed');assert.equal(audit.composition.status,'verified-conditionally');assert.deepEqual(audit.counts,{interfaces:18,probesPerInterface:6,activeProjectionFailures:6,fourCoefficientProjectionFailures:10,geometricContextWithoutCoefficientSlot:2});
 for(const e of audit.edges)assert.ok(e.transportedCases.every(c=>Object.values(c).every(Boolean)));
});
test('projection failures have explicit equal-source-view/different-target-view witnesses',()=>{
 const audit=auditNativeWindowTransport(f);
 for(const edge of audit.edges)for(const projection of [edge.activeProjection,edge.fourGeometricMarkProjection])if(projection.closed===false){assert.equal(projection.witness.sourceProjectionEqual,true);assert.notDeepEqual(projection.witness.targetProjectionA,projection.witness.targetProjectionB);}
 const pn=audit.edges.find(e=>e.kind==='PN');assert.deepEqual(pn.fourGeometricMarkProjection.requiredComplementSlots,[4]);const inverse=audit.edges.find(e=>e.kind==='inverse-PN');assert.deepEqual(inverse.fourGeometricMarkProjection.requiredComplementSlots,[0]);
 for(const edge of audit.edges.filter(e=>e.kind==='NE'))assert.deepEqual(edge.fourGeometricMarkProjection.unboundGeometricMarks,['M2']);
});
test('window transport refuses erased complement, forged context, wrong source and lost full-field reference',()=>{
 const op=f.operations[0],good=retainNativeWindow(f,op.source,value);
 const erased=structuredClone(good);erased.complement.pop();assert.throws(()=>restoreNativeWindow(f,erased));
 const wrong=structuredClone(good);wrong.frame.context.vertex='forged';assert.throws(()=>transportNativeWindow(f,op.id,wrong));
 const lost=structuredClone(good);delete lost.fullFieldReference;assert.throws(()=>restoreNativeWindow(f,lost));
 const short=structuredClone(good);short.active.reverse();assert.throws(()=>restoreNativeWindow(f,short));
 assert.throws(()=>transportNativeWindow(f,op.id,retainNativeWindow(f,op.target,value)));assert.throws(()=>retainNativeWindow(f,op.source,value.slice(0,4)));
});
