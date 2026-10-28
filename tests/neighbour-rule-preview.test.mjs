import test from 'node:test';
import assert from 'node:assert/strict';
import {previewNeighbourRule} from '../research/realization-tower/neighbour-rule-preview.mjs';
const geometry=[{id:'c',kind:'tetrahedron'},...['a','b','d','e'].map(id=>({id,kind:'octahedron'}))],links=['a','b','d','e'].map(to=>({from:'c',to})),assigned=['a','b','d','e'].map((id,i)=>({id,role:i===3?'neutron':'proton'}));
test('exactly 3P+1N proposes P, without mutation',()=>{const before=structuredClone(assigned),r=previewNeighbourRule(geometry,links,assigned);assert.equal(r.candidates.length,1);assert.equal(r.candidates[0].role,'proton');assert.equal(r.candidates[0].arrivals.length,4);assert.deepEqual(assigned,before);});
test('existing contradictions block application, agreeing P is left alone',()=>{for(const role of ['neutron','electron','proton']){const r=previewNeighbourRule(geometry,links,[...assigned,{id:'c',role}]);assert.equal(r.valid,role==='proton');assert.equal(r.candidates.length,0);}});
test('incomplete neighbourhood or wrong shape does not match',()=>{assert.equal(previewNeighbourRule(geometry,links.slice(1),assigned).candidates.length,0);assert.equal(previewNeighbourRule(geometry.map(b=>({...b,kind:'octahedron'})),links,assigned).candidates.length,0);});
