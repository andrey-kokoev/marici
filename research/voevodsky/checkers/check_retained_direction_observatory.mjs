import fs from 'node:fs/promises';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {chromium} from '@playwright/test';

const htmlURL=new URL('../../../papers/witness-generators/retained-direction-observatory.html',import.meta.url);
const sourceURL=new URL('../results/proton_merkle_store.json',import.meta.url);
const results=new URL('../results/',import.meta.url);
const html=await fs.readFile(htmlURL,'utf8'),sourceText=await fs.readFile(sourceURL,'utf8');
const source=JSON.parse(sourceText),store=source.objects;
const context={};vm.runInNewContext(html.match(/<script id="observatory-math">([\s\S]*?)<\/script>/)[1],context);
const M=context.ObservatoryMath;
const close=(a,b)=>Math.abs(a-b)<1e-10;
const same=(a,b)=>a.length===b.length&&a.every((x,i)=>Array.isArray(x)?same(x,b[i]):close(x,b[i]));
const number=s=>{const [a,b='1']=s.split('/');return Number(a)/Number(b);};
const mul=(z,w)=>[z[0]*w[0]-3*z[1]*w[1],z[0]*w[1]+z[1]*w[0]];
const checks={};let compared=0,match=true;
for(const item of Object.values(store)){
 if(item.kind!=='arrow')continue;
 const s=store[item.source],t=store[item.target];if(s.stage!=='raw'||t.stage!=='local')continue;
 const z=store[item.coefficient],actual=[number(z.real),number(z.imag_sqrt3)];
 const v=M.vectors[s.triangle],norm=v.reduce((s,z)=>s+z[0]**2+3*z[1]**2,0);
 const a=v['xyz'.indexOf(t.axis)],b=v['xyz'.indexOf(s.axis)];
 const expected=mul(a,[b[0],-b[1]]).map(x=>x/norm);
 compared++;match&&=same(actual,expected);
}
checks.all_108_local_source_coefficients_reconstructed=compared===108&&match;
const geometry=store[store[source.root].geometry].payload;
checks.all_twelve_triangle_frames_match_source=geometry.triangles_and_transports.every(r=>M.faces[r.outer_arrow]===r.triangle[0].slice(2)&&r.outer_arrow===r.triangle[1]+r.triangle[2]);
const front=[1/3,1/3,1/3,0],back=[0,0,0,1];
const f=M.prepare(front,true),b=M.prepare(back,true);
checks.first_readout_collision=same(f.first,b.first);
checks.second_interface_separates_collision=!same(M.second(f,'AC'),M.second(b,'AC'));
const erased=M.prepare(front,false);
checks.discard_record_contains_no_original_direction=erased.direction===null&&Object.keys(erased).sort().join(',')==='direction,first';
checks.second_reader_refuses_erased_input=M.second(erased,'AC')===null;
checks.sequential_projection_does_not_rescue_collision=same(M.apply('AC',f.first),M.apply('AC',b.first));
let recovered=true,count=0,sameFace=true;
for(let a=0;a<=12;a++)for(let b=0;b<=12-a;b++)for(let c=0;c<=12-a-b;c++){
 const input=[a,b,c,12-a-b-c].map(x=>x/12),record=M.prepare(input,true);count++;
 for(const [edge,face]of Object.entries(M.faces)){
  const r=M.recover(edge,record.first,M.second(record,edge));
  if(face==='ABC')sameFace&&=r===null;
  else recovered&&=r!==null&&same(r.barycentric,input);
 }
}
checks.all_455_inputs_recovered_by_each_different_face_interface=count===455&&recovered;
checks.same_face_interfaces_report_ambiguity=sameFace;
assert(Object.values(checks).every(Boolean));
const browser=await chromium.launch({headless:true,args:['--enable-unsafe-swiftshader']});
const page=await browser.newPage({viewport:{width:1360,height:1050},deviceScaleFactor:1});
const errors=[];page.on('pageerror',e=>errors.push(e.message));
try{
 await page.goto(htmlURL.href);
 await page.waitForFunction(()=>document.querySelector('#view canvas')&&!document.querySelector('#error:not([hidden])'),{timeout:60000});
 checks.webgl_view_started=await page.locator('#view canvas').count()===1;
 assert.match(await page.locator('#recovery').innerText(),/0.33333, 0.33333, 0.33333, 0.00000/);
 await page.screenshot({path:fileURLToPath(new URL('retained_direction_observatory.png',results)),fullPage:true});
 const first=await page.locator('#first-value').innerText(),second=await page.locator('#second-value').innerText();
 await page.locator('#back').click();
 checks.ui_first_output_unchanged=await page.locator('#first-value').innerText()===first;
 checks.ui_second_output_changed=await page.locator('#second-value').innerText()!==second;
 assert.match(await page.locator('#recovery').innerText(),/0.00000, 0.00000, 0.00000, 1.00000/);
 await page.locator('#retain').uncheck();
 checks.discard_blocks_recovery=(await page.locator('#recovery').innerText()).includes('Cannot reconstruct');
 checks.discard_labels_sequential_operation=(await page.locator('#second-value').innerText()).includes('Projecting the first output instead');
 await page.locator('#front').click();
 checks.discard_applies_to_fresh_preparation=(await page.locator('#record').innerText()).includes('discarded');
 await page.locator('#retain').check();await page.locator('#second').selectOption('BC');
 checks.ui_same_face_ambiguity=(await page.locator('#recovery').innerText()).includes('Not unique');
 await page.locator('#second').selectOption('AC');await page.locator('#sample').click();
 checks.other_preparation_recovers=(await page.locator('#recovery').innerText()).includes('Recovered barycentrics');
 await page.setViewportSize({width:390,height:844});await page.waitForTimeout(200);
 checks.mobile_no_horizontal_overflow=await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth);
 await page.screenshot({path:fileURLToPath(new URL('retained_direction_observatory_mobile.png',results)),fullPage:true});
 checks.no_browser_exceptions=errors.length===0;
}finally{await browser.close();}
const result={passed:Object.values(checks).every(Boolean),checks,grid_points:count,source_root:source.root,
 source_sha256:createHash('sha256').update(sourceText).digest('hex'),html_sha256:createHash('sha256').update(html).digest('hex'),browser_errors:errors};
await fs.writeFile(new URL('retained_direction_observatory_check.json',results),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result,null,2));assert(result.passed);
