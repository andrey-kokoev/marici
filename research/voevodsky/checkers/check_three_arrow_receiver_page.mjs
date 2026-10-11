import fs from 'node:fs/promises';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {chromium} from '@playwright/test';
const htmlURL=new URL('../../../papers/witness-generators/three-arrow-receiver.html',import.meta.url);
const results=new URL('../results/',import.meta.url);
const html=await fs.readFile(htmlURL,'utf8');
const exact=JSON.parse(await fs.readFile(new URL('three_arrow_receiver_geometry.json',results),'utf8'));
assert(exact.verification_passed);
const ctx={};vm.runInNewContext(html.match(/<script id="receiver-math">([\s\S]*?)<\/script>/)[1],ctx);const M=ctx.ReceiverMath;
const num=s=>{const [a,b='1']=s.split('/');return Number(a)/Number(b);};
const equal=(a,b)=>a.every((x,i)=>Math.abs(x-b[i])<1e-12);
const checks={
 geometry_matches_exact_checker:Object.entries(exact.coordinates).every(([k,p])=>equal(M.P[k],p.map(num))),
 barycenters_match_exact_checker:equal(M.bP,exact.proton_barycenter.map(num))&&equal(M.bQ,exact.receiver_tetrahedron_barycenter.map(num)),
 face_center_matches_exact_checker:equal(M.F,exact.shared_face_center.map(num)),
 fifteen_primitive_arrows:M.old.length===12&&M.incoming.length===3&&M.incoming.every(([a,b])=>'ABC'.includes(a)&&b==='e'),
 no_new_outgoing_arrows:[...M.old,...M.incoming].every(([a,b])=>a!=='e'),
 signal_compatibility_for_three_characters:[0,1,2].every(k=>M.signals(k).every(r=>(r.input+r.weight)%3===r.arrival&&r.arrival===k)),
};
const browser=await chromium.launch({headless:true,args:['--enable-unsafe-swiftshader']});
const page=await browser.newPage({viewport:{width:1380,height:1080},deviceScaleFactor:1});const errors=[];page.on('pageerror',e=>errors.push(e.message));
try{
 await page.goto(htmlURL.href);
 await page.waitForFunction(()=>document.querySelector('#view canvas')&&document.querySelector('#error').hidden,{timeout:60000});
 checks.webgl_started=await page.locator('#view canvas').count()===1;
 checks.source_stage_labels_correct=(await page.locator('#structure').innerText()).includes('15 primitive arrows');
 await page.screenshot({path:fileURLToPath(new URL('three_arrow_receiver_source.png',results)),fullPage:true});
 await page.locator('#centers').click();
 checks.centers_distinguished_from_apex=(await page.locator('#structure').innerText()).includes('bQ ≠ receiver apex e');
 checks.center_button_selected=await page.locator('#centers').getAttribute('aria-pressed')==='true';
 await page.screenshot({path:fileURLToPath(new URL('three_arrow_receiver_centers.png',results)),fullPage:true});
 await page.locator('#frames').uncheck();await page.locator('#face').uncheck();
 checks.frame_controls_toggle=!(await page.locator('#frames').isChecked())&&!(await page.locator('#face').isChecked());
 await page.screenshot({path:fileURLToPath(new URL('three_arrow_receiver_segment.png',results)),fullPage:true});
 await page.locator('#phase').selectOption({value:'1'});
 checks.cyclic_receiver_updates=(await page.locator('#status').innerText()).includes('equal ω.')&&(await page.locator('#signals').innerText()).includes('ω² × ω² = ω');
 await page.locator('#frames').check();await page.locator('#face').check();await page.locator('#source').click();await page.locator('#reset-camera').click();
 await page.setViewportSize({width:390,height:844});await page.waitForTimeout(250);
 checks.mobile_no_overflow=await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth);
 await page.screenshot({path:fileURLToPath(new URL('three_arrow_receiver_mobile.png',results)),fullPage:true});
 checks.no_browser_errors=errors.length===0;
}finally{await browser.close();}
const result={passed:Object.values(checks).every(Boolean),checks,browser_errors:errors,html_sha256:createHash('sha256').update(html).digest('hex')};
await fs.writeFile(new URL('three_arrow_receiver_page_check.json',results),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result,null,2));assert(result.passed);
