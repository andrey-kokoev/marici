import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {contractionUniverse,inspectContraction} from '../experimental-terminal-pe.mjs';
const root=1,has=(m,i)=>!!(m&(1<<i));
function active(e,m){return has(m,e.s)&&has(m,e.t)&&!(m&(e.forbid??0))&&((m&(e.extra??0))===(e.extra??0));}
function rooted(m,edges){let seen=root;for(let prev=-1;prev!==seen;){prev=seen;for(const e of edges)if(active(e,m)&&has(seen,e.s))seen|=1<<e.t;}return seen===m;}
function generate(n,edges,compatible,start=root){const seen=new Set([start]),queue=[start];for(const m of queue)for(let p=0;p<n;p++){const next=m|(1<<p);if(next===m||seen.has(next)||!compatible(next))continue;if(!edges.some(e=>has(m,e.s)&&e.t===p&&active(e,next))||!rooted(next,edges))continue;seen.add(next);queue.push(next);}return seen;}
function treePrefixes(m,edges){let prefix=root;const trace=[prefix];while(prefix!==m){const e=edges.find(e=>active(e,m)&&has(prefix,e.s)&&!has(prefix,e.t));assert.ok(e);prefix|=1<<e.t;assert.ok(rooted(prefix,edges));trace.push(prefix);}return trace;}
const pairs=[[0,1],[0,2],[1,2]],slots=[];for(let s=0;s<3;s++)for(let t=0;t<3;t++)if(s!==t)slots.push({s,t});
let models=0,selections=0,rootedSelections=0,prefixes=0;
for(let encoding=0;encoding<3**slots.length;encoding++){
 let code=encoding;const edges=[];for(const slot of slots){const choice=code%3;code=Math.floor(code/3);if(choice)edges.push({...slot,forbid:choice===2?7^((1<<slot.s)|(1<<slot.t)):0});}
 for(let conflicts=0;conflicts<8;conflicts++){
  const compatible=m=>!pairs.some(([a,b],i)=>has(conflicts,i)&&has(m,a)&&has(m,b)),generated=generate(3,edges,compatible);models++;
  for(const m of [1,3,5,7]){selections++;const accepted=compatible(m)&&rooted(m,edges);assert.equal(generated.has(m),accepted);if(accepted){rootedSelections++;const trace=treePrefixes(m,edges);assert.ok(trace.every(compatible));prefixes+=trace.length;}}
 }
}
// Positive third-party support invalidates endpoint heredity.
const positive=[{s:0,t:1,extra:4},{s:0,t:2,extra:2}];assert.ok(rooted(7,positive));assert.deepEqual([...generate(3,positive,()=>true)],[1]);
// Compatibility heredity is also essential.
const ordinary=[{s:0,t:1},{s:1,t:2}],nonhereditary=m=>m===1||m===7;assert.ok(rooted(7,ordinary));assert.ok(!generate(3,ordinary,nonhereditary).has(7));
const sourceChecks=[];let rng=719;const random=()=>((rng=(Math.imul(rng,1664525)+1013904223)>>>0)/2**32);
for(const D of [0,1,2,3,4]){
 const u=contractionUniverse({maxOrigin:D}),g=u.rules,cell=p=>g.charts[g.packets[p].chart].cell;
 for(const p of u.packets){const c=g.charts[g.packets[p].chart];assert.ok(g.geometry.cells[c.cell].vertices.every(v=>Object.values(c.aliases).includes(v)));}
 for(const mode of ['native','experimental-terminal-PE']){
  const native=u.operations.map(i=>g.operations[i]),compiled=native.map(o=>({...o,forbidden:[]}));if(mode!=='native')for(const o of u.shortcuts)compiled.push({...o,forbidden:u.packets.filter(p=>cell(p)===o.referenceNeutronCell||native.some(n=>n.source===o.source&&n.target===p))});
  let validChecks=0,edgeRestrictions=0;const samples=[[g.root]];
  for(let trial=0;trial<300;trial++)samples.push([...new Set([g.root,...u.packets.filter(()=>random()<0.06)])]);
  // Include successful, nontrivial source witnesses, not only random compatible sets.
  if(D===4)samples.push(JSON.parse(readFileSync('research/nima/results/persistent-nn-depth4/verification.json')).cases[1].witness.packets);
  for(const ids of samples){const a=inspectContraction(u,ids,{mode});if(!a.valid)continue;validChecks++;const selected=new Set(ids),enabled=compiled.filter(o=>selected.has(o.source)&&selected.has(o.target)&&!o.forbidden.some(p=>selected.has(p)));
   assert.deepEqual(enabled.filter(o=>o.kind==='experimental-terminal-PE').map(o=>o.id),a.shortcuts.map(o=>o.id));
   for(const p of ids){if(p===g.root)continue;const subset=ids.filter(q=>q!==p),b=inspectContraction(u,subset,{mode});assert.ok(b.valid);const sub=new Set(subset);for(const e of enabled)if(sub.has(e.source)&&sub.has(e.target)){assert.ok(!e.forbidden.some(q=>sub.has(q)));if(e.kind==='experimental-terminal-PE')assert.ok(b.shortcuts.some(o=>o.id===e.id));edgeRestrictions++;}}
   if(a.rooted){const prefix=[g.root];for(const step of a.construction){prefix.push(step.target);const b=inspectContraction(u,prefix,{mode});assert.ok(b.valid&&b.rooted);}assert.equal(prefix.length,ids.length);}
  }
  sourceChecks.push({maxOrigin:D,mode,packets:u.packets.length,interfaces:compiled.length,validChecks,edgeRestrictions});
 }
}
const paths=['research/nima/contracts/pne-structural-synthesis-net.v9.json','research/nima/checkers/check_prefix_completeness.mjs','research/nima/prefix-completeness-v1.md','research/nima/experimental-terminal-pe.mjs','research/nima/generative-phase-assembly.mjs','research/nima/interface-synthesis.mjs','research/nima/results/persistent-nn-depth4/verification.json'];
const report={schema:'marici.nima.prefix-completeness.v1',status:'pass',generic:{models,selections,rootedSelections,checkedTreePrefixes:prefixes},sourceChecks,negativeControls:['positive-third-support-rooted-but-no-seed-step','nonhereditary-compatibility-rooted-but-no-seed-step'],scope:'Mathematical seed-prefix theorem with exhaustive finite regression, not a proof-assistant formalization; finite source probes supplement guard analysis. No arbitrary-start extension theorem.',sourceHashes:Object.fromEntries(paths.map(p=>[p,createHash('sha256').update(readFileSync(p)).digest('hex')]))};mkdirSync('research/nima/results/prefix-completeness',{recursive:true});writeFileSync('research/nima/results/prefix-completeness/verification.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
