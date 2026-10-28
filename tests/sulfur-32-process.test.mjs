import test from 'node:test';
import assert from 'node:assert/strict';
import {processes,processState} from '../research/realization-tower/normal-ray-processes.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
import {useViewerModel} from '../examples/normal-ray/useViewerModel.js';

test('Sulfur-32 is the unchanged edge-three single-octahedron geometry',()=>{
 const source=processState('single-octahedral',7,1),p=processState('sulfur-32',7,0);
 assert.equal(processes.find(p=>p.id==='sulfur-32').name,'Sulfur-32');
 assert.deepEqual(p.retainedBodies,source.retainedBodies);
 assert.deepEqual(p.nativeWiringGraph,source.nativeWiringGraph);
 assert.deepEqual(p.presentationLabels,source.presentationLabels);
 assert.equal(p.retainedBodies.length,51);
 assert.equal(p.sulfur32Audit.edgeUnits,3);
 assert.equal(p.sulfur32Audit.fibration,'pending');
 assert.equal(p.sulfur32Audit.colorCellulation,'pending');
 assert.equal(p.sulfur32Audit.physicalInventoryEstablished,false);
 assert.equal(p.canAdvance,true);
 assert.equal(p.step,0);
 assert.deepEqual(p.interfaceGuides,[]);
 assert.equal(p.nTubeAudit,undefined);
 assert.throws(()=>processState('sulfur-32',7,2),/stages/);
});
test('Sulfur-32 ignores inherited routing overlays and persists separately',()=>{
 const p=processState('sulfur-32',7,0,1,{nTubeAxis:'coupled',rimAssembly:true});
 assert.equal(p.retainedBodies.length,51);assert.deepEqual(p.interfaceGuides,[]);
 const s=normalizeSceneSettings({process:{id:'sulfur-32',k:1,step:9,progress:{'single-octahedral':{k:7,step:3},'sulfur-32':{k:7,step:9}}}});
 assert.equal(s.process.id,'sulfur-32');assert.equal(s.process.step,1);
 assert.equal(s.process.progress['single-octahedral'].step,3);
});
test('viewer selection uses the dedicated summary, inventory and fixed stage',()=>{
 const m=useViewerModel();
 m.selectProcess('single-octahedral');assert.equal(m.process.step,3);
 m.selectProcess('sulfur-32');assert.equal(m.process.step,0);
 assert.equal(m.state.value.sulfur32Audit.edgeUnits,3);
 assert.match(m.summary.value,/Sulfur-32/);assert.equal(m.canAdvance.value,true);
 assert.equal(m.pneInventory.value.rows[0].total,51);
 m.move(1);assert.equal(m.process.step,1);assert.equal(m.canAdvance.value,false);
 assert.equal(m.state.value.sulfur32Audit.NChannels,16);assert.equal(m.state.value.sulfur32Audit.wires,64);
 assert.equal(m.state.value.nativeWiringGraph.links.length,131);
 const forward=m.state.value.sulfur32Audit.channelPorts;
 m.process.branch=3;const reverse=m.state.value.sulfur32Audit.channelPorts;
 for(let i=0;i<16;i++)for(let slot=0;slot<4;slot++){assert.equal(reverse[i].slots[slot].wire,forward[i].slots[slot].wire);assert.equal(reverse[i].slots[slot].from,forward[i].slots[slot].to);}
 m.move(1);assert.equal(m.process.step,1);
 m.selectProcess('single-octahedral');assert.equal(m.process.step,3);
 m.disposeSettings();
});
