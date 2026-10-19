import assert from 'node:assert/strict';
import {createServer} from 'node:http';
import {readFile,writeFile,mkdir,stat} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import {chromium} from '@playwright/test';
import * as C from '../demos/particle-overlap-tetrahedron/carrier.mjs';
import * as M from '../demos/particle-overlap-tetrahedron/model.mjs';
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..'),PUBLIC=path.join(ROOT,'public'),OUT=path.join(ROOT,'research/strominger/results/particle-carrier-viewer');
const checks={},ck=(n,b)=>{assert.ok(b,n);checks[n]=true;};
const near=(a,b,tol=1e-10)=>assert.ok(Math.hypot(...a.flat(Infinity).map((v,i)=>v-b.flat(Infinity)[i]))<tol);
const hash=b=>createHash('sha256').update(b).digest('hex');
function volume(points){const [a,...rest]=points,[u,v,w]=rest.map(p=>p.map((x,i)=>x-a[i]));return Math.abs(u[0]*(v[1]*w[2]-v[2]*w[1])-u[1]*(v[0]*w[2]-v[2]*w[0])+u[2]*(v[0]*w[1]-v[1]*w[0]))/6;}
async function main(){
  await mkdir(OUT,{recursive:true});
  for(const body of C.bodies){near([C.orientedVolume(body.nodes)**2],[(8/3)**2]);for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)near([M.distanceSquared(C.points[body.nodes[i]],C.points[body.nodes[j]])],[8]);}
  checks.both_source_facets_unfold_as_regular_positive_volume_tetrahedra=true;
  assert.deepEqual(C.bodies.map(b=>({id:b.id,window:b.window,continuation:b.continuation})),[{id:'proton',window:['C0','M0','C1'],continuation:'M1'},{id:'neutron',window:['M0','C1','M1'],continuation:'C2'}]);
  ck('proton_CMC_M1_and_neutron_MCM_C2_are_distinct_four_vertex_carriers',C.bodies.every(b=>b.nodes.join(',')===[...b.window,b.continuation].join(','))&&!C.bodies[1].nodes.includes('C0'));
  ck('actual_four_vertex_bodies_share_exactly_the_original_MCM_face',C.bodies.every(b=>b.nodes.length===4)&&C.sharedFace.every(n=>C.bodies.every(b=>b.nodes.includes(n)))&&C.edges.length===9);
  ck('tetrahedra_interiors_on_opposite_sides_of_shared_plane',C.points.C0.reduce((a,b)=>a+b,0)>-1&&C.points.C2.reduce((a,b)=>a+b,0)<-1&&C.sharedFace.every(n=>Math.abs(C.points[n].reduce((a,b)=>a+b,0)+1)<1e-12));
  ck('not_falsely_a_global_pentachoron_isometry',Math.abs(M.distanceSquared(C.points.C0,C.points.C2)-8)>1&&M.distanceSquared(M.pentachoron.C0,M.pentachoron.C2)<8+1e-10);
  const trial=C.trial,ep=trial.points;
  for(const body of trial.bodies){near([Math.abs(C.orientedVolume(body.nodes,ep))],[8/3]);for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)near([M.distanceSquared(ep[body.nodes[i]],ep[body.nodes[j]])],[8]);}
  ck('M2_trial_has_three_regular_nonzero_volume_tetrahedra',trial.bodies.length===3&&Object.keys(ep).length===6&&trial.edges.length===12);
  const electron=trial.bodies[2];assert.deepEqual(electron.window,['M1','C1','C2']);assert.deepEqual(electron.nodes,['M1','C1','C2','M2']);
  ck('electron_MCC_M2_has_a_new_distinct_continuation_identity',electron.continuation==='M2'&&trial.extension.originalSourceVertex===false&&Object.values(C.points).every(p=>M.distanceSquared(p,ep.M2)>1e-8));
  near(ep.M2,[-31/9,-1/9,-1/9]);for(const [n,p]of Object.entries(C.points))assert.deepEqual(ep[n],p);
  ck('trial_does_not_move_any_original_PN_vertex',true);
  assert.deepEqual(trial.bodies[1].nodes.filter(n=>electron.nodes.includes(n)).sort(),['C1','C2','M1']);
  ck('neutron_electron_share_exactly_the_MCC_face',trial.sharedFaces[1].join(',')==='M1,C1,C2');
  // Signed plane evaluations for face M1/C1/C2. Opposite apices must not coincide.
  const sub=(a,b)=>a.map((x,i)=>x-b[i]),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),[a,b,c]=C.electronFace.map(n=>ep[n]),u=sub(b,a),v=sub(c,a),normal=[u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]];
  ck('trial_electron_and_neutron_interiors_lie_on_opposite_sides_of_MCC',dot(sub(ep.M0,a),normal)*dot(sub(ep.M2,a),normal)<0);
  ck('trial_electron_does_not_overlap_proton_interior',ep.C2.reduce((s,x)=>s+x,0)<-1&&ep.M2.reduce((s,x)=>s+x,0)<-1&&ep.C0.reduce((s,x)=>s+x,0)>-1);
  const files=['index.html','style.css','app.js','model.mjs','identity.mjs','identity-data.mjs','carrier.mjs'];
  for(const file of files)for(const dir of ['public','website/public'])assert.equal(hash(await readFile(path.join(ROOT,dir,'experiments/particle-overlap-tetrahedron',file))),hash(await readFile(path.join(ROOT,'research/strominger/demos/particle-overlap-tetrahedron',file))));
  checks.both_public_roots_contain_the_same_volumetric_carrier_assets=true;
  let base=process.env.PARTICLE_IDENTITY_BASE_URL,server,browser;
  try{
    if(!base){const mime={'.html':'text/html','.mjs':'text/javascript','.js':'text/javascript','.css':'text/css','.txt':'text/plain'};server=createServer(async(req,res)=>{try{let p=path.resolve(PUBLIC,'.'+new URL(req.url,'http://localhost').pathname);if(path.relative(PUBLIC,p).startsWith('..'))throw Error('path');if((await stat(p)).isDirectory())p=path.join(p,'index.html');res.setHeader('Content-Type',mime[path.extname(p)]||'application/octet-stream');res.end(await readFile(p));}catch{res.writeHead(404);res.end();}});await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));base='http://127.0.0.1:'+server.address().port;}
    browser=await chromium.launch({headless:true,args:['--enable-webgl','--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
    const page=await browser.newPage({viewport:{width:1480,height:1040}}),errors=[];page.on('pageerror',e=>errors.push(String(e)));
    const url=base+'/experiments/particle-overlap-tetrahedron/?view=lattice';
    await page.goto(url,{waitUntil:'load'});await page.waitForFunction(()=>globalThis.ParticleOverlapViewer?.snapshot().frameCount>2);
    const snap=()=>page.evaluate(()=>globalThis.ParticleOverlapViewer.snapshot());let s=await snap();
    ck('requested_URL_defaults_to_actual_tetrahedral_carriers',s.state.geometry==='carrier'&&s.geometry.renderedCarrierBodies.length===2&&s.webgl);
    for(const body of s.geometry.renderedCarrierBodies){assert.equal(body.triangles,4);const p=Array.from({length:4},(_,i)=>body.positions.slice(3*i,3*i+3));near([volume(p)],[8/3],1e-6);}
    checks.actual_rendered_mesh_buffers_have_four_faces_and_nonzero_tetrahedral_volume=true;
    assert.deepEqual(s.coordinates,C.points);assert.deepEqual(s.originalPentachoron,M.pentachoron);
    ck('all_original_identities_and_original_four_dimensional_source_remain',s.geometry.pointCount===5&&s.walk.join(',')===M.walk.join(',')&&s.originalPentachoron.C2[3]===Math.sqrt(5));
    ck('fourth_vertices_and_selected_facet_scope_are_visible',await page.locator('#carrier-note').isVisible()&&/Proton fourth vertex: M₁/.test(await page.locator('#carrier-note').textContent())&&/Neutron fourth vertex: C₂, not C₀/.test(await page.locator('#carrier-note').textContent())&&/unfold/.test(await page.locator('#center-note').textContent()));
    ck('carrier_mode_does_not_claim_unused_y_or_codimension_axes',s.latticeAxes===null&&await page.locator('[data-role="axis"]:visible').count()===0&&await page.locator('#projection-controls').isHidden());
    ck('carrier_view_has_only_two_windows_and_no_electron_controls',s.geometry.particleTriangleCount===2&&s.routes.map(r=>r.id).join(',')==='proton,neutron'&&s.identity.anchors.length===2&&await page.locator('[data-route="electron"]').isHidden()&&await page.locator('[data-identity-route="electron"]').isHidden()&&await page.locator('.walk-panel').isHidden());
    ck('electron_route_is_rejected_in_carrier_view',await page.evaluate(()=>{try{globalThis.ParticleOverlapViewer.selectRoute('electron');return false;}catch{return true;}}));
    const seen={};
    for(const role of ['proton','neutron']){await page.locator(`[data-identity-route="${role}"]`).click();s=await snap();seen[role]=s.identity.branch;assert.equal(s.geometry.renderedCarrierBodies.length,2);
      if(role!=='electron'){const body=s.geometry.carrierBodies.find(b=>b.id===role);assert.equal(body.continuation,role==='proton'?'M1':'C2');assert.match(await page.locator('#detail-formula').textContent(),role==='proton'?/\[M₁\]/:/\[C₂\]/);}
    }
    checks.selected_carrier_details_retain_the_correct_bracketed_fourth_vertex=true;
    ck('spectral_identity_overlay_kept_on_real_bodies',seen.proton==='positive'&&seen.neutron==='positive');
    await page.locator('#faces').uncheck();ck('hiding_triangle_windows_does_not_remove_tetrahedral_bodies',(await snap()).geometry.renderedCarrierBodies.length===2);await page.locator('#faces').check();
    await page.locator('[data-route="all"]').click();await page.evaluate(()=>globalThis.ParticleOverlapViewer.setProgress(0));
    await page.locator('#scene').screenshot({path:path.join(OUT,'tetrahedral-carriers-scene.png')});
    await page.screenshot({path:path.join(OUT,'tetrahedral-carriers-desktop.png'),fullPage:true});
    await page.locator('[data-view="lattice"]').click();s=await snap();ck('flat_chart_remains_an_explicit_separate_alternative',s.state.geometry==='chart'&&s.geometry.renderedCarrierBodies.length===0&&Object.values(s.coordinates).every(p=>p[1]===0)&&new URL(page.url()).searchParams.get('geometry')==='chart');
    await page.locator('[data-route="electron"]').click();s=await snap();ck('legacy_electron_window_is_retained_only_in_chart_views',s.state.route==='electron'&&s.geometry.particleTriangleCount===3&&s.identity.branch==='negative'&&await page.locator('.walk-panel').isVisible());
    await page.evaluate(()=>globalThis.ParticleOverlapViewer.setProgress(4));s=await snap();ck('original_repeated_C1_history_is_retained_in_legacy_chart',s.identity.repeatedVertex&&s.identity.uniqueVertices.length===4);
    await page.locator('#carrier-mode').click();s=await snap();ck('return_to_carriers_restores_nonzero_volume',s.state.geometry==='carrier'&&s.geometry.renderedCarrierBodies.length===2&&s.state.route==='all'&&s.identity.role==='proton'&&s.geometry.particleTriangleCount===2);
    await page.evaluate(()=>globalThis.ParticleOverlapViewer.setProgress(5));s=await snap();ck('historical_progress_cannot_introduce_electron_in_carrier_view',s.identity.role==='neutron'&&s.identity.anchors.length===2);
    await page.locator('[data-route="all"]').click();await page.evaluate(()=>globalThis.ParticleOverlapViewer.setProgress(0));
    await page.setViewportSize({width:430,height:930});await page.goto(url,{waitUntil:'load'});await page.waitForFunction(()=>globalThis.ParticleOverlapViewer?.snapshot().frameCount>2);
    s=await snap();ck('mobile_default_has_real_volumes_without_overflow',s.geometry.renderedCarrierBodies.length===2&&await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    ck('all_five_carrier_node_labels_visible_on_mobile',(await Promise.all(M.carriers.map(n=>page.locator(`[data-point="${n}"]`).isVisible()))).every(Boolean));
    await page.locator('#scene').screenshot({path:path.join(OUT,'tetrahedral-carriers-mobile-scene.png')});await page.screenshot({path:path.join(OUT,'tetrahedral-carriers-mobile.png'),fullPage:true});
    await page.setViewportSize({width:1480,height:1040});await page.locator('#electron-trial').click();s=await snap();
    ck('explicit_M2_trial_switch_adds_a_third_actual_body',s.state.electronTrial&&s.geometry.renderedCarrierBodies.length===3&&s.geometry.pointCount===6&&s.geometry.particleTriangleCount===3&&new URL(page.url()).searchParams.get('electron')==='m2');
    for(const body of s.geometry.renderedCarrierBodies){assert.equal(body.triangles,4);near([volume(Array.from({length:4},(_,i)=>body.positions.slice(i*3,i*3+3)))],[8/3],1e-6);}
    ck('actual_rendered_electron_mesh_has_regular_tetrahedral_volume',true);
    assert.deepEqual(s.coordinates,ep);assert.deepEqual(s.originalPentachoron,M.pentachoron);
    ck('original_source_and_separate_M2_provenance_remain_visible',s.geometry.trialExtension.id==='M2'&&!s.geometry.trialExtension.originalSourceVertex&&await page.locator('#electron-carrier-note').isVisible()&&/M₂ has no spectral coefficient/.test(await page.locator('#identity-view-note').textContent()));
    await page.locator('[data-route="electron"]').click();s=await snap();
    ck('electron_selection_retains_M2_in_its_own_four_vertex_body',s.geometry.carrierBodies[2].continuation==='M2'&&/\[M₂\]/.test(await page.locator('#detail-formula').textContent())&&s.identity.role==='electron'&&s.identity.branch==='negative');
    near(s.identity.anchor,C.electronFace.map(n=>ep[n]).reduce((a,p)=>a.map((v,i)=>v+p[i]/3),[0,0,0]));
    ck('active_face_center_is_labeled_and_excludes_fourth_vertex',await page.locator('.identity-label:not(.assembly-label)').textContent()==='active-face center'&&M.distanceSquared(s.identity.anchor,electron.nodes.map(n=>ep[n]).reduce((a,p)=>a.map((v,i)=>v+p[i]/4),[0,0,0]))>1e-8);
    for(const role of ['all','proton','neutron','electron']){await page.locator(`[data-route="${role}"]`).click();assert.doesNotMatch(await page.locator('body').innerText(),/\btrial\b|\bbinding v\d|\b(?:exact|source) checks\b|\bproposed\b|\bverified\b|E\?:|b · window/i);}
    checks.user_facing_carrier_controls_and_details_have_no_workflow_labels=true;
    await page.locator('[data-point="M2"]').click();ck('new_M2_has_a_separate_inspectable_identity',/electron continuation/.test(await page.locator('#detail-title').textContent()));
    await page.locator('[data-route="all"]').click();await page.evaluate(()=>globalThis.ParticleOverlapViewer.setProgress(0));
    await page.locator('#scene').screenshot({path:path.join(OUT,'electron-M2-trial-scene.png')});await page.screenshot({path:path.join(OUT,'electron-M2-trial-desktop.png'),fullPage:true});
    await page.locator('#carrier-mode').click();s=await snap();ck('leaving_trial_restores_PN_only_without_leaking_M2_or_electron',!s.state.electronTrial&&s.geometry.pointCount===5&&s.geometry.renderedCarrierBodies.length===2&&await page.locator('[data-point="M2"]').isHidden()&&await page.locator('[data-route="electron"]').isHidden());
    await page.setViewportSize({width:430,height:930});await page.goto(url+'&electron=m2',{waitUntil:'load'});await page.waitForFunction(()=>globalThis.ParticleOverlapViewer?.snapshot().frameCount>2);s=await snap();
    ck('direct_trial_URL_on_mobile_has_three_bodies_without_overflow',s.state.electronTrial&&s.geometry.renderedCarrierBodies.length===3&&await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    ck('all_six_trial_vertex_labels_are_visible_on_mobile',(await Promise.all(Object.keys(ep).map(n=>page.locator(`[data-point="${n}"]`).isVisible()))).every(Boolean));
    ck('mobile_trial_carrier_labels_do_not_overlap_each_other',await page.locator('.carrier-label:visible').evaluateAll(els=>{const rs=els.map(el=>el.getBoundingClientRect());return rs.every((a,i)=>rs.slice(i+1).every(b=>a.right<=b.left||b.right<=a.left||a.bottom<=b.top||b.bottom<=a.top));}));
    await page.locator('#scene').screenshot({path:path.join(OUT,'electron-M2-trial-mobile-scene.png')});await page.screenshot({path:path.join(OUT,'electron-M2-trial-mobile.png'),fullPage:true});
    ck('no_browser_script_errors',errors.length===0);
    const pins={};for(const file of files){const p='research/strominger/demos/particle-overlap-tetrahedron/'+file;pins[p]=hash(await readFile(path.join(ROOT,p)));}
    await writeFile(path.join(OUT,'verification.json'),JSON.stringify({status:'pass',checks,tested_url:url,source_sha256:pins,screenshots:['tetrahedral-carriers-scene.png','tetrahedral-carriers-desktop.png','tetrahedral-carriers-mobile-scene.png','tetrahedral-carriers-mobile.png'],trial_tested_url:url+'&electron=m2',trial_screenshots:['electron-M2-trial-scene.png','electron-M2-trial-desktop.png','electron-M2-trial-mobile-scene.png','electron-M2-trial-mobile.png'],scope:'P/N source facets plus an explicit optional new-vertex M2 electron-carrier trial. Regular attachment and display identity only; no native particle equivalence or sixth-label spectral recovery claim.'},null,2)+'\n');
    console.log(JSON.stringify({status:'pass',checks:Object.keys(checks).length,tested_url:url,rendered_tetrahedra:2,volume_each:8/3}));
  }finally{await browser?.close();if(server)await new Promise(resolve=>server.close(resolve));}
}
main().catch(e=>{console.error(e);process.exitCode=1;});
