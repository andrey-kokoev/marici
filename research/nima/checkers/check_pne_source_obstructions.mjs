import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {contractionUniverse,guardedFamily,inspectContraction} from '../experimental-terminal-pe.mjs';
import {deriveObstruction} from '../pne-source-obstructions.mjs';
const contractPath='research/nima/contracts/pne-structural-synthesis-net.v5.json',contract=JSON.parse(readFileSync(contractPath)),test=contract.added_tests.find(t=>t.id==='source-local-obstruction-derivation-D2');assert.ok(test&&!test.executed);
const corePath='research/nima/results/pne-completion-planner/verification.json',coreData=JSON.parse(readFileSync(corePath)),cores=coreData.selectedObstructionCover.map(c=>c.packets);
const u=contractionUniverse({maxOrigin:2}),u3=contractionUniverse({maxOrigin:3}),signature=(g,id)=>{const p=g.packets[id],c=g.charts[p.chart];return JSON.stringify([g.geometry.cells[c.cell].key,c.species,c.aliases,p.origin,p.permutation]);},lookup3=new Map(u3.packets.map(p=>[signature(u3.rules,p),p]));
// Freeze all source-local derivations before looking at a Boolean completion family.
const results=cores.map(core=>({core,sourceCertificate:deriveObstruction(u,core)}));
for(const r of results){const mapped=r.core.map(p=>lookup3.get(signature(u.rules,p)));assert.ok(mapped.every(p=>p!==undefined));r.origin3Core=mapped;r.origin3Relaxation=deriveObstruction(u3,mapped);}
// Residuals require simultaneous choices. Split on an optional packet, then
// prove both occupied and absent cases using the same source-only relaxation.
function splitProof(core,{maxNodes=10000}={}){
 let nodes=0;const g=u.rules;
 function branch(required,forbidden){if(++nodes>maxNodes)throw Error('obstruction-proof-node-limit');const local=deriveObstruction(u,required,{forbidden});if(local.status==='obstructed')return {kind:'contradiction',required,forbidden,certificate:local};
 const optional=local.survivors.filter(p=>!required.includes(p)&&p!==g.root&&!forbidden.includes(p));
 if(!optional.length){const a=inspectContraction(u,[...new Set([g.root,...required])]);assert.ok(a.certifiedExit);return {kind:'witness',selectedPackets:[...new Set([g.root,...required])]};}
 const score=p=>optional.filter(q=>q!==p&&!g.describe([p,q]).valid).length+u.shortcuts.filter(o=>o.source===p||o.target===p||o.referenceNeutronCell===g.charts[g.packets[p].chart].cell).length;
 optional.sort((a,b)=>score(b)-score(a)||a-b);const packet=optional[0];return {kind:'split',packet,present:branch([...required,packet],forbidden),absent:branch(required,[...forbidden,packet])};}
 try{const tree=branch(core,[]);return {status:'complete',nodes,tree};}catch(e){if(e.message!=='obstruction-proof-node-limit')throw e;return {status:'incomplete',nodes,reason:e.message};}
}
function verifyProof(tree,required,forbidden){
 if(tree.kind==='split'){assert.ok(!required.includes(tree.packet)&&!forbidden.includes(tree.packet)&&tree.packet!==u.rules.root);return verifyProof(tree.present,[...required,tree.packet],forbidden)+verifyProof(tree.absent,required,[...forbidden,tree.packet]);}
 assert.equal(tree.kind,'contradiction');assert.deepEqual(tree.required,required);assert.deepEqual(tree.forbidden,forbidden);assert.equal(deriveObstruction(u,required,{forbidden}).status,'obstructed');return 1;
}
for(const r of results)if(r.sourceCertificate.status!=='obstructed'){r.jointProof=splitProof(r.core);if(r.jointProof.status==='complete')r.jointProof.verifiedLeaves=verifyProof(r.jointProof.tree,r.core,[]);}
const f=guardedFamily(u),b=f.diagram,position=new Map(u.packets.map((p,i)=>[p,i]));
function exact(core){const formula=b.and(f.exitRoot,...core.map(p=>b.variable(position.get(p)))),count=b.count(formula);if(!count)return {count:'0'};
 const selection=b.models(formula,1)[0].map(i=>u.packets[i]),a=inspectContraction(u,selection);assert.ok(a.certifiedExit);const prefix=[u.rules.root];for(const step of a.construction){prefix.push(step.target);const check=inspectContraction(u,prefix);assert.ok(check.valid&&check.rooted);}assert.equal(prefix.length,selection.length);
 return {count:count.toString(),selectedPackets:selection,construction:a.construction};}
for(const r of results){r.exactCheck=exact(r.core);assert.equal(r.exactCheck.count,'0');r.properSubsetControls=r.core.map(p=>{const subset=r.core.filter(q=>q!==p),local=deriveObstruction(u,subset),result=exact(subset);assert.notEqual(result.count,'0');assert.equal(local.status,'relaxation-survives');return {subset,relaxation:local.status,...result};});}
// Distinguish a failed optimism test from an exact absence claim: any survivors
// remain a residual unless the exact guarded formula separately rules them out.
const unresolved=results.filter(r=>r.sourceCertificate.status!=='obstructed'&&r.jointProof?.status!=='complete');
const positiveTargets=[];
// All 698 certified selections are hostile controls against unsound elimination.
for(const vars of b.models(f.exitRoot,1000)){
 const selected=vars.map(i=>u.packets[i]),local=deriveObstruction(u,selected);assert.equal(local.status,'relaxation-survives');positiveTargets.push(selected);
}
assert.equal(positiveTargets.length,698);
const negativeControls=[];
const proofExample=results.find(r=>r.jointProof?.status==='complete');
const corrupt=structuredClone(proofExample.jointProof.tree);corrupt.packet=u.rules.root;assert.throws(()=>verifyProof(corrupt,proofExample.core,[]));negativeControls.push('split-on-mandatory-root');
const missingBranch=structuredClone(proofExample.jointProof.tree);delete missingBranch.absent;assert.throws(()=>verifyProof(missingBranch,proofExample.core,[]));negativeControls.push('missing-absent-branch');
const summary=results.map(r=>({core:r.core,status:r.sourceCertificate.status,jointProof:r.jointProof?{status:r.jointProof.status,nodes:r.jointProof.nodes,leaves:r.jointProof.verifiedLeaves,firstSplit:r.jointProof.tree?.packet}:null,rounds:r.sourceCertificate.rounds.length,impossible:r.sourceCertificate.impossible??[],D3:r.origin3Relaxation.status,D3rounds:r.origin3Relaxation.rounds.length,properSubsetCounts:r.properSubsetControls.map(c=>c.count)}));
const out='research/nima/results/pne-source-obstructions';mkdirSync(out,{recursive:true});
const report={schema:'marici.nima.pne-source-obstructions.v1',status:unresolved.length?'partial-source-local-derivation':'pass-all-nine-source-local-obstructions',test:test.id,summary,sourceDerived:results.length-unresolved.length,directRelaxationObstructions:results.filter(r=>r.sourceCertificate.status==='obstructed').length,splitProofObstructions:results.filter(r=>r.jointProof?.status==='complete').length,negativeControls,residualCores:unresolved.map(r=>r.core),properSubsetControls:results.reduce((n,r)=>n+r.properSubsetControls.length,0),certifiedPositiveControls:positiveTargets.length,results,scope:'Core seeds come from prior atlas; elimination uses source compatibility, guarded possible edges, optimistic reachability and mandatory face witnesses only. Exact family consulted afterward for checking. D3 relaxation survival is not a completion certificate.',sourceHashes:Object.fromEntries([contractPath,corePath,'research/nima/pne-source-obstructions.mjs','research/nima/checkers/check_pne_source_obstructions.mjs','research/nima/experimental-terminal-pe.mjs'].map(p=>[p,createHash('sha256').update(readFileSync(p)).digest('hex')]))};
writeFileSync(out+'/verification.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({...report,results:undefined,sourceHashes:undefined},null,2));
