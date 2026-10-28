import test from 'node:test';import assert from 'node:assert/strict';import fs from 'node:fs';
import {encodeFixture,decodeChannel} from '../research/strominger/checkers/native_retained_channel.mjs';
import {nativeDiagramToTable,tableToNativeDiagram,runNativeTableBridge} from '../research/strominger/native-marked-table-bridge.mjs';
import {auditRetainedDiagram} from '../research/strominger/retained-diagram-audit.mjs';
import {boundary,composeEvidence} from '../research/strominger/fibration-evidence.mjs';
const original=JSON.parse(fs.readFileSync(new URL('../research/strominger/results/joint-field-sewing-fixture.json',import.meta.url),'utf8')),fixture=decodeChannel(encodeFixture(original));
test('native diagram passes through four marked presentation steps with exact full recovery',()=>{
 const r=runNativeTableBridge(fixture);assert.equal(r.status,'recovered-native-diagram');assert.equal(r.composition.status,'verified-conditionally');assert.deepEqual(r.recovered,fixture);assert.equal(r.envelope.table.rows.length,18);assert.equal(r.envelope.table.carriers.source.length,14);assert.ok(new Set(r.envelope.table.rows.map(x=>x.label)).size<18);assert.equal(Object.hasOwn(r.envelope.nativeContext,'operations'),false);assert.equal(r.retainedContextUnchanged,true);assert.equal(r.restoredEnvelope.table.history.length,r.envelope.table.history.length+4);assert.deepEqual(r.recovered.histories,fixture.histories);
 assert.deepEqual(boundary('native-diagram',r.recovered),boundary('native-diagram',fixture));
});
test('row order may change but the explicit native occurrence order is recovered',()=>{
 const e=nativeDiagramToTable(fixture);e.table.rows.reverse();assert.deepEqual(tableToNativeDiagram(e),fixture);
 const bad=structuredClone(e);bad.table.rows[0].payload.ordinal=bad.table.rows[1].payload.ordinal;assert.throws(()=>tableToNativeDiagram(bad));
});
test('transposed presentation is not silently interpreted as native inverse execution',()=>{
 const r=runNativeTableBridge(fixture),transposed=tableToNativeDiagram({...r.envelope,table:r.cycle.stages[2]}),audit=auditRetainedDiagram(transposed,fixture);assert.equal(audit.status,'rejected');assert.ok(audit.failures.some(f=>f.category==='type-mismatch'));
});
test('incidental rows and retained context cannot be erased behind a successful table roundtrip',()=>{
 const e=nativeDiagramToTable(fixture),selected=new Set(fixture.histories.flatMap(h=>h.operations)),incidental=e.table.rows.find(r=>!selected.has(r.payload.operation.id));const bad=structuredClone(e),row=bad.table.rows.find(r=>r.id===incidental.id);[row.payload.operation.permutation[0],row.payload.operation.permutation[1]]=[row.payload.operation.permutation[1],row.payload.operation.permutation[0]];
 const report=auditRetainedDiagram(tableToNativeDiagram(bad),fixture);assert.ok(report.failures.some(f=>f.category==='failed-equation'&&f.incidental));
 const hidden=structuredClone(e);hidden.nativeContext.operations=fixture.operations;assert.throws(()=>tableToNativeDiagram(hidden));
 const missing=structuredClone(e);missing.nativeContext.histories=[];assert.ok(auditRetainedDiagram(tableToNativeDiagram(missing),fixture).failures.some(f=>f.category==='history-erasure'));
 const fields=structuredClone(e);fields.table.rows[0].payload.operation.source=0;assert.throws(()=>tableToNativeDiagram(fields));
});
test('evidence composition checks the retained side-context boundary as well as table boundaries',()=>{
 const r=runNativeTableBridge(fixture),records=structuredClone(r.records);records.at(-1).retainedContext=boundary('native-retained-context',{lost:true});const result=composeEvidence(records,r.links);assert.equal(result.status,'rejected');assert.ok(result.failures.some(f=>f.category==='boundary-mismatch'&&f.fromPort==='retainedContext'));
 delete records.at(-1).retainedContext;assert.equal(composeEvidence(records,r.links).status,'rejected');
});
