// Retained-core proton capture and separate neutralization; no reaction dynamics.
import assert from 'node:assert/strict';
import {mkdir,readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {lattice} from '../demos/particle-overlap-tetrahedron/simplex-model.mjs';
import {assemblyDomain} from '../demos/particle-overlap-tetrahedron/lithium6-assembly-model.mjs';
import {selectPhaseAssembly,compilePhaseAssembly,auditPhaseAssembly} from '../demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
const {adjacency,species}=assemblyDomain(),chartKey=c=>JSON.stringify([c.cell,c.species,c.aliases]),hash=b=>createHash('sha256').update(b).digest('hex');
const files=['./check_n13_o14_capture.mjs',...['phase-assembly-model.mjs','lithium6-assembly-model.mjs','phase-advance-model.mjs','phase-discipline-model.mjs','window-construction-model.mjs','deuterium-tunnel-model.mjs','fiber-coverage-model.mjs','simplex-model.mjs','simplex-components.mjs'].map(f=>'../demos/particle-overlap-tetrahedron/'+f)],sourceHashes={};
for(const f of files)sourceHashes[f]=hash(await readFile(new URL(f,import.meta.url)));
function candidate(nucleus,electrons,types){
 const all=[...nucleus,...electrons],interfaces=[];
 if(new Set(all).size!==all.length||all.some(i=>lattice.cells[i].some(v=>!['M','C'].includes(types[v]))||lattice.cells[i].filter(v=>types[v]==='M').length!==2))return null;
 for(const i of all)for(const e of adjacency[i])if(i<e.to&&all.includes(e.to)){
  const a=electrons.includes(i)?'electron':species[i],b=electrons.includes(e.to)?'electron':species[e.to];
  if(a===b&&a!=='neutron'||[a,b].includes('electron')&&[a,b].includes('proton'))return null;
  const kind=[a,b].includes('electron')?'NE':a===b?'NN':'PN';
  if(e.face.filter(v=>types[v]==='M').length!==(kind==='PN'?2:1))return null;
  interfaces.push({from:i,to:e.to,face:[...e.face],kind});
 }
 return {nucleus:[...nucleus].sort((a,b)=>a-b),electrons:[...electrons].sort((a,b)=>a-b),types:{...types},interfaces,nuclearCycleRank:interfaces.filter(e=>e.kind!=='NE').length-nucleus.length+1};
}
function addProton(old){
 const {nucleus,electrons}=old.candidate,candidates=[];let neighboringProtons=0;
 for(let p=0;p<lattice.cells.length;p++){
  if(species[p]!=='proton'||[...nucleus,...electrons].includes(p)||!adjacency[p].some(e=>nucleus.includes(e.to)))continue;neighboringProtons++;
  const types={...old.candidate.types};let good=true;
  for(const e of adjacency[p].filter(e=>nucleus.includes(e.to))){
   if(species[e.to]!=='neutron'||e.face.filter(v=>types[v]==='M').length!==2){good=false;break;}
   const apex=lattice.cells[p].find(v=>!e.face.includes(v));if(types[apex]&&types[apex]!=='C'){good=false;break;}types[apex]='C';
  }
  if(good){const c=candidate([...nucleus,p],electrons,types);if(c)candidates.push(c);}
 }
 return {neighboringProtons,candidates};
}
function* choose(ids,n,start=0,p=[]){if(!n){yield p;return;}for(let i=start;i<=ids.length-n;i++)yield* choose(ids,n-1,i+1,[...p,ids[i]]);}
function addElectrons(old,count){
 const {nucleus,electrons,types}=old.candidate,possible=new Map();
 for(const n of nucleus.filter(i=>species[i]==='neutron'))for(const e of adjacency[n]){
  if([...nucleus,...electrons].includes(e.to)||species[e.to]!=='neutron'||e.face.filter(v=>types[v]==='M').length!==1)continue;
  const apex=lattice.cells[e.to].find(v=>!e.face.includes(v));if(types[apex]&&types[apex]!=='M')continue;possible.set(e.to,apex);
 }
 const candidates=[];let combinationsTested=0;
 for(const extra of choose([...possible.keys()].sort((a,b)=>a-b),count)){
  combinationsTested++;const t={...types};extra.forEach(i=>t[possible.get(i)]='M');const c=candidate(nucleus,[...electrons,...extra],t);if(c)candidates.push(c);
 }
 return {individuallyProposedCells:[...possible.keys()],combinationsTested,candidates};
}
function check(old,geometry){
 const accepted=[],rejections={};let tested=0,phaseCompatible=0;
 for(const c of geometry.candidates)for(let o=0;o<2**c.interfaces.filter(e=>e.kind==='PN').length;o++){
  tested++;const r=compilePhaseAssembly(c,o);if(r.status!=='phase-coherent-reference'){rejections[r.reason]=(rejections[r.reason]??0)+1;continue;}phaseCompatible++;
  const audit=auditPhaseAssembly(r);assert.equal(audit.coverage.coveredCells,c.nucleus.length+c.electrons.length);
  if(!old.charts.every(a=>r.charts.some(b=>chartKey(a)===chartKey(b)))){rejections['old-reader-not-retained']=(rejections['old-reader-not-retained']??0)+1;continue;}
  for(const e of old.edges)assert.ok(r.edges.some(f=>chartKey(old.charts[e.from])===chartKey(r.charts[f.from])&&chartKey(old.charts[e.to])===chartKey(r.charts[f.to])&&e.kind===f.kind&&e.phaseDelta===f.phaseDelta&&JSON.stringify(e.permutation)===JSON.stringify(f.permutation)));
  accepted.push({reference:r,phaseStateCount:audit.phaseStateCount,coveredCells:audit.coverage.coveredCells,addedProtons:c.nucleus.filter(i=>!old.candidate.nucleus.includes(i)),addedElectrons:c.electrons.filter(i=>!old.candidate.electrons.includes(i)),oldReadersAndTransportPreserved:true});
 }
 assert.equal(tested,accepted.length+Object.values(rejections).reduce((a,b)=>a+b,0));
 return {geometry,readerAssignmentsTested:tested,phaseSearchComplete:true,phaseCompatible,accepted,rejections};
}
const carbon=selectPhaseAssembly('carbon12');assert.equal(auditPhaseAssembly(carbon).coverage.coveredCells,18);
const nuclearVertices=new Set(carbon.candidate.nucleus.flatMap(i=>lattice.cells[i]));
const stripped={candidate:{...carbon.candidate,electrons:[],types:Object.fromEntries(Object.entries(carbon.candidate.types).filter(([v])=>nuclearVertices.has(Number(v))))}};
const bareGeometry=addProton(stripped);
const n13=check(carbon,addProton(carbon)),n13Neutral=[],o14=[],o14OneElectron=[],o14Neutral=[];
for(const [parentIndex,a] of n13.accepted.entries()){
 n13Neutral.push({parentIndex,result:check(a.reference,addElectrons(a.reference,1))});
 const result=check(a.reference,addProton(a.reference));o14.push({parentIndex,result});
 for(const [oxygenIndex,b] of result.accepted.entries()){
  o14OneElectron.push({parentIndex,oxygenIndex,result:check(b.reference,addElectrons(b.reference,1))});
  o14Neutral.push({parentIndex,oxygenIndex,result:check(b.reference,addElectrons(b.reference,2))});
 }
}
const summarize=r=>({geometryCandidates:r.geometry.candidates.length,readerAssignmentsTested:r.readerAssignmentsTested,accepted:r.accepted.length,witnesses:r.accepted.map(a=>({addedProtons:a.addedProtons,addedElectrons:a.addedElectrons,orientation:a.reference.orientations,phaseStateCount:a.phaseStateCount,coveredCells:a.coveredCells}))});
const summary={bareRetainedCarbon12ProtonExtensions:bareGeometry.candidates.length,conditionalStagesReached:n13.accepted.length>0,n13SixElectrons:summarize(n13),n13Neutral:n13Neutral.map(x=>({parentIndex:x.parentIndex,...summarize(x.result)})),o14SixElectrons:o14.map(x=>({parentIndex:x.parentIndex,...summarize(x.result)})),o14SevenElectrons:o14OneElectron.map(x=>({parentIndex:x.parentIndex,oxygenIndex:x.oxygenIndex,...summarize(x.result)})),o14Neutral:o14Neutral.map(x=>({parentIndex:x.parentIndex,oxygenIndex:x.oxygenIndex,...summarize(x.result)}))};
for(const f of files)assert.equal(hash(await readFile(new URL(f,import.meta.url))),sourceHashes[f],'Source changed: '+f);
const receipt={status:'retained-capture-and-neutralization-search-complete',sourceHashes,summary,bareGeometry,n13,n13Neutral,o14,o14OneElectron,o14Neutral,scope:'Selected C-12 retained; all passing six-electron N-13 references tested as O-14 parents. Electron additions retain existing cells and readers; original split-electron/contact rules. All valid candidates and reader assignments in these retained scopes tested. Not an unrestricted isotope search, bare-nucleus audit, decay model, stability prediction or physical capture simulation. No production/viewer changes.'};
await mkdir('research/strominger/results/n13-o14-capture',{recursive:true});await writeFile('research/strominger/results/n13-o14-capture/verification.json',JSON.stringify(receipt,null,2)+'\n');console.log(JSON.stringify(summary,null,2));
