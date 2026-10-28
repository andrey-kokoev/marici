import test from 'node:test';import assert from 'node:assert/strict';
import {presentCentralBelt,centralBeltEnvelope} from '../research/realization-tower/central-belt-layout.mjs';
import {beltLayerDefinitions} from '../research/realization-tower/belt-layer-model.mjs';
import {doubleEsd7RuleProcess,doubleEsd7Rules} from '../research/realization-tower/double-esd7-process.mjs';
import {worldPoint} from '../research/realization-tower/normal-ray-model.mjs';
const sub=(a,b)=>a.map((v,i)=>v-b[i]),dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],average=ps=>ps[0].map((_,i)=>ps.reduce((s,p)=>s+p[i]/ps.length,0));
test('declarative six-layer belt is centred, uniformly spaced and symbolically wired at both L1/L2 pairs',()=>{
 const source=doubleEsd7RuleProcess(7,doubleEsd7Rules.map(r=>r.id)),snapshot=JSON.stringify(source),p=presentCentralBelt(source),a=p.centralBeltAudit;
 assert.equal(a.version,2);assert.equal(p.attachmentBodies.length,64);assert.equal(a.nodeCount,64);assert.equal(centralBeltEnvelope.length,8);assert.deepEqual(a.layers.map(l=>l.nodeCount),[16,4,12,12,4,16]);assert.equal(p.beltGraphLinks.length,106);assert.equal(p.terminalBundles.length,2);assert.equal(a.terminalWiring.linkCount,32);assert.equal(a.wiring.length,8);
 const origin=worldPoint(a.origin),normal=a.normal,plus=worldPoint(p.terminalBundles.find(b=>b.beltTerminal.vertexLabel==='+N').point),minus=worldPoint(p.terminalBundles.find(b=>b.beltTerminal.vertexLabel==='−N').point),axis=sub(plus,minus),length=Math.hypot(...axis);
 assert.ok(Math.hypot(...sub(origin,average([plus,minus])))<1e-10);assert.ok(normal.every((v,i)=>Math.abs(v-axis[i]/length)<1e-10));assert.ok(a.layers[0].plane<length/2);
 for(const b of p.attachmentBodies)assert.deepEqual(b.beltPort.normal,normal);
 for(const [i,layer] of a.layers.entries()){
  const definition=beltLayerDefinitions[i],bs=p.attachmentBodies.filter(b=>b.beltPort.layer===i+1),points=bs.map(b=>worldPoint(b.point)),pivot=worldPoint(layer.center);
  assert.equal(layer.kind,definition.kind);assert.equal(layer.rotationDegrees,definition.rotationDegrees);assert.deepEqual(layer.wiring,[...(i<2||i>=4?['central-block-and-three-rim-bundles']:[]),...(i>=1&&i<=4?['uniform-triangle-to-matching-square','three-bundle-transpose']:[]),...([2,3].includes(i)?['three-star-complete-exchange-with-retained-branch']:[])]);
  assert.ok(Math.hypot(...sub(average(points),pivot))<1e-10);
  assert.ok(Math.hypot(...sub(pivot,origin).map((v,j)=>v-normal[j]*layer.plane))<1e-10);
  if(i)assert.ok(Math.abs(a.layers[i-1].plane-layer.plane-a.layerSpacing)<1e-10);
  assert.equal(bs.map(b=>b.beltPort.transportDirection).join(''),definition.rows?.join('')??definition.groups.join(''));
  for(const b of bs){assert.equal(b.role,null);assert.equal(b.beltPort.capacity,undefined);assert.ok(Math.abs(dot(sub(worldPoint(b.point),pivot),normal))<1e-10);}
 }
 assert.ok(Math.abs(a.layers[0].plane+a.layers.at(-1).plane)<1e-10);assert.ok(a.layers[0].plane<a.parentOffset);
 assert.deepEqual(p.retainedBodies.map(b=>[b.id,b.role]),source.retainedBodies.map(b=>[b.id,b.role]));
 for(const b of p.retainedBodies){const before=source.retainedBodies.find(s=>s.id===b.id);
  for(let i=0;i<b.vertices.length;i++)for(let j=0;j<i;j++)assert.ok(Math.abs(Math.hypot(...sub(worldPoint(b.vertices[i]),worldPoint(b.vertices[j])))-Math.hypot(...sub(worldPoint(before.vertices[i]),worldPoint(before.vertices[j]))))<1e-9);
 }
 for(const [vertices,terminal,sign,rotation] of [[centralBeltEnvelope.slice(0,4),plus,-1,a.parentRotation],[centralBeltEnvelope.slice(4),minus,1,a.secondParentRotation]]){
  const outward=sub(terminal,average(vertices.map(worldPoint))),length=Math.hypot(...outward);assert.ok(outward.every((v,i)=>Math.abs(v/length-sign*normal[i])<1e-10));const cap=p.parentCutAudit.caps.find(c=>c.copy===(sign===-1?'original':'clone'));assert.ok(Math.hypot(...sub(terminal,cap.targetCentre))<1e-10);assert.ok(cap.faceError<1e-12);assert.ok(cap.clearance>=-1e-12);
 }
 assert.equal(p.replacedFaceLinks.length,49);assert.equal(JSON.stringify(source),snapshot);assert.deepEqual(p,presentCentralBelt(source));
});
