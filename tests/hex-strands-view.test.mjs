import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildHexStrandsView,hexStrandStages} from '../research/realization-tower/hex-strands-view.mjs';
import {createHexStrandsView} from '../examples/normal-ray/hex-strands-renderer.js';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
test('all stages retain sixteen seed identities and exact transformed source edges',()=>{
 for(let stage=0;stage<=7;stage++){
  const m=buildHexStrandsView({hexStrandStage:stage});
  assert.equal(m.families.length,16);assert.equal(m.audit.traceCopies,16*2**stage);
  for(const [i,f] of m.families.entries()){
   assert.equal(f.copyCount,2**stage);
   assert.deepEqual(f.edges.map(e=>e.id),[...new Set(hexStrandStages[stage].strands[i].traces.flatMap(t=>t.edges))]);
   assert(f.edges.every(e=>e.points.every(p=>p[2]===(i-7.5)*.24)));
  }
 }
});
test('spacing, family selection and copy selection do not change source routes',()=>{
 const before=JSON.stringify(hexStrandStages[7].strands);
 const m=buildHexStrandsView({hexStrandStage:7,hexStrandSpacing:0,hexStrandSelection:'SLLLL',hexStrandCopy:127});
 assert.equal(m.families.filter(f=>f.selected).length,1);assert(m.families.every(f=>f.edges.length===8));
 assert(m.families.every(f=>f.edges.every(e=>e.points.every(p=>p[2]===0))));
 assert.equal(JSON.stringify(hexStrandStages[7].strands),before);
 const rendered=createHexStrandsView(m,{bodies:false,hexStrandIsolate:true});
 assert.equal(rendered.children.length,1);assert.equal(rendered.children[0].userData.hexStrand,'SLLLL');
 rendered.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});
});
test('new view settings persist with bounded stage and copy indexes',()=>{
 const s=normalizeSceneSettings({appearance:{sulfurHexStrands:true,hexStrandStage:7,hexStrandCopy:127,hexStrandSpacing:.5,hexStrandSelection:'SRLRL',hexStrandIsolate:false}}).appearance;
 assert.equal(s.sulfurHexStrands,true);assert.equal(s.hexStrandCopy,127);assert.equal(s.hexStrandSelection,'SRLRL');assert.equal(s.hexStrandIsolate,false);
 assert.equal(normalizeSceneSettings({appearance:{hexStrandStage:0,hexStrandCopy:127}}).appearance.hexStrandCopy,0);
});
