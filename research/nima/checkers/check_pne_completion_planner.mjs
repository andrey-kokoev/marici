import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync,createReadStream,createWriteStream} from 'node:fs';
import {createHash} from 'node:crypto';
import {createGunzip,createGzip} from 'node:zlib';
import {createInterface} from 'node:readline';
import {pipeline} from 'node:stream/promises';
import {once} from 'node:events';
import {contractionUniverse,inspectContraction} from '../experimental-terminal-pe.mjs';
const contractPath='research/nima/contracts/pne-structural-synthesis-net.v4.json',contract=JSON.parse(readFileSync(contractPath)),test=contract.added_tests.find(t=>t.id==='certificate-directed-completion-D2');assert.ok(test&&!test.executed);
const sourcePath='research/nima/results/interface-driven-synthesis/verification.json',source=JSON.parse(readFileSync(sourcePath)),s=source.cases.find(c=>c.maxOrigin===2),graphPath=test.domain.sourceGraph;
const hash=p=>createHash('sha256').update(readFileSync(p)).digest('hex');assert.equal(hash(graphPath),s.graphSha256);
const N=s.configurations,M=s.edges-s.revisits,from=new Int32Array(M),to=new Int32Array(M),operation=new Int32Array(M),masks=Array(N),active=Array(N),cardinality=new Uint8Array(N),outdegree=new Int32Array(N),indegree=new Int32Array(N);let registry=null,e=0,states=0,allEdges=0,revisits=0,footer=null;
const pop=m=>{let n=0;for(;m;m&=m-1n)n++;return n;};
for await(const line of createInterface({input:createReadStream(graphPath).pipe(createGunzip()),crlfDelay:Infinity})){
 const r=JSON.parse(line);
 if(r.type==='registry')registry=r;
 if(r.type==='configuration'){assert.equal(r.id,states++);masks[r.id]=BigInt(r.mask);active[r.id]=BigInt(r.active);cardinality[r.id]=pop(masks[r.id]);}
 if(r.type==='edge'){allEdges++;const [a,b,o]=r.data;if(a===b){revisits++;continue;}assert.ok(b>a,'Source graph no longer cardinality-ordered');from[e]=a;to[e]=b;operation[e]=o;e++;outdegree[a]++;indegree[b]++;}
 if(r.type==='end')footer=r;
}
assert.equal(states,N);assert.equal(e,M);assert.equal(allEdges,s.edges);assert.equal(revisits,s.revisits);assert.ok(footer.complete);
const offsets=counts=>{const a=new Int32Array(counts.length+1);for(let i=0;i<counts.length;i++)a[i+1]=a[i]+counts[i];return a;},outStart=offsets(outdegree),inStart=offsets(indegree),outIndex=new Int32Array(M),inIndex=new Int32Array(M),outCursor=outStart.slice(),inCursor=inStart.slice();
for(let j=0;j<M;j++){outIndex[outCursor[from[j]]++]=j;inIndex[inCursor[to[j]]++]=j;assert.equal(cardinality[to[j]],cardinality[from[j]]+1);assert.equal(masks[from[j]]&masks[to[j]],masks[from[j]]);assert.ok(active[to[j]]&(1n<<BigInt(operation[j])));}
const u=contractionUniverse({maxOrigin:2}),g=u.rules,packets=registry.variablePackets,bits=packets.map((_,i)=>1n<<BigInt(i));assert.deepEqual(packets,u.packets);for(const p of packets)assert.deepEqual(registry.packets[p],g.packets[p]);
const ids=m=>packets.filter((_,i)=>!!(m&bits[i])),certified=new Uint8Array(N),targets=[];
for(let i=0;i<N;i++){const a=inspectContraction(u,ids(masks[i]));assert.ok(a.valid&&a.rooted);if(a.certifiedExit){certified[i]=1;targets.push(i);}}
assert.equal(targets.length,698);console.log('Direct certificates checked');
// Independent graph algorithms: reverse BFS and reverse topological DP.
const distance=new Int16Array(N).fill(-1),nextEdge=new Int32Array(N).fill(-1),queue=new Int32Array(N);let head=0,tail=0;
for(const i of targets){distance[i]=0;queue[tail++]=i;}
while(head<tail){const v=queue[head++];for(let k=inStart[v];k<inStart[v+1];k++){const j=inIndex[k],p=from[j];if(distance[p]>=0)continue;distance[p]=distance[v]+1;nextEdge[p]=j;queue[tail++]=p;}}
const dp=new Int16Array(N).fill(-1);for(let i=N-1;i>=0;i--){if(certified[i])dp[i]=0;else for(let k=outStart[i];k<outStart[i+1];k++){const j=outIndex[k],d=dp[to[j]];if(d>=0&&(dp[i]<0||d+1<dp[i]))dp[i]=d+1;}assert.equal(dp[i],distance[i]);}
let checkedEdges=revisits;for(let j=0;j<M;j++){const a=from[j],b=to[j];if(distance[b]>=0)assert.ok(distance[a]>=0&&distance[a]<=distance[b]+1);if(distance[a]<0)assert.equal(distance[b],-1);checkedEdges++;}
assert.equal(checkedEdges,s.edges);
// A separate certificate-superset index tests whether deadness reflects
// support/history exclusion or an ordering obstruction despite a final target.
const allTargets=(1n<<BigInt(targets.length))-1n,containing=packets.map(()=>0n);
for(let j=0;j<targets.length;j++)for(let p=0;p<packets.length;p++)if(masks[targets[j]]&bits[p])containing[p]|=1n<<BigInt(j);
function supersets(m){let candidates=allTargets;for(let p=0;p<packets.length;p++)if(m&bits[p]){candidates&=containing[p];if(!candidates)break;}return candidates;}
const cores=[];
for(let i=0;i<packets.length;i++)if(!containing[i])cores.push({mask:bits[i],slots:[i]});
for(let i=0;i<packets.length;i++)for(let j=i+1;j<packets.length;j++)if(containing[i]&&containing[j]&&!(containing[i]&containing[j]))cores.push({mask:bits[i]|bits[j],slots:[i,j]});
for(let i=0;i<packets.length;i++)for(let j=i+1;j<packets.length;j++)for(let k=j+1;k<packets.length;k++)if((containing[i]&containing[j])&&(containing[i]&containing[k])&&(containing[j]&containing[k])&&!(containing[i]&containing[j]&containing[k]))cores.push({mask:bits[i]|bits[j]|bits[k],slots:[i,j,k]});
for(const c of cores){assert.equal(supersets(c.mask),0n);for(const p of c.slots)assert.notEqual(supersets(c.mask&~bits[p]),0n);c.coveredDeadStates=0;c.exampleState=null;}
const histogram={},examples=[],noTargetStates=[],supersetButUnreachable=[];let coveredBySmallCore=0,maxDistance=0,minimumSupersetDistanceAgreements=0;
for(let i=0;i<N;i++){
 const d=distance[i];histogram[d]=(histogram[d]??0)+1;maxDistance=Math.max(maxDistance,d);const supers=supersets(masks[i]);
 if(!supers){assert.equal(d,-1);noTargetStates.push(i);}else if(d<0)supersetButUnreachable.push(i);
 if(d>=0){assert.ok(supers);let minimum=Infinity;for(let j=0;j<targets.length;j++)if(supers&(1n<<BigInt(j)))minimum=Math.min(minimum,cardinality[targets[j]]-cardinality[i]);assert.ok(d>=minimum);if(d===minimum)minimumSupersetDistanceAgreements++;}
 if(d<0){const c=cores.find(c=>(masks[i]&c.mask)===c.mask);if(c){coveredBySmallCore++;c.coveredDeadStates++;c.exampleState??=i;}}
 if(d>=0&&!examples.some(x=>x.distance===d)){
 const path=[i],word=[];let v=i;while(distance[v]>0){const j=nextEdge[v];assert.ok(j>=0);const o=registry.interfaces[operation[j]];assert.ok(ids(masks[v]).includes(o.source));v=to[j];assert.equal(distance[v],distance[path.at(-1)]-1);const a=inspectContraction(u,ids(masks[v]));assert.ok(a.valid&&a.rooted);if(o.kind==='experimental-terminal-PE')assert.ok(a.shortcuts.some(s=>s.source===o.source&&s.target===o.target));word.push({interface:operation[j],kind:o.kind,source:o.source,target:o.target});path.push(v);}assert.ok(certified[v]);examples.push({start:i,distance:d,target:v,path,word});
 }
}
const usefulCores=cores.filter(c=>c.exampleState!==null).map(c=>{const selected=ids(c.mask),a=g.describe(selected);return {packets:selected,size:selected.length,mask:c.mask.toString(),compatible:a.valid,reason:a.reason??null,assignedDeadStates:c.coveredDeadStates,exampleState:c.exampleState,properSubsetsHaveCertifiedSupersets:true};});
// This prioritized cover need not list every overlapping minimal core.
for(let i=0;i<N;i++)assert.equal(usefulCores.some(c=>(masks[i]&BigInt(c.mask))===BigInt(c.mask)),distance[i]<0);
const out='research/nima/results/pne-completion-planner';mkdirSync(out,{recursive:true});
const gzip=createGzip({level:6}),writing=pipeline(gzip,createWriteStream(out+'/completion-policy.jsonl.gz'));let buffer='';
for(let i=0;i<N;i++){const j=nextEdge[i];buffer+=JSON.stringify({state:i,distance:distance[i],nextState:j<0?null:to[j],interface:j<0?null:operation[j]})+'\n';if(buffer.length>131072){if(!gzip.write(buffer))await once(gzip,'drain');buffer='';}}
if(buffer)gzip.write(buffer);gzip.end();await writing;
let rows=0;for await(const line of createInterface({input:createReadStream(out+'/completion-policy.jsonl.gz').pipe(createGunzip()),crlfDelay:Infinity})){const r=JSON.parse(line);assert.equal(r.state,rows);assert.equal(r.distance,distance[rows++]);}assert.equal(rows,N);
const report={schema:'marici.nima.pne-completion-planner.v1',status:'pass-complete-D2-completion-policy',test:test.id,maxOrigin:2,mode:'experimental-terminal-PE',states:N,certified:targets.length,additivelyCompletable:tail-targets.length,noCertifiedContinuation:N-tail,maximumMinimumAdditions:maxDistance,distanceHistogram:histogram,allEdgeDistanceChecks:checkedEdges,reverseBfsEqualsTopologicalDp:true,noCertifiedSuperset:noTargetStates.length,certifiedSupersetButUnreachable:supersetButUnreachable.length,minimumSupersetDistanceAgreements,minimalObstructionCoresBySize:Object.fromEntries([1,2,3].map(k=>[k,cores.filter(c=>c.slots.length===k).length])),deadStatesCoveredBySizeAtMost3:coveredBySmallCore,remainingDeadStates:N-tail-coveredBySmallCore,selectedObstructionCover:usefulCores,representativeCompletionPaths:examples,policyRows:rows,sourceHashes:Object.fromEntries([contractPath,sourcePath,graphPath,'research/nima/checkers/check_pne_completion_planner.mjs','research/nima/experimental-terminal-pe.mjs'].map(p=>[p,hash(p)])),policySha256:hash(out+'/completion-policy.jsonl.gz')};
writeFileSync(out+'/verification.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({...report,sourceHashes:undefined,selectedObstructionCover:usefulCores.length,representativeCompletionPaths:examples.length},null,2));
