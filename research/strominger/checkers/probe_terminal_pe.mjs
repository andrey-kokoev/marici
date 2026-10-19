// Counterfactual terminal PE shortcut. Never changes source-rule admission.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
import {phaseUniverse} from '../../nima/origin-bounded-assemblies.mjs';
import {makeLatticeItem} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
function audit(r,ids,root){
 const selected=new Set(ids),chart=p=>r.charts[r.packets[p].chart],cell=p=>chart(p).cell,occupied=new Set(ids.map(cell)),description=r.describe(ids);assert.equal(description.valid,true);
 const native=ids.flatMap(p=>r.outgoing(p).map(i=>r.operations[i])).filter(o=>selected.has(o.target));
 const exits=ids.filter(p=>chart(p).species==='electron');assert.ok(exits.every(p=>r.outgoing(p).length===0));
 const shortcuts=[];
 for(const p of ids.filter(p=>chart(p).species==='proton'))for(const pn of r.outgoing(p).map(i=>r.operations[i]).filter(o=>o.kind==='PN')){
  if(occupied.has(cell(pn.target)))continue;
  for(const ne of r.outgoing(pn.target).map(i=>r.operations[i]).filter(o=>o.kind==='NE'&&selected.has(o.target))){
   r.validateTransfer(pn);r.validateTransfer(ne);const e=ne.target,shared=r.geometry.cells[cell(p)].vertices.filter(v=>r.geometry.cells[cell(e)].vertices.includes(v));
   assert.equal(shared.length,2);assert.deepEqual([...shared].sort(),[chart(p).aliases.C1,chart(p).aliases.M1].sort());assert.equal(r.outgoing(e).length,0);
   const permutation=ne.permutation.map(i=>pn.permutation[i]);assert.deepEqual(permutation.map(i=>r.packets[p].permutation[i]),r.packets[e].permutation);assert.equal(r.packets[p].origin,r.packets[e].origin);
   // Body-level terminal P: none of its selected readers has an outgoing
   // native edge into another occupied nuclear body. Reader advances allowed.
   const bodyTerminal=!native.some(o=>cell(o.source)===cell(p)&&cell(o.target)!==cell(p)&&chart(o.target).species!=='electron');
   const recordTerminal=!native.some(o=>o.source===p); // stricter, reader-level
   shortcuts.push({source:p,target:e,kind:'hypothetical-terminal-PE',referenceNeutronCell:cell(pn.target),nativeFactors:[pn.id,ne.id],edge:shared,permutation,bodyTerminal,recordTerminal});
  }
 }
 function connectivity(edges){
  const rooted=new Set([root]),queue=[root],construction=[];for(let i=0;i<queue.length;i++)for(const o of edges)if(o.source===queue[i]&&!rooted.has(o.target)){rooted.add(o.target);queue.push(o.target);construction.push(o);assert.equal(r.describe(queue).valid,true,'Incompatible construction prefix');}
  const canExit=new Set(exits),back=[...exits];for(let i=0;i<back.length;i++)for(const o of edges)if(o.target===back[i]&&!canExit.has(o.source)){canExit.add(o.source);back.push(o.source);}
  const witnessed=new Set(edges.filter(o=>cell(o.source)!==cell(o.target)).map(o=>[cell(o.source),cell(o.target)].sort((a,b)=>a-b).join(':')));
  const missingContacts=description.contacts.filter(c=>!witnessed.has([...c.cells].sort((a,b)=>a-b).join(':')));
  return {construction,unrootedPackets:ids.filter(p=>!rooted.has(p)),unrootedBodies:[...new Set(ids.filter(p=>!rooted.has(p)).map(cell))],noExitPackets:ids.filter(p=>!canExit.has(p)),missingContacts:missingContacts.length,passesHypotheticalChecks:rooted.size===ids.length&&canExit.size===ids.length&&missingContacts.length===0};
 }
 const baseline=connectivity(native),variants={};for(const [name,extra] of [['electron-terminal',shortcuts],['electron-and-proton-body-terminal',shortcuts.filter(o=>o.bodyTerminal)],['electron-and-proton-record-terminal',shortcuts.filter(o=>o.recordTerminal)]]){
  const result=connectivity([...native,...extra]);
  // A sink-only shortcut cannot change reachability of any nuclear record.
  const nuclear=p=>chart(p).species!=='electron';assert.deepEqual(result.unrootedPackets.filter(nuclear),baseline.unrootedPackets.filter(nuclear));
  variants[name]={shortcuts:extra.length,...result};
 }
 return {selectedPackets:ids,counts:r.inspect(ids).counts,electronRecords:exits.length,allElectronRecordsNativeTerminal:true,protonRecords:ids.filter(p=>chart(p).species==='proton').map(p=>({packet:p,nativeOutgoing:r.outgoing(p).length})),baseline,shortcuts,variants};
}
function* permutations(a){if(!a.length)yield [];for(const x of a)for(const p of permutations(a.filter(y=>y!==x)))yield [x,...p];}
const hydrogen=[],seed=makeLatticeItem('tetrahedron',[0,0,0,0]);for(const marking of permutations([0,1,2,3])){
 const seedBindings=Object.fromEntries(['C0','M0','C1','M1'].map((k,i)=>[k,seed.vertices[marking[i]].join(',')])),r=new GenerativeAssemblyRules({seedBindings}),p=r.root,n=r.operations[r.outgoing(p).find(i=>r.operations[i].kind==='PN')].target,e=r.operations[r.outgoing(n).find(i=>r.operations[i].kind==='NE')].target;
 const h1=audit(r,[p,e],p),h2=audit(r,[p,n,e],p);assert.equal(h1.baseline.passesHypotheticalChecks,false);assert.ok(Object.values(h1.variants).every(v=>v.passesHypotheticalChecks));assert.equal(h2.baseline.passesHypotheticalChecks,true);assert.equal(h2.shortcuts.length,0);hydrogen.push({marking,h1,h2});
}
const deletions=[],sourceHashes={};for(const isotope of ['n15','ne22']){
 const base=`research/strominger/results/reference-${isotope}-search`,summary=JSON.parse(await readFile(base+'/verification.json')),row=summary.rows.find(r=>r.witnessFile),source=base+'/'+row.witnessFile,bytes=await readFile(source),w=JSON.parse(bytes).witness,{rules:r}=phaseUniverse({maxOrigin:row.maxOrigin,maxPackets:5000});sourceHashes[source]=createHash('sha256').update(bytes).digest('hex');
 const cell=p=>r.charts[r.packets[p].chart].cell;for(const body of w.bodies.filter(b=>b.species==='neutron')){const ids=w.selectedPackets.filter(p=>cell(p)!==body.cell);deletions.push({sourceIsotope:isotope,deletedNeutron:body,...audit(r,ids,r.root)});}
}
for(const f of ['research/strominger/checkers/probe_terminal_pe.mjs','research/nima/generative-phase-assembly.mjs','research/nima/origin-bounded-assemblies.mjs'])sourceHashes[f]=createHash('sha256').update(await readFile(f)).digest('hex');
const out='research/strominger/results/terminal-pe-probe';await mkdir(out,{recursive:true});const result={status:'counterfactual-terminality-probe-complete',sourceHashes,hydrogen,deletions,scope:'Selected saved readers only. Each shortcut composes validated PN and NE at equal origin across a C1/M1 edge; intermediate N body must be unoccupied, target E has no outgoing native operations. Original C/M/species/contact guards retained. Three terminality filters compared. Hypothetical graph checks, not native certificates, no arbitrary geometry or new-reader search, no production/viewer changes.'};await writeFile(out+'/verification.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({hydrogenMarkings:hydrogen.length,h1PassesAllVariants:true,h2Unchanged:true,deletions:deletions.map(d=>({isotope:d.sourceIsotope,removedCell:d.deletedNeutron.cell,baselineUnrooted:d.baseline.unrootedPackets.length,variants:Object.fromEntries(Object.entries(d.variants).map(([k,v])=>[k,{shortcuts:v.shortcuts,unrooted:v.unrootedPackets.length,noExit:v.noExitPackets.length,passes:v.passesHypotheticalChecks}]))}))},null,2));
