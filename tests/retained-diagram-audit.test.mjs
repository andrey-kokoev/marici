import test from 'node:test';import assert from 'node:assert/strict';import fs from 'node:fs';
import {decodeChannel,encodeFixture} from '../research/strominger/checkers/native_retained_channel.mjs';
import {auditRetainedDiagram,inspectPartialBeltDiagram} from '../research/strominger/retained-diagram-audit.mjs';
const read=p=>JSON.parse(fs.readFileSync(new URL(p,import.meta.url),'utf8')),original=read('../research/strominger/results/joint-field-sewing-fixture.json'),native=decodeChannel(encodeFixture(original));
const pathOps=new Set(native.histories.flatMap(h=>h.operations)),incidental=native.operations.find(o=>!pathOps.has(o.id));
const categories=f=>auditRetainedDiagram(f,native).failures.map(e=>e.category);
test('complete native diagram includes all four non-generating interfaces',()=>{
 const report=auditRetainedDiagram(native,native);assert.equal(report.status,'native-diagram-consistent');assert.deepEqual(report.failures,[]);assert.equal(report.counts.interfaces,18);assert.equal(report.counts.incidentalInterfaces,4);assert.equal(report.counts.packets,14);
});
test('corrupted incidental coefficient equation fails with an exact location while paths remain intact',()=>{
 const f=structuredClone(native),op=f.operations.find(o=>o.id===incidental.id);[op.permutation[0],op.permutation[1]]=[op.permutation[1],op.permutation[0]];
 assert.deepEqual(f.histories,native.histories);for(const id of pathOps)assert.deepEqual(f.operations.find(o=>o.id===id),native.operations.find(o=>o.id===id));
 const report=auditRetainedDiagram(f,native);assert.equal(report.status,'rejected');assert.ok(report.failures.some(e=>e.category==='failed-equation'&&e.at===`interface:${incidental.id}`&&e.incidental));
});
test('missing incidental witness is not misclassified as an equation failure',()=>{
 const f=structuredClone(native);f.operations=f.operations.filter(o=>o.id!==incidental.id);const failures=auditRetainedDiagram(f,native).failures;assert.ok(failures.some(e=>e.category==='missing-witness'&&e.at===`interface:${incidental.id}`));assert.ok(!failures.some(e=>e.category==='failed-equation'));
});
test('equal endpoints cannot conceal history erasure, context changes or root replacement',()=>{
 const history=structuredClone(native);history.histories[0].occurrences=[];assert.ok(categories(history).includes('history-erasure'));
 const chart=structuredClone(native);chart.charts[0].aliases.C0='forged';assert.ok(categories(chart).includes('retained-data-mismatch'));
 const root=structuredClone(native);root.rootPacket=native.histories[0].packets.at(-1);assert.ok(categories(root).includes('retained-data-mismatch'));
 const erased=structuredClone(native);erased.comparisons=[];assert.ok(categories(erased).includes('comparison-erasure'));
 const unknown=structuredClone(native);unknown.packets.push({...unknown.packets[0],id:999999});assert.ok(categories(unknown).includes('unsupported-packet'));
});
test('incompatible carriers and incomplete packets are typed failures, not invented adapters',()=>{
 const f=structuredClone(native),op=f.operations.find(o=>o.kind==='PN');op.target=op.source;assert.ok(categories(f).includes('type-mismatch'));
 const scalar=structuredClone(native);scalar.packets[0].permutation=[0];assert.ok(categories(scalar).includes('type-mismatch'));
 assert.equal(auditRetainedDiagram({},native).failures[0].category,'malformed-diagram');
});
test('nested malformed native records return precise schema diagnostics without throwing',()=>{
 for(const [key,field,value] of [['histories','operations',null],['packets','permutation',null],['charts','aliases',null],['operations','source',{}]]){const f=structuredClone(native);f[key][0][field]=value;const report=auditRetainedDiagram(f,native);assert.equal(report.status,'rejected');assert.ok(report.failures.some(e=>e.category==='malformed-diagram'&&e.at===`${key}[0].${field}`));}
 const f=structuredClone(native);f.histories[0]=null;assert.equal(auditRetainedDiagram(f,native).status,'rejected');
});
test('parent-belt diagram remains incomplete even if an arbitrary adapter name is supplied',()=>{
 const question=read('../research/strominger/inputs/parent-belt-fibration-question.json'),result=inspectPartialBeltDiagram(question);assert.equal(result.status,'incomplete');assert.equal(result.equationFailures.length,0);assert.equal(result.obligations.filter(e=>e.category==='missing-interface-map').length,14);assert.ok(result.obligations.some(e=>e.category==='undefined-endpoint-claim'));
 question.interfaces[0].adapter='made-up-map';const changed=inspectPartialBeltDiagram(question);assert.equal(changed.status,'incomplete');assert.ok(changed.obligations.some(e=>e.category==='unsupported-adapter'));assert.throws(()=>inspectPartialBeltDiagram({kind:'unknown'}));
});
