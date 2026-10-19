import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {contractionUniverse,inspectContraction} from '../experimental-terminal-pe.mjs';
import {deriveObstruction} from '../pne-source-obstructions.mjs';
import {searchExtension} from '../guarded-extension-search.mjs';
const contractPath='research/nima/contracts/pne-structural-synthesis-net.v8.json',contract=JSON.parse(readFileSync(contractPath)),test=contract.added_tests.find(t=>t.id==='persistent-NN-core-depth4');assert.ok(test&&!test.executed);
const u2=contractionUniverse({maxOrigin:2}),signature=(g,p)=>{const a=g.packets[p],c=g.charts[a.chart];return JSON.stringify([g.geometry.cells[c.cell].key,c.species,c.aliases,a.origin,a.permutation]);};
const report={schema:'marici.nima.persistent-nn-depth4.v1',test:test.id,cases:[],resourceLimits:{maxNodes:test.domain.maxSearchNodes,maxMilliseconds:test.domain.maxMilliseconds}},out='research/nima/results/persistent-nn-depth4';mkdirSync(out,{recursive:true});
for(const D of [3,4]){
 const u=contractionUniverse({maxOrigin:D}),g=u.rules,lookup=new Map(u.packets.map(p=>[signature(g,p),p])),mapped=Object.fromEntries([0,1,4,13,18].map(p=>[p,lookup.get(signature(u2.rules,p))]));assert.ok(Object.values(mapped).every(p=>p!==undefined));
 const core=[mapped[13],mapped[18]],cell=p=>g.charts[g.packets[p].chart].cell,faceCells=core.map(cell),shared=g.geometry.cells[faceCells[0]].vertices.filter(v=>g.geometry.cells[faceCells[1]].vertices.includes(v));assert.equal(shared.length,3);
 const incoming=[g.root,...core,mapped[1],mapped[4]],candidates=u.operations.map(i=>g.operations[i]).filter(o=>cell(o.source)!==cell(o.target)&&faceCells.includes(cell(o.source))&&faceCells.includes(cell(o.target))).map(o=>{
  const endpoints=[o.source,o.target],withCore=g.describe([...new Set([g.root,...core,...endpoints])]),withIncoming=g.describe([...new Set([...incoming,...endpoints])]);
  const pairBlockers=[];for(const p of incoming)for(const q of endpoints){const d=g.describe([...new Set([p,q])]);if(!d.valid)pairBlockers.push({mandatoryPacket:p,witnessPacket:q,reason:d.reason});}
  return {operation:o.id,kind:o.kind,source:o.source,target:o.target,origins:endpoints.map(p=>g.packets[p].origin),compatibleWithCore:withCore.valid,coreReason:withCore.reason??null,compatibleWithIncoming:withIncoming.valid,incomingReason:withIncoming.reason??null,pairBlockers};
 });
 const without1=deriveObstruction(u,core,{forbidden:[mapped[1]]}),without4=deriveObstruction(u,[...core,mapped[1]],{forbidden:[mapped[4]]}),forced=deriveObstruction(u,[...core,mapped[1],mapped[4]]);
 const row={maxOrigin:D,packetUniverse:u.packets.length,core,mapped,faceCells,sharedFace:shared,faceWitnessCandidates:candidates,withoutFirstIncoming:without1,withoutSecondIncoming:without4,withBothIncoming:forced};
 if(D===4){
  const result=searchExtension(u,core,report.resourceLimits);row.search=result;
  if(result.status==='sat'){
   let ids=[...result.selectedPackets];const required=new Set([g.root,...core]);for(let changed=true;changed;){changed=false;for(const p of ids)if(!required.has(p)&&inspectContraction(u,ids.filter(q=>q!==p)).certifiedExit){ids=ids.filter(q=>q!==p);changed=true;break;}}
   const a=inspectContraction(u,ids);assert.ok(a.certifiedExit);assert.ok(core.every(p=>ids.includes(p)));const prefix=[g.root];for(const step of a.construction){prefix.push(step.target);const b=inspectContraction(u,prefix);assert.ok(b.valid&&b.rooted);}assert.equal(prefix.length,ids.length);assert.equal(Math.max(...ids.map(p=>g.packets[p].origin)),4);
   row.witness={packets:ids,counts:a.counts,records:ids.length,operations:a.construction.length,construction:a.construction,shortcuts:a.shortcuts,faceWitnesses:candidates.filter(c=>ids.includes(c.source)&&ids.includes(c.target))};assert.ok(row.witness.faceWitnesses.length);
   const selected=new Set(ids),edges=u.operations.map(i=>g.operations[i]).filter(o=>selected.has(o.source)&&selected.has(o.target)).concat(a.shortcuts);row.witness.bridgeContinuationPaths=[];
   for(const start of [...new Set(row.witness.faceWitnesses.map(o=>o.target))]){
    const queue=[start],parent=new Map([[start,null]]);let end=null;
    for(let i=0;i<queue.length;i++){const p=queue[i];if(g.charts[g.packets[p].chart].species==='electron'){end=p;break;}for(const o of edges)if(o.source===p&&!parent.has(o.target)){parent.set(o.target,o);queue.push(o.target);}}
    assert.notEqual(end,null);const path=[];for(let p=end;p!==start;){const o=parent.get(p);path.push({kind:o.kind,id:o.id,source:o.source,target:o.target,origins:[g.packets[o.source].origin,g.packets[o.target].origin]});p=o.source;}path.reverse();assert.equal(Math.max(...path.flatMap(o=>o.origins)),4);row.witness.bridgeContinuationPaths.push({start,exit:end,path});
   }
  }
  if(result.status==='unsat'){
   let leaves=0;const verify=(t,req,forbid)=>{if(t.kind==='split'){assert.ok(!req.includes(t.packet)&&!forbid.includes(t.packet));verify(t.present,[...req,t.packet],forbid);verify(t.absent,req,[...forbid,t.packet]);}else{assert.equal(t.kind,'contradiction');assert.deepEqual(t.required,req);assert.deepEqual(t.forbidden,forbid);assert.equal(deriveObstruction(u,req,{forbidden:forbid}).status,'obstructed');leaves++;}};verify(result.proof,[...new Set([g.root,...core])],[]);row.verifiedProofLeaves=leaves;
  }
 }
 row.registry={packets:g.packets,charts:g.charts,cells:g.geometry.cells.map(({owner,...c})=>c),operations:g.operations,universePackets:u.packets};report.cases.push(row);writeFileSync(out+'/verification.json',JSON.stringify(report,null,2)+'\n');
 console.log(JSON.stringify({D,packets:u.packets.length,candidates:candidates.length,compatibleCore:candidates.filter(c=>c.compatibleWithCore).length,compatibleIncoming:candidates.filter(c=>c.compatibleWithIncoming).length,without1:without1.status,without4:without4.status,forced:forced.status,search:row.search?{status:row.search.status,nodes:row.search.nodes,reason:row.search.reason}:null,witness:row.witness?{counts:row.witness.counts,records:row.witness.records,faceWitnesses:row.witness.faceWitnesses}:null}));
}
report.status=report.cases[1].search.status==='incomplete'?'partial-D4-search-resource-stop':'complete-D4-outcome';report.sourceHashes=Object.fromEntries([contractPath,'research/nima/checkers/check_persistent_nn_depth4.mjs','research/nima/guarded-extension-search.mjs','research/nima/pne-source-obstructions.mjs','research/nima/experimental-terminal-pe.mjs','research/nima/generative-phase-assembly.mjs'].map(p=>[p,createHash('sha256').update(readFileSync(p)).digest('hex')]));writeFileSync(out+'/verification.json',JSON.stringify(report,null,2)+'\n');
