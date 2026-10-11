import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
import {chromium} from '@playwright/test';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const asset=path.join(root,'website/.vitepress/dist/experiments/fourth-construction.html');
const bridgeRaw=await fs.readFile(path.join(root,'research/voevodsky/results/fourth_construction_bridge_store.json'));
const browser=await chromium.launch({headless:true,args:['--enable-unsafe-swiftshader']});
const errors=[];let states=0;
try{
 const page=await browser.newPage({viewport:{width:1500,height:1000}});page.on('pageerror',e=>errors.push(e.message));await page.goto(pathToFileURL(asset).href);
 await page.waitForFunction(()=>window.fourthAssemblyAudit||!document.querySelector('#error').hidden,null,{timeout:30000});
 async function audit(){assert.equal(await page.locator('#error').isVisible(),false,await page.locator('#error').textContent());const a=await page.evaluate(()=>window.fourthAssemblyAudit);assert(a);assert(a.routeError<1e-9);assert(Math.abs(a.electronWeight-1)<1e-9);if(a.normalized){assert(Math.abs(a.total-1)<1e-9);assert(a.reconstructionError<1e-9);}states++;return a;}
 for(let i=0;i<6;i++){await page.locator(`[data-step="${i}"]`).click();await page.waitForTimeout(850);const a=await audit();assert.equal(a.normalized,i>=3);}
 const hash=await page.evaluate(()=>JSON.parse(document.querySelector('#construction-data').textContent).bridge_store_sha256);assert.equal(hash,createHash('sha256').update(bridgeRaw).digest('hex'));
 for(const route of ['direct','electron']){
  await page.locator('#route').selectOption(route);
  for(const [t,p]of [[0,0],[180,0],[90,90],[90,-90],[53,127]]){
   await page.locator('#theta').fill(String(t));await page.locator('#theta').dispatchEvent('input');await page.locator('#phi').fill(String(p));await page.locator('#phi').dispatchEvent('input');await audit();
  }
 }
 await page.locator('#normalize').uncheck();await page.locator('#plus-y').click();let a=await audit();assert(Math.abs(a.total-(1-5/Math.sqrt(74)))<1e-9);assert(a.reconstructionError>.1);
 await page.locator('#minus-y').click();a=await audit();assert(Math.abs(a.total-(1+5/Math.sqrt(74)))<1e-9);
 await page.locator('#plus-z').click();a=await audit();assert(Math.abs(a.total-1)<1e-9);assert(a.reconstructionError>.1);
 await page.locator('#normalize').check();await audit();assert.equal(await page.locator('canvas').count(),1);
 await page.screenshot({path:path.join(root,'research/voevodsky/results/fourth-construction-browser.png')});
 await page.setViewportSize({width:600,height:900});await page.waitForTimeout(150);await audit();assert.deepEqual(errors,[]);
 for(const name of ['electron-spinor-construction.html','proton-neutron-assembly.html']){const html=await fs.readFile(path.join(root,'website/.vitepress/dist/experiments',name),'utf8');assert(html.includes('href="fourth-construction.html"'));}
 const report={verification_passed:true,six_stages:true,audited_states:states,embedded_bridge_hash_matches:true,both_routes_preserve_correctly_normalized_states:true,naive_y_state_weight_failure_reproduced:true,unit_weight_alone_does_not_guarantee_recovery:true,one_canvas:true,mobile_resize:true,existing_viewer_links:true,page_errors:errors};
 await fs.writeFile(path.join(root,'research/voevodsky/results/fourth_construction_browser.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report,null,2));
}finally{await browser.close();}
