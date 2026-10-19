import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {phaseUniverse} from '../origin-bounded-assemblies.mjs';
import {validateContraction} from '../experimental-terminal-pe.mjs';
const contractPath='research/nima/contracts/pne-structural-synthesis-net.v1.json',contract=JSON.parse(readFileSync(contractPath,'utf8')),test=contract.tests.find(t=>t.id==='interface-path-catalog-D012-L234');assert.ok(test);assert.deepEqual(test.domain.maxOrigins,[0,1,2]);
const sourcePaths=[contractPath,'research/nima/checkers/check_pne_interface_catalog.mjs','research/nima/generative-phase-assembly.mjs','research/nima/origin-bounded-assemblies.mjs','research/nima/experimental-terminal-pe.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs'];
const hash=p=>createHash('sha256').update(readFileSync(p)).digest('hex'),sourceHashes=Object.fromEntries(sourcePaths.map(p=>[p,hash(p)]));
const report={schema:'marici.nima.pne-interface-catalog.v1',test:test.id,status:'pass-bounded-native-path-catalog',domain:test.domain,sourceHashes,cases:[]};
for(const D of test.domain.maxOrigins){
 const u=phaseUniverse({maxOrigin:D});assert.ok(u.complete);const g=u.rules,allowed=new Set(u.operations),records=[];
 const chart=id=>g.charts[g.packets[id].chart],cell=id=>chart(id).cell;
 function save(ids,factors){
 const source=ids[0],target=ids.at(-1),ops=factors.map(i=>g.operations[i]);let permutation=[0,1,2,3,4];for(const o of ops){g.validateTransfer(o);permutation=o.permutation.map(i=>permutation[i]);}
 assert.deepEqual(permutation.map(i=>g.packets[source].permutation[i]),g.packets[target].permutation);
 const originDelta=g.packets[target].origin-g.packets[source].origin;assert.equal(originDelta,ops.reduce((n,o)=>n+o.phaseDelta,0));
 const support=[...new Set(ids.map(cell))].sort((a,b)=>a-b),description=g.describe(ids),endpoints=g.describe([source,target]);
 const shared=g.geometry.cells[cell(source)].vertices.filter(v=>g.geometry.cells[cell(target)].vertices.includes(v)).sort();
 const pe=chart(source).species==='proton'&&chart(target).species==='electron',internalN=pe&&ids.slice(1,-1).every(p=>chart(p).species==='neutron');
 const eligible=internalN&&originDelta===0;
 if(eligible){assert.deepEqual(ops.map(o=>o.kind),['PN','NE']);validateContraction(g,ops[0],ops[1]);}
 const occurrences=ids.map(p=>({packet:p,chart:g.packets[p].chart,origin:g.packets[p].origin,marks:Object.entries(chart(p).aliases).map(([mark,vertex])=>({mark,role:mark[0],index:Number(mark.slice(1))+g.packets[p].origin,vertex}))}));
 records.push({id:records.length,source,target,packets:ids,factors,word:ops.map(o=>o.kind),length:factors.length,permutation,originDelta,sourceOrigin:g.packets[source].origin,targetOrigin:g.packets[target].origin,sharedVertices:shared,referenceSupport:support,referenceOccurrences:occurrences,
 nativePolicy:{permission:'native-factor-path',requiredOccupied:support,requiredVacant:[],fullSupportCompatible:description.valid,rejection:description.reason??null},endpointsCompatible:endpoints.valid,internalN,terminalPE:pe,
 contractedPolicy:eligible?{permission:'experimental-terminal-PE',requiredOccupied:[cell(source),cell(target)],requiredVacant:[cell(ids[1])],referenceSupport:support,forbiddenSelectedNativeSuccessors:g.outgoing(source).map(i=>g.operations[i].target),terminalReader:source,terminalElectron:target,fullMapPreserved:true}:null});
 }
 function visit(ids,factors){if(test.domain.pathLengths.includes(factors.length))save(ids,factors);if(factors.length>=Math.max(...test.domain.pathLengths))return;for(const i of g.outgoing(ids.at(-1))){if(!allowed.has(i))continue;const o=g.operations[i];if(ids.includes(o.target))continue;visit([...ids,o.target],[...factors,i]);}}
 for(const p of u.packets)visit([p],[]);
 const groups=new Map();for(const r of records){const k=[cell(r.source),chart(r.source).species,cell(r.target),chart(r.target).species].join(':');if(!groups.has(k))groups.set(k,[]);groups.get(k).push(r);}
 const geometryCollisions=[...groups].filter(([,rows])=>new Set(rows.map(r=>r.permutation.join(','))).size>1).map(([endpoints,rows])=>({endpoints,records:rows.map(r=>r.id),maps:[...new Set(rows.map(r=>r.permutation.join(',')))]}));
 const pe=records.filter(r=>r.internalN),byWord={};for(const r of pe){const key=r.word.join(' -> ');byWord[key]=(byWord[key]??0)+1;}
 const summaries={maxOrigin:D,packets:u.packets.length,operations:u.operations.length,paths:records.length,byLength:Object.fromEntries(test.domain.pathLengths.map(n=>[n,records.filter(r=>r.length===n).length])),fullSupportCompatible:records.filter(r=>r.nativePolicy.fullSupportCompatible).length,internalN_PtoE:pe.length,sameOrigin_PtoE:pe.filter(r=>r.originDelta===0).length,contractedInterfaces:records.filter(r=>r.contractedPolicy).length,byWord,geometryMapCollisionGroups:geometryCollisions.length,terminalityOnlyCounterexamples:pe.filter(r=>r.originDelta>0&&r.endpointsCompatible).length,edgeOnlyCounterexamples:pe.filter(r=>r.originDelta>0&&r.sharedVertices.length===2&&r.endpointsCompatible).length};
 report.cases.push({summary:summaries,records,geometryCollisions,registry:{root:g.root,universePackets:u.packets,allowedOperations:u.operations,packets:g.packets,charts:g.charts,cells:g.geometry.cells.map(({owner,...c})=>c),operations:g.operations}});console.log(JSON.stringify(summaries));
}
assert.deepEqual(Object.fromEntries(sourcePaths.map(p=>[p,hash(p)])),sourceHashes);
const out='research/nima/results/pne-interface-catalog';mkdirSync(out,{recursive:true});writeFileSync(out+'/verification.json',JSON.stringify(report,null,2)+'\n');
