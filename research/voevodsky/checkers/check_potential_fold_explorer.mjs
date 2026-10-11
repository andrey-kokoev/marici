import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import vm from 'node:vm';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {chromium} from '@playwright/test';

const htmlURL=new URL('../../../papers/witness-generators/potential-fold-explorer.html',import.meta.url);
const results=new URL('../results/',import.meta.url);
const html=await fs.readFile(htmlURL,'utf8');
const math=html.match(/<script id="fold-math">([\s\S]*?)<\/script>/)[1];
const context={};vm.runInNewContext(math,context);const M=context.FoldMath;
const close=(a,b)=>Math.abs(a-b)<1e-10;
const equal=(a,b)=>a.length===b.length&&a.every((x,i)=>close(x,b[i]));
const sub=(a,b)=>a.map((x,i)=>x-b[i]);
const det=(a,b,c)=>a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]);
const volume=pts=>Math.abs(det(sub(pts[1],pts[0]),sub(pts[2],pts[0]),sub(pts[3],pts[0])))/6;
const checks={};
checks.twenty_four_distinct_flags=M.flags.length===24&&new Set(M.flags.map(f=>f.chain.join('|'))).size===24;
checks.six_sectors_per_face=['ABC','ABD','ACD','BCD'].every(face=>M.flags.filter(f=>f.face===face).length===6);
checks.equal_volume_subdivision=M.flags.every(f=>close(volume(f.vertices.map(M.xyz)),volume(M.P)/24));
checks.total_volume_preserved=close(M.flags.reduce((sum,f)=>sum+volume(f.vertices.map(M.xyz)),0),volume(M.P));
checks.boundary_samples_are_distinct=new Set(M.flags.map(f=>f.sample.join(','))).size===24&&M.flags.every(f=>Math.min(...f.sample)===0);
checks.all_positions_collapse_to_center=M.flags.every(f=>equal(M.collapse(f.sample,1),[.25,.25,.25,.25]));
checks.direction_samples_not_mutated=M.flags.every(f=>{const before=f.sample.join(',');M.collapse(f.sample,.7);return f.sample.join(',')===before;});
const coefficientSourceURL=new URL('../results/fold_coefficient_attachment_store.json',import.meta.url);
const coefficientText=await fs.readFile(coefficientSourceURL,'utf8');
const coefficientSource=JSON.parse(coefficientText);
const number=x=>{const [a,b='1']=String(x).split('/');return Number(a)/Number(b);};
const matrix=coefficientSource.record.mode_matrix.map(row=>row.map(z=>z.map(number)));
const actualMode=v=>matrix.flatMap(row=>[0,1].map(part=>row.reduce((sum,z,i)=>sum+z[part]*M.xyz(v)[i],0)));
let samples=0,valid=true,projector=true;
for(let a=0;a<=24;a++)for(let b=0;b<=24-a;b++){
  const u=[a/24,b/24,(24-a-b)/24],{upper,lower}=M.lifts(u);samples++;
  valid&&=equal(M.quotient(upper),u)&&equal(M.quotient(lower),u)&&Math.min(...upper)>=-1e-12&&Math.min(...lower)>=-1e-12;
  valid&&=close(upper.reduce((s,x)=>s+x,0),1)&&close(lower.reduce((s,x)=>s+x,0),1);
  valid&&=(equal(upper,lower)===(Math.min(...u)===0));
  projector&&=equal(actualMode(upper),actualMode(lower));
}
checks.complete_grid_lifts_and_seam=valid;
checks.lifts_match_actual_retained_projector=projector;
checks.loop_closes_on_each_sheet=equal(M.lifts(M.loop(0)).upper,M.lifts(M.loop(1)).upper)&&equal(M.lifts(M.loop(0)).lower,M.lifts(M.loop(1)).lower);
checks.loop_stays_off_seam=Array.from({length:101},(_,i)=>M.loop(i/100)).every(u=>Math.min(...u)>0);
assert(Object.values(checks).every(Boolean),'geometry check failed');

const browser=await chromium.launch({headless:true,args:['--enable-unsafe-swiftshader']});
const page=await browser.newPage({viewport:{width:1440,height:1150},deviceScaleFactor:1});
const errors=[];page.on('pageerror',e=>errors.push(e.message));
try{
  await page.goto(htmlURL.href);
  await page.waitForFunction(()=>document.querySelector('#error').hidden&&document.querySelector('#readout').textContent.includes('Selected piece'),{timeout:60000});
  checks.two_webgl_views_created=await page.locator('.viewport canvas').count()===2;
  await page.locator('#face').selectOption('ABD');
  assert.match(await page.locator('#readout').innerText(),/Showing 6 solid pieces/);
  await page.locator('#only').check();
  assert.match(await page.locator('#readout').innerText(),/Showing 1 solid pieces/);
  await page.locator('#next').click();
  checks.face_and_piece_controls_work=(await page.locator('#readout').innerText()).includes('ABD');
  await page.locator('#reset').click();
  await page.screenshot({path:fileURLToPath(new URL('potential_fold_explorer_sectors.png',results)),fullPage:true});
  await page.locator('[data-step="2"]').click();
  await page.locator('#end-position').click();
  checks.collapse_endpoint_explains_retained_data=(await page.locator('#readout').innerText()).includes('1 visible position; 24 separately retained sector samples');
  await page.screenshot({path:fileURLToPath(new URL('potential_fold_explorer_collapse.png',results)),fullPage:true});
  await page.locator('[data-step="3"]').click();
  await page.locator('#mode-boundary').click();
  checks.seam_preset_merges_directions=(await page.locator('#readout').innerText()).includes('ONE boundary point');
  await page.locator('#mode-center').click();
  checks.interior_preset_has_two_directions=(await page.locator('#readout').innerText()).includes('TWO distinct boundary points');
  const canvas=page.locator('#right-view canvas');const box=await canvas.boundingBox();
  await page.mouse.click(box.x+box.width/2+25,box.y+box.height/2);
  checks.mode_triangle_is_pickable=!(await page.locator('#readout').innerText()).includes('Image value u = (0.333, 0.333, 0.333)');
  await page.locator('#mode-loop').click();
  await page.waitForFunction(()=>document.querySelector('#readout').textContent.includes('Loop complete'),{timeout:30000});
  checks.loop_animation_returns_without_swap=(await page.locator('#readout').innerText()).includes('upper returned to upper; lower returned to lower');
  await page.screenshot({path:fileURLToPath(new URL('potential_fold_explorer_modes.png',results)),fullPage:true});
  await page.setViewportSize({width:390,height:844});
  await page.waitForTimeout(300);
  checks.mobile_has_no_horizontal_overflow=await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth);
  await page.screenshot({path:fileURLToPath(new URL('potential_fold_explorer_mobile.png',results)),fullPage:true});
  checks.no_browser_exceptions=errors.length===0;
}finally{await browser.close();}
const result={passed:Object.values(checks).every(Boolean),checks,grid_samples:samples,browser:'headless Chromium / WebGL',browser_errors:errors,
  html_sha256:createHash('sha256').update(html).digest('hex'),coefficient_source_root:coefficientSource.root,
  coefficient_source_sha256:createHash('sha256').update(coefficientText).digest('hex')};
await fs.writeFile(new URL('potential_fold_explorer_check.json',results),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result,null,2));
assert(result.passed);
