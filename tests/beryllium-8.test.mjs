import {test} from 'node:test';
import assert from 'node:assert/strict';
import {processes,processState} from '../research/realization-tower/normal-ray-processes.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
import {isBranchingSeedView} from '../examples/normal-ray/branching-seed-view.js';
test('Be-8 is a registered single-view exploration without imported sulfur inventory',()=>{
 assert.equal(processes.filter(p=>p.id==='beryllium-8').length,1);
 const state=processState('beryllium-8',7,5);
 assert.equal(state.seedDepth,4);assert.equal(state.view,'branching-seed');assert.equal(state.canAdvance,false);assert.equal(state.step,0);
 assert.deepEqual(state.isotope,{symbol:'Be',mass:8,protons:4,neutrons:4});assert.deepEqual(state.assignments,[]);
 assert.equal(state.sulfur32Audit,undefined);
});
test('Be-8 always selects the shared seed renderer independently of Su-32 view flags',()=>{
 for(const sulfurBranchSeed of [false,true])assert.equal(isBranchingSeedView({processId:'beryllium-8',sulfurBranchSeed}),true);
 assert.equal(isBranchingSeedView({processId:'sulfur-32',sulfurBranchSeed:false}),false);
 assert.equal(isBranchingSeedView({processId:'sulfur-32',sulfurBranchSeed:true}),true);
 assert.equal(isBranchingSeedView({processId:'ruthenium-98',sulfurBranchSeed:true}),false);
});
test('Be-8 process and progress survive settings normalization, with no extra stages',()=>{
 const saved=normalizeSceneSettings({process:{id:'beryllium-8',k:2,step:99,branch:1,progress:{'beryllium-8':{k:2,step:99},'sulfur-32':{k:7,step:1}}},appearance:{sulfurBranchSeed:false}});
 assert.equal(saved.process.id,'beryllium-8');assert.equal(saved.process.k,7);assert.equal(saved.process.step,0);
 assert.equal(saved.process.progress['beryllium-8'].step,0);assert.equal(saved.process.progress['sulfur-32'].step,1);
 assert.equal(saved.appearance.sulfurBranchSeed,false);
});
