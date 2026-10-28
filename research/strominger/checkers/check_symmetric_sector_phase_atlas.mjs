// Exact finite source construction; does not modify any native phase rule.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {gzipSync,gunzipSync} from 'node:zlib';
import {fileURLToPath} from 'node:url';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {makeLatticeItem,itemKey} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {createWindowConstruction,windowProtocol} from '../demos/particle-overlap-tetrahedron/window-construction-model.mjs';
import {phaseFrame,phaseAdvanceWitness} from '../demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {auditPhaseCombination} from '../demos/particle-overlap-tetrahedron/phase-discipline-model.mjs';
import {transportCarrierCoefficients} from '../demos/particle-overlap-tetrahedron/deuterium-tunnel-model.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const out=path.join(root,'research/strominger/results/symmetric-sector-phase-atlas');
const contractPath='research/strominger/contracts/symmetric-sector-phase-atlas-v1.json';
const contract=JSON.parse(await fs.readFile(path.join(root,contractPath),'utf8'));
assert(contract.enumeration.includes('24'));
const sector=buildPESymmetricSector(3),pk=p=>p.join(','),mod2=n=>((n%2)+2)%2;
const family=p=>mod2(p[0]+p[2])?'C':'M';
const inside=p=>p.every((x,i)=>x>=sector.lower[i]&&x<=sector.upper[i]);
const permutations=xs=>xs.length?xs.flatMap((x,i)=>permutations(xs.filter((_,j)=>j!==i)).map(rest=>[x,...rest])):[[]];
const markings=permutations([0,1,2,3]),marks=windowProtocol[0].nodes;
const checkResults={};
const check=(name,condition)=>{assert(condition,name);checkResults[name]=true;};
const nativeItems=new Map(),primitiveByKey=new Map(),primitiveFaces=new Map(),vertices=new Map();
for(const host of sector.cells){
 const inverted=host.kind==='tetrahedron'&&host.role==='proton';
 const origin=host.vertices[0].map((_,i)=>host.kind==='octahedron'?Math.max(...host.vertices.map(q=>q[i]))-1:inverted?Math.max(...host.vertices.map(q=>q[i])):Math.min(...host.vertices.map(q=>q[i])));
 const native=makeLatticeItem(host.kind,origin,inverted);assert.equal(native.key,itemKey(host.vertices));nativeItems.set(host.id,native);
 for(const [index,vs] of native.components.entries()){
  const key=itemKey(vs);assert(!primitiveByKey.has(key));
  const record={id:host.id+'/primitive-'+index,key,host:host.id,vertices:vs,geometricRole:host.role};primitiveByKey.set(key,record);
  vs.forEach(q=>vertices.set(pk(q),q));
  for(let missing=0;missing<4;missing++){const f=vs.filter((_,i)=>i!==missing),fk=itemKey(f);if(!primitiveFaces.has(fk))primitiveFaces.set(fk,[]);primitiveFaces.get(fk).push(record.id);}
 }
}
check('native_whole_cell_decomposition_is_exact',nativeItems.size===679&&primitiveByKey.size===1372);
check('all_primitive_faces_are_manifold',[...primitiveFaces.values()].every(owners=>owners.length<=2));
check('candidate_family_field_is_MMCC_on_every_primitive',[...primitiveByKey.values()].every(p=>p.vertices.filter(q=>family(q)==='M').length===2));
const canonical=makeLatticeItem('tetrahedron',[0,0,0,0]);
const rootBindings=Object.fromEntries(marks.map((m,i)=>[m,canonical.vertices[i]]));
check('candidate_retains_canonical_root_families',Object.entries(rootBindings).every(([mark,q])=>family(q)===mark[0]));
// Constraint propagation is independent of the parity formula. Unforced
// values remain unassigned; each inference retains its known antecedents.
const forced=new Map(Object.entries(rootBindings).map(([mark,q])=>[pk(q),mark[0]])),inferences=[];
let changed=true;
while(changed){changed=false;for(const p of primitiveByKey.values()){
 const known=p.vertices.filter(q=>forced.has(pk(q))).map(q=>({vertex:pk(q),family:forced.get(pk(q))})),unknown=p.vertices.filter(q=>!forced.has(pk(q)));
 const m=known.filter(x=>x.family==='M').length;
 assert(m<=2&&m+unknown.length>=2);
 const value=m===2?'C':m+unknown.length===2?'M':null;
 if(value)for(const q of unknown){forced.set(pk(q),value);inferences.push({vertex:pk(q),family:value,primitive:p.id,known});changed=true;}
}}
check('forced_family_values_agree_with_independent_candidate',[...forced].every(([v,f])=>family(vertices.get(v))===f));
check('canonical_root_MMCC_constraints_force_all_vertex_families',forced.size===vertices.size);
const counts={attempted:0,failed:0,occupiedOutside:0,contextOutside:0,internal:0,globalFamilySeedMarkings:0,globalFamilyInternal:0};
const failureExamples={},packets=[],allCoverage=new Map(),familyCoverage=new Map();
const cover=(map,key,species)=>{if(!map.has(key))map.set(key,new Set());map.get(key).add(species);};
const identity=[0,1,2,3,4];let nativeEdgeAudits=0,wrappedPoints=0;
function wrap2(q){
 const U=q[0]+q[1]-1,V=q[0]+q[2]-1,W=q[0]+q[3];
 const e=(7-Math.abs(U)-Math.abs(V)+W)/2,f=(7-Math.abs(U)-Math.abs(V)-W)/2;
 return [e+2*Math.max(U,0),e+2*Math.max(-U,0),f+2*Math.max(V,0),f+2*Math.max(-V,0)].map(b=>4-b);
}
function unwrap2(y){
 const b=y.map(x=>4-x),u=(b[0]-b[1])/2,v=(b[2]-b[3])/2,w=Math.min(b[0],b[1])-Math.min(b[2],b[3]);
 const axes=[[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]],c2=[1,1,1,-1];
 return c2.map((c,i)=>(c+u*axes[0][i]+v*axes[1][i]+w*axes[2][i])/2);
}
for(const host of sector.cells.filter(c=>c.kind==='tetrahedron'))for(const permutation of markings){
 counts.attempted++;
 const seed=nativeItems.get(host.id),bindings=Object.fromEntries(marks.map((m,i)=>[m,seed.vertices[permutation[i]]]));
 const familySeed=Object.entries(bindings).every(([m,q])=>family(q)===m[0]);if(familySeed)counts.globalFamilySeedMarkings++;
 const id=host.id+'/mark-'+permutation.join(''),model=createWindowConstruction({seed,bindings,identity:{id}});
 let snapshot=model.snapshot();for(let step=0;step<2&&snapshot.status==='ready';step++)snapshot=model.step();
 if(snapshot.status!=='complete'){
  counts.failed++;failureExamples.failed??={id,status:snapshot.status,reason:snapshot.reason};continue;
 }
 const physicalInside=snapshot.items.every(item=>primitiveByKey.has(item.key));
 const allContextInside=Object.values(snapshot.bindings).every(inside);
 if(!physicalInside){counts.occupiedOutside++;failureExamples.occupiedOutside??={id,items:snapshot.items.map(i=>({species:i.species,key:i.key})),bindings:snapshot.bindings};continue;}
 if(!allContextInside){counts.contextOutside++;failureExamples.contextOutside??={id,bindings:snapshot.bindings};continue;}
 counts.internal++;
 const aliases=Object.fromEntries(Object.entries(snapshot.bindings).map(([m,q])=>[m,id+'/vertex/'+pk(q)]));
 const frames=snapshot.items.map((item,i)=>phaseFrame({id:id+'/chart-'+i,species:item.species,aliases},0));
 const eventRows=[];
 for(let i=0;i<2;i++){
  const from=frames[i],to=frames[i+1],kind=i===0?'PN':'NE';
  assert.equal(auditPhaseCombination([from,to],[{from:from.id,to:to.id,kind,identification:'same-occurrence',vertices:to.window.map(o=>o.vertex)}]).status,'native-phase-compatible');nativeEdgeAudits++;
  const permutation=transportCarrierCoefficients(identity.map(i=>[i,0]),snapshot.events[i]).map(z=>z[0]);
  assert.deepEqual([...permutation].sort(),identity);eventRows.push({kind,permutation,event:snapshot.events[i]});
 }
 const familyCompatible=Object.entries(snapshot.bindings).every(([m,q])=>family(q)===m[0]);
 if(familySeed)assert(familyCompatible);
 if(familyCompatible)counts.globalFamilyInternal++;
 const wrappedBindings2=Object.fromEntries(Object.entries(snapshot.bindings).map(([mark,q])=>{const y=wrap2(q);assert(y.every(Number.isInteger)&&y.reduce((a,b)=>a+b,0)===2&&y.every(x=>x<=4));assert.deepEqual(unwrap2(y),q);wrappedPoints++;return [mark,y];}));
 const items=snapshot.items.map(item=>{cover(allCoverage,item.key,item.species);if(familyCompatible)cover(familyCoverage,item.key,item.species);return {species:item.species,primitiveId:primitiveByKey.get(item.key).id,key:item.key,host:primitiveByKey.get(item.key).host};});
 packets.push({id,seed:host.id,marking:permutation,origin:0,occurrenceNamespace:id,bindings:snapshot.bindings,wrappedBindings2,items,frames,events:eventRows,history:snapshot.history,familyCompatible});
}
check('all_448_regular_seeds_and_24_markings_executed',counts.attempted===448*24);
check('construction_dispositions_partition_attempts',counts.failed+counts.occupiedOutside+counts.contextOutside+counts.internal===counts.attempted);
check('four_candidate_family_markings_per_regular_seed',counts.globalFamilySeedMarkings===448*4);
check('every_internal_packet_has_actual_phase_witnesses',nativeEdgeAudits===2*counts.internal);
check('every_internal_binding_has_exact_wrapped_inverse',wrappedPoints===6*counts.internal);
check('candidate_family_transport_is_checked_not_assumed',counts.globalFamilyInternal>0);
const coverage=map=>{
 const hosts=new Set([...map.keys()].map(k=>primitiveByKey.get(k).host));
 const fullHosts=sector.cells.filter(h=>nativeItems.get(h.id).components.every(vs=>map.has(itemKey(vs)))).map(h=>h.id);
 return {primitiveCarriers:map.size,touchedHosts:hosts.size,fullyCoveredHosts:fullHosts.length,missingHosts:sector.cells.filter(h=>!hosts.has(h.id)).map(h=>h.id),partiallyCoveredHosts:[...hosts].filter(id=>!fullHosts.includes(id)),missingPrimitives:[...primitiveByKey].filter(([k])=>!map.has(k)).map(([,p])=>p.id),roleMultiplicityHistogram:Object.fromEntries([...map.values()].reduce((acc,set)=>{const key=[...set].sort().join('+');acc.set(key,(acc.get(key)??0)+1);return acc;},new Map()))};
};
const all=coverage(allCoverage),global=coverage(familyCoverage);
// No simultaneous global occurrence identification is implied by an atlas.
const collisions=new Map();let mixedFamilyExample=null;
for(const p of packets)for(const [mark,q] of Object.entries(p.bindings)){
 const k=pk(q);if(!collisions.has(k))collisions.set(k,{});const seen=collisions.get(k);
 if(!seen[mark[0]])seen[mark[0]]={packet:p.id,mark};
 if(seen.C&&seen.M&&!mixedFamilyExample)mixedFamilyExample={vertex:k,C:seen.C,M:seen.M};
}
check('independent_packet_family_collision_is_retained',mixedFamilyExample!==null);
check('candidate_family_atlas_does_not_silently_cover_every_host',global.touchedHosts<sector.cells.length);
const inaccessible=sector.cells.filter(h=>h.kind==='octahedron'&&nativeItems.get(h.id).faces.every(f=>f.filter(q=>family(q)==='M').length!==2));
check('candidate_family_has_octahedra_without_any_PN_boundary_face',inaccessible.length>0);
check('PN_boundary_inaccessible_hosts_are_absent_from_candidate_atlas',inaccessible.every(h=>global.missingHosts.includes(h.id)));
// The MMCC/PN argument is independent of the parity candidate.
const rootPrimitive=primitiveByKey.get(canonical.key),denseWitnesses=[];
for(const permutation of markings){
 const labels=new Map(marks.map((m,i)=>[pk(canonical.vertices[permutation[i]]),m[0]]));
 const faces=canonical.faces.map(f=>({vertices:f,M:f.filter(q=>labels.get(pk(q))==='M').length,owners:primitiveFaces.get(itemKey(f))}));
 assert(faces.every(f=>f.owners.length===2));
 const allowed=faces.filter(f=>f.M===windowProtocol[1].window.filter(m=>m[0]==='M').length),blocked=faces.filter(f=>!allowed.includes(f));
 assert.equal(allowed.length,2);assert.equal(blocked.length,2);
 denseWitnesses.push({marking:permutation,allowedPNFaces:allowed,blockedOccupiedFaces:blocked});
}
check('every_root_marking_blocks_two_fully_occupied_faces',denseWitnesses.length===24);
check('no_missing_boundary_neighbor_used_to_fake_dense_obstruction',denseWitnesses.every(w=>w.blockedOccupiedFaces.every(f=>f.owners.includes(rootPrimitive.id)&&f.owners.length===2)));
const forcedBlocked=inaccessible.filter(h=>h.vertices.every(q=>forced.has(pk(q))));
check('canonical_root_constraints_force_at_least_one_PN_inaccessible_host',forcedBlocked.length>0);
const rootFaces=new Set(canonical.faces.map(itemKey));
const proofHost=forcedBlocked.find(h=>nativeItems.get(h.id).faces.some(f=>rootFaces.has(itemKey(f))));assert(proofHost);
// Finite reference-chart graph. An edge means an actual source command, not
// simultaneous occupation of every carrier visited by a path.
const charts=[],edges=[],adj=[];
for(const [packetIndex,p] of packets.entries())for(const [stage,item] of p.items.entries()){
 const id=charts.length;
 charts.push({id:p.id+'/chart-'+stage,cell:item.key,species:item.species,aliases:Object.fromEntries(Object.entries(p.bindings).map(([m,q])=>[m,'vertex/'+pk(q)])),packetIndex,stage});adj.push([]);
}
function add(from,to,kind,phaseDelta,permutation){const id=edges.length;edges.push({from,to,kind,phaseDelta,permutation});adj[from].push(id);}
for(const [i,p] of packets.entries()){add(3*i,3*i+1,'PN',0,p.events[0].permutation);add(3*i+1,3*i,'inverse-PN',0,p.events[0].permutation);add(3*i+1,3*i+2,'NE',0,p.events[1].permutation);}
const protonIndex=new Map(),neutronIndex=new Map();
const tupleKey=xs=>JSON.stringify(xs);
for(const [i,c] of charts.entries()){
 if(c.species==='proton'){const key=tupleKey(['C0','M0','C1','M1'].map(m=>c.aliases[m]));if(!protonIndex.has(key))protonIndex.set(key,[]);protonIndex.get(key).push(i);}
 if(c.species==='neutron'){const key=tupleKey(['M0','C1','C2'].map(m=>c.aliases[m]));if(!neutronIndex.has(key))neutronIndex.set(key,[]);neutronIndex.get(key).push(i);}
}
let failedReaderCandidates=0;
for(const [i,c] of charts.entries()){
 let candidates=[];
 if(c.species==='proton')candidates=protonIndex.get(tupleKey(['C1','M1','C0','M0'].map(m=>c.aliases[m])))??[];
 if(c.species==='neutron')candidates=neutronIndex.get(tupleKey(['M1','C2','C1'].map(m=>c.aliases[m])))??[];
 for(const j of candidates){
  const d=charts[j],sameBody=c.cell===d.cell,nextBody=c.species==='neutron'&&d.cell===packets[c.packetIndex].items[2].key;
  if(!sameBody&&!nextBody)continue;
  let witness;try{witness=phaseAdvanceWitness(c,d,0);}catch{failedReaderCandidates++;continue;}
  if(!sameBody){const a=primitiveByKey.get(c.cell).vertices,b=new Set(primitiveByKey.get(d.cell).vertices.map(pk));assert.equal(a.filter(q=>b.has(pk(q))).length,3);}
  add(i,j,sameBody?'reader-phase-advance':'NN-phase-advance',1,witness.permutation);
 }
}
check('every_added_reader_edge_uses_actual_source_witness',edges.some(e=>e.kind==='reader-phase-advance')&&edges.some(e=>e.kind==='NN-phase-advance'));
check('candidate_family_is_preserved_by_all_admitted_edges',edges.every(e=>!packets[charts[e.from].packetIndex].familyCompatible||packets[charts[e.to].packetIndex].familyCompatible));
const rootPacket=packets.findIndex(p=>p.seed==='electron:0,0,0,0'&&p.marking.join('')==='0123');assert(rootPacket>=0);
const entry=3*rootPacket,queue=[entry],states=new Map([[entry,{chart:entry,origin:0,permutation:[...identity],parent:null,edge:null}]]);
for(let at=0;at<queue.length;at++)for(const edgeId of adj[queue[at]]){
 const edge=edges[edgeId],a=states.get(edge.from);
 if(states.has(edge.to))continue;
 if(edge.phaseDelta)assert.deepEqual(phaseAdvanceWitness(charts[edge.from],charts[edge.to],a.origin).permutation,edge.permutation);
 states.set(edge.to,{chart:edge.to,origin:a.origin+edge.phaseDelta,permutation:edge.permutation.map(i=>a.permutation[i]),parent:edge.from,edge:edgeId});queue.push(edge.to);
}
const rootCoverage=new Map();for(const i of queue)cover(rootCoverage,charts[i].cell,charts[i].species);
const rootReport=coverage(rootCoverage);
check('all_reachable_charts_retain_the_root_family_field',queue.every(i=>packets[charts[i].packetIndex].familyCompatible));
check('root_lift_is_not_reported_as_whole_sector_coverage',rootReport.touchedHosts<679);
for(const state of states.values())if(state.parent!==null){const p=states.get(state.parent),e=edges[state.edge];assert(e.from===p.chart&&e.to===state.chart&&state.origin===p.origin+e.phaseDelta);assert.deepEqual(state.permutation,e.permutation.map(i=>p.permutation[i]));}
check('representative_paths_retain_origins_coefficients_and_history',states.size>1);
const loopEdge=edges.find(e=>states.has(e.from)&&e.kind==='reader-phase-advance'&&edges.some(f=>f.from===e.to&&f.to===e.from&&f.kind===e.kind));assert(loopEdge);
const back=edges.find(f=>f.from===loopEdge.to&&f.to===loopEdge.from&&f.kind===loopEdge.kind),returned=back.permutation.map(i=>loopEdge.permutation[i]);
check('two_forward_reader_steps_are_not_identity_realizations',JSON.stringify(returned)===JSON.stringify(identity)&&loopEdge.phaseDelta+back.phaseDelta===2);
const planeOf=p=>p.bindings.M0[0]+p.bindings.M0[2];
check('all_candidate_family_M_references_share_one_plane',packets.filter(p=>p.familyCompatible).every(p=>['M0','M1','M2'].every(m=>p.bindings[m][0]+p.bindings[m][2]===planeOf(p))));
check('every_native_edge_preserves_the_candidate_M_plane',edges.every(e=>!packets[charts[e.from].packetIndex].familyCompatible||planeOf(packets[charts[e.from].packetIndex])===planeOf(packets[charts[e.to].packetIndex])));
const planeCoverages=new Map();for(const p of packets.filter(p=>p.familyCompatible)){const h=planeOf(p);if(!planeCoverages.has(h))planeCoverages.set(h,new Map());for(const item of p.items)cover(planeCoverages.get(h),item.key,item.species);}
const D=q=>q.map((x,i)=>2*sector.centre[i]-x),packetLookup=new Map(packets.map((p,i)=>[tupleKey(marks.map(m=>p.bindings[m])),i]));
const dualPackets=packets.map(p=>packetLookup.get(tupleKey(marks.map(m=>D(p.bindings[m])))));
check('geometric_dual_has_an_actual_native_packet_everywhere',dualPackets.every(i=>Number.isInteger(i)));
for(const [i,p] of packets.entries()){
 const d=packets[dualPackets[i]];assert.equal(dualPackets[dualPackets[i]],i);
 for(const [mark,q] of Object.entries(p.bindings)){
  assert.deepEqual(d.bindings[mark],D(q));
  assert.deepEqual(d.wrappedBindings2[mark],wrap2(D(unwrap2(p.wrappedBindings2[mark]))));
 }
 assert.deepEqual(d.history,p.history);
 for(let stage=0;stage<3;stage++){
  assert.equal(d.items[stage].species,p.items[stage].species);
  assert.equal(d.items[stage].key,itemKey(primitiveByKey.get(p.items[stage].key).vertices.map(D)));
 }
 for(let stage=0;stage<2;stage++){
  assert.deepEqual(d.events[stage].permutation,p.events[stage].permutation);
  assert.deepEqual(d.events[stage].event.face,p.events[stage].event.face.map(D));
  assert.deepEqual(d.events[stage].event.newContext.coordinate,D(p.events[stage].event.newContext.coordinate));
  assert.deepEqual(d.events[stage].event.modeAfter,p.events[stage].event.modeAfter);
 }
}
check('dual_packet_preserves_species_all_contexts_and_source_commands',true);
const edgeKey=e=>tupleKey([e.from,e.to,e.kind,e.phaseDelta,e.permutation]),edgeLookup=new Map(edges.map((e,i)=>[edgeKey(e),i]));assert.equal(edgeLookup.size,edges.length);
const dualChart=i=>3*dualPackets[Math.floor(i/3)]+i%3;
const dualEdges=edges.map(e=>edgeLookup.get(edgeKey({...e,from:dualChart(e.from),to:dualChart(e.to)})));
check('dual_is_equivariant_on_every_native_operation_edge',dualEdges.every(i=>Number.isInteger(i)));
check('dual_history_transport_is_involutive_without_reset',dualEdges.every((d,i)=>dualEdges[d]===i));
check('dual_maps_M_plane_h_to_two_minus_h',packets.filter(p=>p.familyCompatible).every(p=>{const d=packets[dualPackets[packetLookup.get(tupleKey(marks.map(m=>p.bindings[m])))]];return d.familyCompatible&&planeOf(d)===2-planeOf(p);}));
check('dual_root_component_is_not_a_native_reachable_component',!states.has(dualChart(entry)));
const dualRootCoverage=new Map();for(const i of queue){const d=charts[dualChart(i)];cover(dualRootCoverage,d.cell,d.species);}
const atlasGraph={charts,edges,entry,dualPackets,dualEdges,representativeLiftStates:[...states.values()],scope:'Finite base atlas with symbolic unbounded origin/history lift. One representative per base chart is for reachability only, not an identification of distinct paths or a simultaneous occupied assembly.'};
const report={status:'sector-reader-atlas-built-global-amalgamation-not-admitted',checks:checkResults,source:{wholeCells:sector.cells.length,primitiveCells:primitiveByKey.size,vertices:vertices.size},enumeration:counts,nativeEdgeAudits,wrappedReferencePoints:wrappedPoints,independentPacketAtlas:all,candidateFamilyAtlas:global,familyPropagation:{rootBindings,forcedVertices:forced.size,totalVertices:vertices.size,uniquelyForcedEveryVertex:forced.size===vertices.size},readerGraph:{charts:charts.length,edges:edges.length,edgeKinds:edges.reduce((a,e)=>(a[e.kind]=(a[e.kind]??0)+1,a),{}),failedReaderCandidates,reachableBaseCharts:states.size,maximumRepresentativeOrigin:Math.max(...[...states.values()].map(s=>s.origin)),rootCoverage:rootReport,MPlaneInvariant:{rootPlane:planeOf(packets[rootPacket]),planes:[...planeCoverages].sort((a,b)=>a[0]-b[0]).map(([plane,map])=>{const c=coverage(map);return {plane,primitiveCarriers:c.primitiveCarriers,touchedHosts:c.touchedHosts};})},duality:{packetsCompared:dualPackets.length,edgeComparisons:dualEdges.length,physicalSpeciesExchanged:false,geometricRoleExchange:true,dualRootChart:dualChart(entry),dualRootPlane:planeOf(packets[dualPackets[rootPacket]]),dualRootCoverage:coverage(dualRootCoverage)},twoReaderStepControl:{from:loopEdge.from,via:loopEdge.to,coefficientReturn:returned,originIncrement:2}},obstructions:{incompatibleFamilyExample:mixedFamilyExample,PNInaccessibleOctahedra:inaccessible.length,rootForcedPNInaccessibleHosts:forcedBlocked.map(h=>h.id),rootForcedExample:{host:proofHost.id,vertices:proofHost.vertices,forcedFamilies:proofHost.vertices.map(q=>forced.get(pk(q)))},denseOccupancy:'All24 MMCC root markings have2 PN-compatible and2 incompatible occupied faces; root has4 actual neighbors.'},scope:contract.scope+' Independent packet atlas is not a simultaneous physical assembly. Candidate family field is not an absolute phase index or a derived unique physical marking.'};
await fs.mkdir(out,{recursive:true});
report.archives={};
for(const [name,records] of [['retained-packets',packets],['reader-graph',atlasGraph]]){
 const text=JSON.stringify(records)+'\n',archive=gzipSync(text);
 check(name+'_archive_is_lossless',gunzipSync(archive).toString('utf8')===text);
 await fs.writeFile(path.join(out,name+'.json.gz'),archive);
 report.archives[name]={path:name+'.json.gz',uncompressedBytes:Buffer.byteLength(text),compressedBytes:archive.length,uncompressedSha256:createHash('sha256').update(text).digest('hex')};
}
await fs.writeFile(path.join(out,'family-propagation.json'),JSON.stringify({rootBindings,inferences},null,2)+'\n');
await fs.writeFile(path.join(out,'dense-occupancy-hostiles.json'),JSON.stringify(denseWitnesses,null,2)+'\n');
const digest=x=>createHash('sha256').update(JSON.stringify(x)).digest('hex');
const leftEdges=edges.map(e=>({...e,from:dualChart(e.from),to:dualChart(e.to)})),rightEdges=dualEdges.map(i=>edges[i]);
assert.deepEqual(leftEdges,rightEdges);
const diagram={id:'symmetric-sector-native-duality',objects:[{id:'native-edge-requests'},{id:'dual-edge-packets'},{id:'retained-command-identities'}],arrows:[{id:'native-then-dual',source:'native-edge-requests',target:'dual-edge-packets',map_token:digest(leftEdges)},{id:'dual-then-native',source:'native-edge-requests',target:'dual-edge-packets',map_token:digest(rightEdges)},{id:'dual-twice',source:'retained-command-identities',target:'retained-command-identities',map_token:digest(dualEdges.map(i=>dualEdges[i]))},{id:'retained-identity',source:'retained-command-identities',target:'retained-command-identities',map_token:digest(edges.map((_,i)=>i))}],cells:[{id:'all42016-native-edge-duality-squares',routes:[['native-then-dual'],['dual-then-native']]},{id:'dual-history-word-involution',routes:[['dual-twice'],['retained-identity']]}],obstructions:[],claims:[{id:'joint-whole-sector-assembly',requires:['compatible-occupation-selection','all-occupied-contact-witnesses','active-interplane-handoff']}],available_witnesses:['complete-local-packet-atlas','five-slot-reference-duality','native-command-graph'],higher_coherence:[{id:'joint-whole-sector-assembly','degree':2,state:'unsupported'}],scope:'Finite evaluated reference-duality laws. Hashes come from independently formed edge packets. These cells do not promote symmetry into a native advance command or atlas coverage into occupied assembly.'};
await fs.writeFile(path.join(out,'duality-route-diagram.json'),JSON.stringify(diagram,null,2)+'\n');
report.sourceHashes={};for(const relative of [contractPath,'research/strominger/checkers/check_symmetric_sector_phase_atlas.mjs','research/strominger/pe-symmetric-sector.mjs',...['lattice-items.mjs','simplex-components.mjs','window-construction-model.mjs','phase-advance-model.mjs','phase-discipline-model.mjs'].map(n=>'research/strominger/demos/particle-overlap-tetrahedron/'+n)])report.sourceHashes[relative]=createHash('sha256').update(await fs.readFile(path.join(root,relative))).digest('hex');
await fs.writeFile(path.join(out,'verification.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report,null,2));
