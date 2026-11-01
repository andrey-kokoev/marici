// Bind a declared four-face macrostep to the actual retained geometric routes.
// Reflection compares charts; it is never inserted as a physical face hop.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildFiveSideOctRoutingObligations} from '../../realization-tower/five-side-oct-routing-obligations.mjs';
const root='research/strominger',paths={
 contract:root+'/contracts/su32-edge5-twisted-return-v1.json',
 wiring:root+'/results/su32-edge5-global-routing-witness-v1/verification.json',
 carrier:root+'/results/su32-edge5-extension-contract-v1/verification.json',
 binding:root+'/results/su32-edge5-fibre-placement-binding-v1/verification.json'};
const digest=async p=>createHash('sha256').update(await fs.readFile(p)).digest('hex');
const docs={},sourceHashes={};
for(const [key,p] of Object.entries(paths)){
 docs[key]=JSON.parse(await fs.readFile(p,'utf8'));sourceHashes[p]=await digest(p);
 for(const [s,h] of Object.entries(docs[key].sourceHashes??{}))assert.equal(await digest(s),h,`Stale source ${s}`);
}
assert.equal(docs.contract.source,paths.wiring);
const geometry=docs.carrier.edge5Carrier,routes=docs.wiring.routes;
assert.equal(routes.length,80);assert.equal(new Set(routes.map(r=>r.fibre)).size,80);
const sector=buildPESymmetricSector(2);
const reading=buildFiveSideOctRoutingObligations(sector).readings.find(r=>r.id==='reading:0:-1');assert(reading);
const shape=vs=>vs.map(v=>v.join(',')).sort().join('|');
const reflect=v=>{const h=reading.axis.reduce((s,a,i)=>s+a*(v[i]-sector.centre[i]),0)/2;return v.map((x,i)=>x-h*reading.axis[i]);};
const cellByShape=new Map(geometry.cells.map(c=>[shape(c.vertices),c]));
const cells=new Map(geometry.cells.map(c=>[c.id,c])),faces=new Map(geometry.faces.map(f=>[f.id,f]));
const R=new Map(geometry.cells.map(c=>[c.id,cellByShape.get(shape(c.vertices.map(reflect)))?.id]));
const RF=new Map(geometry.faces.map(f=>[f.id,shape(f.vertices.map(reflect))]));
for(const [c,d] of R){assert(d);assert.equal(R.get(d),c);assert.equal(cells.get(d).role,({proton:'electron',electron:'proton',neutron:'neutron'})[cells.get(c).role]);}
for(const [f,g] of RF){assert(faces.has(g));assert.equal(RF.get(g),f);assert.deepEqual(faces.get(f).owners.map(x=>R.get(x)).sort(),[...faces.get(g).owners].sort());}
const layer=new Map(geometry.layers.flatMap(l=>l.cells.map(id=>[id,l.layer])));
const originalSupport=new Set(routes.flatMap(r=>r.faces)),dualSupport=new Set();
const reverse=r=>({fibre:r.fibre,cells:[...r.cells].reverse(),faces:[...r.faces].reverse()});
const programs=routes.map(route=>{
 const dual={fibre:route.fibre,cells:route.cells.map(c=>R.get(c)),faces:route.faces.map(f=>RF.get(f))};
 dual.faces.forEach(f=>dualSupport.add(f));
 assert.equal(route.cells.at(-1),dual.cells[0]);assert.equal(dual.cells.at(-1),route.cells[0]);
 for(const [chart,r] of [route,dual].entries()){
  assert.equal(r.cells.length,17);assert.equal(r.faces.length,16);
  for(let i=0;i<16;i++){
   assert.deepEqual([...faces.get(r.faces[i]).owners].sort(),[r.cells[i],r.cells[i+1]].sort());
   assert.equal(layer.get(r.cells[i+1])-layer.get(r.cells[i]),chart===0?1:-1);
  }
 }
 const halves=[route,dual];
 const blocks=halves.flatMap((r,chart)=>Array.from({length:4},(_,phase)=>({chart,phase,
  cells:r.cells.slice(4*phase,4*phase+5),faces:r.faces.slice(4*phase,4*phase+4)})));
 for(let i=0;i<8;i++)assert.equal(blocks[i].cells.at(-1),blocks[(i+1)%8].cells[0]);
 return {fibre:route.fibre,blocks,reflectedRouteIsInverse:JSON.stringify(dual)===JSON.stringify(reverse(route))};
});
const dualOnlyFaces=[...dualSupport].filter(f=>!originalSupport.has(f)).sort();
const state=(p,k)=>({fibre:p.fibre,chart:Math.floor(k/4),phase:k%4,cell:p.blocks[k].cells[0]});
const next=k=>(k+1)%8,dualIndex=k=>(k+4)%8;
const advance=(p,k,history)=>{
 const b=p.blocks[k];return {index:next(k),history:[...history,{...structuredClone(b),fibre:p.fibre}]};
};
let testedStates=0,ordinaryFourFailures=0,eightReferenceReturns=0,historyNonreturns=0;
const witnesses=[];
for(const p of programs){
 for(let start=0;start<8;start++){
  let run={index:start,history:[]};const initial=state(p,start);
  for(let j=0;j<4;j++)run=advance(p,run.index,run.history);
  const terminal=state(p,run.index),dualReference=state(p,dualIndex(start));
  assert.deepEqual(terminal,dualReference);assert.equal(terminal.cell,R.get(initial.cell));
  assert.notDeepEqual(terminal,initial);ordinaryFourFailures++;
  const firstHistory=structuredClone(run.history);
  assert.equal(run.history.flatMap(h=>h.faces).length,16);
  for(let j=0;j<4;j++)run=advance(p,run.index,run.history);
  assert.deepEqual(state(p,run.index),initial);eightReferenceReturns++;
  assert.deepEqual(run.history.slice(0,4),firstHistory);assert.equal(run.history.flatMap(h=>h.faces).length,32);
  assert.notDeepEqual({active:state(p,run.index),history:run.history},{active:initial,history:[]});historyNonreturns++;
  if(start===0)witnesses.push({fibre:p.fibre,initial,intermediate:[1,2,3].map(k=>state(p,k)),terminal,
   retainedFourBlockHistory:firstHistory,returnWitness:{kind:'dual-reference',comparedWith:dualReference,ordinaryEquality:false},
   eightBlockActiveReturn:state(p,run.index),retainedEightBlockHistory:run.history});
  testedStates++;
 }
}
assert.equal(testedStates,640);assert.equal(witnesses.length,80);
// The same payload bank survives each block; traversal logs are not new tokens.
let bank=new Map(programs.map(p=>[p.fibre,{index:0,payload:{fibre:p.fibre,opaque:['retained']},history:[]}])) ;
const originalPayload=structuredClone([...bank].map(([id,s])=>[id,s.payload]));
for(let i=0;i<8;i++){
 bank=new Map(programs.map(p=>{const s=bank.get(p.fibre),r=advance(p,s.index,s.history);return [p.fibre,{...r,payload:s.payload}];}));
 assert.equal(bank.size,80);
}
assert.deepEqual([...bank].map(([id,s])=>[id,s.payload]),originalPayload);
assert([...bank.values()].every(s=>s.index===0&&s.history.length===8));
const agdaPath=root+'/results/su32-edge5-twisted-return-v1/agda.json';
const agda=JSON.parse((await fs.readFile(agdaPath,'utf8')).replace(/^\uFEFF/,''));
assert.equal(agda.module,'TwistedRouteReturn');assert.equal(agda.passed,true);
assert.equal(agda.ignore_interfaces,true);assert.equal(agda.inputs_stable_during_check,true);
const proof=root+'/agda/TwistedRouteReturn.agda',wrapper=root+'/checkers/check_dependent_four_return_agda.ps1';
assert.equal(await digest(proof),agda.source_sha256);assert.equal(await digest(wrapper),agda.source_inventory.checker);
for(const name of ['DependentFourReturn.agda','CoherentFourReturn.agda'])assert.equal(await digest(root+'/agda/'+name),agda.source_inventory.owner[name]);
for(const p of [proof,wrapper,agdaPath,root+'/checkers/check_su32_edge5_twisted_return.mjs',
 root+'/pe-symmetric-sector.mjs','research/realization-tower/five-side-oct-routing-obligations.mjs'])sourceHashes[p]=await digest(p);
const counts={fibres:80,orientedProgramStates:testedStates,ordinaryFourFailures,eightReferenceReturns,historyNonreturns,
 reflectedRoutesEqualOwnInverse:programs.filter(p=>p.reflectedRouteIsInverse).length,
 originalUsedFaces:originalSupport.size,dualUsedFaces:dualSupport.size,dualOnlyFaces:dualOnlyFaces.length,
 unionUsedFaces:new Set([...originalSupport,...dualSupport]).size};
const result={schema:'su32.edge5-twisted-return.v1',passed:true,counts,
 conclusion:'The declared four-face-block executor has G^4=R and G^8=id on active oriented references, not ordinary four-return. Retained histories do not return.',
 agda:{receipt:agdaPath,fresh:true,theorems:['Twisted.eight-return','Program.four-is-dual','Program.no-Per4','Program.eight-is-return','Program.distinct-frames']},
 interpretation:{macrostep:'Chosen granularity of four actual crossings, not a derived native operation.',
 secondLeg:'Reflected entire route, an added dual-chart continuation. Not automatically the original inverse route.',
 reflection:'Comparison and whole-plan duality only; never an executed teleportation.',
 histories:'Every crossing retained, including the original four-block prefix.',
 period:'Eight is the active period of this declared controller, not a derived physical period.',
 nonverification:'No native junction/filling law, signed pair-content binding or canonical route selection is established.'},
 programs,witnesses,dualOnlyFaces,sourceHashes};
await fs.writeFile(root+'/results/su32-edge5-twisted-return-v1/verification.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({...result,programs:undefined,witnesses:undefined,dualOnlyFaces:undefined,sourceHashes:undefined},null,2));
