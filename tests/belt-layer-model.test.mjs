import test from 'node:test';import assert from 'node:assert/strict';
import {buildBeltLayers,beltLayerDefinitions,transportColors} from '../research/realization-tower/belt-layer-model.mjs';
import {Color} from 'three';
import {createBeltNodeArrow,createBeltTransportLines} from '../examples/normal-ray/belt-renderer.js';
import {beltViewerPoint} from '../research/realization-tower/neutron-belt-process.mjs';
const frame={origin:[0,0,0],x:[1,0,0],y:[0,1,0],normal:[0,0,1]};
test('one immutable definition drives every layer and rotation',()=>{
 const before=JSON.stringify(beltLayerDefinitions),layout=buildBeltLayers(frame);
 assert.deepEqual(layout.layers.map(l=>l.label),['L1','L2','L3','L3′','L2′','L1′']);
 assert.deepEqual([...layout.layers].sort((a,b)=>a.displayOrder-b.displayOrder).map(l=>l.label),['L1','L1′','L2','L2′','L3','L3′']);
 for(let i=0;i<3;i++){assert.equal(layout.layers[i].depth,layout.layers[5-i].depth);assert.equal(layout.layers[i].plane,-layout.layers[5-i].plane);}
 assert.deepEqual(layout.layers.map(l=>l.kind),['tube-ports','node-star','bundle-stars','bundle-stars','node-star','tube-ports']);
 assert.deepEqual(layout.layers.map(l=>l.directionCounts),[{P:4,E:12},{P:1,E:3},{P:3,E:9},{P:9,E:3},{P:3,E:1},{P:12,E:4}]);
 assert.equal(new Set(layout.layers.flatMap(l=>l.nodes.map(n=>n.id))).size,64);
 const a=layout.layers[0].nodes[0].position,b=layout.layers[5].nodes[0].position;assert.ok(Math.abs(a[0]+b[0])<1e-10);assert.ok(Math.abs(a[1]+b[1])<1e-10);
 for(const spacing of [.5,1.05,2]){const result=buildBeltLayers({...frame,spacing});for(let i=1;i<6;i++)assert.ok(Math.abs(result.layers[i-1].center[2]-result.layers[i].center[2]-spacing)<1e-10);}
 assert.throws(()=>buildBeltLayers({...frame,spacing:0}));assert.equal(JSON.stringify(beltLayerDefinitions),before);
});
test('outer layers regroup by tube while retaining four star lanes per port',()=>{
 const model=buildBeltLayers(frame);
 for(const [index,minority] of [[0,'P'],[5,'E']]){
  const layer=model.layers[index];
  for(let slot=0;slot<4;slot++){
   const ns=layer.nodes.filter(n=>n.tubeSlot===slot),centre=[0,1].map(i=>ns.reduce((s,n)=>s+n.local[i]/4,0));
   assert.equal(ns.length,4);assert.deepEqual(ns.map(n=>n.tubeLane).sort(),[0,1,2,3]);assert.equal(new Set(ns.map(n=>n.direction)).size,1);assert.equal(ns[0].direction===minority,slot===3);
   assert.ok(Math.abs(Math.hypot(...centre)-(slot===3?0:1.25*model.pitch))<1e-10);
   for(const n of ns){assert.equal(n.group,n.tubeLane);assert.equal(n.arm,slot===3?null:slot);assert.equal(n.starCentre,slot===3);assert.ok(Math.abs(Math.hypot(...n.local.map((v,i)=>v-centre[i]))-.35*model.pitch/Math.sqrt(2))<1e-10);}
  }
 }
});
test('L2 stars retain their geometry independently of regrouped outer ports',()=>{
 const m=buildBeltLayers(frame);
 for(const [index,outerIndex,minority] of [[1,0,'P'],[4,5,'E']]){
  const star=m.layers[index],previous=m.layers[outerIndex],central=star.nodes.find(n=>n.direction===minority),outer=star.nodes.filter(n=>n.direction!==minority);
  assert.ok(Math.hypot(...central.local)<1e-10);assert.equal(outer.length,3);
  for(let j=0;j<3;j++){assert.ok(Math.abs(Math.hypot(...outer[j].local)-.4*m.pitch)<1e-10);assert.ok(Math.abs(Math.hypot(...outer[j].local.map((v,i)=>v-outer[(j+1)%3].local[i]))-Math.sqrt(3)*.4*m.pitch)<1e-10);}
  assert.equal(previous.kind,'tube-ports');
 }
});
test('L3 layers contain three minority-centred stars matching their L2 star geometry',()=>{
 const m=buildBeltLayers(frame),distance=(a,b)=>Math.hypot(...a.map((v,i)=>v-b[i]));
 for(const [index,reference,minority] of [[2,1,'P'],[3,4,'E']]){
  const layer=m.layers[index],centres=[];assert.equal(layer.groupLayout,'three-stars');assert.equal(layer.nodes.length,12);
  for(let star=0;star<3;star++){
   const ns=layer.nodes.filter(n=>n.star===star),central=ns.filter(n=>n.starCentre);assert.equal(ns.length,4);assert.equal(central.length,1);assert.equal(central[0].direction,minority);const pivot=central[0].local;centres.push(pivot);
   assert.equal(ns.filter(n=>n.direction!==minority).length,3);assert.equal(new Set(ns.map(n=>n.group)).size,4);
   for(const node of ns){const offset=node.local.map((v,i)=>v-pivot[i]);assert.ok(m.layers[reference].nodes.some(n=>n.direction===node.direction&&distance(n.local,offset)<1e-10));}
  }
  for(let i=0;i<3;i++){assert.ok(Math.abs(Math.hypot(...centres[i])-1.5*m.pitch)<1e-10);assert.ok(Math.abs(distance(centres[i],centres[(i+1)%3])-Math.sqrt(3)*1.5*m.pitch)<1e-10);}
 }
 for(let star=0;star<3;star++){const a=m.layers[2].nodes.find(n=>n.star===star&&n.starCentre).local,b=m.layers[3].nodes.find(n=>n.star===star&&n.starCentre).local;assert.ok(a.every((v,i)=>Math.abs(v+b[i])<1e-10));}
});
test('belt wires use their endpoint arrow colours and omit hidden endpoints',()=>{
 const m=buildBeltLayers(frame),bodies=m.layers.flatMap(l=>l.nodes).map(n=>({id:n.id,point:beltViewerPoint(n.position),beltPort:{transportDirection:n.direction}})),byId=new Map(bodies.map(b=>[b.id,b]));
 const lines=createBeltTransportLines(bodies,m.links),colors=lines.geometry.getAttribute('color');assert.equal(colors.count,m.links.length*2);
 m.links.forEach((e,i)=>[e.from,e.to].forEach((id,j)=>assert.equal(new Color().fromBufferAttribute(colors,2*i+j).getHex(),transportColors[byId.get(id).beltPort.transportDirection])));
 const hidden=createBeltTransportLines([],m.links);assert.equal(hidden.geometry.getAttribute('position').count,0);
 for(const mesh of [lines,hidden]){mesh.geometry.dispose();mesh.material.dispose();}
});
test('shared belt arrow renderer uses model positions, colours and opposite normal headings',()=>{
 for(const layer of buildBeltLayers(frame).layers)for(const node of layer.nodes){
  const orb=createBeltNodeArrow({point:beltViewerPoint(node.position),beltPort:{transportDirection:node.direction,normal:frame.normal}});
  assert.equal(orb.userData.beltGlyph,'arrow');assert.equal(orb.geometry.type,'LatheGeometry');
  const heading=orb.position.clone().set(0,1,0).applyQuaternion(orb.quaternion);assert.ok(Math.abs(heading.z-(node.direction==='P'?1:-1))<1e-10);
  assert.ok(orb.position.toArray().every((v,i)=>Math.abs(v-node.position[i])<1e-10));assert.equal(orb.material.color.getHex(),transportColors[node.direction]);
  orb.geometry.dispose();orb.material.dispose();
 }
});
