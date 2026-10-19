// Exact reference-boundary response, not a regional quantum action or occupancy law.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {phaseUniverse} from '../demos/particle-overlap-tetrahedron/local-reference-universe.mjs';
import {POLICY,auditReferencePEAssembly} from './experimental_reference_pe.mjs';
import {compileTessellatedAtlas} from '../../nima/tessellated-atlas.mjs';
import {planExecution,replayExecution} from '../../nima/atlas-execution-plans.mjs';
const ROOT=new URL('../../../',import.meta.url),OUT=new URL('../results/cavity-reference-closure/',import.meta.url);
const MARKS=['C0','M0','C1','M1','C2'],sorted=xs=>[...xs].sort((a,b)=>a-b),same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const hash=b=>createHash('sha256').update(b).digest('hex'),sourceHashes={};
async function load(path){const b=await readFile(new URL(path,ROOT));sourceHashes[path]=hash(b);return JSON.parse(b);}
const protocol=await load('research/strominger/inputs/cavity-reference-closure-protocol-v1.json');
const geometryReceipt=await load('research/strominger/results/proton-witness-faces/verification.json');assert.equal(geometryReceipt.status,'pass');
const experiments=await load('research/strominger/results/isotope-obstruction-atlas/verification.json');assert.equal(experiments.status,'pass');
let prerequisiteHashesChecked=0;
for(const receipt of [geometryReceipt,experiments])for(const [path,digest] of Object.entries(receipt.sourceHashes)){
 assert.equal(hash(await readFile(new URL(path.replaceAll('\\','/'),ROOT))),digest,`stale prerequisite: ${path}`);prerequisiteHashesChecked++;
}
const cache=new Map();
async function source(isotope){
 if(cache.has(isotope))return cache.get(isotope);
 const base=`research/strominger/results/reference-${isotope}-search/`,summary=await load(base+'verification.json'),entry=summary.rows.find(r=>r.witnessFile);
 const w=(await load(base+entry.witnessFile)).witness,u=phaseUniverse({maxOrigin:entry.maxOrigin});assert(u.complete);
 for(const p of w.packets)assert.deepEqual(u.rules.packets[p.id],p);
 for(const o of w.operations)assert.deepEqual(u.rules.operations[o.id],o);
 const model=compileTessellatedAtlas({maxOrigin:entry.maxOrigin,mode:'experimental-terminal-PE'});
 for(const p of w.packets)assert.deepEqual(model.universe.rules.packets[p.id],p);
 const value={r:u.rules,w,model};cache.set(isotope,value);return value;
}
function linearResponse(r,boundary,interior,edges,faceObservations=[]){
 const nodes=[...boundary,...interior],index=new Map(nodes.map((p,i)=>[p,i])),parent=Array.from({length:5*nodes.length},(_,i)=>i);
 function find(a){while(parent[a]!==a){parent[a]=parent[parent[a]];a=parent[a];}return a;}
 function union(a,b){a=find(a);b=find(b);if(a!==b)parent[b]=a;}
 const variable=(p,i)=>5*index.get(p)+i;
 for(const op of edges)for(let i=0;i<5;i++)union(variable(op.target,i),variable(op.source,op.permutation[i]));
 const groups=new Map();
 for(const p of nodes)for(let i=0;i<5;i++){
  const key=find(variable(p,i));if(!groups.has(key))groups.set(key,[]);
  groups.get(key).push({packet:p,slot:i,rootCoordinate:r.packets[p].permutation[i],boundary:boundary.includes(p)});
 }
 const conflicts=[...groups.values()].filter(g=>new Set(g.map(x=>x.rootCoordinate)).size>1);
 const hidden=[...groups.values()].filter(g=>g.every(x=>!x.boundary));
 const relations=[],recoveries=[];let boundaryComponents=0;
 for(const g of groups.values()){
  const b=g.filter(x=>x.boundary);if(!b.length)continue;boundaryComponents++;
  for(const x of b.slice(1))relations.push({left:[x.packet,x.slot],right:[b[0].packet,b[0].slot]});
  for(const x of g.filter(x=>!x.boundary))recoveries.push({interior:[x.packet,x.slot],boundary:[b[0].packet,b[0].slot]});
 }
 const observedComponents=new Set(faceObservations.map(row=>find(variable(row.packet,row.slot))));
 const interiorComponents=[...groups].filter(([,g])=>g.some(x=>!x.boundary));
 const faceHidden=interiorComponents.filter(([key])=>!observedComponents.has(key)).map(([,g])=>g);
 return {boundaryComplexCoordinates:5*boundary.length,interiorComplexCoordinates:5*interior.length,
  independentInteriorModes:interiorComponents.length,faceObservationRankOnLocalRelation:observedComponents.size,
  interiorAmbiguityFromFaceShadows:faceHidden.length,faceHiddenComponents:faceHidden,
  independentFaceAmbiguityWitness:faceHidden.length?{nonzeroVariables:faceHidden[0].map(x=>[x.packet,x.slot]),value:1,domain:'formal independent boundary ports; not automatically a common-root source state'}:null,
  uniqueInteriorFromFaceBoundary:faceHidden.length===0,
  equationRank:5*nodes.length-groups.size,boundaryRelationRank:relations.length,boundarySolutionDimension:boundaryComponents,
  commonRootImageRank:boundary.length?5:0,extraBoundaryModesBeyondCommonRoot:boundaryComponents-(boundary.length?5:0),
  interiorAmbiguityDimension:hidden.length,uniqueInteriorFromFullBoundary:hidden.length===0,
  rootConsistency:conflicts.length===0,conflicts,hiddenComponents:hidden,relations,recoveries};
}
function observations(r,edges,interior,faces){
 const I=new Set(interior),seen=new Set(),rows=[],missing=[];
 for(const op of edges){
  if(I.has(op.source)===I.has(op.target))continue;
  const b=I.has(op.source)?op.target:op.source,chart=r.charts[r.packets[b].chart];
  for(const vertex of op.face){
   const slot=MARKS.findIndex(mark=>chart.aliases[mark]===vertex),key=`${b}:${vertex}`;
   if(seen.has(key))continue;seen.add(key);
   if(slot<0){missing.push({packet:b,vertex,reason:'no five-slot coefficient assigned to this geometric vertex'});continue;}
   rows.push({packet:b,slot,vertex,rootCoordinate:r.packets[b].permutation[slot],faceIndex:faces.findIndex(f=>same([...f].sort(),[...op.face].sort()))});
  }
 }
 const observed=sorted(new Set(rows.map(x=>x.rootCoordinate))),kernel=[0,1,2,3,4].filter(i=>!observed.includes(i));
 return {type:'coordinate shadows at actual native contact readers, not a sewn physical field',rows,missing,
         rank:observed.length,observedRootCoordinates:observed,kernelRootCoordinates:kernel,
         recovery:observed.map(i=>({rootCoordinate:i,observation:rows.findIndex(row=>row.rootCoordinate===i)}))};
}
function rowRank(rows){return new Set(rows.map(x=>x.rootCoordinate)).size;}
const results=[];let nitrogenAdapter=null;
for(const [isotope,label,body] of [
 ['n15','n15:delete:16',16],['n15','n15:delete:17',17],
 ['ne22','ne22:delete:16',16],['ne22','ne22:delete:29',29],['ne22','ne22:delete-pair:16,29',16]]){
 const {r,w,model}=await source(isotope),family=label.includes('pair')?'ne22-double':isotope+'-single';
 const trial=experiments.families[family].find(x=>x.label===label);assert(trial?.fullAuditPass);
 const S=new Set(trial.selectedPackets),chart=p=>r.charts[r.packets[p].chart],cell=p=>chart(p).cell;
 const description=r.describe([...S]);assert(description.valid&&!description.bodies.has(body));
 const geometry=r.geometry.cells[body],faces=geometry.faces,interior=w.selectedPackets.filter(p=>cell(p)===body);assert(interior.length);
 const neighboringCells=faces.map(f=>r.geometry.neighbor(body,f));
 const boundary=sorted([...S].filter(p=>neighboringCells.includes(cell(p))));
 const all=new Set([...boundary,...interior]),inside=new Set(interior);
 const edges=[...all].flatMap(p=>r.outgoing(p).map(i=>r.operations[i])).filter(op=>all.has(op.target)&&(inside.has(op.source)||inside.has(op.target)));
 for(const op of edges)r.validateTransfer(op);
 const facePorts=faces.map((face,i)=>({faceIndex:i,vertices:face,neighbor:neighboringCells[i],species:description.bodies.get(neighboringCells[i])??'vacant',
   nativeFactors:edges.filter(op=>op.face&&same([...op.face].sort(),[...face].sort())).map(op=>op.id)}));
 const shadow=observations(r,edges,interior,faces);
 const response=linearResponse(r,boundary,interior,edges,shadow.rows);assert(response.rootConsistency);
 assert(response.uniqueInteriorFromFullBoundary,'A retained source trace must anchor each interior reader component to boundary');
 const incident=new Set(edges.flatMap(op=>[op.source,op.target]));
 const activeBoundary=boundary.filter(p=>incident.has(p)),spectatorBoundary=boundary.filter(p=>!incident.has(p));
 const activeResponse=linearResponse(r,activeBoundary,interior,edges,shadow.rows);
 if(activeResponse.independentFaceAmbiguityWitness){
  const nonzero=new Set(activeResponse.independentFaceAmbiguityWitness.nonzeroVariables.map(([p,i])=>`${p}:${i}`));
  for(const op of edges)for(let i=0;i<5;i++)assert.equal(nonzero.has(`${op.target}:${i}`),nonzero.has(`${op.source}:${op.permutation[i]}`));
  assert(shadow.rows.every(row=>!nonzero.has(`${row.packet}:${row.slot}`)));
  assert(interior.some(p=>[0,1,2,3,4].some(i=>nonzero.has(`${p}:${i}`))));
 }
 const baseReader=r.packets[interior[0]],advance=[0,3,4,1,2],identity=[0,1,2,3,4];
 const interiorPairComparisons=interior.slice(1).map(id=>{
  const packet=r.packets[id],relative=packet.permutation.map(i=>baseReader.permutation.indexOf(i)),delta=packet.origin-baseReader.origin;
  return {from:baseReader.id,to:id,originDelta:delta,commonRootAdapter:relative,
          generatedByNativeSameBodyAdvance:same(relative,identity)||same(relative,advance),
          matchesOriginAdvance:delta>=0&&same(relative,delta%2?advance:identity),
          caution:'Derived from the shared root response, not thereby an admitted interior reader operation'};
 });
 let conditionalClosure=null;
 if(interior.length===2){
  if(nitrogenAdapter===null){assert.equal(label,'n15:delete:17');nitrogenAdapter=[...interiorPairComparisons[0].commonRootAdapter];}
  const comparison={id:'declared-common-root-comparison',kind:'conditional-reference-comparison',source:interior[0],target:interior[1],
                    phaseDelta:r.packets[interior[1]].origin-r.packets[interior[0]].origin,permutation:[...nitrogenAdapter],face:null};
  const responseWithComparison=linearResponse(r,activeBoundary,interior,[...edges,comparison],shadow.rows);
  assert(responseWithComparison.rootConsistency&&responseWithComparison.uniqueInteriorFromFaceBoundary);
  assert.throws(()=>r.validateTransfer({...comparison,kind:'reader-phase-advance'}),'The comparison must not be silently registered as a native advance');
  conditionalClosure={comparison,extractedFrom:'n15:delete:17',response:responseWithComparison,nativeAdvanceRejected:true,
   scope:'Explicit shared-root comparison retained as conditional boundary data, not a new native move or an occupancy permission'};
 }
 // Verify the shadow's exact left inverse on every observable common-root basis coordinate.
 for(const recovery of shadow.recovery)assert.equal(shadow.rows[recovery.observation].rootCoordinate,recovery.rootCoordinate);
 // Removing all observations of one coordinate exposes that coordinate as a kernel direction.
 assert(shadow.rank>0);const removed=shadow.observedRootCoordinates[0],restricted=shadow.rows.filter(row=>row.rootCoordinate!==removed);
 assert.equal(rowRank(restricted),shadow.rank-1);
 // A wrong actual transport cannot remain consistent with the saved common-root response.
 const corrupt=structuredClone(edges),first=corrupt.find(op=>inside.has(op.source)!==inside.has(op.target));assert(first);
 [first.permutation[0],first.permutation[1]]=[first.permutation[1],first.permutation[0]];
 assert(!linearResponse(r,boundary,interior,corrupt).rootConsistency);
 const before=auditReferencePEAssembly(r,[...S],{policy:POLICY,expectedCounts:trial.counts});assert(before.experimentalPass&&!before.nativePass);
 const restored=sorted(new Set([...S,...interior])),afterCounts=r.inspect(restored).counts;
 const after=auditReferencePEAssembly(r,restored,{policy:POLICY,expectedCounts:afterCounts});assert(after.experimentalPass);
 const plan=planExecution(model,[...S],restored,{maxStates:100000,maxMilliseconds:10000});assert.equal(plan.status,'planned');
 const replay=replayExecution(model,plan),single=planExecution(model,[...S],restored,{maxStates:100000,maxMilliseconds:10000,allowMaterialization:false});
 const geometric=geometryReceipt.rows.find(row=>row.name===label);assert(geometric);
 const cavity=geometric.cavityComponents.find(c=>c.cells.includes(body))??null;
 const shortcutFactors=before.witnesses.filter(x=>x.referenceNeutronCell===body).map(x=>({source:x.source,target:x.target,referencePacket:x.nativeWord[0].target,factors:x.nativeFactors,permutation:x.permutation}));
 const strictFaceCriterion=facePorts.every(f=>f.nativeFactors.length>0)&&shadow.missing.length===0&&shadow.rank===5;
 const refFaceCriterion=facePorts.every(f=>f.species!=='vacant'&&f.nativeFactors.length>0)&&response.uniqueInteriorFromFullBoundary&&response.rootConsistency;
 results.push({label,deletedBody:body,counts:trial.counts,cavity:cavity!==null,cavityCertificate:cavity,
  boundaryReaders:boundary.map(p=>({packet:r.packets[p],chart:chart(p)})),interiorReaders:interior.map(p=>({packet:r.packets[p],chart:chart(p)})),facePorts,
  nativeFactors:edges,response,activeBoundaryReaders:activeBoundary,spectatorBoundaryReaders:spectatorBoundary,
  activeResponse,interiorPairComparisons,conditionalClosure,faceShadow:shadow,strictFaceCriterion,reconstructibleFourFaceReference:refFaceCriterion,
  noNativeVacancyAdmission:!before.nativePass,experimentalVacancyAdmission:before.experimentalPass,activeReferenceShortcuts:shortcutFactors,
  restoration:{counts:afterCounts,nativePass:after.nativePass,experimentalPass:after.experimentalPass,replay,
   plan,singletonOnly:{status:single.status,reason:single.reason??null}},
  controls:{removedRootCoordinate:removed,reducedShadowRank:rowRank(restricted),corruptFactorDetected:true},
  physicalBoundaryAction:null,physicalNormalization:null});
}
for(const path of ['research/strominger/checkers/check_cavity_reference_closure.mjs','research/strominger/checkers/experimental_reference_pe.mjs','research/strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs','research/strominger/demos/particle-overlap-tetrahedron/deuterium-tunnel-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs','research/nima/tessellated-atlas.mjs','research/nima/atlas-execution-plans.mjs'])sourceHashes[path]=hash(await readFile(new URL(path,ROOT)));
const report={schema:'marici.cavity-reference-closure.v1',status:'pass',protocol,sourceHashes,prerequisiteHashesChecked,results,
 controls:['removed-coordinate-observations-expose-kernel','corrupt-factor-breaks-common-root-consistency','independent-face-null-directions-retained','conditional-comparison-rejected-as-native-advance'],
 disposition:'Exact reference reconstruction and occupancy admission are separately recorded. Face shadows are typed bookkeeping projections; no physical field sewing or regional quantum amplitude has been invented.'};
await mkdir(OUT,{recursive:true});await writeFile(new URL('verification.json',OUT),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:'pass',results:results.map(r=>({label:r.label,cavity:r.cavity,faceWitnesses:r.facePorts.map(f=>f.nativeFactors.length),faceShadowRank:r.faceShadow.rank,
 geometricShadowKernel:r.faceShadow.kernelRootCoordinates,strictFaceCriterion:r.strictFaceCriterion,uniqueFullBoundaryRecovery:r.response.uniqueInteriorFromFullBoundary,
 boundarySolutionDimension:r.response.boundarySolutionDimension,extraBoundaryModesBeyondCommonRoot:r.response.extraBoundaryModesBeyondCommonRoot,
 activeBoundaryDimension:r.activeResponse.boundarySolutionDimension,faceAmbiguityWithoutCommonRoot:r.activeResponse.interiorAmbiguityFromFaceShadows,
 interiorPairComparisons:r.interiorPairComparisons,
 restore:r.restoration.replay,singletonOnly:r.restoration.singletonOnly.status}))},null,2));
