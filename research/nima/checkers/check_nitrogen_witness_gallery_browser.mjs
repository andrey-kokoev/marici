import assert from 'node:assert/strict';
import {readFileSync,writeFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
import {chromium} from '@playwright/test';
const out='research/nima/results/assembly-atlas',browser=await chromium.launch({headless:true});
try{
 const page=await browser.newPage({viewport:{width:1500,height:1100}}),errors=[];page.on('pageerror',e=>errors.push(String(e)));
 await page.goto(pathToFileURL(resolve(out+'/index.html')).href);await page.locator('a[href="nitrogen.html"]').click();await page.waitForFunction(()=>window.NitrogenWitnesses);
 const checks=await page.evaluate(()=>{
 const v=window.NitrogenWitnesses,$=id=>document.getElementById(id),check=(ok,m)=>{if(!ok)throw Error(m);},change=(id,value)=>{$(id).value=value;$(id).dispatchEvent(new Event('change'));};let prefixes=0;
 check(v.data.witnessOnly,'Missing witness-only declaration');check(v.data.witnesses.length===11,'Lost saved witness');
 for(const w of v.data.witnesses){change('witness',w.id);check(v.snapshot().certifiedExit,'Full witness not certified');for(let step=w.word.length;step>=0;step--){const s=v.snapshot();check(s.id===w.id&&s.step===step,'Wrong replay position');check(JSON.stringify(s.packets)===JSON.stringify(w.prefixes[step].packets),'Lost branch on replay');check(s.grade<=w.maxOrigin,'Operation index used as phase');check(document.querySelectorAll('svg polygon').length>0,'Geometry missing');prefixes++;if(step)$('previous').click();} $('next').click();check(v.snapshot().step===1,'Forward operation failed');$('full').click();check(v.snapshot().step===w.word.length,'Full replay failed');$('electrons').click();$('electrons').click();}
 change('budget','4');change('isotope','7');check(v.snapshot().id===null,'Empty filter retained witness');check($('summary').textContent.includes('not an absence result'),'Empty filter confused with exclusion');change('isotope','8');check(v.snapshot().id==='D4-N15-7e','Neutral-count witness unavailable');
 check($('searches').textContent.includes('UNRESOLVED'),'Resource stop lost');return {witnesses:v.data.witnesses.length,prefixes,neutralOperations:v.snapshot().step};
 });
 assert.equal(checks.witnesses,11);assert.equal(checks.neutralOperations,37);assert.deepEqual(errors,[]);
 await page.screenshot({path:out+'/nitrogen-viewer.png',fullPage:true});
 const report={status:'pass-nitrogen-gallery-browser',...checks,pageErrors:errors,htmlSha256:createHash('sha256').update(readFileSync(out+'/nitrogen.html')).digest('hex')};writeFileSync(out+'/browser-verification.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
}finally{await browser.close();}
