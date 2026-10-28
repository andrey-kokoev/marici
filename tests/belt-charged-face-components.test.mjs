import test from 'node:test';import assert from 'node:assert/strict';
import {chargedFaceComponentAudit} from '../research/strominger/checkers/check_belt_charged_face_components.mjs';
test('predeclared face groupings preserve records and do not produce 82/82',()=>{
 const a=chargedFaceComponentAudit();assert.deepEqual(a.faceCounts,{proton:250,electron:206});assert.equal(a.neutronFillers,126);assert.equal(a.status,'no-match-for-tested-groupings');assert.deepEqual(a.matchingRules,[]);
 assert.deepEqual(a.rules.map(r=>r.counts),[{proton:176,electron:194},{proton:3,electron:1},{proton:167,electron:127}]);
 const byId=new Map(a.faceRecords.map(f=>[f.id,f]));for(const rule of a.rules){const members=rule.components.flatMap(c=>c.faces);assert.equal(members.length,456);assert.equal(new Set(members).size,456);for(const c of rule.components){assert.ok(c.faces.every(id=>byId.get(id).role===c.role));assert.deepEqual(new Set(c.owners),new Set(c.faces.map(id=>byId.get(id).owner)));if(rule.rule==='same-native-cell')assert.equal(c.owners.length,1);}}
 const edge=a.rules[0];assert.deepEqual(edge.byShape.original,{proton:73,electron:82});assert.deepEqual(edge.byShape.clone,{proton:73,electron:82});assert.deepEqual(edge.byShape.belt,{proton:30,electron:30});assert.equal(edge.crossShapeComponents.length,0);
 assert.equal(a.rules[1].crossShapeComponents.length,1);const across=a.rules[1].components.find(c=>c.shapes.length>1);assert.equal(across.role,'electron');assert.equal(across.faces.length,206);
});
test('component counts are stable under three coordinate-key precisions',()=>{
 const counts=digits=>chargedFaceComponentAudit({digits}).rules.map(r=>r.counts);assert.deepEqual(counts(6),counts(8));assert.deepEqual(counts(10),counts(8));
});
