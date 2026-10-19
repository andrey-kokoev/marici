// Exact fixed-selection obstruction classifier; prediction never reads old pass labels.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {phaseUniverse} from '../demos/particle-overlap-tetrahedron/local-reference-universe.mjs';
import {POLICY,auditReferencePEAssembly} from './experimental_reference_pe.mjs';
const ROOT=new URL('../../../',import.meta.url),OUT=new URL('../results/isotope-obstruction-atlas/',import.meta.url);
const hash=b=>createHash('sha256').update(b).digest('hex'),sourceHashes={};
const sorted=s=>[...s].sort((a,b)=>a-b);
async function load(path){const b=await readFile(new URL(path,ROOT));sourceHashes[path]=hash(b);return JSON.parse(b);}
function close(seeds,edges,reverse=false){
 const seen=new Set(seeds),queue=[...seen],adj=new Map();
 for(const o of edges){const a=reverse?o.target:o.source,b=reverse?o.source:o.target;if(!adj.has(a))adj.set(a,[]);adj.get(a).push(b);}
 for(let i=0;i<queue.length;i++)for(const b of adj.get(queue[i])??[])if(!seen.has(b)){seen.add(b);queue.push(b);}
 return seen;
}
function predict(r,ids){
 const selected=new Set(ids),chart=p=>r.charts[r.packets[p].chart],cell=p=>chart(p).cell;
 const d=r.describe(ids);assert(d.valid&&selected.has(r.root));
 const occupied=new Set(ids.map(cell));
 const native=ids.flatMap(p=>r.outgoing(p).map(i=>r.operations[i])).filter(o=>selected.has(o.target));
 const exits=ids.filter(p=>chart(p).species==='electron');assert(exits.every(p=>r.outgoing(p).length===0));
 const rooted=close([r.root],native),canExit=close(exits,native,true);
 const shortcuts=[],rejections=[];
 for(const p of ids){
  if(chart(p).species!=='proton')continue;
  for(const pi of r.outgoing(p)){
   const pn=r.operations[pi];if(pn.kind!=='PN')continue;
   const n=pn.target;
   for(const ni of r.outgoing(n)){
    const ne=r.operations[ni];if(ne.kind!=='NE'||!selected.has(ne.target))continue;
    const e=ne.target,fail=[];
    if(occupied.has(cell(n)))fail.push('reference-body-occupied');
    if(native.some(o=>o.source===p))fail.push('source-reader-nonterminal');
    if(pn.phaseDelta!==0||ne.phaseDelta!==0||r.packets[p].origin!==r.packets[n].origin||r.packets[n].origin!==r.packets[e].origin)fail.push('grade-mismatch');
    if(new Set([cell(p),cell(n),cell(e)]).size!==3)fail.push('body-alias');
    const shared=r.geometry.cells[cell(p)].vertices.filter(v=>r.geometry.cells[cell(e)].vertices.includes(v)).sort();
    if(JSON.stringify(shared)!==JSON.stringify([chart(p).aliases.C1,chart(p).aliases.M1].sort()))fail.push('wrong-marked-edge');
    const permutation=ne.permutation.map(i=>pn.permutation[i]);
    if(JSON.stringify(permutation.map(i=>r.packets[p].permutation[i]))!==JSON.stringify(r.packets[e].permutation))fail.push('coefficient-mismatch');
    if(fail.length){rejections.push({source:p,target:e,referenceBody:cell(n),fail});continue;}
    r.validateTransfer(pn);r.validateTransfer(ne);
    shortcuts.push({source:p,target:e,referenceBody:cell(n),factors:[pi,ni],permutation});
   }
  }
 }
 // Closed formulas: PE ends at a native sink, so no alternating closure is needed.
 const predictedRooted=new Set([...rooted,...shortcuts.filter(o=>rooted.has(o.source)).map(o=>o.target)]);
 const extraExitAncestors=close(shortcuts.map(o=>o.source),native,true);
 const predictedCanExit=new Set([...canExit,...extraExitAncestors]);
 const inspection=r.inspect(ids);
 const nuclearCut=ids.filter(p=>chart(p).species!=='electron'&&!rooted.has(p));
 const unreachableElectrons=exits.filter(p=>!predictedRooted.has(p));
 const noExit=ids.filter(p=>!predictedCanExit.has(p));
 const flags={nuclearRootCut:nuclearCut.length>0,unservedElectron:unreachableElectrons.length>0,
              exitAncestryFailure:noExit.length>0,missingNativeFace:!inspection.allContactsWitnessed};
 const predictedPass=!Object.values(flags).some(Boolean);
 const oldPass=inspection.allContactsWitnessed&&rooted.size===ids.length&&canExit.size===ids.length;
 const category=oldPass?'already-native':predictedPass?'terminal-boundary-repair':flags.nuclearRootCut?'nuclear-root-cut':flags.missingNativeFace?'native-face-obligation':flags.unservedElectron?'unserved-terminal':'exit-ancestry';
 const contactCounts=Object.fromEntries(['PN','NE','NN'].map(kind=>[kind,d.contacts.filter(c=>c.kind===kind).length]));
 const aggregate={contactCounts,freeProtonMCMPorts:2*inspection.counts.proton-contactCounts.PN,
                  eligiblePESchemas:shortcuts.length,nativeEdges:native.length,selectedReaders:ids.length};
 return {counts:inspection.counts,aggregate,flags,category,predictedPass,nativePass:oldPass,
         deficits:{nuclearRootReaders:nuclearCut,unservedElectrons:unreachableElectrons,noExitReaders:noExit,pendingContacts:inspection.pendingContacts},
         shortcuts,rejections,nativeRooted:sorted(rooted),predictedRooted:sorted(predictedRooted),predictedCanExit:sorted(predictedCanExit)};
}
async function saved(isotope){
 const base=`research/strominger/results/reference-${isotope}-search/`,summary=await load(base+'verification.json');
 const row=summary.rows.find(x=>x.witnessFile);assert(row);
 const w=(await load(base+row.witnessFile)).witness,u=phaseUniverse({maxOrigin:row.maxOrigin});assert(u.complete);
 for(const p of w.packets)assert.deepEqual(u.rules.packets[p.id],p);
 for(const op of w.operations)assert.deepEqual(u.rules.operations[op.id],op);
 return {r:u.rules,w,maxOrigin:row.maxOrigin};
}
function test(r,ids,label){
 const signature=predict(r,ids);
 const actual=auditReferencePEAssembly(r,ids,{policy:POLICY,expectedCounts:signature.counts});
 assert.equal(signature.predictedPass,actual.experimentalPass,label);
 assert.equal(signature.nativePass,actual.nativePass,label);
 assert.deepEqual(signature.predictedRooted,sorted(ids.filter(p=>!actual.extended.unrooted.includes(p))),label);
 assert.deepEqual(signature.predictedCanExit,sorted(ids.filter(p=>!actual.extended.noExit.includes(p))),label);
 const keys=xs=>xs.map(o=>`${o.source}:${o.target}:${o.referenceBody??o.referenceNeutronCell}`).sort();
 assert.deepEqual(keys(signature.shortcuts),keys(actual.witnesses),label);
 return {label,selectedPackets:sorted(ids),...signature,fullAuditPass:actual.experimentalPass,prefixReplayCompared:true,
         verifiedConstruction:actual.experimentalPass?actual.extended.construction:null};
}
function summarize(rows){
 const categories={},flags={};for(const r of rows){categories[r.category]=(categories[r.category]??0)+1;for(const [f,v] of Object.entries(r.flags))if(v)flags[f]=(flags[f]??0)+1;}
 return {cases:rows.length,passes:rows.filter(r=>r.predictedPass).length,nativePasses:rows.filter(r=>r.nativePass).length,categories,nonexclusiveFailures:flags};
}
async function main(){
 const protocol=await load('research/strominger/inputs/isotope-obstruction-protocol-v1.json');
 const families={};
 for(const isotope of ['n15','ne22']){
  const {r,w}=await saved(isotope),neutrons=w.bodies.filter(b=>b.species==='neutron');
  const cell=p=>r.charts[r.packets[p].chart].cell;
  families[isotope+'-single']=neutrons.map(b=>test(r,w.selectedPackets.filter(p=>cell(p)!==b.cell),`${isotope}:delete:${b.cell}`));
  if(isotope==='ne22'){
   const rows=[];
   for(let i=0;i<neutrons.length;i++)for(let j=i+1;j<neutrons.length;j++){
    const removed=[neutrons[i].cell,neutrons[j].cell];
    rows.push(test(r,w.selectedPackets.filter(p=>!removed.includes(cell(p))),`ne22:delete-pair:${removed.join(',')}`));
   }
   families['ne22-double']=rows;assert.equal(rows.length,66);
  }
 }
 const knownNe20=await saved('ne20');families['independent-ne20']=[test(knownNe20.r,knownNe20.w.selectedPackets,'independent-ne20-origin5')];
 // Same isotope counts, different structural fates: count-only sufficiency fails.
 for(const name of ['n15-single','ne22-single']){
  const rows=families[name];assert(rows.some(r=>r.predictedPass)&&rows.some(r=>!r.predictedPass));
  assert(rows.every(r=>JSON.stringify(r.counts)===JSON.stringify(rows[0].counts)));
 }
 const summaries=Object.fromEntries(Object.entries(families).map(([k,v])=>[k,summarize(v)]));
 const collisions=[];
 for(const [family,rows] of Object.entries(families)){
  const buckets=new Map();
  for(const row of rows){
   const key=JSON.stringify([row.counts,row.aggregate.freeProtonMCMPorts]);
   if(!buckets.has(key))buckets.set(key,[]);buckets.get(key).push(row);
  }
  for(const [key,bucket] of buckets)if(bucket.some(r=>r.predictedPass)&&bucket.some(r=>!r.predictedPass)){
   const good=bucket.find(r=>r.predictedPass),bad=bucket.find(r=>!r.predictedPass);
   collisions.push({family,countsAndFreePorts:JSON.parse(key),passing:good.label,failing:bad.label,failingFlags:bad.flags});
  }
 }
 assert(collisions.length>0,'Need an actual counterexample to scalar port-budget sufficiency');
 for(const path of ['research/strominger/checkers/check_isotope_obstruction_atlas.mjs','research/strominger/checkers/experimental_reference_pe.mjs','research/strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs','research/strominger/demos/particle-overlap-tetrahedron/local-reference-universe.mjs'])sourceHashes[path]=hash(await readFile(new URL(path,ROOT)));
 await mkdir(OUT,{recursive:true});
 const report={schema:'marici.isotope-obstruction-atlas.v1',status:'pass',policy:POLICY,protocol,sourceHashes,summaries,portBudgetCollisions:collisions,families,
  scope:'Independent incidence-signature computation compared with existing full audit, sharing source geometry and native guards. Ne22 singles are retrospective validation; 66 double deletions are a new fixed-footprint family, not a new isotope discovery. No whole-domain absence, physical law or native adoption.'};
 await writeFile(new URL('verification.json',OUT),JSON.stringify(report,null,2)+'\n');
 console.log(JSON.stringify({status:'pass',summaries,portBudgetCollisions:collisions,newPositiveDoubleDeletions:families['ne22-double'].filter(r=>r.predictedPass).map(r=>({label:r.label,aggregate:r.aggregate,shortcuts:r.shortcuts}))},null,2));
}
await main();
