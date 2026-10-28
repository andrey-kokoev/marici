import assert from 'node:assert/strict';
import {mkdir} from 'node:fs/promises';
import {createServer} from 'vite';
import {chromium} from '@playwright/test';
const server=await createServer({configFile:false,root:'examples/realization-lattice',server:{host:'127.0.0.1',port:0},logLevel:'error'});
let browser;
try{
  await server.listen();const address=server.httpServer.address(),url=`http://127.0.0.1:${address.port}/`;
  browser=await chromium.launch({headless:true,args:['--enable-webgl','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
  const page=await browser.newPage({viewport:{width:1100,height:760}}),errors=[];
  page.on('pageerror',e=>errors.push(e.message));await page.goto(url);
  await page.waitForFunction(()=>document.querySelector('#fallback').hidden);
  assert.match(await page.locator('#selection-status').textContent(),/12\/12 neighbours/);
  const canvas=page.locator('canvas');
  // Larger invisible mouse target around the central vertex, not sphere raycast.
  await page.locator('#extent').evaluate(el=>{el.value='1';el.dispatchEvent(new Event('input'));});
  await page.waitForFunction(()=>document.querySelector('#extent-value').value==='1');
  await page.locator('#reset').click();
  await page.locator('#vertex').selectOption('1,1,0');assert.equal(await page.locator('#vertex').inputValue(),'1,1,0');
  let rect=await canvas.boundingBox();await page.mouse.click(rect.x+rect.width/2+9,rect.y+rect.height/2);
  assert.equal(await page.locator('#vertex').inputValue(),'0,0,0','mouse halo selects centre');
  await canvas.focus();await page.keyboard.press('ArrowLeft');await page.keyboard.press('q');await page.keyboard.press('+');
  const before=await canvas.screenshot(),selected=await page.locator('#vertex').inputValue();
  rect=await canvas.boundingBox();await page.mouse.move(rect.x+rect.width/2,rect.y+rect.height/2);await page.mouse.down();await page.mouse.move(rect.x+rect.width/2+100,rect.y+rect.height/2+60,{steps:15});await page.mouse.up();await page.waitForTimeout(100);
  const after=await canvas.screenshot();assert(!before.equals(after),'drag changes rendered view');assert.equal(await page.locator('#vertex').inputValue(),selected,'drag must not select');
  // Appearance changes must not reconstruct the lattice / vertex list.
  await page.evaluate(()=>{window.savedOption=document.querySelector('#vertex').firstElementChild;});
  await page.locator('#opacity').evaluate(el=>{el.value='0.04';el.dispatchEvent(new Event('input'));});
  for(const id of ['edges','points','star','colors','planes']){await page.locator('#'+id).click();await page.locator('#'+id).click();}
  assert(await page.evaluate(()=>window.savedOption===document.querySelector('#vertex').firstElementChild));
  const start=Date.now();await page.locator('#extent').evaluate(el=>{el.value='6';el.dispatchEvent(new Event('input'));});
  await page.waitForFunction(()=>document.querySelector('#extent-value').value==='6');const rebuildMs=Date.now()-start;
  await page.locator('#distance').evaluate(el=>{el.value='1.1';el.dispatchEvent(new Event('input'));});
  await page.waitForFunction(()=>document.querySelector('#distance-value').value==='1.10');
  await page.locator('#reset').click();assert.match(await page.locator('#selection-status').textContent(),/12\/12 neighbours/);
  // Return to readable defaults for visual inspection.
  await page.locator('#extent').evaluate(el=>{el.value='3';el.dispatchEvent(new Event('input'));});
  await page.waitForFunction(()=>document.querySelector('#extent-value').value==='3');
  await page.locator('#opacity').evaluate(el=>{el.value='0.02';el.dispatchEvent(new Event('input'));});
  await page.locator('#reset').click();
  const output='research/realization-tower/results/lattice-ui';await mkdir(output,{recursive:true});
  await page.screenshot({path:`${output}/desktop.png`});
  await page.locator('#helium-mode').selectOption('interval');
  await page.locator('#helium-preset').click();
  await page.waitForFunction(()=>document.querySelectorAll('.pole-label:not([hidden])').length===2);
  assert(await page.locator('#helium').isChecked());
  assert.match(await page.locator('#helium-info').textContent(),/Four equal-volume wedges/);
  await page.screenshot({path:`${output}/helium-candidate.png`});
  for(const w of ['0','1','2','3']){await page.locator('#wedge').selectOption(w);assert.match(await page.locator('#helium-info').textContent(),new RegExp(`W${Number(w)+1} highlighted`));}
  await page.locator('#helium').uncheck();await page.waitForFunction(()=>[...document.querySelectorAll('.pole-label')].every(el=>el.hidden));
  assert(await page.locator('#wedge').isDisabled());
  await page.locator('#helium-mode').selectOption('carriers');await page.locator('#helium-preset').click();
  await page.waitForFunction(()=>document.querySelectorAll('.pole-label:not([hidden])').length===6);
  assert.match(await page.locator('#helium-info').textContent(),/2 P · 2 N · 2 E/);
  await page.screenshot({path:`${output}/helium-six-carriers.png`});
  for(let i=0;i<6;i++){await page.locator('#wedge').selectOption(String(i));await page.waitForFunction(()=>document.querySelectorAll('.pole-label:not([hidden])').length===1);}
  const touch=await browser.newContext({viewport:{width:390,height:844},hasTouch:true,isMobile:true,deviceScaleFactor:1});
  const mobile=await touch.newPage();mobile.on('pageerror',e=>errors.push(e.message));await mobile.goto(url);
  await mobile.waitForFunction(()=>document.querySelector('#fallback').hidden);
  await mobile.locator('#extent').evaluate(el=>{el.value='1';el.dispatchEvent(new Event('input'));});
  await mobile.waitForFunction(()=>document.querySelector('#extent-value').value==='1');
  await mobile.locator('#vertex').selectOption('1,1,0');await mobile.evaluate(()=>scrollTo(0,0));
  rect=await mobile.locator('canvas').boundingBox();await mobile.touchscreen.tap(rect.x+rect.width/2+18,rect.y+rect.height/2);
  assert.equal(await mobile.locator('#vertex').inputValue(),'0,0,0','24px touch halo selects central vertex');
  // Hidden points must not be selectable by touch.
  await mobile.locator('#vertex').selectOption('1,1,0');await mobile.locator('#points').uncheck();await mobile.evaluate(()=>scrollTo(0,0));
  await mobile.touchscreen.tap(rect.x+rect.width/2,rect.y+rect.height/2);assert.equal(await mobile.locator('#vertex').inputValue(),'1,1,0');
  await mobile.locator('#points').check();await mobile.locator('#reset').click();await mobile.evaluate(()=>scrollTo(0,0));
  assert(await mobile.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  await mobile.screenshot({path:`${output}/mobile.png`,fullPage:true});
  await mobile.locator('#helium-preset').tap();await mobile.evaluate(()=>scrollTo(0,0));
  await mobile.waitForFunction(()=>document.querySelectorAll('.pole-label:not([hidden])').length===6);
  await mobile.screenshot({path:`${output}/helium-mobile.png`});
  assert.deepEqual(errors,[]);
  console.log(`PASS: mouse/touch halo selection, drag without selection, keyboard/list access, appearance reuse, controls, reset, mobile layout. Extent-6 update observed in ${rebuildMs}ms (single local run, not a benchmark). Screenshots: ${output}`);
  await touch.close();
}finally{await browser?.close();await server.close();}
