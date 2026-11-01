import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildNNPEComposition as build} from '../research/realization-tower/sulfur-nnpe-composition.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
const leaves=h=>h.star?[h.star]:[...leaves(h.left),...leaves(h.right)];
test('NNPE generators distinguish centre, attachment labels and retained inventory',()=>{
 const model=build();assert.equal(model.stars.length,16);assert.equal(model.audit.boundaryPorts,48);
 for(const star of model.stars){assert.equal(star.centre,'N');assert.deepEqual(star.ports.map(p=>p.role),['N','P','E']);}
 assert.deepEqual(model.inventory,{N:16,P:16});assert.equal(model.components.length,16);
});
test('composition contracts matched ports, retains inventory and a complete decorated history',()=>{
 const joins=Array.from({length:15},(_,i)=>[`S${i+1}:E`,`S${i+2}:P`]),model=build(joins);
 assert.equal(model.rejected.length,0);assert.equal(model.components.length,1);assert.equal(model.audit.boundaryPorts,18);assert.deepEqual(model.inventory,{N:16,P:16});
 const c=model.components[0];assert.equal(c.stars.length,16);assert.equal(new Set(leaves(c.history)).size,16);assert.equal(leaves(c.history).length,16);
 assert.equal(c.boundary.filter(id=>id.endsWith(':N')).length,16);assert(c.boundary.includes('S1:P'));assert(c.boundary.includes('S16:E'));
 const restored=normalizeSceneSettings({appearance:{sulfurComposition:true,sulfurCompositionJoins:joins,sulfurCompositionCollapsed:true}});
 assert.deepEqual(restored.appearance.sulfurCompositionJoins,joins);assert.equal(restored.appearance.sulfurCompositionCollapsed,true);
});
test('incompatible colours, reused ports and loop-producing joins are rejected',()=>{
 const model=build([['S1:N','S2:N'],['S1:P','S2:E'],['S1:N','S3:N'],['S1:P','S3:P'],['S1:P','S3:E']]);
 assert.equal(model.joins.length,2);assert.equal(model.rejected.length,3);assert.equal(model.components.length,14);assert.equal(model.audit.boundaryPorts,44);
 assert.deepEqual(model.inventory,{N:16,P:16});assert.match(model.rejected[0].reason,/loop/);
});
