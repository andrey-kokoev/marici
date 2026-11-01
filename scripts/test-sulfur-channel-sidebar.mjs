import assert from 'node:assert/strict';
import {mkdir} from 'node:fs/promises';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');
 await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','channels');
 for(const selector of ['#procedure','#prev','#next','#sulfur-32-fibrate','#process-notes','#sulfur-32-fibration'])assert.equal(await page.locator(selector).isVisible(),false,selector);
 for(const selector of ['#sulfur-channel-open','#sulfur-channel-expose','#sulfur-channel-cut','#sulfur-wire-opacity'])assert.equal(await page.locator(selector).isVisible(),true,selector);
 const text=await page.locator('#process-panel').innerText();for(const phrase of ['Edge units','Voxel approximation','Release to update','Fibrate globally','End of defined steps'])assert(!text.includes(phrase),phrase);
 await page.click('#sulfur-channel-expose');assert.equal(await page.locator('#sulfur-channel-cut').inputValue(),'0.35');assert.equal(await page.locator('#sulfur-channel-open').isChecked(),true);assert.equal(await page.locator('#sulfur-wire-opacity').inputValue(),'0.2');
 await page.uncheck('#sulfur-channel-open');assert.equal(await page.locator('#sulfur-channel-open').isChecked(),false);
 await mkdir('test-results',{recursive:true});await page.screenshot({path:'test-results/sulfur-channel-sidebar.png'});
 await page.selectOption('#sulfur-32-view','geometry');assert.equal(await page.locator('#sulfur-32-fibrate').isVisible(),true);assert.equal(await page.locator('#procedure').isVisible(),true);
 assert.deepEqual(errors,[]);console.log('PASS: channel sidebar contains relevant controls only; controls work and geometry navigation is retained.');
}finally{await browser.close();}
