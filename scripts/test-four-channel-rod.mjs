import http from 'node:http';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..'),out=await fs.mkdtemp(path.join(os.tmpdir(),'four-channel-rod-'));
const server=http.createServer(async(req,res)=>{try{
 const file=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));if(!file.startsWith(root+path.sep))throw Error('Outside root');
 const data=await fs.readFile(file);res.setHeader('Content-Type',({'.html':'text/html','.mjs':'text/javascript','.js':'text/javascript'})[path.extname(file)]??'text/plain');res.end(data);
}catch{res.statusCode=404;res.end('Not found');}});
await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));let browser;
try{
 browser=await chromium.launch();const page=await browser.newPage({viewport:{width:1250,height:1100}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(`http://127.0.0.1:${server.address().port}/research/realization-tower/four-channel-rod.html`);await page.waitForFunction(()=>globalThis.fourChannelAudit);
 for(const k of [1,5,6,7])for(const anchor of ['center','electron']){
  await page.locator('#k').fill(String(k));await page.locator('#anchor').selectOption(anchor);
  const audit=await page.evaluate(()=>fourChannelAudit);assert.equal(audit.k,k);assert.equal(audit.anchor,anchor);assert.equal(await page.locator('[data-fiber]').count(),4);assert.deepEqual(audit.assignments,[]);
  for(const p of [audit.projection.center,...audit.projection.vertices])assert(p[0]>20&&p[0]<980&&p[1]>50&&p[1]<710,'Projected reference must fit the view');
  await page.screenshot({path:path.join(out,`k${k}-${anchor}.png`),fullPage:true});await fs.writeFile(path.join(out,`k${k}-${anchor}.json`),JSON.stringify(audit,null,2));
 }
 const before=await page.evaluate(()=>fourChannelAudit.yaw);const box=await page.locator('#view').boundingBox();await page.mouse.move(box.x+300,box.y+200);await page.mouse.down();await page.mouse.move(box.x+380,box.y+240);await page.mouse.up();assert.notEqual(await page.evaluate(()=>fourChannelAudit.yaw),before);
 await page.locator('#reset').click();assert.equal(await page.evaluate(()=>fourChannelAudit.yaw),.25);
 await page.setViewportSize({width:390,height:844});assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));await page.screenshot({path:path.join(out,'mobile.png'),fullPage:true});
 assert.deepEqual(errors,[]);console.log(`PASS four-channel rod: size, anchors, four retained labels, bounds, orbit, mobile, no assignments. Screenshots: ${out}`);
}finally{await browser?.close();await new Promise(resolve=>server.close(resolve));}
