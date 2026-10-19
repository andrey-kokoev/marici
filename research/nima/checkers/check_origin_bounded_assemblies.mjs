import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir,copyFile,stat} from 'node:fs/promises';
import {createWriteStream,createReadStream} from 'node:fs';
import {createHash} from 'node:crypto';
import {createGzip,createGunzip} from 'node:zlib';
import {pipeline} from 'node:stream/promises';
import {once} from 'node:events';
import {createInterface} from 'node:readline';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
const root=fileURLToPath(new URL('../../../',import.meta.url)),out=path.join(root,'research/nima/results/origin-bounded-assemblies');
const base='research/strominger/demos/particle-overlap-tetrahedron/';
const common=['lattice-items','simplex-components','carrier','model','window-construction-model','phase-advance-model','phase-discipline-model','deuterium-tunnel-model','fiber-coverage-model'].map(n=>base+n+'.mjs');
const own=['research/nima/generative-phase-assembly.mjs','research/nima/origin-bounded-assemblies.mjs','research/nima/origin-assembly-family.mjs','research/nima/inputs/origin-bounded-assemblies-v1.json','research/nima/checkers/check_origin_bounded_assemblies.mjs','research/nima/demos/origin-bounded-assemblies.template.html'];
const ownerChecker='research/strominger/checkers/check_nima_phase_budget_semantics.mjs',sha=b=>createHash('sha256').update(b).digest('hex');
async function fingerprint(){return Object.fromEntries(await Promise.all([...common,...own,ownerChecker].map(async p=>[p,sha(await readFile(path.join(root,p)))])));}
const hashes=await fingerprint(),contract=JSON.parse(await readFile(path.join(root,own[3]),'utf8'));
const {enumerateOriginAssemblies,phaseUniverse,auditRecordSewing,GenerativeAssemblyRules}=await import('../origin-bounded-assemblies.mjs');
const {buildPhaseFamily,reconstructPhaseSelection,BooleanDiagram}=await import('../origin-assembly-family.mjs');
const {windowProtocol}=await import('../../strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs');
// Execute the owner's unmodified audit with copied read-only inputs and isolated outputs.
const sandbox=path.join(root,'.ai/tmp/nima-origin-budget-owner-audit');
for(const p of ['research/nima/generative-phase-assembly.mjs',base+'phase-advance-model.mjs',base+'phase-discipline-model.mjs',base+'window-construction-model.mjs']){
 const q=path.join(sandbox,p);await mkdir(path.dirname(q),{recursive:true});await copyFile(path.join(root,p),q);
}
const audit=spawnSync('node',[path.join(root,ownerChecker)],{cwd:sandbox,encoding:'utf8'});assert.equal(audit.status,0,audit.stderr);
await mkdir(out,{recursive:true});
const auditReceipt=JSON.parse(await readFile(path.join(sandbox,'research/strominger/results/nima-phase-budget-audit/verification.json'),'utf8'));
assert.equal(auditReceipt.status,'pass-local-semantics-falsifiers');
await writeFile(path.join(out,'strominger-audit-replay.json'),JSON.stringify(auditReceipt,null,2)+'\n');
// Tiny Boolean-diagram truth-table, free-variable counting and maximum-selection control.
const tiny=new BooleanDiagram(3),v=[0,1,2].map(i=>tiny.variable(i)),formula=tiny.and(v[0],tiny.or(v[1],v[2]));
assert.equal(tiny.count(formula),3n);assert.equal(tiny.models(formula,100).length,3);assert.deepEqual(tiny.maximumSelection(formula),[0,1,2]);
const g=new GenerativeAssemblyRules(),edge=(id,kind)=>{const e=g.outgoing(id).map(i=>g.operations[i]).find(e=>e.kind===kind);assert.ok(e,kind);return e;};
const pn=edge(g.root,'PN'),inverse=edge(pn.target,'inverse-PN'),p1=edge(g.root,'reader-phase-advance'),p2=edge(p1.target,'reader-phase-advance'),n1=edge(pn.target,'reader-phase-advance'),ne=edge(pn.target,'NE'),nn=edge(pn.target,'NN-phase-advance');
assert.equal(inverse.target,g.root);assert.equal(g.packets[p2.target].origin,2);assert.notEqual(p2.target,g.root);assert.deepEqual(g.packets[p2.target].permutation,g.packets[g.root].permutation);
assert.equal(g.describe([g.root,pn.target,p1.target,n1.target]).valid,true);assert.equal(Math.max(...[g.root,pn.target,p1.target,n1.target].map(p=>g.packets[p].origin)),1);
assert.equal(g.describe([g.root,pn.target,ne.target,nn.target]).reason,'occupied-cell-species-conflict');
assert.equal(g.inspect([g.root,pn.target,ne.target]).certifiedExit,true);assert.ok(g.packets.length>3);
let negativeControls=0;
assert.equal(phaseUniverse({maxOrigin:1,maxPackets:2}).complete,false);negativeControls++;
assert.equal(enumerateOriginAssemblies({maxOrigin:1,maxConfigurations:2,inspect:false}).complete,false);negativeControls++;
assert.throws(()=>phaseUniverse({}));negativeControls++;
assert.throws(()=>buildPhaseFamily({maxOrigin:0,maxDiagramNodes:2}),/resource-limit/);negativeControls++;
assert.throws(()=>buildPhaseFamily({maxOrigin:0,sewingAssertions:[]}),/family\/key extension/);negativeControls++;
const identity=[0,1,2,3,4],nativeSewing=auditRecordSewing(g,{from:g.root,to:pn.target,coefficientIdentification:pn.permutation,occurrences:['M0','C1','M1'].map(m=>({fromMark:m,toMark:m}))});assert.equal(nativeSewing.generic,true);
const wrongOccurrence=auditRecordSewing(g,{from:g.root,to:p2.target,coefficientIdentification:identity,occurrences:[{fromMark:'C0',toMark:'C0'}]});assert.equal(wrongOccurrence.status,'occurrence-identification-rejected');negativeControls++;
const forged=g.packet(g.packets[g.root].chart,0,[3,1,2,0,4]),wrongMap=auditRecordSewing(g,{from:g.root,to:forged,coefficientIdentification:identity});assert.equal(wrongMap.generic,false);assert.equal(wrongMap.status,'explicit-input-subspace-required');assert.ok(wrongMap.rootEqualities.length);negativeControls++;
const equalInput=identity.map(()=>[1,0]);const {applyPhasePermutation}=await import('../generative-phase-assembly.mjs');assert.deepEqual(applyPhasePermutation(equalInput,g.packets[g.root].permutation),applyPhasePermutation(equalInput,g.packets[forged].permutation));
assert.equal(auditRecordSewing(g,{from:g.root,to:forged,coefficientIdentification:identity,identifiedSlots:[1,2,4]}).status,'identified-slot-sewing-pass');
assert.equal(auditRecordSewing(g,{scope:'history'}).status,'ancestry-key-required');negativeControls++;
assert.throws(()=>auditRecordSewing(g,{from:g.root,to:forged,coefficientIdentification:identity,identifiedSlots:[]}));negativeControls++;
const signature=(rules,id)=>{const p=rules.packets[id],c=rules.charts[p.chart];return JSON.stringify([rules.geometry.cells[c.cell].key,c.species,c.aliases,p.origin,p.permutation]);};
const expected={0:[3,1],1:[108,14],2:[198356,459]},reports={},cases={};let edgeChecks=0;
for(const D of contract.validationMaxOrigins){
 const family=buildPhaseFamily({maxOrigin:D}),r=enumerateOriginAssemblies({maxOrigin:D,maxConfigurations:contract.explicitConfigurationResourceLimit,inspect:false});
 assert.equal(r.complete,true,'Resource stop cannot pass explicit phase completeness');assert.equal(r.stop,null);
 assert.equal(family.summary.compatibleConfigurations,String(expected[D][0]));assert.equal(family.summary.selectedRecordExitCertificates,String(expected[D][1]));
 assert.equal(BigInt(r.nodes.length),family.diagram.count(family.validRoot));
 const familyPacket=new Map(family.variablePackets.map(p=>[signature(family.universe.rules,p),p]));
 const convert=new Map(r.universe.packets.map(p=>[p,familyPacket.get(signature(r.rules,p))]));assert.ok([...convert.values()].every(p=>p!==undefined));
 const nodeByKey=new Map(r.nodes.map(n=>[n.packets.join(','),n.id]));assert.equal(nodeByKey.size,r.nodes.length);
 const allowed=new Set(r.universe.operations),profiles=[],profileIds=new Map(),records=[],shapeKeys=new Set();let edgeCursor=0,exitCount=0,maxBodies=0,maxOperations=0;
 const gradingCounts=Array(D+1).fill(0);
 for(const node of r.nodes){
  const chosen=new Set(node.packets),grade=node.packets.reduce((m,p)=>Math.max(m,r.rules.packets[p].origin),0);assert.equal(grade,node.grade);assert.ok(grade<=D);gradingCounts[grade]++;
  assert.equal(node.minOperations,node.packets.length-1);maxOperations=Math.max(maxOperations,node.minOperations);
  assert.equal(family.accepts(node.packets.map(p=>convert.get(p))),true);
  const actual=new Map();while(edgeCursor<r.edges.length&&r.edges[edgeCursor].from===node.id){const e=r.edges[edgeCursor++],op=r.rules.operations[e.operation];assert.ok(allowed.has(e.operation)&&chosen.has(op.source));assert.equal(actual.has(e.operation),false);actual.set(e.operation,e.to);const ids=[...new Set([...node.packets,op.target])].sort((a,b)=>a-b);assert.deepEqual(r.nodes[e.to].packets,ids);edgeChecks++;}
  const wanted=new Map();for(const p of node.packets)for(const opId of r.rules.outgoing(p)){
   if(!allowed.has(opId))continue;const op=r.rules.operations[opId],ids=[...new Set([...node.packets,op.target])].sort((a,b)=>a-b);if(!chosen.has(op.target)&&!family.accepts(ids.map(p=>convert.get(p))))continue;const target=nodeByKey.get(ids.join(','));assert.notEqual(target,undefined);wanted.set(opId,target);
  }
  assert.deepEqual([...actual].sort(([a],[b])=>a-b),[...wanted].sort(([a],[b])=>a-b));
  const desc=r.rules.describe(node.packets),inspection=r.rules.inspect(node.packets,desc);assert.equal(inspection.valid,true);assert.equal(family.accepts(node.packets.map(p=>convert.get(p)),{exits:true}),inspection.certifiedExit);
  if(inspection.certifiedExit)exitCount++;
  const c=inspection.counts,key=[c.proton,c.neutron,c.electron].join('/');maxBodies=Math.max(maxBodies,c.proton+c.neutron+c.electron);
  if(!profileIds.has(key)){profileIds.set(key,profiles.length);profiles.push({counts:c,configurations:0,selectedRecordExitCertificates:0});}const profile=profileIds.get(key);profiles[profile].configurations++;if(inspection.certifiedExit)profiles[profile].selectedRecordExitCertificates++;
  const vertices=new Set([...desc.bodies.keys()].flatMap(c=>r.rules.geometry.cells[c].vertices));const shape=[...desc.bodies].sort(([a],[b])=>a-b).map(([a,b])=>a+':'+b).join(',')+'|'+[...desc.roles].filter(([v])=>vertices.has(v)).sort(([a],[b])=>a.localeCompare(b)).map(([a,b])=>a+':'+b).join(';');shapeKeys.add(shape);
  records.push([node.parent??-1,node.operation??-1,grade,node.minOperations,(inspection.exitPackets.length?1:0)|(inspection.certifiedExit?2:0),profile]);
 }
 assert.equal(edgeCursor,r.edges.length);assert.equal(BigInt(exitCount),family.diagram.count(family.exitRoot));
 const reverseConvert=new Map([...convert].map(([a,b])=>[b,a])),witnessFamily=family.maximumRecordWitness({exits:true}),witnessPackets=witnessFamily.map(p=>reverseConvert.get(p)).sort((a,b)=>a-b),witnessNode=nodeByKey.get(witnessPackets.join(','));assert.notEqual(witnessNode,undefined);
 const witnessConstruction=reconstructPhaseSelection(family,witnessFamily),witnessInspection=r.rules.inspect(witnessPackets);
 assert.equal(witnessConstruction.grade,D);assert.equal(witnessInspection.certifiedExit,true);
 if(D===2){assert.ok(witnessConstruction.word.length>9);assert.ok(witnessInspection.cells.length>10);}
 // All sampled Boolean models construct without an operation bound; do not
 // infer completeness from these samples (counts + all explicit models do it).
 for(const ids of family.models({limit:512}))reconstructPhaseSelection(family,ids);
 const dir=path.join(out,'D'+D);await mkdir(dir,{recursive:true});
 const summary={maxOrigin:D,originLayers:D+1,packetUniverse:r.universe.packets.length,allowedOperations:r.universe.operations.length,configurations:r.nodes.length,constructionEdges:r.edges.length,
  selectedRecordExitCertificates:exitCount,geometryRoleCandidates:shapeKeys.size,compositionProfiles:profiles.length,maxOccupiedBodies:maxBodies,maxRepresentativeOperations:maxOperations,gradingCounts,
  exactBooleanModels:family.summary.compatibleConfigurations,exactBooleanExitModels:family.summary.selectedRecordExitCertificates,diagramNodes:family.diagram.nodes.length,complete:true};
 const witness={node:witnessNode,grade:D,operationCount:witnessConstruction.word.length,recordCount:witnessPackets.length,occupiedBodies:witnessInspection.cells.length,counts:witnessInspection.counts};
 const cells=r.rules.geometry.cells.map(({owner,...c})=>({...c,owner:{kind:owner.kind,origin:owner.origin,inverted:owner.inverted}}));
 const familyJSON={schema:family.schema,complete:true,maxOrigin:D,variablePackets:family.variablePackets,diagram:{variables:family.diagram.variables,nodes:family.diagram.nodes,validRoot:family.validRoot,exitRoot:family.exitRoot},summary:family.summary,conflicts:family.conflicts,supports:family.supports,
  zeroGradeComponents:family.components.groups,condensationTopologicalOrder:family.components.topological,representation:family.representation,operationSchemas:family.universe.operations.map(i=>family.universe.rules.operations[i]),packets:family.universe.rules.packets,charts:family.universe.rules.charts};
 await writeFile(path.join(dir,'family.json'),JSON.stringify(familyJSON)+'\n');
 const gzip=createGzip({level:6}),writing=pipeline(gzip,createWriteStream(path.join(dir,'configurations.jsonl.gz'))),put=async row=>{if(!gzip.write(JSON.stringify(row)+'\n'))await once(gzip,'drain');};
 await put({type:'header',schema:r.schema,contract:r.contract,summary,witness,configurationColumns:['id','grade','parent','operation','selectedPackets'],edgeColumns:['from','to','operation'],sewing:'Local selected-record certificate only; no unasserted global state sewing.'});
 await put({type:'registry',root:r.rules.root,cells,points:Object.fromEntries(r.rules.geometry.points),charts:r.rules.charts,packets:r.rules.packets,operations:r.rules.operations,allowedOperations:r.universe.operations});
 for(const n of r.nodes)await put({type:'configuration',data:[n.id,n.grade,n.parent,n.operation,n.packets]});
 for(const e of r.edges)await put({type:'edge',data:[e.from,e.to,e.operation]});await put({type:'end',complete:true,configurations:r.nodes.length,edges:r.edges.length});gzip.end();await writing;
 let decodedNodes=0,decodedEdges=0,footer=false;const reader=createInterface({input:createReadStream(path.join(dir,'configurations.jsonl.gz')).pipe(createGunzip()),crlfDelay:Infinity});
 for await(const line of reader){const row=JSON.parse(line);if(row.type==='configuration')decodedNodes++;if(row.type==='edge')decodedEdges++;if(row.type==='end')footer=row.complete;}
 assert.equal(decodedNodes,r.nodes.length);assert.equal(decodedEdges,r.edges.length);assert.equal(footer,true);
 reports[D]={...summary,witness,archiveBytes:(await stat(path.join(dir,'configurations.jsonl.gz'))).size,archiveFooterChecked:true};
 cases[D]={maxOrigin:D,root:r.rules.root,summary,witness,profiles,nodes:records,cells,points:Object.fromEntries(r.rules.geometry.points),charts:r.rules.charts,packets:r.rules.packets,operations:r.rules.operations,allowedOperations:r.universe.operations,
  protocol:Object.fromEntries(windowProtocol.map(p=>[p.species,{window:p.window,continuation:p.continuation}]))};
 console.log(JSON.stringify({completedOrigin:D,...summary,witness}));
}
assert.deepEqual(await fingerprint(),hashes,'Inputs changed during phase enumeration');
const data={contract,cases},template=await readFile(path.join(root,own[5]),'utf8');assert.equal(template.split('__ORIGIN_JSON__').length,2);
await writeFile(path.join(out,'index.html'),template.replace('__ORIGIN_JSON__',JSON.stringify(data).replaceAll('<','\\u003c')));
const report={schema:'marici.nima.origin-budget-validation.v1',status:'pass-explicit-origin-budgets-and-alternative-preserving-closure',budgetKind:'realization-advances',complete:true,cases:reports,
 verification:{allExplicitStatesMatchExactBooleanFamily:true,allSelectedExitFlagsMatchIndependentBooleanFormula:true,allEdgesAndFanoutsChecked:edgeChecks,ownerAuditReplayedReadOnly:true,
  sourceOwnerOutputsModified:false,negativeControls,sewing:{nativeTransport:nativeSewing,repeatedCoefficientsDoNotIdentifyOccurrences:wrongOccurrence,allEqualInputCannotProveGenericSewing:wrongMap,ancestryDependentAssertionsRequireNewKey:true}},
 sourceHashes:hashes,scope:'Exact local reference-construction families for origins0/1/2. Operation count is unbounded. Global coupled-field sewing, physical clock/binding and the operator interpretation of8/10 remain unestablished.'};
assert.deepEqual(await fingerprint(),hashes);
await writeFile(path.join(out,'verification.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({status:report.status,cases:reports,edgesChecked:edgeChecks,negativeControls}));
