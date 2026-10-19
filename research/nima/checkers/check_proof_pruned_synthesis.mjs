import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync,createReadStream,createWriteStream} from 'node:fs';
import {createHash} from 'node:crypto';
import {createGunzip,createGzip} from 'node:zlib';
import {createInterface} from 'node:readline';
import {pipeline} from 'node:stream/promises';
import {once} from 'node:events';
import {contractionUniverse,inspectContraction} from '../experimental-terminal-pe.mjs';
import {compileInterfaces} from '../interface-synthesis.mjs';
import {admitPruning,synthesizePruned} from '../proof-pruned-synthesis.mjs';
const contractPath='research/nima/contracts/pne-structural-synthesis-net.v6.json',contract=JSON.parse(readFileSync(contractPath)),test=contract.added_tests.find(t=>t.id==='proof-carrying-pruned-synthesis-D2');assert.ok(test&&!test.executed);
const hash=p=>createHash('sha256').update(readFileSync(p)).digest('hex'),proofPath=test.domain.proofSource,proof=JSON.parse(readFileSync(proofPath)),catalogPath='research/nima/results/pne-interface-catalog/verification.json',catalog=JSON.parse(readFileSync(catalogPath));
const u=contractionUniverse({maxOrigin:2}),c=compileInterfaces(u,catalog.cases.find(r=>r.summary.maxOrigin===2));
const args={maxOrigin:2,mode:'experimental-terminal-PE',proofSha256:hash(proofPath),sourceHashes:proof.sourceHashes,actualSourceHashes:Object.fromEntries(Object.keys(proof.sourceHashes).map(p=>[p,hash(p)]))};
const admission=admitPruning(u,proof,args),started=performance.now(),r=synthesizePruned(u,c,admission,{maxConfigurations:test.domain.maxConfigurations}),generationMilliseconds=performance.now()-started;assert.ok(r.complete);
console.log(JSON.stringify({stage:'generated-before-policy-read',states:r.nodes.length,prunedCandidates:r.prunedCandidates}));
// Completed target memberships and full graph are first read AFTER generation.
const policyPath='research/nima/results/pne-completion-planner/completion-policy.jsonl.gz',plannerPath='research/nima/results/pne-completion-planner/verification.json',planner=JSON.parse(readFileSync(plannerPath)),sourcePath='research/nima/results/interface-driven-synthesis/verification.json',source=JSON.parse(readFileSync(sourcePath)),baseline=source.cases.find(s=>s.maxOrigin===2),graphPath='research/nima/results/interface-driven-synthesis/D2-graph.jsonl.gz';
assert.equal(hash(graphPath),baseline.graphSha256);assert.equal(hash(policyPath),planner.policySha256);
const alive=new Uint8Array(planner.states),distance=new Int16Array(planner.states),originalToPruned=new Int32Array(planner.states).fill(-1);let policyRows=0;
for await(const line of createInterface({input:createReadStream(policyPath).pipe(createGunzip()),crlfDelay:Infinity})){const p=JSON.parse(line);assert.equal(p.state,policyRows++);distance[p.state]=p.distance;alive[p.state]=+(p.distance>=0);}assert.equal(policyRows,planner.states);
const edges=[],edgeKeys=new Set();let exits=0,revisits=0,peEdges=0,disableEdges=0;
for(let i=0;i<r.nodes.length;i++){
 const n=r.nodes[i],ids=c.decode(n.mask),a=inspectContraction(u,ids);assert.ok(a.valid&&a.rooted);exits+=+a.certifiedExit;
 if(n.parent>=0){const p=r.nodes[n.parent];assert.equal(p.mask|c.bit[c.index.get(n.added)],n.mask);assert.equal(c.update(p.active,n.mask,c.index.get(n.added)),n.active);assert.ok(c.interfaces.some(o=>o.target===n.added&&(p.mask&o.sourceBit)&&(n.active&o.bit)));}
 for(const o of c.interfaces){if(!(n.mask&o.sourceBit))continue;const to=r.byMask.get(n.mask|o.targetBit);if(to===undefined||!(r.nodes[to].active&o.bit))continue;const key=[i,to,o.index].join(':');assert.ok(!edgeKeys.has(key));edgeKeys.add(key);edges.push([i,to,o.index]);revisits+=+(i===to);peEdges+=+(o.kind==='experimental-terminal-PE');disableEdges+=+c.interfaces.some(q=>q.kind==='experimental-terminal-PE'&&(n.active&q.bit)&&!(r.nodes[to].active&q.bit));}
}
let graphStates=0,inducedEdges=0,originalEdges=0,footer=null,originalRegistry=null;
for await(const line of createInterface({input:createReadStream(graphPath).pipe(createGunzip()),crlfDelay:Infinity})){
 const row=JSON.parse(line);
 if(row.type==='registry'){originalRegistry=row;assert.deepEqual(row.variablePackets,c.packets);assert.equal(row.interfaces.length,c.interfaces.length);for(let j=0;j<c.interfaces.length;j++){const a=c.interfaces[j],b=row.interfaces[j];for(const field of ['kind','source','target','operation'])assert.equal(a[field],b[field]);}}
 if(row.type==='configuration'){graphStates++;const p=r.byMask.get(BigInt(row.mask));assert.equal(p!==undefined,!!alive[row.id]);if(p!==undefined){if(originalToPruned[row.id]>=0)assert.equal(originalToPruned[row.id],p);originalToPruned[row.id]=p;assert.equal(r.nodes[p].active,BigInt(row.active));}}
 if(row.type==='edge'){originalEdges++;const [a,b,o]=row.data;if(alive[a]&&alive[b]){const pa=originalToPruned[a];assert.ok(pa>=0);const pb=r.byMask.get(r.nodes[pa].mask|c.interfaces[o].targetBit);assert.notEqual(pb,undefined);if(originalToPruned[b]>=0)assert.equal(originalToPruned[b],pb);else originalToPruned[b]=pb;assert.ok(edgeKeys.delete([pa,pb,o].join(':')));inducedEdges++;}}
 if(row.type==='end')footer=row;
}
assert.equal(graphStates,planner.states);assert.equal(originalEdges,baseline.edges);assert.ok(footer.complete);assert.equal(edgeKeys.size,0);assert.equal(inducedEdges,edges.length);assert.equal(r.nodes.length,planner.certified+planner.additivelyCompletable);assert.equal(exits,planner.certified);
// Complete family is retained, but enumeration completeness is intentionally
// relative to the certified pruning contract, not all compatible states.
const negativeControls=[];
assert.throws(()=>admitPruning(u,proof,{...args,maxOrigin:3}),/budget/);negativeControls.push('wrong-origin-budget');
assert.throws(()=>admitPruning(u,proof,{...args,mode:'native'}),/mode/);negativeControls.push('wrong-mode');
assert.throws(()=>admitPruning(u,proof,{...args,actualSourceHashes:{...args.actualSourceHashes,[Object.keys(args.actualSourceHashes)[0]]:'changed'}}),/hash/);negativeControls.push('changed-source-hash');
assert.throws(()=>synthesizePruned(u,c,{...admission,universeFingerprint:'changed'}),/universe/);negativeControls.push('changed-universe');
const broken=structuredClone(proof),joint=broken.results.find(x=>x.jointProof);delete joint.jointProof.tree.absent;assert.throws(()=>admitPruning(u,broken,args));negativeControls.push('incomplete-split-proof');
assert.equal(synthesizePruned(u,c,admission,{maxConfigurations:1}).complete,false);negativeControls.push('configuration-resource-stop');
const out='research/nima/results/proof-pruned-synthesis';mkdirSync(out,{recursive:true});
const gzip=createGzip({level:6}),writing=pipeline(gzip,createWriteStream(out+'/D2-pruned-graph.jsonl.gz'));let buffer='';const put=async row=>{buffer+=JSON.stringify(row)+'\n';if(buffer.length>131072){if(!gzip.write(buffer))await once(gzip,'drain');buffer='';}};
await put({type:'header',maxOrigin:2,mode:u.mode,pruning:admission,completeWithinPrunedContract:true});await put(originalRegistry);
for(let i=0;i<r.nodes.length;i++){const n=r.nodes[i];await put({type:'configuration',id:i,mask:n.mask.toString(),active:n.active.toString(),parent:n.parent,added:n.added});}for(const e of edges)await put({type:'edge',data:e});await put({type:'end',complete:true,configurations:r.nodes.length,edges:edges.length});if(buffer)gzip.write(buffer);gzip.end();await writing;
let decodedStates=0,decodedEdges=0,complete=false;for await(const line of createInterface({input:createReadStream(out+'/D2-pruned-graph.jsonl.gz').pipe(createGunzip()),crlfDelay:Infinity})){const x=JSON.parse(line);decodedStates+=+(x.type==='configuration');decodedEdges+=+(x.type==='edge');if(x.type==='end')complete=x.complete;}assert.ok(complete);assert.equal(decodedStates,r.nodes.length);assert.equal(decodedEdges,edges.length);
const report={schema:'marici.nima.proof-pruned-synthesis.v1',status:'pass-complete-proof-pruned-D2-live-family',test:test.id,maxOrigin:2,mode:u.mode,admission,states:r.nodes.length,exitCertificates:exits,edges:edges.length,revisits,peEdges,shortcutReplacementEdges:disableEdges,baselineStates:baseline.configurations,statesAvoided:baseline.configurations-r.nodes.length,retainedFraction:r.nodes.length/baseline.configurations,prunedCandidates:r.prunedCandidates,prunedByCore:r.prunedByCore,lostRootCandidates:r.lostRootCandidates,generationMilliseconds,exactLiveSetAgreement:true,exactInducedLabelledGraphAgreement:true,policyReadAfterGeneration:true,negativeControls,archiveFooterChecked:true,sourceHashes:Object.fromEntries([contractPath,proofPath,catalogPath,policyPath,plannerPath,sourcePath,graphPath,'research/nima/proof-pruned-synthesis.mjs','research/nima/interface-synthesis.mjs','research/nima/checkers/check_proof_pruned_synthesis.mjs'].map(p=>[p,hash(p)])),graphSha256:hash(out+'/D2-pruned-graph.jsonl.gz')};
writeFileSync(out+'/verification.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({...report,admission:undefined,sourceHashes:undefined},null,2));
