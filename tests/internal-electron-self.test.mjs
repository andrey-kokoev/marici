import test from 'node:test';
import assert from 'node:assert/strict';
import {previewPathRules} from '../research/realization-tower/path-rule-preview.mjs';
import {doubleEsd7RuleProcess,doubleEsd7Rules} from '../research/realization-tower/double-esd7-process.mjs';
const input={bodies:[{id:'e',role:'electron'}],states:[{node:'e',front:'internal',suffix:'NE'}],wires:[{from:'e',to:'p',direction:'E'}],enabledRules:[],electronSelfRule:true};
test('E + E proposes P only in the internal sector',()=>{
 assert.equal(previewPathRules(input).candidates.length,0);
 const r=previewPathRules({...input,sector:'internal'});assert.equal(r.valid,true);assert.equal(r.candidates.length,1);assert.equal(r.candidates[0].role,'proton');assert.equal(r.candidates[0].arrivals[0].suffix,'EP');
});
test('internal E self rule reports conflicting assignments',()=>{
 const r=previewPathRules({...input,sector:'internal',bodies:[...input.bodies,{id:'p',role:'neutron'}]});assert.equal(r.valid,false);assert.equal(r.conflicts.length,1);
});
test('sandbox never changes parent cells; current carrier has no E-to-E-direction matches',()=>{
 const rules=doubleEsd7Rules.map(r=>r.id),before=doubleEsd7RuleProcess(7,rules),after=doubleEsd7RuleProcess(7,rules,true);
 assert.deepEqual(after.retainedBodies,before.retainedBodies);assert.deepEqual(after.emptyBodies,before.emptyBodies);
 assert.equal(after.doubleEsd7Audit.internalExperiment.matches,0);assert.equal(after.doubleEsd7Audit.internalExperiment.conflicts.length,0);
});
