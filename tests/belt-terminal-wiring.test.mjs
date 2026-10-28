import test from 'node:test';import assert from 'node:assert/strict';import {Color} from 'three';
import {buildCentralBeltLayout,buildCentralTerminalWiring,centralParentPoint} from '../research/realization-tower/central-belt-layout.mjs';
import {buildFoldedFibration} from '../research/realization-tower/fibration-folded-process.mjs';
import {restoreTerminalFiber} from '../research/realization-tower/belt-terminal-wiring.mjs';
import {beltViewerPoint} from '../research/realization-tower/neutron-belt-process.mjs';
import {transportColors} from '../research/realization-tower/belt-layer-model.mjs';
import {createBeltTransportLines,createBeltTerminal} from '../examples/normal-ray/belt-renderer.js';
const layout=buildCentralBeltLayout(),w=buildCentralTerminalWiring(layout),parent=buildFoldedFibration();
test('one same-sign N terminal retains each complete current parent occurrence fiber',()=>{
 assert.equal(w.bundles.length,2);for(const [i,copy,label] of [[0,'original','+N'],[1,'clone','−N']]){const b=w.bundles[i],t=b.body.beltTerminal,binding=parent.bindings.find(p=>p.text===label);assert.equal(t.copy,copy);assert.equal(t.vertexLabel,label);assert.equal(t.anchor,'exposed-N-cut-face-centre');assert.notDeepEqual(b.body.point,centralParentPoint(binding.point,copy));const face=w.surface.faces.find(f=>f.patch===copy&&f.slot===3),centre=face.indices.map(i=>w.surface.vertices[i]).reduce((a,p)=>a.map((v,j)=>v+p[j]/3),[0,0,0]);assert.deepEqual(b.body.point,beltViewerPoint(centre));assert.equal(b.body.role,null);assert.deepEqual(restoreTerminalFiber(b),parent.occurrences.filter(o=>o.copy===copy));assert.equal(t.memberIds.length,175);assert.equal(t.fieldFibration,null);assert.equal(t.directionConversion,null);}
});
test('each N bundle sends to twelve majority satellites and receives four minority centres',()=>{
 assert.equal(w.links.length,32);for(const b of w.bundles){const id=b.body.id,t=b.body.beltTerminal,edges=w.links.filter(e=>e.terminal===id),out=edges.filter(e=>e.from===id),incoming=edges.filter(e=>e.to===id);assert.equal(out.length,12);assert.equal(incoming.length,4);assert.ok(out.every(e=>e.direction===t.outgoingDirection&&e.flux===1));assert.ok(incoming.every(e=>e.direction===t.incomingDirection&&e.flux===3));
  for(let star=0;star<4;star++){assert.equal(out.filter(e=>e.star===star).reduce((s,e)=>s+e.flux,0),3);assert.equal(incoming.filter(e=>e.star===star).reduce((s,e)=>s+e.flux,0),3);}
 }assert.equal(layout.links.length,74,'internal belt wiring unchanged');
});
test('terminal connections render with their P/E edge colours and respect missing endpoints',()=>{
 const arrows=layout.layers.flatMap(l=>l.nodes).map(n=>({id:n.id,point:beltViewerPoint(n.position),beltPort:{transportDirection:n.direction}})),bodies=[...arrows,...w.bundles.map(b=>b.body)],links=[...layout.links,...w.links];
 const lines=createBeltTransportLines(bodies,links),colors=lines.geometry.getAttribute('color');assert.equal(colors.count,228);assert.equal(lines.userData.tubeTrunks.length,8);lines.userData.tubeTrunks.forEach((tube,i)=>{assert.deepEqual([...tube.lanes].sort(),[0,1,2,3]);for(let end=0;end<10;end++)assert.equal(new Color().fromBufferAttribute(colors,148+10*i+end).getHex(),transportColors[tube.direction]);});
 const hidden=createBeltTransportLines(arrows,links);assert.equal(hidden.geometry.getAttribute('position').count,148);
 const marker=createBeltTerminal(w.bundles[0].body);assert.equal(marker.userData.beltGlyph,'terminal-bundle');for(const object of [lines,hidden,marker]){object.geometry.dispose();object.material.dispose();}
});
