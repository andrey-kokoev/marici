import assert from 'node:assert/strict';
import {createServer} from 'node:http';
import {readFile,writeFile,mkdir,stat} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import {chromium} from '@playwright/test';
import * as M from '../demos/particle-overlap-tetrahedron/model.mjs';
import {identityState,identityProof} from '../demos/particle-overlap-tetrahedron/identity.mjs';
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const PUBLIC=path.join(ROOT,'public'),OUT=path.join(ROOT,'research/strominger/results/particle-overlap-identity-viewer');
const checks={};const ck=(n,b)=>{assert.ok(b,n);checks[n]=true;};
const hash=b=>createHash('sha256').update(b).digest('hex');
const near=(a,b)=>assert.ok(Math.hypot(...a.flat(Infinity).map((v,i)=>v-b.flat(Infinity)[i]))<1e-10);
const projector=w=>w.flatMap(a=>w.flatMap(b=>[(a[0]*b[0]+a[1]*b[1])/3,(a[1]*b[0]-a[0]*b[1])/3]));
async function main(){
  await mkdir(OUT,{recursive:true});
  const receipt=await readFile(path.join(ROOT,identityProof.source_receipt));
  ck('viewer_data_bound_to_exact_verified_receipt',hash(receipt)===identityProof.receipt_sha256&&identityProof.verified_checks===Object.keys(JSON.parse(receipt).checks).length);
  for(const view of Object.keys(M.views))for(const mode of ['common','positive','negative']) {
    const a=identityState({view,route:'electron',mode}),b=identityState({view,route:'electron',mode,phase:75});
    near(projector(a.weights),projector(b.weights));
    ck(view+'_'+mode+'_phase_probe_preserves_identity_projector',a.branch===b.branch&&a.modeRecord.label===b.modeRecord.label);
  }
  assert.deepEqual(identityState({route:'electron'}).branchPath,['positive','positive','negative']);
  near([identityState({route:'neutron'}).transportPhaseDegrees],[120]);
  near([identityState({route:'electron'}).transportPhaseDegrees],[0]);
  checks.actual_branch_and_cumulative_phase_transport=true;
  for(const view of Object.keys(M.views)) {
    const a=identityState({view,progress:3}),b=identityState({view,progress:4});near(a.assemblyAnchor,b.assemblyAnchor);
    ck(view+'_revisit_retains_occurrence_without_double_insertion',b.uniqueVertices.length===4&&b.occurrence===4&&b.repeatedVertex&&JSON.stringify(b.assemblyAnchor)!==JSON.stringify(b.occurrenceMean));
  }
  const authored=['index.html','style.css','app.js','model.mjs','identity.mjs','identity-data.mjs','carrier.mjs'];
  for(const file of authored)for(const dir of ['public','website/public'])assert.equal(hash(await readFile(path.join(ROOT,dir,'experiments/particle-overlap-tetrahedron',file))),hash(await readFile(path.join(ROOT,'research/strominger/demos/particle-overlap-tetrahedron',file))));
  checks.all_identity_assets_match_both_targeted_public_roots=true;
  let server,browser;let base=process.env.PARTICLE_IDENTITY_BASE_URL;
  try {
    if(!base) {
      const mime={'.html':'text/html','.js':'text/javascript','.mjs':'text/javascript','.css':'text/css','.txt':'text/plain'};
      server=createServer(async(req,res)=>{try{let p=path.resolve(PUBLIC,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));const rel=path.relative(PUBLIC,p);if(rel.startsWith('..')||path.isAbsolute(rel))throw Error('path');if((await stat(p)).isDirectory())p=path.join(p,'index.html');res.setHeader('Content-Type',mime[path.extname(p)]||'application/octet-stream');res.end(await readFile(p));}catch{res.writeHead(404);res.end('Not found');}});
      await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));base='http://127.0.0.1:'+server.address().port;
    }
    browser=await chromium.launch({headless:true,args:['--enable-webgl','--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
    const page=await browser.newPage({viewport:{width:1480,height:1040},deviceScaleFactor:1}),errors=[],external=[];
    page.on('pageerror',e=>errors.push(String(e)));page.on('request',r=>{if(!r.url().startsWith(base))external.push(r.url());});
    const snap=()=>page.evaluate(()=>globalThis.ParticleOverlapViewer.snapshot());
    await page.goto(base+'/experiments/particle-overlap-tetrahedron/?view=lattice&geometry=chart',{waitUntil:'load'});
    await page.waitForFunction(()=>globalThis.ParticleOverlapViewer?.snapshot().frameCount>2);
    let s=await snap();ck('identity_layer_draws_real_WebGL_on_requested_lattice_view',s.webgl&&s.identity.visible&&s.identity.sceneObjectCount>4&&s.identity.word==='CMC');
    assert.deepEqual(s.walk,['C0','M0','C1','M1','C1','C2']);assert.deepEqual(s.coordinates,M.lattice);
    ck('original_five_sites_and_six_occurrences_unchanged',s.geometry.pointCount===5&&await page.locator('[data-occurrence]').count()===6);
    await page.locator('[data-route="neutron"]').click();s=await snap();assert.equal(s.identity.branch,'positive');near([s.identity.transportPhaseDegrees],[120]);
    ck('neutron_window_carries_the_verified_phase',await page.locator('#identity-phase-readout').textContent()==='120° transport + 0° probe');
    await page.locator('[data-route="electron"]').click();s=await snap();assert.equal(s.identity.branch,'negative');assert.match(s.identity.operation,/inverse/);
    ck('electron_window_shows_required_branch_and_inverse_cycle',/negative/.test(await page.locator('#identity-branch').textContent()));
    await page.locator('.identity-retained summary').click();
    ck('retained_packet_exposes_native_occurrences_and_extra_closure',(await page.locator('#identity-occurrences').textContent()).includes('walk:3')&&(await page.locator('#identity-closure').textContent()).includes('not a supplied native command'));
    const before=await snap();
    await page.locator('#identity-phase').evaluate(el=>{el.value='75';el.dispatchEvent(new Event('input',{bubbles:true}));});
    s=await snap();near(projector(before.identity.weights),projector(s.identity.weights));
    ck('live_phase_probe_rotates_glyph_not_identity',s.identity.probePhaseDegrees===75&&JSON.stringify(s.identity.realVector)!==JSON.stringify(before.identity.realVector));
    await page.locator('#identity-mode').selectOption('negative');s=await snap();assert.equal(s.identity.branch,'positive');checks.negative_seed_transports_to_positive_electron_branch=true;
    await page.locator('#identity-mode').selectOption('common');s=await snap();assert.equal(s.identity.branch,'common');assert.match(await page.locator('#identity-glyph-note').textContent(),/no centered directional ellipse/);checks.common_mode_is_retained_not_misdrawn_as_zero_identity=true;
    await page.locator('#identity-enabled').uncheck();s=await snap();assert.equal(s.identity.visible,false);assert.deepEqual(s.coordinates,M.lattice);ck('overlay_toggle_preserves_underlying_geometry',await page.locator('.identity-label').first().isHidden());
    await page.locator('#identity-enabled').check();await page.locator('#identity-mode').selectOption('positive');await page.locator('#identity-phase-reset').click();
    await page.locator('[data-route="all"]').click();
    await page.evaluate(()=>globalThis.ParticleOverlapViewer.setProgress(3));const a=await snap();
    await page.evaluate(()=>globalThis.ParticleOverlapViewer.setProgress(4));s=await snap();near(a.identity.assemblyAnchor,s.identity.assemblyAnchor);
    ck('live_C1_revisit_preserves_identity_and_occurrence_distinction',s.identity.uniqueVertices.length===4&&s.identity.occurrence===4&&/same vertex; new occurrence/.test(await page.locator('#identity-revisit').textContent()));
    for(const view of ['hex','pentachoron','barycenter','lattice']) {
      await page.locator(`[data-view="${view}"]`).click();s=await snap();assert.equal(s.state.progress,4);assert.equal(s.identity.proofHash,identityProof.receipt_sha256);
      ck(view+'_identity_reprojects_without_mutating_source_walk',s.identity.visible&&s.identity.walk.join(',')===M.walk.join(','));
    }
    await page.locator('[data-identity-route="neutron"]').click();assert.equal((await snap()).state.route,'neutron');
    checks.identity_stage_buttons_drive_the_same_retained_window=true;
    async function identityLabelsSeparate(name) {
      await page.waitForTimeout(80);
      const ok=await page.evaluate(()=>{const boxes=[...document.querySelectorAll('#scene .point-label,#scene .identity-label')].filter(el=>!el.hidden&&getComputedStyle(el).visibility==='visible').map(el=>({identity:el.classList.contains('identity-label'),r:el.getBoundingClientRect()}));return boxes.every((a,i)=>boxes.slice(i+1).every(b=>!(a.identity||b.identity)||a.r.right<=b.r.left||b.r.right<=a.r.left||a.r.bottom<=b.r.top||b.r.bottom<=a.r.top));});
      ck(name,ok);
    }
    await identityLabelsSeparate('desktop_identity_labels_do_not_cover_carrier_or_axis_labels');
    await page.screenshot({path:path.join(OUT,'lattice-identity-desktop.png'),fullPage:true});
    await page.locator('#scene').screenshot({path:path.join(OUT,'lattice-identity-scene.png')});
    await page.locator('[data-view="pentachoron"]').click();await page.locator('[data-route="electron"]').click();
    await page.screenshot({path:path.join(OUT,'pentachoron-identity-desktop.png'),fullPage:true});
    await page.setViewportSize({width:430,height:930});await page.goto(base+'/experiments/particle-overlap-tetrahedron/?view=lattice&geometry=chart',{waitUntil:'load'});
    await page.waitForFunction(()=>globalThis.ParticleOverlapViewer?.snapshot().frameCount>2);
    await page.locator('[data-route="electron"]').click();await page.locator('#identity-mode').selectOption('negative');await page.locator('.identity-retained summary').click();
    ck('mobile_identity_controls_work_and_no_horizontal_overflow',(await snap()).identity.branch==='positive'&&await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    await identityLabelsSeparate('mobile_identity_labels_do_not_cover_carrier_or_axis_labels');
    await page.screenshot({path:path.join(OUT,'lattice-identity-mobile.png'),fullPage:true});
    ck('no_page_script_errors',errors.length===0);ck('no_external_network_dependencies',external.length===0);
    const pins={};for(const file of authored){const p='research/strominger/demos/particle-overlap-tetrahedron/'+file;pins[p]=hash(await readFile(path.join(ROOT,p)));}
    const own=path.relative(ROOT,fileURLToPath(import.meta.url)).replaceAll('\\','/');pins[own]=hash(await readFile(path.join(ROOT,own)));
    await writeFile(path.join(OUT,'verification.json'),JSON.stringify({status:'pass',checks,browser:browser.version(),tested_url:base+'/experiments/particle-overlap-tetrahedron/?view=lattice&geometry=chart',proof_receipt:identityProof.source_receipt,proof_sha256:identityProof.receipt_sha256,source_sha256:pins,screenshots:['lattice-identity-desktop.png','lattice-identity-scene.png','pentachoron-identity-desktop.png','lattice-identity-mobile.png'],scope:'Browser geometry and declared identity adapter visualization, not physical particle validation.'},null,2)+'\n');
    console.log(JSON.stringify({status:'pass',checks:Object.keys(checks).length,tested_url:base+'/experiments/particle-overlap-tetrahedron/?view=lattice&geometry=chart',errors}));
  } finally {await browser?.close();if(server)await new Promise(resolve=>server.close(resolve));}
}
main().catch(e=>{console.error(e);process.exitCode=1;});
