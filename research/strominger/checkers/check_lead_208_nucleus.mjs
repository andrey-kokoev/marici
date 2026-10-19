import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath,pathToFileURL} from 'node:url';
import path from 'node:path';
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const HTML=path.join(ROOT,'research/strominger/demos/lead-208-nucleus/index.html');
const OUT=path.join(ROOT,'research/strominger/results/lead-208-nucleus');
const checks={};
function ck(name,value){checks[name]=Boolean(value);assert.ok(value,name);}
const hash=b=>createHash('sha256').update(b).digest('hex');
const pause=page=>page.evaluate(()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve))));
async function main(){
 await mkdir(OUT,{recursive:true});
 const errors=[];
 const browser=await chromium.launch({headless:true});
 try{
  const context=await browser.newContext({viewport:{width:1400,height:950},deviceScaleFactor:1});
  await context.setOffline(true);
  const page=await context.newPage();
  page.on('pageerror',e=>errors.push(String(e)));
  await page.goto(pathToFileURL(HTML).href);
  await page.waitForFunction(()=>window.nucleus?.counts.full.total===208);
  await pause(page);
  const data=await page.evaluate(()=>({Z:nucleus.Z,N:nucleus.N,A:nucleus.A,points:nucleus.points,counts:nucleus.counts,camera:nucleus.camera}));
  ck('lead_208_exact_total_and_identity_counts',data.Z===82&&data.N===126&&data.A===208&&data.points.length===208);
  ck('82_proton_and_126_neutron_markers',data.points.filter(p=>p.type==='p').length===82&&data.points.filter(p=>p.type==='n').length===126);
  ck('all_marker_ids_unique',new Set(data.points.map(p=>p.id)).size===208);
  ck('positions_are_finite',data.points.every(p=>[p.x,p.y,p.z].every(Number.isFinite)));
  let min=Infinity;
  for(let i=0;i<208;i++)for(let j=i+1;j<208;j++){const a=data.points[i],b=data.points[j];min=Math.min(min,(a.x-b.x)**2+(a.y-b.y)**2+(a.z-b.z)**2);}
  ck('illustrative_FCC_centers_have_no_collisions',Math.abs(min-2)<1e-10);
  ck('all_208_present_in_full_view',data.counts.full.total===208);
  ck('cutaway_exposes_interior_without_changing_isotope',data.counts.cut.total>0&&data.counts.cut.total<208);
  const text=await page.locator('body').innerText();
  ck('physical_scope_disclaimer_visible',text.includes('NOT a claimed nuclear crystal')&&text.includes('nor a packing derived from the P/N/E loom'));
  ck('quantum_shells_not_literal_layers',text.includes('not concentric layers of packed balls'));
  await page.locator('[data-filter="p"]').click();
  ck('proton_filter_exact_count',await page.evaluate(()=>nucleus.counts.full.p===82&&nucleus.counts.full.n===0));
  await page.locator('[data-filter="n"]').click();
  ck('neutron_filter_exact_count',await page.evaluate(()=>nucleus.counts.full.n===126&&nucleus.counts.full.p===0));
  await page.locator('[data-filter="all"]').click();
  const box=await page.locator('#full').boundingBox();
  await page.mouse.move(box.x+box.width/2,box.y+box.height/2);
  await page.mouse.down();await page.mouse.move(box.x+box.width/2+80,box.y+box.height/2+30,{steps:6});await page.mouse.up();
  ck('drag_rotates_shared_view',await page.evaluate(initial=>Math.abs(nucleus.camera.ay-initial.ay)>.2,data.camera));
  await page.locator('#reset').click();
  ck('reset_restores_camera',await page.evaluate(initial=>Math.abs(nucleus.camera.ax-initial.ax)<1e-12&&Math.abs(nucleus.camera.ay-initial.ay)<1e-12,data.camera));
  await page.locator('#cut').focus();await page.keyboard.press('ArrowRight');
  ck('keyboard_rotation_works',await page.evaluate(initial=>nucleus.camera.ay!==initial.ay,data.camera));
  await page.locator('#reset').click();await page.locator('h1').click();await pause(page);
  await page.screenshot({path:path.join(OUT,'lead-208.png'),fullPage:true});
  ck('desktop_image_rendered',(await readFile(path.join(OUT,'lead-208.png'))).length>40000);
  await page.setViewportSize({width:420,height:980});await pause(page);
  ck('mobile_has_no_horizontal_overflow',await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
  ck('mobile_retains_all_identities',await page.evaluate(()=>nucleus.points.length===208&&nucleus.counts.full.total===208));
  await page.screenshot({path:path.join(OUT,'lead-208-mobile.png'),fullPage:true});
  ck('no_uncaught_browser_errors',errors.length===0);
  const paths=[HTML,fileURLToPath(import.meta.url),path.join(ROOT,'research/strominger/checkers/check_lead_208_nucleus.py'),path.join(ROOT,'research/strominger/demos/lead-208-nucleus/README.md'),path.join(ROOT,'research/strominger/scc-models/lead-208-nucleus-v1.json')];
  const sources={};for(const p of paths)sources[path.relative(ROOT,p).replaceAll('\\','/')]=hash(await readFile(p));
  const report={status:'pass',classification:'illustrative_lead_208_display_only',checks,isotope:{name:'lead-208',protons:82,neutrons:126},layout:'Illustrative FCC marker arrangement, not a nuclear lattice, measured positions or loom-derived packing',counts_at_initial_view:data.counts,minimum_squared_center_separation:min,source_sha256:sources,screenshot:'research/strominger/results/lead-208-nucleus/lead-208.png',browser_errors:errors};
  await writeFile(path.join(OUT,'verification.json'),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify({status:'pass',classification:report.classification,checks:Object.keys(checks).length,screenshot:report.screenshot}));
 }finally{await browser.close();}
}
main().catch(async error=>{await mkdir(OUT,{recursive:true});await writeFile(path.join(OUT,'execution-failure.json'),JSON.stringify({status:'fail',checks,error:String(error)},null,2)+'\n');console.error(error);process.exitCode=1;});
