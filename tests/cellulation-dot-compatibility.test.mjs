import {test} from 'node:test';
import assert from 'node:assert/strict';
import {analyzeDotCompatibility} from '../research/strominger/cellulation-dot-compatibility.mjs';
test('source-role obstruction, both legacy orders, strict rejection, and retained UI claims reproduce',async()=>{
 await import('../research/strominger/checkers/check_cellulation_dot_compatibility.mjs');
});
test('unknown boundary colors do not count as compatible source data',()=>{
 const r=analyzeDotCompatibility([{point:'p',cell:'c',role:'A:white-source',kind:'requirement',colour:0xffffff,observedColour:null}]);
 assert.equal(r.status,'unresolved');assert.equal(r.readings[0].unknownSources.length,1);
});
test('different normals are reported separately rather than normalized into a common vertex reading',()=>{
 const c={point:'p',cell:'c',role:'turn',kind:'proposal',colour:0xff3030,normal:[1,1,-1]};
 const r=analyzeDotCompatibility([c,{...c,cell:'d',normal:[1,-1,1]}]);assert.equal(r.status,'no-colour-obstruction-observed');assert.equal(r.readings[0].normalStatus,'multiple-cell-relative-normals');
});
