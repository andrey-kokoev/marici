import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath, pathToFileURL} from 'node:url';
import {chromium} from '@playwright/test';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const dist=path.join(root,'website/.vitepress/dist');
const asset=path.join(dist,'experiments/proton-neutron-assembly.html');
const slug1='20261009-4315-shared-proton-and-neutron-assembly';
const slug2='20261009-4316-electron-coupling-from-retained-phase-and-spinor-pairing';
const ledger1=await fs.readFile(path.join(dist,'research/ledger',slug1,'index.html'),'utf8');
const ledger2=await fs.readFile(path.join(dist,'research/ledger',slug2,'index.html'),'utf8');
assert(ledger1.includes('href="/experiments/proton-neutron-assembly.html"'));
assert(ledger2.includes(`/research/ledger/${slug1}`));
assert.equal(await fs.readFile(asset,'utf8'),await fs.readFile(path.join(root,'website/public/experiments/proton-neutron-assembly.html'),'utf8'));
const browser=await chromium.launch({headless:true,args:['--enable-unsafe-swiftshader']});
const errors=[];const stages=[];
try {
  const page=await browser.newPage({viewport:{width:1500,height:1000}});
  page.on('pageerror',e=>errors.push(e.message));
  await page.goto(pathToFileURL(asset).href);
  await page.waitForFunction(()=>window.protonAssemblyAudit||!document.querySelector('#error').hidden,null,{timeout:30000});
  for(let i=0;i<8;i++){
    await page.locator(`[data-step="${i}"]`).click();
    await page.waitForTimeout(1100);
    assert.equal(await page.locator('#error').isVisible(),false,await page.locator('#error').textContent());
    const a=await page.evaluate(()=>({proton:window.protonAssemblyAudit,belt:window.assemblyAudit}));
    assert(a.proton&&a.belt);
    if(i===4)assert(a.proton.maxSharedFaceGap>0.1);
    if(i>=3)assert(a.belt.maxPairGap<1e-10);
    if(i>=6)assert(a.proton.maxSharedFaceGap<1e-10&&a.belt.maxSharedFaceGap<1e-10);
    stages.push({step:i+1,proton_gap:a.proton.maxSharedFaceGap,belt_gap:a.belt.maxSharedFaceGap});
  }
  for(let i=1;i<=12;i++){
    await page.locator('#orbit').fill(String(i));
    await page.locator('#orbit').dispatchEvent('input');
  }
  await page.locator('#coordinates').check();
  await page.locator('#coordinates').uncheck();
  assert.equal(await page.locator('canvas').count(),1);
  assert.deepEqual(errors,[]);
  const report={verification_passed:true,built_ledger_links_resolve:true,built_asset_matches_published_source:true,
    stages,triangle_selections:12,coordinate_toggle:true,one_canvas:true,page_errors:errors};
  await fs.writeFile(path.join(root,'research/voevodsky/results/assembly_ledger_browser.json'),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify(report,null,2));
} finally {await browser.close();}
