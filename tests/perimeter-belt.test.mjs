import test from 'node:test';import assert from 'node:assert/strict';
import {perimeterBeltNodes as nodes,perimeterBeltLinks as links,perimeterBeltRule as rule,presentPerimeterBelt} from '../research/realization-tower/perimeter-belt.mjs';
import {doubleEsd7RuleProcess} from '../research/realization-tower/double-esd7-process.mjs';
test('native previous-layer perimeter has six points on each side and fifteen distinct ports',()=>{
 assert.equal(nodes.length,15);assert.equal(new Set(nodes.map(b=>b.point.join(','))).size,15);
 const p=presentPerimeterBelt(doubleEsd7RuleProcess(7));assert.deepEqual(p.perimeterBeltAudit.sideCounts,[6,6,6]);assert.equal(p.perimeterBeltAudit.previousLayerPorts,21);
 for(const b of nodes){assert.equal(links.filter(e=>e.from===b.id||e.to===b.id).length,4);assert.equal(b.beltPort.parents.length,2);assert.equal(b.faces.length,0);}
 assert.equal(links.filter(e=>e.kind==='perimeter').length,15);assert.equal(p.replacedFaceLinks.length,15);
 assert.deepEqual(p.retainedBodies,doubleEsd7RuleProcess(7).retainedBodies);
});
test('three requested rules and no invented incoming letters',()=>{
 assert.deepEqual(rule('neutron'),{role:'proton',rule:'N → P'});
 assert.deepEqual(rule('electron','N'),{role:'proton',rule:'E + |N| → P'});
 assert.deepEqual(rule('electron','P'),{role:'neutron',rule:'E + |P| → N'});
 assert.deepEqual(rule('electron'),{role:'electron',rule:null});assert.deepEqual(rule('proton','N'),{role:'proton',rule:null});
});
