import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {contractionUniverse,inspectContraction} from '../experimental-terminal-pe.mjs';
import {deriveObstruction} from '../pne-source-obstructions.mjs';
import {searchExtension} from '../guarded-extension-search.mjs';
const contractPath='research/nima/contracts/pne-structural-synthesis-net.v7.json',contract=JSON.parse(readFileSync(contractPath)),test=contract.added_tests.find(t=>t.id==='origin-lifted-obstruction-repair-D3');assert.ok(test&&!test.executed);
const proofPath='research/nima/results/pne-source-obstructions/verification.json',prior=JSON.parse(readFileSync(proofPath)),u2=contractionUniverse({maxOrigin:2}),u=contractionUniverse({maxOrigin:3}),g=u.rules;
const signature=(r,p)=>{const a=r.packets[p],c=r.charts[a.chart];return JSON.stringify([r.geometry.cells[c.cell].key,c.species,c.aliases,a.origin,a.permutation]);},bySignature=new Map(u.packets.map(p=>[signature(g,p),p]));
const out='research/nima/results/origin-lifted-repairs';mkdirSync(out,{recursive:true});
const report={schema:'marici.nima.origin-lifted-repairs.v1',test:test.id,mode:u.mode,maxOrigin:3,scope:'Retain each entire marked core, but choose other packets freely from the source universe; this is not a repair of every full D2 configuration containing that core.',cases:[],resourceLimits:{maxNodes:test.domain.maxSearchNodesPerCore,maxMilliseconds:test.domain.maxMillisecondsPerCore}};
function pathToExit(ids,source){const selected=new Set(ids),a=inspectContraction(u,ids),edges=u.operations.map(i=>g.operations[i]).filter(o=>selected.has(o.source)&&selected.has(o.target)).concat(a.shortcuts),q=[source],parent=new Map([[source,null]]);let target=null;
 for(let i=0;i<q.length;i++){const p=q[i];if(g.charts[g.packets[p].chart].species==='electron'){target=p;break;}for(const o of edges)if(o.source===p&&!parent.has(o.target)){parent.set(o.target,o);q.push(o.target);}}
 assert.notEqual(target,null);const path=[];while(target!==source){const o=parent.get(target);path.push({kind:o.kind,id:o.id,source:o.source,target:o.target,sourceOrigin:g.packets[o.source].origin,targetOrigin:g.packets[o.target].origin});target=o.source;}return path.reverse();}
for(const previous of prior.results){
 const core=previous.core.map(p=>bySignature.get(signature(u2.rules,p)));assert.ok(core.every(p=>p!==undefined));assert.equal(deriveObstruction(u,core).status,'relaxation-survives');
 const s=searchExtension(u,core,report.resourceLimits),row={sourceCore:previous.core,mappedCore:core,sourceSignatures:previous.core.map(p=>signature(u2.rules,p)),...s};
 if(s.status==='sat'){
  const initialCount=s.selectedPackets.length;let ids=[...s.selectedPackets].sort((a,b)=>a-b);const mandatory=new Set([g.root,...core]);
  // Remove optional records only when the direct complete-set certificate survives.
  for(let changed=true;changed;){changed=false;for(const p of ids){if(mandatory.has(p))continue;const candidate=ids.filter(q=>q!==p);if(inspectContraction(u,candidate).certifiedExit){ids=candidate;changed=true;break;}}}
  const a=inspectContraction(u,ids);assert.ok(a.certifiedExit);assert.ok(core.every(p=>ids.includes(p)));for(const p of ids)if(!mandatory.has(p))assert.equal(!!inspectContraction(u,ids.filter(q=>q!==p)).certifiedExit,false);
  const prefixes=[[g.root]];for(const o of a.construction){const p=[...prefixes.at(-1),o.target],audit=inspectContraction(u,p);assert.ok(audit.valid&&audit.rooted);prefixes.push(p);}assert.equal(prefixes.at(-1).length,ids.length);
  const grade=Math.max(...ids.map(p=>g.packets[p].origin));assert.equal(grade,3);
  const selected=new Set(ids),active=u.operations.map(i=>g.operations[i]).filter(o=>selected.has(o.source)&&selected.has(o.target)).concat(a.shortcuts);
  const origin3Interfaces=active.filter(o=>g.packets[o.source].origin===3||g.packets[o.target].origin===3);
  row.selectedPackets=ids;row.witness={grade,counts:a.counts,initialRecords:initialCount,records:ids.length,operationCount:a.construction.length,singleDeletionMinimal:true,construction:a.construction,shortcuts:a.shortcuts,origin3Interfaces,coreExitPaths:core.map(p=>({packet:p,path:pathToExit(ids,p)}))};
 }
 if(s.status==='unsat'){
  const check=(tree,required,forbidden)=>{if(tree.kind==='split'){assert.ok(!required.includes(tree.packet)&&!forbidden.includes(tree.packet));check(tree.present,[...required,tree.packet],forbidden);check(tree.absent,required,[...forbidden,tree.packet]);}else{assert.equal(tree.kind,'contradiction');assert.deepEqual(tree.required,required);assert.deepEqual(tree.forbidden,forbidden);assert.equal(deriveObstruction(u,required,{forbidden}).status,'obstructed');}};check(s.proof,[...new Set([g.root,...core])],[]);
  // Compress the search tree into forced-support implications when possible:
  // if forbidding an optional packet is already impossible, it is mandatory.
  const required=[...new Set([g.root,...core])],steps=[];let conclusion=null;
  for(let round=0;round<u.packets.length;round++){
   const local=deriveObstruction(u,required);if(local.status==='obstructed'){conclusion=local;break;}
   let forced=null;for(const p of local.survivors.filter(p=>!required.includes(p)).sort((a,b)=>a-b)){const without=deriveObstruction(u,required,{forbidden:[p]});if(without.status==='obstructed'){forced=p;steps.push({required:[...required],forcedPacket:p,absenceContradiction:without});break;}}
   if(forced===null)break;required.push(forced);
  }
  row.forcedSupportExplanation={steps,finalMandatory:required,conclusion};
 }
 report.cases.push(row);writeFileSync(out+'/verification.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({core:row.sourceCore,status:row.status,nodes:row.nodes,elapsedMilliseconds:row.elapsedMilliseconds,counts:row.witness?.counts,records:row.witness?.records,operations:row.witness?.operationCount,origin3Interfaces:row.witness?.origin3Interfaces.length}));
}
assert.equal(searchExtension(u,[u.rules.root],{maxNodes:0}).status,'incomplete');assert.equal(searchExtension(u,[u.rules.root],{maxMilliseconds:-1}).status,'incomplete');
report.status=report.cases.every(c=>c.status==='sat')?'pass-all-nine-D3-extensions':report.cases.some(c=>c.status==='incomplete')?'partial-resource-limited':'complete-mixed-outcomes';report.summary={sat:report.cases.filter(c=>c.status==='sat').length,unsat:report.cases.filter(c=>c.status==='unsat').length,incomplete:report.cases.filter(c=>c.status==='incomplete').length};report.negativeControls=['node-limit-is-incomplete','time-limit-is-incomplete'];
report.registry={packets:g.packets,charts:g.charts,cells:g.geometry.cells.map(({owner,...c})=>c),operations:g.operations,universePackets:u.packets};
report.sourceHashes=Object.fromEntries([contractPath,proofPath,'research/nima/guarded-extension-search.mjs','research/nima/pne-source-obstructions.mjs','research/nima/experimental-terminal-pe.mjs','research/nima/checkers/check_origin_lifted_repairs.mjs'].map(p=>[p,createHash('sha256').update(readFileSync(p)).digest('hex')]));
writeFileSync(out+'/verification.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({status:report.status,summary:report.summary}));
