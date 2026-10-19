// Publication/browser verification only, not scientific proof or physical acceptance.
import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import path from 'node:path'
import http from 'node:http'
import { fileURLToPath } from 'node:url'
import { createHash } from 'node:crypto'
import { chromium, expect } from '@playwright/test'
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..'),dist=path.join(root,'website/.vitepress/dist')
const server=http.createServer(async(req,res)=>{try{const url=new URL(req.url,'http://local'),base=path.resolve(dist,'.'+decodeURIComponent(url.pathname));if(!base.startsWith(dist+path.sep))throw new Error('Bad path');for(const file of [base,base+'.html',path.join(base,'index.html')]){if(!(await fs.stat(file).catch(()=>null))?.isFile())continue;res.setHeader('Content-Type',({'.html':'text/html','.mjs':'text/javascript','.js':'text/javascript','.json':'application/json','.css':'text/css'})[path.extname(file)]||'application/octet-stream');res.end(await fs.readFile(file));return}res.writeHead(404);res.end('Not found')}catch{res.writeHead(400);res.end('Bad request')}})
await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve))
const base=process.argv.includes('--live')?'https://marici.andrei-kokoev.workers.dev':`http://127.0.0.1:${server.address().port}`
const sha=bytes=>createHash('sha256').update(bytes).digest('hex')
let browser
try {
 browser=await chromium.launch({headless:true});const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[]
 page.on('pageerror',e=>errors.push(e.message))
 await page.goto(base+'/experiments/research-lab.html');await page.waitForFunction(()=>window.researchLabAudit?.ready)
 const manifest=await (await fetch(base+'/experiments/research-lab/manifest.json')).json()
 for(const [key,entry] of Object.entries(manifest.files)){const r=await fetch(base+`/experiments/research-lab/${key}.json`);assert(r.ok,key);assert.equal(sha(Buffer.from(await r.arrayBuffer())),entry.sha256,`Published ${key} bytes must match the pinned manifest`)}
 const data=await (await fetch(base+'/experiments/research-lab/data.json')).json()
 let a=await page.evaluate(()=>window.researchLabAudit.arrow);assert.equal(a.primitiveCount,12);assert.equal(a.sourceAB,a.hingedAB)
 await page.locator('#hinge').selectOption('hinged');a=await page.evaluate(()=>window.researchLabAudit.arrow);assert.deepEqual(a.points,data.arrow.geometries.hinged);assert.equal(a.sourceAB,a.hingedAB)
 await page.locator('#response-branch').selectOption('unequal_incident_metric_control');a=await page.evaluate(()=>window.researchLabAudit.arrow);assert(a.hingedAB>a.sourceAB);assert(Math.abs(a.local-.25)<1e-12)
 await page.locator('#response-probe').selectOption('1');a=await page.evaluate(()=>window.researchLabAudit.arrow);assert.equal(a.packet.length,6)
 let link=await page.evaluate(()=>window.researchLabAudit.link);assert.equal(link.rank,1);assert.deepEqual(link.readings[0],link.readings[1]);assert(Math.abs(link.norms[0]-link.norms[1])<1e-12)
 await page.locator('#second-reading').check()
 for(const rotation of ['0','1']){await page.locator('#link-rotation').selectOption(rotation);link=await page.evaluate(()=>window.researchLabAudit.link);assert.equal(link.rank,2);assert.notDeepEqual(link.readings[0][1],link.readings[1][1]);link.states.forEach((state,i)=>state.forEach((z,j)=>z.forEach((v,k)=>assert(Math.abs(v-link.recovered[i][j][k])<1e-12,'Use the stored exact decoder'))))}
 await page.locator('#addresses-minimum').click();let tasks=await page.evaluate(()=>window.researchLabAudit.tasks);assert.equal(tasks.addresses.length,data['proton-tasks'].minimum_addresses);assert.equal(tasks.rank,36)
 await page.locator('[data-address="0"]').uncheck();assert.equal(await page.evaluate(()=>window.researchLabAudit.tasks.rank),35)
 await page.locator('#task-carrier').selectOption('neutron');await page.locator('#addresses-minimum').click();tasks=await page.evaluate(()=>window.researchLabAudit.tasks);assert.equal(tasks.addresses.length,data.tasks.minimum_addresses);assert.equal(tasks.rank,36)
 await page.locator('[data-address="0"]').uncheck();assert.equal(await page.evaluate(()=>window.researchLabAudit.tasks.rank),35)
 await page.locator('#addresses-none').click();assert.equal(await page.evaluate(()=>window.researchLabAudit.tasks.rank),0)
 await page.locator('#addresses-all').click();assert.equal(await page.evaluate(()=>window.researchLabAudit.tasks.rank),36)
 for(let i=1;i<=3;i++){await page.locator('#reference-advance').click();const ref=await page.evaluate(()=>window.researchLabAudit.reference);assert.equal(ref.depth,i);assert.equal(ref.history.length,i);assert.equal(ref.operator,i===3?0:2);assert.equal(ref.eligible,i<3)}
 await expect(page.locator('#reference-advance')).toBeDisabled();await page.locator('#reference-recover').click();assert.equal(await page.evaluate(()=>window.researchLabAudit.reference.depth),3)
 for(const units of ['0','1','3']){await page.locator('#reference-units').selectOption(units);await page.locator('#reference-prepare').click();await page.locator('#reference-advance').click();const ref=await page.evaluate(()=>window.researchLabAudit.reference);assert(!ref.eligible);assert.equal(ref.operator,+units);assert.equal(ref.representedNorm,2*(+units)**2)}
 let context=await page.evaluate(()=>window.researchLabAudit.context);assert.equal(context.pairCount,977);assert.equal(context.leafCount,137);assert.equal(context.familyCount,32);assert(!context.admitted)
 await page.locator('#context-b').selectOption('0');assert(await page.evaluate(()=>window.researchLabAudit.context.admitted))
 const branch=await page.evaluate(()=>window.researchLabAudit.branches);assert.equal(branch.rank,8)
 branch.J4.forEach((row,i)=>row.forEach((x,j)=>assert(Math.abs((121*branch.arrow[i][j]+16*branch.state[i][j])/137-x)<1e-12)))
 await page.locator('#retain-contrast').uncheck();assert.equal(await page.evaluate(()=>window.researchLabAudit.branches.rank),4);assert.equal(await page.evaluate(()=>window.researchLabAudit.branches.arrow),null)
 for(let i=0;i<3;i++){await page.locator('#clock-reading').selectOption(String(i));const before=await page.evaluate(()=>window.researchLabAudit.clock);assert.deepEqual(before.populations,data.clock.cases[i].all_forty_populations);assert.equal(before.populations.length,40);await page.locator('#clock-rate').selectOption('3');assert.deepEqual(await page.evaluate(()=>window.researchLabAudit.clock.populations),before.populations);await page.locator('#clock-rate').selectOption('1')}
 await page.locator('#clock-matching').uncheck();const clock=await page.evaluate(()=>window.researchLabAudit.clock);assert(!clock.chartValid);assert.equal(clock.reading,0);assert.deepEqual(clock.populations,data.clock.actual_initial_density);await expect(page.locator('#clock-reading')).toBeDisabled()
 let spatial=await page.evaluate(()=>window.researchLabAudit.spatial);assert(Math.abs(spatial.relativeChange+27.482)<.001);assert.deepEqual(spatial.fullSTests,[1,1,1]);assert.deepEqual(spatial.preparedTests,[32,32,32]);assert(!spatial.continuumCertified)
 for(const metric of ['rate_per_residence','product_probability']){await page.locator('#spatial-metric').selectOption(metric);spatial=await page.evaluate(()=>window.researchLabAudit.spatial);assert.deepEqual(spatial.values,data.spatial.rows.map(row=>row[metric]*(metric==='product_probability'?100:1000)))}
 await page.setViewportSize({width:390,height:844});assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'Research lab mobile overflow')
 for(const name of ['neutron-rest-energy-boundary','hydrogen-binding-boundary','relational-carrier-programme']){await page.goto(base+'/research/results/'+name);await expect(page.locator('h1')).toBeVisible();assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),name+' mobile overflow')}
 await page.goto(base+'/experiments/arrow-symmetry-viewer.html');await expect(page.locator('h1')).toHaveText('Arrow · phase · process');await expect(page.locator('a[href="/experiments/"]')).toBeVisible()
 await page.locator('[data-turn="360"]').click();await expect(page.locator('#returnStatus')).toContainText(/360|opposite|minus|−/i)
 // Published copy remains self-contained even without network access after load.
 await page.context().setOffline(true);await page.locator('[data-turn="720"]').click();await expect(page.locator('#returnStatus')).toContainText(/720|both|same/i);await page.context().setOffline(false)
 assert.equal(errors.length,0,errors.join('\n'))
 console.log('Research lab passed: source-byte manifests, all six interactive sections, both stored link decoders, reconstruction thresholds, reference/context rejection, branch recovery, clock scope, spatial audits, mobile layout and offline symmetry controls. Publication checks only.')
} finally {if(browser)await browser.close();await new Promise(resolve=>server.close(resolve))}
