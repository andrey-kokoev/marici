import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync,createReadStream} from 'node:fs';
import {createHash} from 'node:crypto';
import {createGunzip} from 'node:zlib';
import {createInterface} from 'node:readline';
import {contractionUniverse,inspectContraction} from '../experimental-terminal-pe.mjs';
const active=(e,m)=>(m&(1<<e.s))&&(m&(1<<e.t))&&!(m&(e.forbid??0));
function rooted(m,edges){let r=1;for(let old=-1;old!==r;){old=r;for(const e of edges)if(active(e,m)&&(r&(1<<e.s)))r|=1<<e.t;}return r===m;}
function closure(A,S,edges){const queue=[A],seen=new Set(queue);for(const m of queue)for(let p=0;p<4;p++){const n=m|(1<<p);if(n===m||(n&S)!==n||seen.has(n)||!rooted(n,edges))continue;seen.add(n);queue.push(n);}return [...seen];}
// Enumerate every three-packet negative-third-guard graph and rooted interval.
const slots=[];for(let s=0;s<3;s++)for(let t=0;t<3;t++)if(s!==t)slots.push({s,t});let intervals=0;
for(let code=0;code<729;code++){let k=code;const edges=[];for(const e of slots){const d=k%3;k=Math.floor(k/3);if(d)edges.push({...e,forbid:d===2?7^((1<<e.s)|(1<<e.t)):0});}for(const S of [1,3,5,7])if(rooted(S,edges))for(const A of [1,3,5,7])if((A&S)===A&&rooted(A,edges)){intervals++;assert.ok(closure(A,S,edges).includes(S));}}
const edges=[{s:0,t:1,forbid:4},{s:0,t:2},{s:2,t:3},{s:3,t:1}],A=3,S=15,reachable=closure(A,S,edges);assert.ok(rooted(A,edges)&&rooted(S,edges));assert.deepEqual(reachable,[A]);assert.ok(closure(1,S,edges).includes(S));
const blockedSingles=[7,11].map(m=>({mask:m,rooted:rooted(m,edges)}));assert.ok(blockedSingles.every(x=>!x.rooted));
// A sufficient anchor test: A already rooted using only final-active edges.
const finalEdges=edges.filter(e=>active(e,S));assert.equal(rooted(A,finalEdges),false);
const graphPath='research/nima/results/proof-pruned-synthesis/D2-pruned-graph.jsonl.gz',masks=[],out=[],activeMasks=[];let registry,footer,edgeCount=0;
for await(const line of createInterface({input:createReadStream(graphPath).pipe(createGunzip()),crlfDelay:Infinity})){const r=JSON.parse(line);if(r.type==='registry')registry=r;if(r.type==='configuration'){assert.equal(r.id,masks.length);masks.push(BigInt(r.mask));activeMasks.push(BigInt(r.active));out.push([]);}if(r.type==='edge'){edgeCount++;const [a,b]=r.data;if(a!==b){assert.ok(b>a);out[a].push(b);}}if(r.type==='end')footer=r;}
assert.ok(footer.complete);assert.equal(masks.length,10682);assert.equal(edgeCount,224537);
const u=contractionUniverse({maxOrigin:2}),packets=registry.variablePackets;assert.deepEqual(packets,u.packets);const bits=packets.map((_,i)=>1n<<BigInt(i)),ids=m=>packets.filter((p,i)=>!!(m&bits[i])),targets=[];
for(let i=0;i<masks.length;i++){const a=inspectContraction(u,ids(masks[i]));assert.ok(a.valid&&a.rooted);if(a.certifiedExit)targets.push(i);}assert.equal(targets.length,698);
const reach=masks.map(()=>0n),containing=packets.map(()=>0n);for(let j=0;j<targets.length;j++){const b=1n<<BigInt(j);reach[targets[j]]|=b;for(let p=0;p<packets.length;p++)if(masks[targets[j]]&bits[p])containing[p]|=b;}
for(let i=masks.length-1;i>=0;i--)for(const j of out[i])reach[i]|=reach[j];
let pairs=0,missing=0,blockedStarts=0;const examples=[],all=(1n<<BigInt(targets.length))-1n;const pop=m=>{let n=0;for(;m;m&=m-1n)n++;return n;};
for(let i=0;i<masks.length;i++){let sup=all;for(let p=0;p<packets.length;p++)if(masks[i]&bits[p])sup&=containing[p];assert.equal(reach[i]&~sup,0n);pairs+=pop(sup);const lost=sup&~reach[i];missing+=pop(lost);if(lost)blockedStarts++;if(lost&&examples.length<10){const j=targets.findIndex((t,k)=>!!(lost&(1n<<BigInt(k))));examples.push({startState:i,targetState:targets[j],startPackets:ids(masks[i]),targetPackets:ids(masks[targets[j]])});}}
// Independently verify the first source interval, including every possible singleton first step.
assert.ok(examples.length);const example=examples[0],difference=example.targetPackets.filter(p=>!example.startPackets.includes(p));assert.equal(difference.length,2);
const startAudit=inspectContraction(u,example.startPackets),targetAudit=inspectContraction(u,example.targetPackets);assert.ok(startAudit.certifiedExit&&targetAudit.certifiedExit);
const singletons=difference.map(p=>{const a=inspectContraction(u,[...example.startPackets,p]);assert.ok(a.valid&&!a.rooted);return {added:p,unrooted:a.unrooted,shortcuts:a.shortcuts.map(o=>o.id)};});
const body=p=>u.rules.charts[u.rules.packets[p].chart].cell;assert.equal(body(difference[0]),body(difference[1]));
const sourceCounterexample={...example,difference,sharedNeutronBody:body(difference[0]),startCertified:true,targetCertified:true,singletons,removedShortcuts:startAudit.shortcuts.filter(o=>!targetAudit.shortcuts.some(t=>t.id===o.id)),targetConstruction:targetAudit.construction,minimumBatchSize:2};
const hash=p=>createHash('sha256').update(readFileSync(p)).digest('hex'),paths=['research/nima/contracts/pne-structural-synthesis-net.v10.json','research/nima/checkers/check_extension_scheduling.mjs','research/nima/extension-scheduling-v1.md',graphPath,'research/nima/results/proof-pruned-synthesis/verification.json','research/nima/results/pne-completion-planner/verification.json','research/nima/experimental-terminal-pe.mjs'];
const pruning=JSON.parse(readFileSync('research/nima/results/proof-pruned-synthesis/verification.json'));assert.equal(hash(graphPath),pruning.graphSha256);assert.ok(pruning.exactLiveSetAgreement&&pruning.exactInducedLabelledGraphAgreement);assert.equal(hash('research/nima/experimental-terminal-pe.mjs'),pruning.admission.sourceHashes['research/nima/experimental-terminal-pe.mjs']);
const report={schema:'marici.nima.extension-scheduling.v1',status:'complete',generic:{threePacketGraphs:729,threePacketRootedIntervals:intervals,counterexample:{vertices:['root','a','b','c'],edges,start:A,target:S,reachable,blockedSingles,minimumBatchSize:2,stableAnchor:false},conclusion:'Four packets suffice and are minimal for failure; two-packet atomic addition repairs the generic example.'},source:{maxOrigin:2,mode:u.mode,states:masks.length,certificates:targets.length,edges:edgeCount,certifiedSupersetPairs:pairs,unreachablePairs:missing,blockedStarts,examples,sourceCounterexample,method:'Reverse DAG bitsets of individually reachable target certificates compared with independent selected-subset bitsets; graph includes every D2 live state by pinned earlier proof-pruned verification.',scope:'All D2 live-state/certified-superset pairs, not all rooted target supersets or higher origins.'},sourceHashes:Object.fromEntries(paths.map(p=>[p,hash(p)]))};mkdirSync('research/nima/results/extension-scheduling',{recursive:true});writeFileSync('research/nima/results/extension-scheduling/verification.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
