import assert from 'node:assert/strict';
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {chromium} from '@playwright/test';
const out=fileURLToPath(new URL('../results/origin-bounded-assemblies/',import.meta.url)),browser=await chromium.launch({headless:true});
try{
 const page=await browser.newPage({viewport:{width:1500,height:1100}}),errors=[];page.on('pageerror',e=>errors.push(String(e)));
 await page.goto(pathToFileURL(out+'index.html').href);await page.waitForFunction(()=>globalThis.OriginAssemblies);
 const checked=await page.evaluate(()=>{
  const view=window.OriginAssemblies,$=id=>document.getElementById(id),check=(ok,message)=>{if(!ok)throw Error(message);},eq=(a,b,m)=>check(JSON.stringify(a)===JSON.stringify(b),m);
  function change(id,value){$(id).value=String(value);$(id).dispatchEvent(new Event('change',{bubbles:true}));}
  let metadata=0,profiles=0,records=0,witnessOperations=0;
  for(const [key,d]of Object.entries(view.data.cases)){
   const D=Number(key),sets=[];
   for(let id=0;id<d.nodes.length;id++){
    const [parent,operation,grade,minOps,flags,profile]=d.nodes[id];let chosen;
    if(!id){check(parent===-1&&grade===0,'Invalid origin seed');chosen=[d.root];}
    else{check(parent<id,'Nonconstructive record');const op=d.operations[operation];check(sets[parent].includes(op.source),'Lost parent packet');chosen=[...new Set([...sets[parent],op.target])].sort((a,b)=>a-b);}
    sets.push(chosen);check(chosen.length===minOps+1,'Operation metadata is not representative length');
    check(chosen.every(p=>d.packets[p].origin<=D),'Phase cap violated');eq(chosen.reduce((g,p)=>Math.max(g,d.packets[p].origin),0),grade,'Sibling origin grades were summed');
    const bodies=new Map();for(const p of chosen){const c=d.charts[d.packets[p].chart];check(!bodies.has(c.cell)||bodies.get(c.cell)===c.species,'Incompatible species union');bodies.set(c.cell,c.species);check(d.packets[p].permutation.length===5,'Coefficient discarded');}
    const counts={proton:0,neutron:0,electron:0};for(const s of bodies.values())counts[s]++;eq(counts,d.profiles[profile].counts,'Wrong output composition');metadata++;
   }
   change('budget',key);change('filter','all');eq(view.snapshot().matching,d.nodes.length,'Phase case catalog truncated');
   if(d.nodes.length>200){$('page-next').click();eq(view.snapshot().page,1,'Pagination failed');$('page-previous').click();eq(view.snapshot().page,0,'Reverse pagination failed');}
   for(let p=0;p<d.profiles.length;p++){change('profile',p);const expected=d.nodes.filter(n=>n[5]===p).length;eq(view.snapshot().matching,expected,'Profile filter changed family');profiles++;}
   change('profile','all');$('witness').click();eq(view.snapshot().node,d.witness.node,'Wrong branching witness');
   const chain=view.nodeChain(d.witness.node);eq(chain.length-1,d.witness.operationCount,'Wrong representative word');
   for(let i=chain.length-1;i>=0;i--){const s=view.snapshot();eq(s.node,chain[i],'Wrong operation replay');eq(s.packets,sets[chain[i]],'Record replay dropped a branch');check(s.grade<=D,'Replay consumed total operations as phases');if(i)$('previous').click();records++;}
   $('complete').click();if(D===2){check(view.snapshot().step>9,'Old nine-operation cutoff survived');check(d.witness.occupiedBodies>10,'Old ten-body bound survived');witnessOperations=view.snapshot().step;}
   change('filter','exit');eq(view.snapshot().matching,d.summary.selectedRecordExitCertificates,'Unselected cache contaminated exit filter');
   const noExits=d.profiles.findIndex(p=>!p.counts.electron);change('profile',noExits);eq(view.snapshot().chosen,null,'Empty filter retained a false exit');change('profile','all');
  }
  return {metadataConfigurations:metadata,compositionFilters:profiles,displayRecords:records,originTwoWitnessOperations:witnessOperations};
 });
 assert.equal(checked.metadataConfigurations,3+108+198356);assert.equal(checked.originTwoWitnessOperations,21);assert.deepEqual(errors,[]);
 await page.selectOption('#budget','2');await page.locator('#witness').click();await page.screenshot({path:out+'viewer.png',fullPage:true});
 const html=await readFile(out+'index.html'),report={status:'pass-origin-budget-assembly-explorer',...checked,pageErrors:errors,htmlSha256:createHash('sha256').update(html).digest('hex'),scope:'All D0/1/2 catalog metadata and composition filters, pagination, empty selections and branching witness replay. This is not a global coupled-field or physical assembly proof.'};
 await writeFile(out+'browser-verification.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
}finally{await browser.close();}
