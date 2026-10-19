import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync,createReadStream} from 'node:fs';
import {createHash} from 'node:crypto';
import {createGunzip} from 'node:zlib';
import {createInterface} from 'node:readline';
import {contractionUniverse,inspectContraction} from '../experimental-terminal-pe.mjs';
import {materializationCandidates} from '../body-coherent-materialization.mjs';
const graphPath='research/nima/results/proof-pruned-synthesis/D2-pruned-graph.jsonl.gz',priorPath='research/nima/results/extension-scheduling/verification.json',prior=JSON.parse(readFileSync(priorPath));
const hash=p=>createHash('sha256').update(readFileSync(p)).digest('hex');assert.equal(hash(graphPath),prior.sourceHashes[graphPath]);
const masks=[],out=[];let registry,footer,edgeCount=0;
for await(const line of createInterface({input:createReadStream(graphPath).pipe(createGunzip()),crlfDelay:Infinity})){const r=JSON.parse(line);if(r.type==='registry')registry=r;if(r.type==='configuration'){assert.equal(r.id,masks.length);masks.push(BigInt(r.mask));out.push([]);}if(r.type==='edge'){edgeCount++;const [a,b]=r.data;if(a!==b){assert.ok(b>a);out[a].push(b);}}if(r.type==='end')footer=r;}
assert.ok(footer.complete);assert.equal(masks.length,10682);assert.equal(edgeCount,224537);
const u=contractionUniverse({maxOrigin:2}),g=u.rules,packets=registry.variablePackets;assert.deepEqual(packets,u.packets);const bits=packets.map((_,i)=>1n<<BigInt(i)),bitByPacket=new Map(packets.map((p,i)=>[p,bits[i]])),ids=m=>packets.filter((p,i)=>!!(m&bits[i])),mask=ps=>ps.reduce((m,p)=>m|bitByPacket.get(p),0n),byMask=new Map(masks.map((m,i)=>[m,i])),targets=[];
const cell=p=>g.charts[g.packets[p].chart].cell;
// Source rule shape needed for the guard-preservation argument.
for(const shortcut of u.shortcuts)for(const i of u.operations){const o=g.operations[i];if(o.source===shortcut.source&&g.charts[g.packets[o.target].chart].species==='neutron')assert.equal(cell(o.target),shortcut.referenceNeutronCell);}
for(let i=0;i<masks.length;i++){const a=inspectContraction(u,ids(masks[i]));assert.ok(a.valid&&a.rooted);if(a.certifiedExit)targets.push(i);}assert.equal(targets.length,698);
const macros=[],failures=[],batchHistogram={};let candidates=0,compatible=0,faceFailures=0;
for(const from of targets){const selected=ids(masks[from]),before=inspectContraction(u,selected);
 for(const m of materializationCandidates(u,selected)){candidates++;batchHistogram[m.added.length]=(batchHistogram[m.added.length]??0)+1;
  if(!m.valid){failures.push({from,...m});continue;}compatible++;assert.ok(m.rooted);assert.equal(m.noExit.length,0);
  const after=inspectContraction(u,m.selected),remaining=new Set(after.shortcuts.map(o=>o.id));for(const old of before.shortcuts)assert.equal(remaining.has(old.id),old.referenceNeutronCell!==m.body);
  for(const sid of m.shortcuts){const shortcut=u.shortcuts[sid];for(const id of shortcut.nativeFactors){const o=g.operations[id];assert.ok(m.selected.includes(o.source)&&m.selected.includes(o.target));g.validateTransfer(o);}}
  if(!m.certified){faceFailures++;assert.ok(m.missingContacts.length);failures.push({from,...m});continue;}
  const to=byMask.get(mask(m.selected));assert.notEqual(to,undefined);assert.ok(to>from);macros.push({from,to,body:m.body,added:m.added,shortcuts:m.shortcuts});
 }
}
const augmented=out.map(a=>[...a]);for(const m of macros)augmented[m.from].push(m.to);
function targetReach(adjacency){const reach=masks.map(()=>0n);for(let j=0;j<targets.length;j++)reach[targets[j]]|=1n<<BigInt(j);for(let i=masks.length-1;i>=0;i--)for(const t of adjacency[i])reach[i]|=reach[t];return reach;}
const baseline=targetReach(out),expanded=targetReach(augmented),containing=packets.map(()=>0n),all=(1n<<BigInt(targets.length))-1n;for(let j=0;j<targets.length;j++)for(let p=0;p<packets.length;p++)if(masks[targets[j]]&bits[p])containing[p]|=1n<<BigInt(j);
const pop=m=>{let n=0;for(;m;m&=m-1n)n++;return n;};let pairs=0,blockedBefore=0,blockedAfter=0,repaired=0;const residual=[];
for(let i=0;i<masks.length;i++){let sup=all;for(let p=0;p<packets.length;p++)if(masks[i]&bits[p])sup&=containing[p];assert.equal(expanded[i]&~sup,0n);assert.equal(baseline[i]&~expanded[i],0n);pairs+=pop(sup);blockedBefore+=pop(sup&~baseline[i]);blockedAfter+=pop(sup&~expanded[i]);repaired+=pop(expanded[i]&~baseline[i]);if((sup&~expanded[i])&&residual.length<10){const j=targets.findIndex((t,k)=>!!((sup&~expanded[i])&(1n<<BigInt(k))));residual.push({start:i,target:targets[j],startPackets:ids(masks[i]),targetPackets:ids(masks[targets[j]])});}}
assert.equal(pairs,prior.source.certifiedSupersetPairs);assert.equal(blockedBefore,prior.source.unreachablePairs);
const example=prior.source.sourceCounterexample,repair=macros.find(m=>m.from===example.startState&&m.to===example.targetState);assert.ok(repair);assert.deepEqual([...repair.added].sort((a,b)=>a-b),[...example.difference].sort((a,b)=>a-b));
// Explicit guard regression: adding either reader alone loses an old electron.
for(const p of repair.added)assert.equal(inspectContraction(u,[...example.startPackets,p]).rooted,false);
const paths=['research/nima/contracts/pne-structural-synthesis-net.v11.json','research/nima/body-coherent-materialization.mjs','research/nima/checkers/check_body_coherent_materialization.mjs','research/nima/body-coherent-materialization-v1.md','research/nima/experimental-terminal-pe.mjs',graphPath,priorPath];
const report={schema:'marici.nima.body-coherent-materialization.v1',status:'complete',maxOrigin:2,startingCertificates:targets.length,candidates,compatible,compatibilityFailures:candidates-compatible,faceFailures,certifiedMacros:macros.length,batchHistogram,targetPairs:pairs,blockedBefore,blockedAfter,repaired,residual,exampleRepair:repair,macros,failures,scope:'Only macros from certified starts are added to the complete D2 live graph. Native rules unchanged. Root/exit preservation is separate from occupied-face obligations.',sourceHashes:Object.fromEntries(paths.map(p=>[p,hash(p)]))};mkdirSync('research/nima/results/body-coherent-materialization',{recursive:true});writeFileSync('research/nima/results/body-coherent-materialization/verification.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({...report,macros:macros.length,failures:failures.length}));
