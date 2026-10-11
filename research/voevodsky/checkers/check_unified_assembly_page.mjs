import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {chromium} from '@playwright/test';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const store=JSON.parse(await fs.readFile(path.join(root,'research/voevodsky/results/electron_tetrahedral_spinor_store.json'),'utf8'));
const frac=s=>{const p=s.split('/').map(Number);return p.length===1?p[0]:p[0]/p[1];};
const real=p=>frac(p[0])+Math.sqrt(3)*frac(p[1]);
const browser=await chromium.launch({headless:true,args:['--enable-unsafe-swiftshader']});
const errors=[];let samples=0;
try{
 const page=await browser.newPage({viewport:{width:1500,height:1000}});
 page.on('pageerror',e=>errors.push(e.message));
 const audit=async()=>{assert.equal(await page.locator('#error').isVisible(),false,await page.locator('#error').textContent());const a=await page.evaluate(()=>window.electronAssemblyAudit);assert(a);assert(Math.abs(a.totalWeight-1)<1e-10);assert(Math.abs(a.polarization+1)<1e-10);assert(a.reconstructionError<1e-10&&a.covarianceError<1e-10);const markers=await page.evaluate(()=>window.vertexMarkerAudit);assert(markers.count>0);assert(Math.abs(markers.minRadius-markers.standardRadius)<1e-12);assert(Math.abs(markers.maxRadius-markers.standardRadius)<1e-12);samples++;return a;};
 for(const asset of ['papers/witness-generators/proton-neutron-assembly.html','website/public/experiments/proton-neutron-assembly.html']){
  await page.goto(pathToFileURL(path.join(root,asset)).href);
  await page.waitForFunction(()=>window.electronAssemblyAudit||!document.querySelector('#error').hidden);
  let a=await audit();
  store.normals.forEach((n,i)=>n.map(real).forEach((v,j)=>assert(Math.abs(a.normals[i][j]-v)<1e-12)));
  store.face_projectors.forEach((P,i)=>{for(let k=0;k<2;k++)P[k][0].map(real).forEach((v,j)=>assert(Math.abs(a.faceStates[i][k][j]-v/Math.sqrt(2))<1e-12));});
  for(let i=0;i<8;i++){await page.locator(`[data-step="${i}"]`).click();await page.waitForTimeout(1100);await audit();const g=await page.evaluate(()=>window.electronPentachoronAudit);assert.equal(g.geometryStage,i+1);assert.equal(g.filledTriangleCount,i<2?0:i>=3&&i<=5?20:10);assert.equal(g.displayedCellRecords,i>=3&&i<=5?5:0);if(i>=6)assert.equal(g.maxSharedFaceGap,0);}
  assert.equal(await page.getByRole('heading',{name:'Proton / neutron / electron geometry stages',exact:true}).count(),1);
  // Actual DFT guides: complex links stay dotted through a complete return;
  // spatial geometry and the two fixed neutron channels are not discarded.
  const phaseStart=await page.evaluate(()=>window.retainedPhaseAudit);
  assert(phaseStart.visible);assert.equal(phaseStart.complexLinksAreSpatialEdges,false);
  for(const [name,moving,fixed,dotted] of [['proton',4,0,8],['neutron',6,2,12],['electron',5,0,20]]){
   const p=phaseStart.particles[name];assert.equal(p.movingFacets,moving);assert.equal(p.fixedFacets,fixed);assert.equal(p.dottedLinks,dotted);
   for(const c of p.channels){assert.equal(c.material,c.retainedComplex?'LineDashedMaterial':'LineBasicMaterial');if(c.retainedComplex)assert(c.hasLineDistances);}
  }
  assert(phaseStart.particles.neutron.channels.filter(c=>c.facet>=6).every(c=>c.k===0&&!c.retainedComplex));
  for(let tick=1;tick<=15;tick++){
   await page.locator('#phase-tick').fill(String(tick));await page.locator('#phase-tick').dispatchEvent('input');
   const p=await page.evaluate(()=>window.retainedPhaseAudit);assert.equal(p.tick,tick);assert(p.maxDecodeError<1e-10);assert(p.maxMetricError<1e-10);
   for(const name of ['proton','neutron','electron'])assert.equal(p.particles[name].dottedLinks,phaseStart.particles[name].dottedLinks);
   if(tick===15)for(const name of ['proton','neutron','electron'])p.particles[name].channels.forEach((c,i)=>c.tip.forEach((x,j)=>assert(Math.abs(x-phaseStart.particles[name].channels[i].tip[j])<1e-6)));
  }
  await page.locator('#phase-links').uncheck();assert.equal((await page.evaluate(()=>window.retainedPhaseAudit)).visible,false);
  await page.locator('#phase-links').check();await page.locator('#phase-reset').click();
  await page.locator('#phase-play').click();await page.waitForTimeout(720);assert((await page.evaluate(()=>window.retainedPhaseAudit)).tick>0);
  await page.locator('#phase-reset').click();assert.equal(await page.locator('#phase-play').getAttribute('aria-pressed'),'false');
  assert.equal((await page.evaluate(()=>window.retainedPhaseAudit)).tick,0);
  await page.locator('#electron-panel summary').click();
  const geometry=await page.evaluate(()=>({p:window.protonAssemblyAudit,n:window.assemblyAudit}));
  assert.equal(geometry.p.maxSharedFaceGap,0);assert.equal(geometry.n.maxSharedFaceGap,0);assert.equal(geometry.n.sectors,3);
  for(let i=0;i<6;i++){await page.locator(`[data-electron-step="${i}"]`).click();await audit();}
  for(const [t,p]of [[180,0],[45,30],[90,90],[120,-60]]){await page.locator('#electron-theta').fill(String(t));await page.locator('#electron-theta').dispatchEvent('input');await page.locator('#electron-phi').fill(String(p));await page.locator('#electron-phi').dispatchEvent('input');await audit();}
  await page.locator('#electron-zero').click();a=await audit();assert(a.weights[0]<1e-12);
  await page.locator('[data-electron-step="5"]').click();
  for(const [angle,sign]of [[360,-1],[720,1],[0,1]]){await page.locator(`[data-turn="${angle}"]`).click();a=await audit();assert(Math.abs(a.referenceOverlap[0]-sign)<1e-10);assert(Math.abs(a.referenceOverlap[1])<1e-10);}
  for(const focus of ['proton','neutron','electron','all']){await page.locator('#focus').selectOption(focus);await audit();}
  await page.locator('#focus').selectOption('electron-positron');
  assert.equal(await page.locator('#pair-comparison-panel').isVisible(),true);
  for(let i=0;i<8;i++){await page.locator(`[data-step="${i}"]`).click();await page.waitForTimeout(1100);const pair=await page.evaluate(()=>({a:window.electronPositronAudit,g:window.inspectElectronPositronGeometry()}));assert.equal(pair.a.geometryStage,i+1);assert(pair.g[0].length>0);assert.deepEqual(pair.g[0],pair.g[1]);assert.equal(pair.a.chargeAssigned,false);assert.equal(pair.a.chargeConjugationDerived,false);assert.equal(pair.a.annihilationDerived,false);}
  for(const phase of ['-90','0','45','180']){await page.locator('#pair-phase').fill(phase);await page.locator('#pair-phase').dispatchEvent('input');const p=await page.evaluate(()=>window.electronPositronAudit);assert.equal(p.phaseDegrees,+phase);assert.equal(p.coefficients[0][0],p.coefficients[1][0]);assert.equal(p.coefficients[0][1],-p.coefficients[1][1]);}
  await page.locator('#focus').selectOption('all');assert.equal(await page.locator('#pair-comparison-panel').isVisible(),false);
  for(const arrangement of ['h1','h2','h1']){await page.locator('#assembly').selectOption(arrangement);await page.waitForFunction(()=>window.hydrogenAssemblyAudit.progress===1);const h=await page.evaluate(()=>window.hydrogenAssemblyAudit);assert.equal(h.neutrons,arrangement==='h1'?0:1);assert.equal(h.visible.neutron,arrangement==='h2');assert.equal(h.visible.proton,true);assert.equal(h.visible.electron,true);const ep=await page.evaluate(()=>window.electronPentachoronAudit);assert.equal(ep.dimension,4);assert.equal(ep.facets.length,5);assert.equal(ep.drawnVertexCount,5);assert.equal(ep.drawnEdgeCount,10);assert.equal(ep.filledTriangleCount,10);assert.equal(ep.filledTrianglesAtE,6);assert.equal(ep.spinorGuidesVisible,false);assert.equal(ep.vertices4D.length,5);for(let i=0;i<5;i++)for(let j=i+1;j<5;j++){const d=ep.vertices4D[i].reduce((s,x,k)=>s+(x-ep.vertices4D[j][k])**2,0);assert(Math.abs(d-8)<1e-12);}assert.deepEqual(ep.attachmentTriangle,[0,1,2]);const cell=ep.projectedVertices.slice(0,4);for(const value of ['0','1.4','0']){await page.locator('#electron-lift').fill(value);await page.locator('#electron-lift').dispatchEvent('input');const changed=await page.evaluate(()=>window.electronPentachoronAudit);assert.deepEqual(changed.projectedVertices.slice(0,4),cell);assert.equal(changed.projection,+value);}
  if(arrangement==='h1'){assert(h.sharedFaceGap<1e-12);assert(h.apexSides[0]*h.apexSides[1]<0);assert.equal(await page.locator('#electron-angle').isDisabled(),true);}else {assert(h.lowerRimGap<1e-12);assert(h.upperRimGap<1e-12);assert(h.protonApexY<h.lowerRimY);assert(h.electronApexY>h.upperRimY);assert(h.lowerRimY<h.upperRimY);assert(Math.abs(h.beltDisplayScale-Math.sqrt(8/3))<1e-12);}await audit();}
  // Geometry navigation after an attached isotope must restore independent frames.
  for(let i=0;i<8;i++){await page.locator(`[data-step="${i}"]`).click();await page.waitForTimeout(1100);assert.equal(await page.locator('#assembly').inputValue(),'separate');const layout=await page.evaluate(()=>window.inspectGeometryLayout());layout.forEach((g,j)=>{assert.deepEqual(g.position,[-6+6*j,0,0]);assert.deepEqual(g.rotation,[0,0,0,1]);assert.deepEqual(g.scale,[1,1,1]);});assert(layout[0].bounds.max[0]<layout[1].bounds.min[0]);assert(layout[1].bounds.max[0]<layout[2].bounds.min[0]);}
  await page.locator('#assembly').selectOption('h2');await page.waitForFunction(()=>window.hydrogenAssemblyAudit.progress===1);
  await page.locator('#replay-assembly').click();await page.waitForFunction(()=>window.hydrogenAssemblyAudit.progress>0&&window.hydrogenAssemblyAudit.progress<1);const moving=await page.evaluate(()=>window.hydrogenAssemblyAudit);assert(moving.progress>0&&moving.progress<1);await page.setViewportSize({width:1450,height:950});await page.waitForTimeout(80);const resized=await page.evaluate(()=>window.hydrogenAssemblyAudit);assert(resized.progress<1);await page.waitForFunction(()=>window.hydrogenAssemblyAudit.progress===1);
  await page.locator('#assembly').selectOption('separate');
  await page.locator('#pentachoron-panel summary').click();
  await page.locator('#pentachoron-enabled').check();
  let trial=await page.evaluate(()=>window.pentachoronAssemblyAudit);assert.equal(trial.facets.length,2);assert.equal(trial.dimension,4);assert.equal(trial.chargeAssigned,false);
  const base=trial.projectedVertices;
  for(const [choice,count]of [['complement',3],['all',5],['pair',2]]){await page.locator('#pentachoron-cells').selectOption(choice);trial=await page.evaluate(()=>window.pentachoronAssemblyAudit);assert.equal(trial.facets.length,count);}
  await page.locator('#pentachoron-projection').fill('1');await page.locator('#pentachoron-projection').dispatchEvent('input');trial=await page.evaluate(()=>window.pentachoronAssemblyAudit);assert(Math.abs(trial.projectedVertices[4][0]-base[4][0]-1)<1e-12);assert.deepEqual(trial.projectedVertices.slice(0,4),base.slice(0,4));
  const outward=trial.path;await page.locator('#pentachoron-direction').selectOption('inward');trial=await page.evaluate(()=>window.pentachoronAssemblyAudit);assert.deepEqual(trial.path,[...outward].reverse());
  await page.locator('#pentachoron-progress').fill('2');await page.locator('#pentachoron-progress').dispatchEvent('input');assert.equal((await page.evaluate(()=>window.pentachoronAssemblyAudit)).progress,2);
  await page.locator('#pentachoron-enabled').uncheck();await page.locator('#assembly').selectOption('separate');
  assert.equal(await page.locator('canvas').count(),1);
  for(const width of [600,390,1500]){await page.setViewportSize({width,height:900});await page.waitForTimeout(150);await audit();const box=await page.locator('#view').boundingBox();assert(box.width>0&&box.height>150);assert(box.x+box.width<=width+1);}
 }
 assert.deepEqual(errors,[]);
 const result={verification_passed:true,samples,source_and_public_asset:true,electron_positron_comparison_all_stages:true,illustrative_conjugation_not_charge_assignment:true,shared_geometry_stages:8,retained_complex_links_dotted_all_phase_steps:true,neutron_fixed_cap_channels_retained:true,facet_mode_decode_and_metric_checks:true,phase_play_pause_reset:true,separate_geometry_frames_after_isotope:true,nonoverlapping_geometry_bounds_all_stages:true,resize_preserves_replay:true,electron_operator_checks:6,electron_geometry_responds_to_every_shared_stage:true,exact_store_normals_and_seed_projection_match:true,zero_face_and_rotation_checks:true,focus_and_mobile_checks:true,hydrogen_isotope_assembly_and_replay:true,h1_shared_face_coincidence_and_opposite_apices:true,h2_both_rims_coincide_and_apices_outside_belt:true,pentachoron_projection_cells_and_direction:true,electron_regular_pentachoron_in_both_isotopes:true,page_errors:errors};
 await fs.writeFile(path.join(root,'research/voevodsky/results/unified_assembly_browser.json'),JSON.stringify(result,null,2)+'\n');
 console.log(JSON.stringify(result,null,2));
}finally{await browser.close();}
