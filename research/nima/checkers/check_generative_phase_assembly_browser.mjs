import assert from 'node:assert/strict';
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {chromium} from '@playwright/test';
const out=fileURLToPath(new URL('../results/generative-phase-assembly/',import.meta.url));
const browser=await chromium.launch({headless:true});
try{
 const page=await browser.newPage({viewport:{width:1500,height:1150}}),errors=[];page.on('pageerror',e=>errors.push(String(e)));
 await page.goto(pathToFileURL(out+'index.html').href);await page.waitForFunction(()=>globalThis.GeneratedAssemblies);
 const result=await page.evaluate(()=>{
  const view=window.GeneratedAssemblies,d=view.data,$=id=>document.getElementById(id),check=(v,m)=>{if(!v)throw Error(m);};
  function change(id,value){$(id).value=value;$(id).dispatchEvent(new Event('change',{bubbles:true}));}
  check(d.complete&&d.contract.maxSourceTransitions===9,'Wrong completeness/cutoff');
  check(d.nodes.length===d.summary.configurations&&d.shapes.length===d.summary.distinctGeometryRoleAssemblies,'Incomplete catalog');
  const sets=[],seen=new Set();
  for(let i=0;i<d.nodes.length;i++){
   const [parent,op,shape,depth]=d.nodes[i];let packets;
   if(i===0){check(parent===-1&&depth===0,'Bad seed');packets=[d.root];}
   else{check(parent<i,'Nonconstructive parent');const e=d.operations[op];check(sets[parent].includes(e.source),'Missing source record');check(!sets[parent].includes(e.target),'Lost distinction of a newly activated packet');packets=[...sets[parent],e.target].sort((a,b)=>a-b);}
   sets.push(packets);check(packets.length===depth+1,'Hidden multi-stage step');
   const bodies=new Map();for(const p of packets){const c=d.charts[d.packets[p].chart];check(!bodies.has(c.cell)||bodies.get(c.cell)===c.species,'Double occupation');bodies.set(c.cell,c.species);check(d.packets[p].permutation.length===5,'Lost coefficient');}
   const counts={proton:0,neutron:0,electron:0};for(const s of bodies.values())counts[s]++;
   check(JSON.stringify(counts)===JSON.stringify(d.shapes[shape].counts),'Composition mismatch');
  }
  for(const s of d.shapes)for(const id of s.nodes){check(!seen.has(id)&&d.nodes[id][2]===s.id,'Variant missing or duplicated');seen.add(id);}
  check(seen.size===d.nodes.length,'Some realizations hidden');
  for(const p of d.profiles){const key=[p.counts.proton,p.counts.neutron,p.counts.electron].join('/');change('profile',key);const expected=d.shapes.filter(s=>JSON.stringify(s.counts)===JSON.stringify(p.counts)).length;check(view.snapshot().matchingShapes===expected,'Composition filter silently pruned a shape');}
  change('profile','all');let samples=0,records=0;
  for(let k=0;k<d.shapes.length;k+=Math.max(1,Math.floor(d.shapes.length/64))){
   const s=d.shapes[k];change('shape',String(s.id));check(view.snapshot().variants.length===s.nodes.length,'Phase variants lost');
   const id=s.nodes.at(-1);change('variant',String(id));const chain=view.nodeChain(id);
   for(let i=chain.length-1;i>=0;i--){const snap=view.snapshot();check(snap.node===chain[i]&&JSON.stringify(snap.packets)===JSON.stringify(sets[chain[i]]),'Display construction does not match generated word');check($('geometry').querySelectorAll('polygon').length>0,'Missing actual geometry');if(i)$('previous').click();records++;}
   $('complete').click();check(view.snapshot().node===id,'Replay control failed');
   $('packet').value=String(sets[id].at(-1));$('packet').dispatchEvent(new Event('change'));const detail=JSON.parse($('detail').textContent);check(detail.fullCoefficientMap.length===5,'Packet inspector collapsed field');samples++;
  }
  change('filter','certified');const certified=d.shapes.filter(s=>s.nodes.some(i=>d.nodes[i][4]&2));check(view.snapshot().matchingShapes===certified.length,'Certified filter incorrect');
  change('profile','1/0/0');check(view.snapshot().chosen===null,'Empty result displayed a seed instead');
  change('profile','all');check(view.snapshot().chosen!==null,'Failed to restore catalog');
  return {metadataConfigurations:d.nodes.length,metadataGeometryRoleAssemblies:d.shapes.length,compositionFilters:d.profiles.length,certifiedShapes:certified.length,interactiveSamples:samples,displayRecords:records};
 });
 assert.equal(result.metadataConfigurations,136979);assert.equal(result.metadataGeometryRoleAssemblies,2784);assert.deepEqual(errors,[]);
 await page.screenshot({path:out+'viewer.png',fullPage:true});
 const html=await readFile(out+'index.html'),report={status:'pass-generated-assembly-explorer',...result,pageErrors:errors,
  htmlSha256:createHash('sha256').update(html).digest('hex'),scope:'All catalog/phase-variant metadata and composition filters; sampled interactive construction playback and empty/certified filters. No physical assembly or disassembly performed.'};
 await writeFile(out+'browser-verification.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
}finally{await browser.close();}
