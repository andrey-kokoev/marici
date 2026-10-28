import test from 'node:test';import assert from 'node:assert/strict';
import {extractBeltFibrationDiagram,inspectExtractedBelt} from '../research/realization-tower/belt-fibration-diagram.mjs';
import {buildCentralBeltLayout} from '../research/realization-tower/central-belt-layout.mjs';
test('extraction covers actual nodes, all 106 links and same-sign N terminal boundaries',()=>{
 const d=extractBeltFibrationDiagram(),m=buildCentralBeltLayout(),r=inspectExtractedBelt(d);assert.deepEqual(r.counts,{nodes:66,interfaces:106,parentTerminals:2,boundaryRequirements:32});assert.deepEqual(r.errors,[]);assert.equal(r.status,'incomplete');assert.equal(r.equationFailures.length,0);
 assert.deepEqual(d.interfaces.slice(0,74).map(e=>[e.id,e.from,e.to]),m.links.map(e=>[e.id,e.from,e.to]));assert.deepEqual(d.nodes.slice(0,64).map(n=>n.id),m.layers.flatMap(l=>l.nodes.map(n=>n.id)));assert.equal(r.obligations.filter(o=>o.category==='missing-interface-map').length,106);assert.equal(r.obligations.filter(o=>o.category==='missing-parent-attachment').length,0);assert.equal(r.obligations.filter(o=>o.category==='missing-terminal-field-fibration').length,2);assert.ok(d.interfaces.every(e=>e.wiringRule));
});
test('dangling actual endpoints and fabricated adapter names are not silently admitted',()=>{
 const d=extractBeltFibrationDiagram();d.interfaces[0].to='unknown';assert.equal(inspectExtractedBelt(d).status,'rejected');d.interfaces[0].to=d.nodes[0].id;d.interfaces[0].nativeAdapter='invented';const r=inspectExtractedBelt(d);assert.equal(r.status,'incomplete');assert.ok(r.obligations.some(o=>o.category==='unsupported-adapter'));
});
