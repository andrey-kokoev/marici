import assert from 'node:assert/strict';
import {readFile,writeFile} from 'node:fs/promises';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {chromium} from '@playwright/test';
const out=fileURLToPath(new URL('../results/bounded-phase-path-atlas/',import.meta.url));
const browser=await chromium.launch({headless:true});
try{
 const page=await browser.newPage({viewport:{width:1400,height:1050}}),errors=[];
 page.on('pageerror',e=>errors.push(String(e)));
 await page.goto(pathToFileURL(out+'index.html').href);
 await page.waitForFunction(()=>globalThis.BoundedPhaseAtlas);
 const checked=await page.evaluate(()=>{
  const $=id=>document.getElementById(id),view=globalThis.BoundedPhaseAtlas;
  const eq=(a,b,message)=>{if(JSON.stringify(a)!==JSON.stringify(b))throw Error(message);};
  function change(id,value){$(id).value=value;$(id).dispatchEvent(new Event('change',{bubbles:true}));}
  let paths=0,records=0;
  for(const [name,m] of Object.entries(view.data.models)){
   $('cspan').checked=false;change('length','all');change('model',name);
   eq($('path').options.length,m.paths.length,'Wrong path count');
   for(let p=0;p<m.paths.length;p++){
    change('path',String(p));const path=m.paths[p];
    for(let i=0;i<=path.length;i++){
     const state=view.snapshot();eq(state.step,i,'Wrong forward step');eq(state.state,path.trace[i],'Forward record mismatch');records++;
     if(i<path.length)$('next').click();
    }
    $('reverse').click();eq(view.snapshot().state,path.trace.at(-1),'Reverse boundary mismatch');
    for(let i=0;i<path.length;i++){
     $('next').click();eq(view.snapshot().state,path.inverseSteps[i].to,'Inverse record mismatch');records++;
    }
    eq(view.snapshot().state.history,[],'Reverse did not recover entry history');
    eq(view.snapshot().state.origin,0,'Reverse did not recover origin');
    if(!$('status').textContent.includes('NOT admitted'))throw Error('False native-reversal status');
    $('previous').click();eq(view.snapshot().step,path.length-1,'Earlier record control failed');paths++;
   }
   const limit=view.data.summary.maxTotalTransitions;
   change('length',String(limit));eq($('path').options.length,m.summary.byLength[limit],'Maximum-length filter failed');
   change('length','8');eq($('path').options.length,m.summary.byLength[8],'Previous cutoff filter failed');
   change('length','all');$('cspan').checked=true;$('cspan').dispatchEvent(new Event('change'));
   eq($('path').options.length,m.summary.withinC0ThroughC4,'C-index filter failed');
   change('length','0');eq(view.snapshot().state,null,'Empty result handling failed');$('reverse').click();
  }
  for(const [name,m] of Object.entries(view.data.models)){
   change('length','all');change('model',name);change('graphkind','cap');
   eq($('graph').querySelectorAll('rect').length,m.CExitCapGraph.states.length,'C-exit packet graph node count failed');
   eq($('path').options.length,m.summary.withinC0ThroughC4,'Cap graph did not enable boundary filter');
   change('graphkind','base');eq($('graph').querySelectorAll('rect').length,m.source.charts.length,'Reader graph node count failed');
  }
  return {paths,records};
 });
 assert.equal(checked.paths,255);assert.deepEqual(errors,[]);
 assert.equal(await page.title(),'9-transition C-entry / C-exit atlas');
 assert.equal(await page.locator('#length option[value="9"]').count(),1);
 await page.selectOption('#length','all');await page.selectOption('#model','helium3');await page.selectOption('#graphkind','cap');
 await page.screenshot({path:out+'viewer.png',fullPage:true});
 const atlas=await readFile(out+'index.html');
 const {createHash}=await import('node:crypto');
 const report={status:'pass-self-contained-atlas-browser',...checked,pageErrors:errors,
  htmlSha256:createHash('sha256').update(atlas).digest('hex'),scope:`Local self-contained viewer controls and all${checked.paths} forward/formal-reverse record sequences through nine transitions; no native reverse commands or physical transport executed.`};
 await writeFile(out+'browser-verification.json',JSON.stringify(report,null,2)+'\n');
 console.log(JSON.stringify(report));
}finally{await browser.close();}
