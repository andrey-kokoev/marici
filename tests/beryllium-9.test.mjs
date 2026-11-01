import {test} from 'node:test';
import assert from 'node:assert/strict';
import {processes,processState} from '../research/realization-tower/normal-ray-processes.mjs';
import {buildBranchingSeed} from '../research/realization-tower/branching-seed.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
import {isBranchingSeedView} from '../examples/normal-ray/branching-seed-view.js';
test('Be-9 is a separate registered process cloned from Be-8',()=>{
 assert.equal(processes.filter(p=>p.id==='beryllium-9').length,1);
 const a=processState('beryllium-8',7,0),b=processState('beryllium-9',7,0);
 assert.equal(b.processId,'beryllium-9');assert.equal(b.clonedFrom,'beryllium-8');assert.equal(b.seedDepth,4);assert.equal(b.view,'branching-seed');assert.equal(b.canAdvance,false);
 assert.deepEqual(b.isotope,{symbol:'Be',mass:9,protons:4,neutrons:5});assert.equal(a.isotope.neutrons,4);
 assert.deepEqual(b.assignments,a.assignments);assert.notEqual(b.assignments,a.assignments);
 const seed9=buildBranchingSeed({processId:'beryllium-9'}),seed8=buildBranchingSeed({processId:'beryllium-8'});
 assert.equal(JSON.stringify(seed9),JSON.stringify(seed8));
 for(const operation of ['reflect','reflectLower','reflectBlockLower'])assert.deepEqual(seed9[operation]([1,2,3]),seed8[operation]([1,2,3]));
});
test('Be-9 always uses the depth-four seed view and has persistent independent process progress',()=>{
 for(const sulfurBranchSeed of [true,false])assert.equal(isBranchingSeedView({processId:'beryllium-9',sulfurBranchSeed}),true);
 const settings=normalizeSceneSettings({process:{id:'beryllium-9',k:2,step:12,progress:{'beryllium-8':{k:7,step:0},'beryllium-9':{k:3,step:9},'sulfur-32':{k:7,step:1}}}});
 assert.equal(settings.process.id,'beryllium-9');assert.equal(settings.process.k,7);assert.equal(settings.process.step,0);
 assert.equal(settings.process.progress['beryllium-9'].step,0);assert.equal(settings.process.progress['beryllium-8'].step,0);assert.equal(settings.process.progress['sulfur-32'].step,1);
});
