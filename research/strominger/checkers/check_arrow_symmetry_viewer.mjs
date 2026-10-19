// Deterministic geometry checks plus a real offline Chromium interaction test.
import assert from 'node:assert/strict';
import {readFile, writeFile, mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath, pathToFileURL} from 'node:url';
import path from 'node:path';
import {runInNewContext} from 'node:vm';
import {chromium} from '@playwright/test';

const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const HTML=path.join(ROOT,'research/strominger/arrow-symmetry-viewer.html');
const OUT=path.join(ROOT,'research/strominger/results');
const sha=bytes=>createHash('sha256').update(bytes).digest('hex');
const distance=(a,b)=>Math.hypot(...a.flat(Infinity).map((v,i)=>v-b.flat(Infinity)[i]));
const near=(a,b,tol=1e-12)=>assert.ok(distance(a,b)<tol,`distance ${distance(a,b)}`);
const checks={};

async function main() {
  const text=await readFile(HTML,'utf8');
  const source=text.match(/<script id="symmetry-math">([\s\S]*?)<\/script>/);
  assert.ok(source);const context={};runInNewContext(source[1],context);
  const M=context.ArrowSymmetryMath;
  const axisCases=Array.from({length:97},(_,i)=>M.quat(i*7.5,(i*53)%360-180,(i*79)%360-180));
  for(const q of axisCases) {
    assert.ok(Math.abs(Math.hypot(...q)-1)<1e-12);
    assert.ok(Math.abs(Math.hypot(...M.spinor(q).flat())-1)<1e-12);
    const f=M.frame(q);
    for(let i=0;i<3;i++)for(let j=0;j<3;j++) {
      const dot=f[i].reduce((sum,x,k)=>sum+x*f[j][k],0);
      assert.ok(Math.abs(dot-Number(i===j))<1e-12);
    }
  }
  checks.unit_quaternion_spinor_and_orthonormal_frame_97_cases=true;
  const q0=M.quat(0,40,-20),q360=M.quat(360,40,-20),q720=M.quat(720,40,-20);
  near(q360,q0.map(x=>-x));near(q720,q0);
  near(M.frame(q360),M.frame(q0));near(M.frame(q720),M.frame(q0));
  near(M.spinor(q360),M.spinor(q0).map(z=>z.map(x=>-x)));
  checks.spinor_360_degree_sign_and_720_degree_return=true;
  assert.ok(distance(q360,q0)>1.99 && distance(M.frame(q360),M.frame(q0))<1e-12);
  checks.frame_only_projection_deliberately_fails_to_distinguish_antipodal_lifts=true;
  const identity={q:[1,0,0,0],phase:[1,0],flowDirection:1};
  const r={...identity,q:M.axis(1,75)},p={...identity,phase:M.circle(32)},f={...identity,flowDirection:-1};
  for(const [a,b] of [[r,p],[r,f],[p,f]]) {
    const ab=M.compose(a,b),ba=M.compose(b,a);
    near(ab.q,ba.q);near(ab.phase,ba.phase);assert.equal(ab.flowDirection,ba.flowDirection);
  }
  const lhs=M.compose(M.compose(r,p),f),rhs=M.compose(r,M.compose(p,f));
  near(lhs.q,rhs.q);near(lhs.phase,rhs.phase);assert.equal(lhs.flowDirection,rhs.flowDirection);
  checks.direct_product_cross_factor_commutation_and_composition=true;
  assert.equal(M.compose(f,f).flowDirection,1);
  assert.throws(()=>M.flowOrder(0),/direction/);
  assert.deepEqual(Array.from(M.flowOrder(1)),[0,1,2,3]);
  assert.deepEqual(Array.from(M.flowOrder(-1)),[3,2,1,0]);
  checks.process_reversal_is_a_binary_involution_not_a_phase=true;
  for(const step of [0,.25,1,1.5,2,2.75,3]) near(M.flowCursor(-1,step),M.flowCursor(1,3-step));
  near(M.flowCursor(1,3),M.processNodes[3]);near(M.flowCursor(-1,3),M.processNodes[0]);
  checks.forward_and_reverse_traversal_share_the_same_open_path=true;
  assert.ok(distance(M.mul(M.axis(0,60),M.axis(1,80)),M.mul(M.axis(1,80),M.axis(0,60)))>.1);
  checks.SU2_axes_do_not_falsely_commute=true;
  near(M.circle(0),M.circle(360));near(M.circle(90),[0,1]);
  checks.phase_ring_has_quarter_turn_and_full_period=true;

  const browser=await chromium.launch({headless:true});
  let version;
  try {
    version=browser.version();
    const page=await browser.newPage({viewport:{width:1500,height:960},deviceScaleFactor:1});
    const errors=[],network=[];
    page.on('pageerror',error=>errors.push(String(error)));
    page.on('request',request=>{if(/^https?:/.test(request.url()))network.push(request.url());});
    await page.goto(pathToFileURL(HTML).href,{waitUntil:'load'});
    await page.waitForFunction(()=>Boolean(globalThis.ArrowSymmetryViewer));
    const snapshot=()=>page.evaluate(()=>globalThis.ArrowSymmetryViewer.snapshot());
    const initial=await snapshot();
    await page.locator('[data-turn="360"]').click();
    const turned=await snapshot();near(turned.frame,initial.frame);near(turned.q,initial.q.map(x=>-x));
    assert.match(await page.locator('#returnStatus').textContent(),/opposite spinor/);
    await page.locator('[data-turn="720"]').click();
    const returned=await snapshot();near(returned.q,initial.q);
    checks.browser_buttons_display_both_spinor_returns=true;
    await page.locator('#phaseStep').click();
    const phase=await snapshot();near(phase.q,returned.q);assert.equal(phase.flowDirection,returned.flowDirection);near(phase.phase,[0,1]);
    await page.locator('#flowBack').click();
    const flow=await snapshot();near(flow.q,phase.q);near(flow.phase,phase.phase);assert.equal(flow.flowDirection,-1);
    assert.deepEqual(flow.process.order,[3,2,1,0]);near(flow.process.cursor,M.processNodes[3]);
    assert.equal(await page.locator('#processOrder').textContent(),'N → G → L → Input');
    assert.equal(await page.locator('#flowAngle').count(),0);
    checks.browser_process_control_reverses_sequence_without_changing_arrow_or_phase=true;
    await page.locator('#flowNext').click();
    const stepped=await snapshot();assert.equal(stepped.controls.flowStep,1);near(stepped.process.cursor,M.processNodes[2]);
    await page.locator('#flowFlip').click();await page.locator('#flowFlip').click();
    const flippedTwice=await snapshot();assert.equal(flippedTwice.flowDirection,stepped.flowDirection);
    assert.deepEqual(flippedTwice.process.order,stepped.process.order);near(flippedTwice.process.cursor,stepped.process.cursor);
    near(flippedTwice.q,stepped.q);near(flippedTwice.phase,stepped.phase);
    checks.browser_double_process_flip_restores_order_and_cursor=true;
    await page.locator('#flowForward').click();await page.locator('#flowReset').click();
    assert.equal(await page.locator('#processOrder').textContent(),'Input → L → G → N');
    near((await snapshot()).process.cursor,M.processNodes[0]);
    await page.locator('#tilt').evaluate(input=>{input.value='80';input.dispatchEvent(new Event('input',{bubbles:true}));});
    const tilt=await snapshot();assert.ok(distance(tilt.q,flow.q)>.1);near(tilt.phase,phase.phase);
    checks.browser_orientation_slider_reaches_actual_SU2_rotation=true;
    const canvas=page.locator('#scene'),bounds=await canvas.boundingBox();
    assert.ok(bounds.width>500 && bounds.height>500);
    const beforeCamera=await snapshot();
    await page.mouse.move(bounds.x+bounds.width*.5,bounds.y+bounds.height*.5);
    await page.mouse.down();await page.mouse.move(bounds.x+bounds.width*.5+50,bounds.y+bounds.height*.5+20);await page.mouse.up();
    const afterCamera=await snapshot();near(afterCamera.q,beforeCamera.q);near(afterCamera.phase,beforeCamera.phase);assert.equal(afterCamera.flowDirection,beforeCamera.flowDirection);near(afterCamera.process.cursor,beforeCamera.process.cursor);
    checks.camera_orbit_does_not_change_group_element=true;
    const stepBefore=(await snapshot()).controls.flowStep;
    await page.locator('#play').click();await page.waitForTimeout(180);await page.locator('#play').click();
    const played=await snapshot();assert.ok(played.controls.flowStep>stepBefore);
    near(played.q,afterCamera.q);near(played.phase,afterCamera.phase);assert.equal(played.flowDirection,afterCamera.flowDirection);
    checks.playback_moves_only_the_traversal_cursor=true;
    await page.locator('#play').click();
    await page.waitForFunction(()=>globalThis.ArrowSymmetryViewer.snapshot().controls.flowStep===3,{},{timeout:8000});
    const finished=await snapshot();assert.equal(finished.process.playing,false);near(finished.process.cursor,M.processNodes[3]);
    await page.waitForTimeout(150);assert.equal((await snapshot()).controls.flowStep,3);
    assert.equal(await page.locator('#flowNext').isDisabled(),true);
    checks.playback_stops_at_the_endpoint_without_phase_wraparound=true;
    await page.locator('#flowBack').click();await page.locator('#flowReset').click();
    await page.locator('#flowNext').click();await page.locator('#flowNext').click();await page.locator('#flowNext').click();
    const reverseEnd=await snapshot();near(reverseEnd.process.cursor,M.processNodes[0]);assert.equal(reverseEnd.controls.flowStep,3);
    checks.reverse_steps_reach_the_original_input_endpoint=true;
    await page.setViewportSize({width:480,height:900});
    await page.waitForFunction(()=>document.getElementById('scene').width>300);
    const horizontalOverflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
    assert.equal(horizontalOverflow,false);
    checks.mobile_layout_has_no_horizontal_overflow=true;
    assert.equal(network.length,0);assert.equal(errors.length,0);
    checks.offline_browser_has_no_network_dependencies_or_script_errors=true;
  } finally {
    await browser.close();
  }
  const result={status:'passed',checks,math_sample_count:axisCases.length,chromium_version:version,
    scope:'Numerical implementation and browser checks of SU(2) × SO(2) × Z2 with an open process traversal; not inverse execution of the stage projectors or particle dynamics.',
    retained_coordinates:'Unit quaternion q, one unit-circle marker, and binary process direction. Traversal position is display state, not another group parameter.',
    image_generated:false,
    source_hashes:{'research/strominger/arrow-symmetry-viewer.html':sha(await readFile(HTML)),
                   'research/strominger/checkers/check_arrow_symmetry_viewer.mjs':sha(await readFile(fileURLToPath(import.meta.url)))}};
  await mkdir(OUT,{recursive:true});
  await writeFile(path.join(OUT,'arrow-symmetry-viewer.json'),JSON.stringify(result,null,2)+'\n');
  console.log(JSON.stringify({status:result.status,checks:Object.keys(checks).length,chromium_version:version},null,2));
}

main().catch(error=>{console.error(error);process.exitCode=1;});
