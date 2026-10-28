import test from 'node:test';import assert from 'node:assert/strict';
import {buildCentralBeltLayout,buildCentralTerminalWiring} from '../research/realization-tower/central-belt-layout.mjs';
import {Color} from 'three';
import {buildFoldedFibration} from '../research/realization-tower/fibration-folded-process.mjs';
import {transportColors} from '../research/realization-tower/belt-layer-model.mjs';
import {createBeltSurface} from '../examples/normal-ray/belt-renderer.js';
const sub=(a,b)=>a.map((v,i)=>v-b[i]),dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
test('frequency-two octahedral surface is closed, consistently oriented and has 18/48/32 incidence',()=>{
 const layout=buildCentralBeltLayout(),s=buildCentralTerminalWiring(layout).surface;assert.deepEqual(s.counts,{vertices:18,edges:48,faces:32,euler:2});
 const degree=Array(18).fill(0);for(const e of s.edges){assert.equal(e.faces.length,2);for(const i of e.indices)degree[i]++;const signs=e.faces.map(id=>{const f=s.faces.find(f=>f.id===id),i=f.indices.indexOf(e.indices[0]);return f.indices[(i+1)%3]===e.indices[1]?1:-1;});assert.equal(signs[0]+signs[1],0);}
 assert.deepEqual(degree.sort((a,b)=>a-b),[...Array(6).fill(4),...Array(12).fill(6)]);
 for(const f of s.faces){const [a,b,c]=f.indices.map(i=>s.vertices[i]);assert.ok(dot(cross(sub(b,a),sub(c,a)),sub(f.centre,layout.origin))>0);}
 const walls=s.faces.filter(f=>!f.patch),wallIds=new Set(walls.map(f=>f.id)),wallEdges=s.edges.filter(e=>e.faces.some(id=>wallIds.has(id))),boundary=wallEdges.filter(e=>e.faces.filter(id=>wallIds.has(id)).length===1);assert.equal(walls.length,24);assert.equal(wallEdges.length,42);assert.equal(boundary.length,12);assert.equal(18-42+24,0);
});
test('opposite planar four-face patches match all tube centres and contain their lane glyph origins',()=>{
 const layout=buildCentralBeltLayout(),w=buildCentralTerminalWiring(layout),s=w.surface;
 for(const {body} of w.bundles){const layer=layout.layers[body.beltTerminal.layer-1];for(const tube of body.beltTerminal.tubes){const f=s.faces.find(f=>f.id===tube.faceBinding.face),nodes=layer.nodes.filter(n=>n.tubeSlot===tube.slot),centre=[0,1,2].map(i=>nodes.reduce((sum,n)=>sum+n.position[i]/4,0));assert.ok(Math.hypot(...sub(centre,f.centre))<1e-10);assert.equal(tube.nativeFieldMap,null);
  const [a,b,c]=f.indices.map(i=>s.vertices[i]),u=sub(b,a),v=sub(c,a),uu=dot(u,u),uv=dot(u,v),vv=dot(v,v),det=uu*vv-uv*uv;
  for(const i of f.indices)assert.ok(Math.abs(dot(sub(s.vertices[i],layer.center),layout.normal))<1e-10);
  for(const n of nodes){const q=sub(n.position,a),alpha=(dot(q,u)*vv-dot(q,v)*uv)/det,beta=(dot(q,v)*uu-dot(q,u)*uv)/det;assert.ok(alpha>=0&&beta>=0&&alpha+beta<=1);}
 }}
 assert.equal(w.links.length,32);assert.equal(layout.links.length,74);
});
test('every belt face has an opaque native P/E color, retaining attachment colors',()=>{
 const s=buildCentralTerminalWiring().surface,source=buildFoldedFibration().geometry,group=createBeltSurface(s),mesh=group.children[0],colors=mesh.geometry.getAttribute('color');
 assert.equal(mesh.material.opacity,1);assert.equal(mesh.material.transparent,false);assert.equal(mesh.material.depthWrite,true);
 for(const [i,f] of s.cellulation.faces.entries()){assert.ok(['proton','electron'].includes(f.colorRole));if(f.colorSourceGeometry)assert.equal(f.colorRole,source.find(c=>c.id===f.colorSourceGeometry).role);const expected=transportColors[f.colorRole==='proton'?'P':'E'];for(let j=0;j<3;j++)assert.equal(new Color().fromBufferAttribute(colors,3*i+j).getHex(),expected);}
 for(const f of s.faces.filter(f=>f.patch)){const central=f.patch==='original'?'proton':'electron';assert.equal(f.colorRole,f.slot===3?central:central==='proton'?'electron':'proton');}
 assert.equal(s.faces.filter(f=>f.colorRole==='proton').length,16);assert.equal(s.faces.filter(f=>f.colorRole==='electron').length,16);
 for(const child of group.children){child.geometry.dispose();child.material.dispose();}
});
test('cellulation renderer draws 60 unique edges and optional 56 whole-cell triangular faces',()=>{
 const s=buildCentralTerminalWiring().surface;for(const wireOnly of [false,true]){const group=createBeltSurface(s,{wireOnly});assert.equal(group.children.length,wireOnly?1:2);const outline=group.children.at(-1);assert.equal(outline.geometry.getAttribute('instanceStart').count,60);assert.equal(outline.material.color.getHex(),0xffffff);assert.equal(outline.material.linewidth,3.5);assert.equal(outline.userData.sector,'inside-N');if(!wireOnly)assert.equal(group.children[0].geometry.getAttribute('position').count,168);for(const child of group.children){child.geometry.dispose();child.material.dispose();}}
});
