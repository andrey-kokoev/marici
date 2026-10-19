import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync,createReadStream} from 'node:fs';
import {createHash} from 'node:crypto';
import {createGunzip} from 'node:zlib';
import {createInterface} from 'node:readline';
import {contractionUniverse,inspectContraction} from '../experimental-terminal-pe.mjs';
import {admitPruning} from '../proof-pruned-synthesis.mjs';
import {deriveObstruction} from '../pne-source-obstructions.mjs';
import {searchExtension} from '../guarded-extension-search.mjs';
const contractPath='research/nima/contracts/pne-structural-synthesis-net.v12.json',contract=JSON.parse(readFileSync(contractPath)),test=contract.added_tests.find(t=>t.id==='materialization-face-witness-closure-D2');assert.ok(test&&!test.executed);
const priorPath='research/nima/results/body-coherent-materialization/verification.json',prior=JSON.parse(readFileSync(priorPath)),proofPath='research/nima/results/pne-source-obstructions/verification.json',proof=JSON.parse(readFileSync(proofPath)),hash=p=>createHash('sha256').update(readFileSync(p)).digest('hex');
assert.equal(prior.failures.length,70);const u=contractionUniverse({maxOrigin:2}),g=u.rules,admission=admitPruning(u,proof,{maxOrigin:2,mode:u.mode,proofSha256:hash(proofPath),sourceHashes:proof.sourceHashes,actualSourceHashes:Object.fromEntries(Object.keys(proof.sourceHashes).map(p=>[p,hash(p)]))});
const unique=new Map();prior.failures.forEach((f,i)=>{const selected=[...f.selected].sort((a,b)=>a-b),key=selected.join(',');if(!unique.has(key))unique.set(key,{selected,origins:[],missingContacts:f.missingContacts});unique.get(key).origins.push({failure:i,from:f.from,body:f.body,added:f.added});});
const cases=[];for(const c of unique.values()){
 const a=inspectContraction(u,c.selected);assert.ok(a.valid&&a.rooted&&!a.certifiedExit);assert.equal(a.noExit.length,0);assert.ok(a.missingContacts.length);
 const cores=admission.cores.filter(core=>core.every(p=>c.selected.includes(p)));
 if(cores.length){c.status='unsat';c.obstructionCores=cores;c.method='replayed-source-retained-subset-proof';}
 else{
  const result=searchExtension(u,c.selected,{maxNodes:test.domain.maxSearchNodesPerCase,maxMilliseconds:test.domain.maxMillisecondsPerCase});c.status=result.status;c.search=result;
  if(result.status==='sat'){
   let ids=result.selectedPackets;const mandatory=new Set(c.selected);for(let changed=true;changed;){changed=false;for(const p of ids)if(!mandatory.has(p)&&inspectContraction(u,ids.filter(q=>q!==p)).certifiedExit){ids=ids.filter(q=>q!==p);changed=true;break;}}
   const b=inspectContraction(u,ids);assert.ok(b.certifiedExit);assert.ok(c.selected.every(p=>ids.includes(p)));const added=ids.filter(p=>!mandatory.has(p));
   const cell=p=>g.charts[g.packets[p].chart].cell,selected=new Set(ids),native=u.operations.map(i=>g.operations[i]).filter(o=>selected.has(o.source)&&selected.has(o.target));
   const witnesses=a.missingContacts.map(contact=>({contact,operations:native.filter(o=>cell(o.source)!==cell(o.target)&&contact.cells.includes(cell(o.source))&&contact.cells.includes(cell(o.target)))}));assert.ok(witnesses.every(w=>w.operations.length));
   // Exact singleton scheduling inside this particular repaired selection.
   const queue=[c.selected],seen=new Set([c.selected.join(',')]);let schedule=null;
   const parent=new Map();for(const state of queue){const key=[...state].sort((a,b)=>a-b).join(',');if(state.length===ids.length){schedule=[];let k=key;while(parent.has(k)){const p=parent.get(k);schedule.push(p.added);k=p.before;}schedule.reverse();break;}for(const p of added)if(!state.includes(p)){const next=[...state,p].sort((a,b)=>a-b),nk=next.join(',');if(seen.has(nk))continue;const audit=inspectContraction(u,next);if(audit.valid&&audit.rooted){seen.add(nk);parent.set(nk,{before:key,added:p});queue.push(next);}}}
   c.witness={selected:ids,added,counts:b.counts,faceWitnesses:witnesses,singletonSchedule:schedule,atomicResultCertified:true};
  }
  if(result.status==='unsat'){const verify=(t,req,forbidden)=>{if(t.kind==='split'){assert.ok(!req.includes(t.packet)&&!forbidden.includes(t.packet));verify(t.present,[...req,t.packet],forbidden);verify(t.absent,req,[...forbidden,t.packet]);}else{assert.equal(t.kind,'contradiction');assert.equal(deriveObstruction(u,req,{forbidden}).status,'obstructed');}};verify(result.proof,[...new Set([g.root,...c.selected])],[]);}
 }
 cases.push(c);
}
// Compress successful source witnesses into two explicit bounded closure templates.
// Templates are tested before target membership is opened; they are not universal rules.
const templates={'0:2':[2,6,8],'2:5':[1,5,16,20,51,53],'1:5':[1,5,16,20,51,53]},contactHistogram={},templateAdditionHistogram={};
for(const c of cases){assert.equal(c.status,'sat');assert.equal(c.missingContacts.length,1);const contact=c.missingContacts[0];assert.equal(contact.kind,'PN');contactHistogram[contact.key]=(contactHistogram[contact.key]??0)+1;const template=templates[contact.key];assert.ok(template);const ids=[...c.selected],added=[];for(const p of template)if(!ids.includes(p)){ids.push(p);added.push(p);const a=inspectContraction(u,ids);assert.ok(a.valid&&a.rooted);}assert.ok(inspectContraction(u,ids).certifiedExit);c.compactClosure={template,added,selected:ids,singletonSchedule:added};templateAdditionHistogram[added.length]=(templateAdditionHistogram[added.length]??0)+1;}
// Target membership is opened only after all source classifications.
const graphPath='research/nima/results/proof-pruned-synthesis/D2-pruned-graph.jsonl.gz';assert.equal(hash(graphPath),prior.sourceHashes[graphPath]);let registry,footer;const targets=[];
for await(const line of createInterface({input:createReadStream(graphPath).pipe(createGunzip()),crlfDelay:Infinity})){const r=JSON.parse(line);if(r.type==='registry')registry=r;if(r.type==='configuration'){const m=BigInt(r.mask),ids=registry.variablePackets.filter((p,i)=>!!(m&(1n<<BigInt(i))));if(inspectContraction(u,ids).certifiedExit)targets.push(ids);}if(r.type==='end')footer=r;}
assert.ok(footer.complete);assert.equal(targets.length,698);
for(const c of cases){c.certifiedSupersetCount=targets.filter(ids=>c.selected.every(p=>ids.includes(p))).length;if(c.status==='sat')assert.ok(c.certifiedSupersetCount);if(c.status==='unsat')assert.equal(c.certifiedSupersetCount,0);}
const summary={inputFailures:70,distinctSelections:cases.length,sourceSat:cases.filter(c=>c.status==='sat').length,sourceUnsat:cases.filter(c=>c.status==='unsat').length,incomplete:cases.filter(c=>c.status==='incomplete').length,contactHistogram,templateAdditionHistogram,allCompactClosuresSingletonReplay:true,repairedOriginalCases:cases.filter(c=>c.status==='sat').reduce((n,c)=>n+c.origins.length,0),impossibleOriginalCases:cases.filter(c=>c.status==='unsat').reduce((n,c)=>n+c.origins.length,0)};
const paths=[contractPath,priorPath,proofPath,graphPath,'research/nima/checkers/check_materialization_face_closure.mjs','research/nima/materialization-face-closure-v1.md','research/nima/guarded-extension-search.mjs','research/nima/pne-source-obstructions.mjs','research/nima/proof-pruned-synthesis.mjs','research/nima/experimental-terminal-pe.mjs'];
const report={schema:'marici.nima.materialization-face-closure.v1',status:summary.incomplete?'partial':'complete',summary,sourceProofAdmission:admission,comparisonReadAfterSourceClassification:true,cases,sourceHashes:Object.fromEntries(paths.map(p=>[p,hash(p)]))};mkdirSync('research/nima/results/materialization-face-closure',{recursive:true});writeFileSync('research/nima/results/materialization-face-closure/verification.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(summary));for(const c of cases)console.log(JSON.stringify({from:c.origins.map(o=>o.from),status:c.status,cores:c.obstructionCores,added:c.witness?.added,schedule:c.witness?.singletonSchedule,supersets:c.certifiedSupersetCount}));
