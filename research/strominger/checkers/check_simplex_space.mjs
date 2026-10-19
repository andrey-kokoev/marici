import assert from 'node:assert/strict';
import './check_simplex_components.mjs';
import './check_atom_models.mjs';
import {createServer} from 'node:http';
import {readFile,mkdir} from 'node:fs/promises';
import path from 'node:path';
import {chromium} from '@playwright/test';
import * as M from '../demos/particle-overlap-tetrahedron/simplex-model.mjs';
const distance=(a,b)=>Math.hypot(...a.map((x,i)=>x-b[i]));
assert.equal(M.corners.length,4);assert.equal(M.edges.length,6);assert.equal(M.faces.length,4);
const lattice=M.makeSimplexLattice();
assert.equal(M.resolution,7);assert.equal(lattice.nodes.length,120);assert.equal(lattice.cells.length,343);
const incidence=new Map();let volume=0;
for(const cell of lattice.cells){
 const [a,b,c,d]=cell.map(i=>lattice.nodes[i].point),u=b.map((x,i)=>x-a[i]),v=c.map((x,i)=>x-a[i]),w=d.map((x,i)=>x-a[i]);
 const det=u[0]*(v[1]*w[2]-v[2]*w[1])-u[1]*(v[0]*w[2]-v[2]*w[0])+u[2]*(v[0]*w[1]-v[1]*w[0]);
 assert.ok(Math.abs(det)>1e-10);volume+=Math.abs(det)/6;
 for(const f of M.faces){const key=f.map(i=>cell[i]).sort((a,b)=>a-b).join(',');incidence.set(key,(incidence.get(key)||0)+1);}
}
assert.ok(Math.abs(volume-(6*M.spaceScale)**3/(6*Math.sqrt(2)))<1e-9);
assert.ok([...incidence.values()].every(n=>n===1||n===2));
assert.equal([...incidence.values()].filter(n=>n===1).length,196);
Object.values(M.coordinates).forEach(M.validateCoordinate);
assert.throws(()=>M.worldPoint([0,0,0,0]));assert.throws(()=>M.worldPoint([NaN,1,1,0]));
assert.deepEqual(M.lattice.cells[M.centralCellId].map(id=>M.lattice.nodes[id].address),M.corners);
assert.equal(M.lattice.assembly.items[0].inverted,false);
const oldViewer=await readFile('public/experiments/eight-node-coherence-pyramid/app.js','utf8');
assert.ok(oldViewer.includes('input.value = "(1,2,2,2); (2,1,2,2); (2,2,1,2); (2,2,2,1)"'));
assert.deepEqual(M.surfaceLayers.counts,{'1':126,'2':44,'3':4,'4':1});
assert.deepEqual(M.surfaceLayers.deepestCellIds,[M.centralCellId]);
assert.equal(M.surfaceLayers.cellLayers[M.centralCellId],4);
for(const group of M.lattice.assembly.groups)assert.equal(new Set(group.children.map(id=>M.surfaceLayers.cellLayers[id])).size,1);
const containing=M.lattice.cells.map((c,i)=>({id:i,w:M.cellWeights(M.barycenter,c)})).filter(c=>c.w.every(w=>w>=-1e-10));
assert.equal(containing.length,1);
assert.equal(containing[0].id,M.bodies[0].cellId);
assert.ok(containing[0].w.every(w=>Math.abs(w-.25)<1e-10));
const center=M.bodies[0].nodeIds.reduce((s,id)=>s.map((x,i)=>x+M.lattice.nodes[id].point[i]/4),[0,0,0]);
assert.ok(distance(center,M.worldPoint(M.barycenter))<1e-10);
assert.deepEqual(M.cellFaceLayers(M.protonAnchor.cellId),Array.from({length:4},()=>({min:0,max:1,layer:6})));
for(const [i,j] of M.edges)assert.ok(Math.abs(distance(M.lattice.nodes[M.bodies[0].nodeIds[i]].point,M.lattice.nodes[M.bodies[0].nodeIds[j]].point)-M.primitiveEdgeLength)<1e-10);
// A vertex is on a boundary, not a strict interior point.
assert.ok(M.cellWeights(M.coordinates.C0,M.lattice.cells[M.bodies[0].cellId]).some(w=>Math.abs(w)<1e-10));
const all=M.selectCarriers('all');
for(const [name,id] of Object.entries(M.nodeIds)) {
 assert.equal(all.coordinates[name],M.lattice.nodes[id].coordinate);
 assert.equal(all.points[name],M.lattice.nodes[id].point);
}
for(const body of M.bodies) {
 assert.deepEqual([...body.nodeIds].sort((a,b)=>a-b),[...M.lattice.cells[body.cellId]].sort((a,b)=>a-b));
 for(const [i,j] of M.edges)assert.ok(M.lattice.edges.some(e=>e.includes(body.nodeIds[i])&&e.includes(body.nodeIds[j])));
}
assert.equal(new Set(M.bodies.map(b=>b.cellId)).size,3);
assert.equal(M.bodies[0].nodeIds.filter(v=>M.bodies[1].nodeIds.includes(v)).length,3);
assert.equal(M.bodies[1].nodeIds.filter(v=>M.bodies[2].nodeIds.includes(v)).length,3);
const root=path.resolve('public'),out='research/strominger/results/simplex-space';await mkdir(out,{recursive:true});
const server=createServer(async(req,res)=>{try{const url=new URL(req.url,'http://localhost');const f=path.resolve(root,'.'+url.pathname);if(path.relative(root,f).startsWith('..'))throw Error('path');res.setHeader('Content-Type',f.endsWith('.html')?'text/html':f.endsWith('.css')?'text/css':'text/javascript');res.end(await readFile(f));}catch{res.writeHead(404);res.end();}});
await new Promise(r=>server.listen(0,'127.0.0.1',r));let browser;
try{
 browser=await chromium.launch({headless:true,args:['--enable-webgl','--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
 const page=await browser.newPage({viewport:{width:1480,height:1040}}),errors=[];page.on('pageerror',e=>errors.push(String(e)));
 await page.goto(`http://127.0.0.1:${server.address().port}/experiments/particle-overlap-tetrahedron/vacuum.html`);await page.waitForFunction(()=>globalThis.SimplexSpaceViewer?.snapshot().frameCount>2);
 const snap=()=>page.evaluate(()=>globalThis.SimplexSpaceViewer.snapshot());
 assert.equal(await page.locator('.space-dimension,#space-dimensions').count(),0);
 let canvas=await page.locator('#scene canvas').boundingBox();
 await page.mouse.move(canvas.x+canvas.width/2,canvas.y+canvas.height/2);
 assert.equal((await snap()).hoverText,null);
 await page.locator('#hover-coordinates').check();
 await page.locator('#scene canvas').scrollIntoViewIfNeeded();canvas=await page.locator('#scene canvas').boundingBox();
 let hover;
 for(let dy=-80;dy<=80&&!hover;dy+=16)for(let dx=-80;dx<=80&&!hover;dx+=16){
  await page.mouse.move(canvas.x+canvas.width/2+dx,canvas.y+canvas.height/2+dy);
  await page.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))));
  const s=await snap();if(s.hoverText)hover=s;
 }
 assert.ok(hover,'A lattice node exposes hover coordinates');
 assert.ok(hover.hoverText.includes(M.lattice.nodes[hover.hoveredNode].address.join(', ')));
 await page.locator('#hover-coordinates').uncheck();assert.equal((await snap()).hoverText,null);
 assert.equal((await snap()).lattice.nodes,120);assert.equal((await snap()).lattice.cells,343);assert.equal((await snap()).lattice.visible,true);
 assert.deepEqual((await snap()).mode,[]);assert.equal(await page.locator('[data-axis]').count(),0);
 const ids=['proton','neutron','electron'];
 for(const mask of [0,1,2,3,4,5,6,7,0]){
  const selected=ids.filter((_,i)=>mask&(1<<i));
  for(const id of ids)await page.locator(`[data-carrier="${id}"]`).setChecked(selected.includes(id));
  const s=await snap();assert.deepEqual(s.protonAnchor,M.placementAtCell(M.layerReferenceCellId).anchor);assert.deepEqual(s.renderedCarriers.map(b=>b.id).sort(),[...selected].sort());assert.equal(s.lattice.visible,true);assert.equal(s.lattice.cells,343);assert.equal(s.componentMeshCount,343);
  const highlightedEdges=new Set([...s.selection.bodies.map(b=>b.nodeIds),...s.inspectedCellIds.map(id=>M.lattice.cells[id])].flatMap(cell=>M.edges.map(([i,j])=>[cell[i],cell[j]].sort((a,b)=>a-b).join(','))));
  assert.equal(s.outlineEdgeCount,highlightedEdges.size);
  assert.equal(await page.locator('#focus-carriers').isDisabled(),selected.length===0);
  for(const mesh of s.renderedCarriers){assert.deepEqual(mesh.nodeIds,M.lattice.cells[mesh.cellId]);mesh.nodeIds.forEach((id,i)=>assert.ok(distance(mesh.positions.slice(3*i,3*i+3),M.lattice.nodes[id].point)<1e-6));}
 }
 assert.equal(await page.locator('#coordinate-form,#node-bindings,header,footer').count(),0);
 await page.locator('#scene').screenshot({path:out+'/empty.png'});
 for(const id of ids)await page.locator(`[data-carrier="${id}"]`).check();
 await page.locator('#focus-carriers').click();await page.locator('#scene').screenshot({path:out+'/carriers.png'});
 const ordered=M.lattice.assembly.items.map(item=>item.id);
 assert.equal((await snap()).inspectedItemId,'layer0-item1');
 assert.deepEqual((await snap()).layerCounts,[1,4,44,126]);
 assert.ok((await page.locator('#element-id').textContent()).includes('layer0-item1'));
 await page.evaluate(()=>{const prev=document.getElementById('previous-element');while(!prev.disabled)prev.click();});
 assert.equal((await snap()).inspectedItemId,ordered[0]);assert.ok(await page.locator('#previous-element').isDisabled());
 await page.locator('#next-ten-elements').click();assert.equal((await snap()).inspectedIndex,10);
 await page.locator('#previous-ten-elements').click();assert.equal((await snap()).inspectedIndex,0);
 await page.locator('#next-element').click();await page.locator('#previous-ten-elements').click();assert.equal((await snap()).inspectedIndex,0);
 const labelBox=await page.locator('#element-id').boundingBox(),buttonBox=await page.locator('#next-element').boundingBox();assert.ok(labelBox.y>=buttonBox.y+buttonBox.height);
 const firstMesh=(await snap()).inspectedMeshId;
 await page.locator('#next-element').click();assert.equal((await snap()).inspectedItemId,ordered[1]);
 assert.equal((await snap()).inspectedCellIds.length,4);
 assert.ok((await page.locator('#element-id').textContent()).includes(ordered[1]));
 assert.ok((await page.locator('.realization-label').allTextContents()).includes(ordered[1]));
 await page.locator('#previous-element').click();assert.equal((await snap()).inspectedMeshId,firstMesh);
 const visited=await page.evaluate(()=>{const ids=[SimplexSpaceViewer.snapshot().inspectedItemId];const next=document.getElementById('next-element');while(!next.disabled){next.click();ids.push(SimplexSpaceViewer.snapshot().inspectedItemId);}return ids;});
 assert.deepEqual(visited,ordered);assert.ok(await page.locator('#next-element').isDisabled());assert.ok(await page.locator('#next-ten-elements').isDisabled());
 await page.locator('#previous-element').click();await page.locator('#next-ten-elements').click();assert.equal((await snap()).inspectedIndex,ordered.length-1);
 await page.evaluate(()=>{const prev=document.getElementById('previous-element');while(!prev.disabled)prev.click();});
 const before=await snap();
 const originalMeshes=before.highlightedCells;
 await page.locator('[data-carrier="proton"]').uncheck();await page.locator('[data-carrier="proton"]').check();
 assert.deepEqual((await snap()).highlightedCells,originalMeshes);
 assert.equal(await page.locator('#center-arrows,#reset-center').count(),0);
 assert.ok(!(await page.locator('.realization-label').allTextContents()).some(t=>['B','O','Center','Selected'].includes(t)));
 assert.equal(await page.locator('[data-layer-axis]').count(),8);
 for(let axis=0;axis<4;axis++){
  const button=page.locator(`[data-layer-axis="${axis}"]:enabled`).first();
  const step=Number(await button.getAttribute('data-layer-step')),beforeMove=await snap();
  const oldLayer=M.cellFaceLayers(beforeMove.inspectedElement)[axis].layer;
  await button.click();const moved=await snap();
  assert.equal(M.cellFaceLayers(moved.inspectedElement)[axis].layer,oldLayer+step);
  assert.equal(moved.centerCell,moved.inspectedElement);
  assert.equal(moved.selection.bodies.find(b=>b.id==='proton').cellId,moved.inspectedElement);
  for(const sign of [-1,1])assert.equal(await page.locator(`[data-layer-axis="${axis}"][data-layer-step="${sign}"]`).isDisabled(),M.nextLayerCell(moved.inspectedElement,axis,sign)===null);
 }
 for(const [kind,counts] of [['hydrogen',[1,0,1]],['deuterium',[1,1,1]],['helium',[2,2,2]]]){
  await page.locator('#atom').selectOption(kind);const s=await snap();
  assert.equal(s.atomKind,kind);assert.equal(s.highlightedCells.length,counts.reduce((a,b)=>a+b,0));
  const labels=await page.locator('.atom-vertex-label').allTextContents();
  assert.equal(labels.length,new Set(s.selection.bodies.flatMap(b=>b.nodeIds)).size);
  for(const b of s.selection.bodies)for(const name of b.vertexLabels)assert.ok(labels.some(text=>text.split('\n').includes(b.symbol+':'+name)));
  ['proton','neutron','electron'].forEach((species,i)=>assert.equal(s.selection.bodies.filter(b=>b.species===species).length,counts[i]));
  assert.equal(new Set(s.renderedCarriers.map(b=>b.cellId)).size,s.renderedCarriers.length);
  for(const mesh of s.renderedCarriers)mesh.nodeIds.forEach((id,i)=>assert.ok(distance(mesh.positions.slice(i*3,i*3+3),M.lattice.nodes[id].point)<1e-6));
 }
 await page.locator('[data-carrier="electron"]').uncheck();assert.equal((await snap()).renderedCarriers.length,4);
 await page.locator('[data-carrier="electron"]').check();assert.equal((await snap()).renderedCarriers.length,6);
 await page.locator('#focus-carriers').click();await page.locator('#scene').screenshot({path:out+'/helium.png'});
 await page.locator('#atom').selectOption('manual');assert.equal((await snap()).renderedCarriers.length,0);
 await page.setViewportSize({width:430,height:930});await page.locator('#reset-view').click();assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
 assert.deepEqual(errors,[]);console.log('PASS: simplex coordinates, upright seed, regular tetrahedral envelope, layer-first assembly 1/4/44/126, persistent cell highlights, selectors, minimal UI, mobile layout');
}finally{await browser?.close();await new Promise(r=>server.close(r));}
