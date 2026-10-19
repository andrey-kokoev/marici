import assert from 'node:assert/strict';
import './check_simplex_components.mjs';
import './check_atom_models.mjs';
import './check_lead208_model.mjs';
import './check_sequential_space.mjs';
import './check_window_construction.mjs';
import './check_fiber_coverage.mjs';
import './check_deuterium_tunnel.mjs';
import './check_deuterium_cycles.mjs';
import './check_helium3_tunnel.mjs';
import './check_helium4_core.mjs';
import './check_helium4_window.mjs';
import './check_lithium6_growth.mjs';
import './check_lithium6_assembly.mjs';
import './check_phase_discipline.mjs';
import './check_phase_assembly.mjs';
import './check_lithium7_assembly.mjs';
import './check_beryllium9_assembly.mjs';
import './check_boron_assemblies.mjs';
import './check_carbon_assemblies.mjs';
import './check_window_attachment_recovery.mjs';
import {mkdir,readFile,writeFile} from 'node:fs/promises';
import {createServer} from 'node:http';
import path from 'node:path';
import {chromium} from '@playwright/test';
import * as F from '../demos/particle-overlap-tetrahedron/fiber-space-model.mjs';
assert.deepEqual(F.lattice.assembly.layers.map(l=>l.items.length),[1,4,44,126]);
assert.equal(new Set(F.traversal).size,175);
for(const perspective of [0,1])for(const {a,b} of F.connections){const route=[...F.pathBetween(0,a),b,...F.pathBetween(b,0).slice(1)];assert.equal(F.transport(route,perspective).canonical,0);}
const root=path.resolve('public'),out='research/strominger/results/fiber-space';await mkdir(out,{recursive:true});
const server=createServer(async(req,res)=>{try{const file=path.resolve(root,'.'+new URL(req.url,'http://localhost').pathname);if(path.relative(root,file).startsWith('..'))throw Error('path');res.setHeader('Content-Type',file.endsWith('.html')?'text/html':file.endsWith('.css')?'text/css':'text/javascript');res.end(await readFile(file));}catch{res.writeHead(404);res.end();}});
await new Promise(r=>server.listen(0,'127.0.0.1',r));let browser;
try{
 browser=await chromium.launch({headless:true,args:['--enable-webgl','--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
 const page=await browser.newPage({viewport:{width:1480,height:1040}}),errors=[];page.on('pageerror',e=>errors.push(String(e)));page.on('console',m=>{if(m.type()==='error'&&/shader|WebGLProgram|VALIDATE_STATUS/i.test(m.text()))errors.push(m.text());});
 await page.goto(`http://127.0.0.1:${server.address().port}/experiments/particle-overlap-tetrahedron/vacuum.html`);await page.waitForFunction(()=>globalThis.FiberSpaceViewer?.snapshot().frameCount>2);
 const snap=()=>page.evaluate(()=>FiberSpaceViewer.snapshot()),state=()=>page.evaluate(()=>FiberSpaceViewer.sequentialSnapshot());
 assert.deepEqual(await page.locator('button').allTextContents(),['Previous item','Next item']);
 assert.equal(await page.locator('#construction-step,#toward-entry,#toward-exit,#previous-cycle,#next-cycle,#read-electron,#reset-view').count(),0);
 assert.equal(await page.locator('#atom option[value="lithium6"]').count(),1);
 assert.equal(await page.locator('option[value="nitrogen14"]').count(),0);
 assert.equal(await page.locator('option[value="nitrogen15"]').count(),2);
 assert.equal(await page.evaluate(()=>['passSequential','crossRealization','readElectron'].some(k=>k in FiberSpaceViewer)),false);
 assert.deepEqual(await page.locator('.particle-legend li').allTextContents(),['P — Proton (cyan)','N — Neutron (gold)','E — Electron (pink)']);
 assert.deepEqual(await page.locator('.particle-swatch').evaluateAll(nodes=>nodes.map(n=>getComputedStyle(n).backgroundColor)),['rgb(80, 207, 255)','rgb(255, 207, 114)','rgb(255, 126, 219)']);
 const geometry=(await snap()).geometryIds;
 const assertOrthogonal=async()=>{const p=(await snap()).projection;assert.equal(p.type,'orthographic');p.direction.forEach((x,i)=>assert.ok(Math.abs(x-[0,0,-1][i])<1e-10));};
 await assertOrthogonal();
 assert.equal(await page.getByLabel('Show vertex labels').isChecked(),true);
 const strokes=(await snap()).edgeStyle;assert.equal(strokes.rendering,'LineSegments2');assert.ok(strokes.strokes.length>0);assert.ok(strokes.strokes.every(s=>s.color==='#000000'&&s.type==='LineSegments2'&&s.material==='LineMaterial'&&s.widthPx===2&&s.opacity===1&&s.depthTest&&s.depthWrite&&!s.transparent));
 const occlusion=await page.evaluate(async()=>{
  const {createEdgeSegments}=await import(new URL('./edge-segments.mjs',location.href).href),T=globalThis.THREE,r=new T.WebGLRenderer({antialias:false,preserveDrawingBuffer:true});r.setSize(32,32,false);
  const scene=new T.Scene();scene.background=new T.Color(0xffffff);const camera=new T.OrthographicCamera(-1,1,1,-1,.1,10);camera.position.z=5;
  const face=new T.Mesh(new T.PlaneGeometry(1.5,1.5),new T.MeshBasicMaterial({color:0xff0000})),stroke=createEdgeSegments(T);stroke.setResolution(32,32);stroke.setPairs([[[-1,0,-1],[1,0,-1]]]);scene.add(face,stroke);
  const sample=()=>{r.render(scene,camera);const p=new Uint8Array(4);r.getContext().readPixels(16,16,1,1,r.getContext().RGBA,r.getContext().UNSIGNED_BYTE,p);return [...p].slice(0,3);};
  const samples=[];for(const opacity of [1,.99,.75,.5,.25,.01,0]){face.material.transparent=opacity<1;face.material.opacity=opacity;face.material.depthWrite=opacity===1;face.material.needsUpdate=true;samples.push({opacity,pixel:sample()});}
  stroke.setPairs([[[-1,0,1],[1,0,1]]]);face.material.opacity=.99;face.material.transparent=true;face.material.depthWrite=false;face.material.needsUpdate=true;const front=sample();
  face.geometry.dispose();face.material.dispose();stroke.geometry.dispose();stroke.material.dispose();r.dispose();return {samples,front};
 });for(const {opacity,pixel} of occlusion.samples){assert.ok(Math.abs(pixel[0]-255*opacity)<=1);assert.deepEqual(pixel.slice(1),[0,0]);}assert.deepEqual(occlusion.front,[0,0,0]);
 const setTransparency=async percent=>{await page.locator('#face-transparency').evaluate((el,value)=>{el.value=String(value);el.dispatchEvent(new Event('input',{bubbles:true}));},percent);const s=await snap();assert.equal(s.faceTransparencyPercent,percent);for(const style of Object.values(s.faceStyles)){assert.ok(Math.abs(style.opacity-(1-percent/100))<1e-12);assert.equal(style.transparent,percent>0);assert.equal(style.depthWrite,percent===0);}assert.equal(s.electronStyle.dotted,true);assert.deepEqual(s.edgeStyle,strokes);assert.equal(await page.locator('#face-transparency-value').textContent(),percent+'%');};
 await page.locator('#face-transparency').focus();await page.locator('#face-transparency').press('Home');await page.locator('#face-transparency').press('ArrowRight');assert.equal((await snap()).faceTransparencyPercent,1);
 for(const percent of [0,50,100,35])await setTransparency(percent);
 for(const [kind,total,phaseStatus] of [['sequential',3,'native-phase-compatible'],['helium3',5,'phase-coherent-reference'],['helium4',6,'phase-coherent-reference'],['lithium6',9,'phase-coherent-reference'],['lithium7',10,'phase-coherent-reference'],['beryllium9',13,'phase-coherent-reference'],['boron10',15,'phase-coherent-reference'],['boron11',16,'phase-coherent-reference'],['carbon12',18,'phase-coherent-reference'],['carbon13',19,'phase-coherent-reference'],['nitrogen15',22,'phase-coherent-reference']]){
  await page.locator('#atom').selectOption(kind);await assertOrthogonal();assert.equal((await snap()).faceTransparencyPercent,35);assert.equal((await snap()).visibleComponentCount,total);
  await page.locator('#next-item').click();const prefixes=[await state()];
  assert.equal((await snap()).visibleComponentCount,1);assert.equal(await page.locator('#previous-item').isDisabled(),false);
  for(let n=2;n<=total;n++){
   await page.locator('#next-item').click();const s=await snap(),next=await state();
   assert.equal(s.visibleComponentCount,n);assert.equal(s.uniqueVisibleCells,n);assert.equal(next.items.length,n);assert.deepEqual(next.items.slice(0,-1),prefixes.at(-1).items);prefixes.push(next);
   assert.deepEqual(s.geometryIds,geometry);assert.equal(s.decorativeMeshCount,0);assert.equal(s.routeVisible,false);assert.equal(s.visibleAddedComponents,0);assert.equal(s.phaseAudit.status,phaseStatus);assert.equal(s.faceTransparencyPercent,35);assert.deepEqual(s.faceStyles.proton,s.faceStyles.electron);assert.deepEqual(s.faceStyles.neutron,s.faceStyles.electron);
  }
  assert.equal(await page.locator('#next-item').isDisabled(),false);
  assert.ok((await page.locator('#loadout-readout').textContent()).includes(`${total}/${total} items`));
  assert.equal((await snap()).coverage.coveredCells,total);
  if(phaseStatus==='phase-coherent-reference'){
   const proof=await state();assert.ok((await page.locator('#loadout-readout').textContent()).includes(`R${proof.displayPhase.origin}: ${proof.displayPhase.word}`));
   assert.deepEqual((await page.locator('.realization-label').allTextContents()).sort(),proof.displayVertexLabels.map(label=>label.text).sort());
   assert.ok(proof.displayVertexLabels.every(label=>/^[CM]\d+( \/ [CM]\d+)*$/.test(label.text)));
   assert.equal(proof.displayVertexLabels.length,new Set(proof.items.flatMap(item=>item.vertices.map(p=>JSON.stringify(p)))).size);
   assert.equal(proof.displayVertexLabels.reduce((sum,label)=>sum+label.occurrences.length,0),4*total);
   const displayedOwners=await page.locator('.realization-label[data-item-indices]').evaluateAll(els=>[...new Set(els.flatMap(el=>el.dataset.itemIndices.split(',').map(Number)))].sort((a,b)=>a-b));
   assert.deepEqual(displayedOwners,Array.from({length:total},(_,i)=>i));assert.equal(proof.phaseAudit.allFiveSlotsRetained,true);
  }
  await page.getByLabel('Show vertex labels').uncheck();
  await page.waitForFunction(()=>[...document.querySelectorAll('.realization-label')].every(el=>el.hidden));
  const beforeToggle=await state();await page.locator('#previous-item').click();await page.locator('#next-item').click();assert.deepEqual(await state(),beforeToggle);
  assert.equal((await snap()).showVertexLabels,false);assert.equal(await page.locator('.realization-label:visible').count(),0);
  await page.getByLabel('Show vertex labels').check();await page.waitForFunction(()=>[...document.querySelectorAll('.realization-label')].some(el=>!el.hidden));
  await page.screenshot({path:out+'/'+kind+'-assembly.png'});
  for(let n=total-1;n>=1;n--){await page.locator('#previous-item').click();assert.equal((await snap()).visibleComponentCount,n);assert.deepEqual(await state(),prefixes[n-1]);}
  assert.equal(await page.locator('#previous-item').isDisabled(),false);
  await page.locator('#previous-item').click();assert.deepEqual(await state(),prefixes.at(-1));await page.locator('#next-item').click();assert.deepEqual(await state(),prefixes[0]);
  for(let n=2;n<=total;n++)await page.locator('#next-item').click();assert.deepEqual(await state(),prefixes.at(-1));
  await page.setViewportSize({width:430,height:930});assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  await setTransparency(75);await setTransparency(35);const sliderBox=await page.locator('#face-transparency').boundingBox();assert.ok(sliderBox.width>sliderBox.height);
  await page.locator('#previous-item').click();assert.equal((await snap()).visibleComponentCount,total-1);await page.locator('#next-item').click();assert.equal((await snap()).visibleComponentCount,total);
  await page.screenshot({path:out+'/'+kind+'-assembly-mobile.png'});await page.setViewportSize({width:1480,height:1040});
 }
 for(const [first,second,aTotal,bTotal] of [['helium3','helium4',5,6],['helium4','helium3',6,5],['sequential','lithium6',3,9],['lithium6','lithium7',9,10],['lithium7','lithium6',10,9],['lithium7','beryllium9',10,13],['beryllium9','lithium7',13,10],['beryllium9','boron10',13,15],['boron10','boron11',15,16],['boron11','boron10',16,15],['boron11','carbon12',16,18],['carbon12','carbon13',18,19],['carbon13','carbon12',19,18],['carbon13','nitrogen15',19,22],['nitrogen15','carbon13',22,19]]){
  await page.locator('#atom').selectOption(first);await page.locator('#comparison-atom').selectOption(second);
  assert.equal((await snap()).comparison.primaryShown,aTotal);assert.equal((await snap()).comparison.secondary.shown,bTotal);
  await page.locator('#next-item').click();assert.equal((await snap()).comparison.step,1);
  const a=[await state()],b=[await page.evaluate(()=>FiberSpaceViewer.comparisonSnapshot())],total=Math.max(aTotal,bTotal);
  assert.equal((await snap()).comparison.layout,'side-by-side');
  for(let n=2;n<=total;n++){
   await page.locator('#next-item').click();const s=await snap();a.push(await state());b.push(await page.evaluate(()=>FiberSpaceViewer.comparisonSnapshot()));
   assert.equal(s.comparison.step,n);assert.equal(s.comparison.primaryShown,Math.min(n,aTotal));assert.equal(s.comparison.secondary.shown,Math.min(n,bTotal));assert.equal(s.comparison.visibleComponents,Math.min(n,bTotal));assert.deepEqual(s.comparison.faceOpacities,[.65]);assert.equal(s.decorativeMeshCount,0);
   if(first==='helium3'&&second==='helium4'&&n===4){assert.notDeepEqual(a.at(-1).items.map(i=>i.key),b.at(-1).items.map(i=>i.key));await setTransparency(0);await page.screenshot({path:out+'/helium3-helium4-step4-opaque.png'});await setTransparency(35);}
  }
  if(first==='lithium6'&&second==='lithium7')await page.screenshot({path:out+'/lithium6-lithium7-comparison.png'});
  if(first==='lithium7'&&second==='beryllium9')await page.screenshot({path:out+'/lithium7-beryllium9-comparison.png'});
  if(first==='boron10'&&second==='boron11')await page.screenshot({path:out+'/boron10-boron11-comparison.png'});
  if(first==='carbon12'&&second==='carbon13')await page.screenshot({path:out+'/carbon12-carbon13-comparison.png'});
  if(first==='carbon13'&&second==='nitrogen15')await page.screenshot({path:out+'/carbon13-nitrogen15-comparison.png'});
  assert.equal(await page.locator('#next-item').isDisabled(),false);
  for(const [slot,totalItems] of [['primary',aTotal],['secondary',bTotal]])if(first!=='sequential'||slot==='secondary'){
   const owners=await page.locator(`.realization-label[data-slot="${slot}"][data-item-indices]`).evaluateAll(els=>[...new Set(els.flatMap(el=>el.dataset.itemIndices.split(',').map(Number)))].sort((a,b)=>a-b));assert.deepEqual(owners,Array.from({length:totalItems},(_,i)=>i));
  }
  if(first==='helium3'&&second==='helium4'){
   await page.screenshot({path:out+'/helium3-helium4-comparison.png'});
   await page.getByLabel('Show vertex labels').uncheck();await page.waitForFunction(()=>[...document.querySelectorAll('.realization-label.node')].every(el=>el.hidden));
   assert.equal(await page.locator('.realization-label.carrier:visible').count(),2);await setTransparency(75);assert.deepEqual((await snap()).comparison.faceOpacities,[.25]);await setTransparency(35);
   await page.getByLabel('Show vertex labels').check();await page.waitForFunction(()=>[...document.querySelectorAll('.realization-label.node')].every(el=>!el.hidden));
  }
  for(let n=total-1;n>=1;n--){await page.locator('#previous-item').click();assert.deepEqual(await state(),a[n-1]);assert.deepEqual(await page.evaluate(()=>FiberSpaceViewer.comparisonSnapshot()),b[n-1]);}
  assert.equal(await page.locator('#previous-item').isDisabled(),false);await page.locator('#previous-item').click();assert.deepEqual(await state(),a.at(-1));assert.deepEqual(await page.evaluate(()=>FiberSpaceViewer.comparisonSnapshot()),b.at(-1));await page.locator('#next-item').click();assert.equal((await snap()).comparison.step,1);await page.locator('#comparison-atom').selectOption('none');assert.equal((await snap()).comparison,null);assert.deepEqual((await snap()).geometryIds,geometry);
 }
 await page.getByLabel('Show vertex labels').uncheck();await page.locator('#atom').selectOption('helium3');assert.equal((await snap()).showVertexLabels,false);assert.equal(await page.locator('.realization-label:visible').count(),0);await page.getByLabel('Show vertex labels').check();
 for(const [kind,total] of [['hydrogen',2],['deuterium',3],['helium',6]]){
  await page.locator('#atom').selectOption(kind);assert.equal((await snap()).visibleComponentCount,total);await page.locator('#next-item').click();assert.equal((await snap()).visibleComponentCount,1);
  for(let n=2;n<=total;n++){await page.locator('#next-item').click();assert.equal((await snap()).visibleComponentCount,n);}
  assert.equal(await page.locator('#next-item').isDisabled(),false);assert.equal((await snap()).electronStyle.dotted,true);assert.deepEqual((await snap()).geometryIds,geometry);
  for(let n=total-1;n>=1;n--){await page.locator('#previous-item').click();assert.equal((await snap()).visibleComponentCount,n);}
 }
 await page.locator('#atom').selectOption('lead208');assert.equal((await snap()).visibleLeadBodies.length,290);await page.locator('#next-item').click();assert.equal((await snap()).visibleLeadBodies.length,1);
 await page.evaluate(()=>{while(FiberSpaceViewer.snapshot().assemblyDisplay.shown<FiberSpaceViewer.snapshot().assemblyDisplay.total)FiberSpaceViewer.nextItem();});
 let s=await snap();assert.equal(s.visibleLeadBodies.length,290);assert.equal(s.visibleAddedComponents,418);assert.equal(s.componentMeshCount,761);assert.deepEqual(s.geometryIds,geometry);
 await page.locator('#previous-item').click();assert.equal((await snap()).visibleLeadBodies.length,289);await page.locator('#next-item').click();assert.equal((await snap()).visibleLeadBodies.length,290);
 await page.locator('#neutron-channel').uncheck();assert.equal((await snap()).visibleLeadBodies.filter(b=>b.species==='neutron').length,0);await page.locator('#neutron-channel').check();
 await page.locator('#atom').selectOption('none');assert.equal((await snap()).visibleComponentCount,343);assert.equal(await page.locator('#previous-item').isDisabled(),true);assert.equal(await page.locator('#next-item').isDisabled(),true);
 await page.locator('#atom').selectOption('helium3');await page.locator('#comparison-atom').selectOption('helium4');
 const rotationToggle=page.locator('#rotate-shapes');assert.equal(await rotationToggle.isEnabled(),true);await rotationToggle.check();
 const beforeRotation=await snap(),canvas=await page.locator('#scene canvas').boundingBox();
 const drag=async()=>{await page.mouse.move(canvas.x+canvas.width*.4,canvas.y+canvas.height*.5);await page.mouse.down();await page.mouse.move(canvas.x+canvas.width*.4+110,canvas.y+canvas.height*.5+55,{steps:12});await page.mouse.up();await page.waitForFunction(n=>FiberSpaceViewer.snapshot().frameCount>n+3,(await snap()).frameCount);};
 await drag();const rotated=await snap();assert.equal(rotated.shapeRotation.enabled,true);assert.deepEqual(rotated.projection,beforeRotation.projection);
 assert.notDeepEqual(rotated.shapeRotation.frames[0].quaternion,beforeRotation.shapeRotation.frames[0].quaternion);assert.deepEqual(rotated.shapeRotation.frames[0].quaternion,rotated.shapeRotation.frames[1].quaternion);
 const assertAnchors=s=>s.shapeRotation.frames.forEach((f,i)=>{assert.deepEqual(f.anchor,beforeRotation.shapeRotation.frames[i].anchor);f.worldCenter.forEach((v,j)=>assert.ok(Math.abs(v-f.anchor[j])<1e-9));});assertAnchors(rotated);
 await page.locator('#previous-item').click();assertAnchors(await snap());assert.deepEqual((await snap()).shapeRotation.frames[0].quaternion,rotated.shapeRotation.frames[0].quaternion);
 await page.screenshot({path:out+'/paired-local-rotation.png'});
 await rotationToggle.uncheck();await drag();const orbited=await snap();assert.notDeepEqual(orbited.projection.direction,rotated.projection.direction);assert.deepEqual(orbited.shapeRotation.frames[0].quaternion,rotated.shapeRotation.frames[0].quaternion);
 await rotationToggle.check();await drag();assertAnchors(await snap());assert.deepEqual((await snap()).shapeRotation.frames[0].quaternion,(await snap()).shapeRotation.frames[1].quaternion);
 await page.locator('#comparison-atom').selectOption('none');assert.equal(await rotationToggle.isDisabled(),true);assert.equal((await snap()).shapeRotation.enabled,false);
 await page.locator('#atom').selectOption('helium4');assert.equal((await snap()).visibleComponentCount,6);assert.deepEqual(await page.locator('button').allTextContents(),['Previous item','Next item']);
 assert.deepEqual(errors,[]);
 await writeFile(out+'/verification.json',JSON.stringify({status:'pass-phase-gated-assembly-display',buttons:['Previous item','Next item'],itemRoundTrips:{deuterium:3,helium3:5,helium4:6,lithium6:9,lithium7:10,beryllium9:13,boron10:15,boron11:16,carbon12:18,carbon13:19,nitrogen15:22},legacyAssemblyControls:true,orthographicProjection:true,defaultViewAxis:'Z',edgeColor:'#000000',edgeWidthPx:2,edgeImplementation:'Three.js r128 LineSegments2 / LineMaterial',edgeCompositing:occlusion,edgesDepthTested:true,initiallyAssembled:true,loopingItemButtons:true,plainCMLabels:true,vertexLabelToggle:true,vertexLabelsCoverAllVisibleShapes:true,sharedVertexPhaseOccurrencesPreserved:true,sharedFaceTransparencySlider:true,pairedAssemblies:{synchronizedOwnCenterRotation:true,sceneOrbitToggle:true,rotationAnchorsStableAcrossSteps:true,sharedStep:true,unequalLengthReversal:true,desktopSideBySide:true,responsiveRearrangement:false,allShapesLabelled:true},meshIdentityPreserved:true,tubes:false,transportControls:false,lithiumViewerAdmitted:true,lithium7ViewerAdmitted:true,beryllium9ViewerAdmitted:true,boron10ViewerAdmitted:true,boron11ViewerAdmitted:true,carbon12ViewerAdmitted:true,carbon13ViewerAdmitted:true,nitrogen15ViewerAdmitted:true,nitrogen14ViewerAdmitted:false,helium3PhaseAdmitted:true,helium4PhaseAdmitted:true,admissionScope:'phase-coherent reference, not derived physical binding',geometryIdentifiersSeparatedFromPhaseLabels:true,desktop:true,mobile:true,scope:'Assembly display only. He-3, He-4, Li-6, Li-7, Be-9, B-10, B-11, C-12, C-13 and N-15 use ordered phase-advance witnesses with retained full context and all face modes. Labels cover all visible items with plain C/M names; full provenance remains in the model data. Outside-context transport remains a reference law, not a derivation of physical binding.'},null,2)+'\n');
 console.log('PASS viewer: only Previous item / Next item; phase-checked He-3 / He-4 / Li-6 / Li-7 / Be-9 / B-10 / B-11 / C-12 / C-13 / N-15, reversible assembly display, witnessed phase labels, no transport controls; desktop/mobile.');
}finally{await browser?.close();await new Promise(r=>server.close(r));}
