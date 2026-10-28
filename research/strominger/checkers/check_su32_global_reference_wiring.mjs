// Complete fixed-carrier candidate BEFORE local verification. No native relay
// authority is inferred from this transparent-reference propagation policy.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSu32SignedReferenceAtlas,encodeSignedReferences} from '../su32-signed-reference-encoder.mjs';
const tracePath='research/strominger/results/su32-fixed-reading-trace-v1/verification.json';
const pairsPath='research/strominger/results/su32-six-pair-falsification-v1/verification.json';
const fixturePath='research/strominger/results/su32-hopf-tests-v1/fixture.json';
const load=async p=>JSON.parse(await fs.readFile(p,'utf8'));
const trace=await load(tracePath),pairs=await load(pairsPath),fixture=await load(fixturePath);
const hash=x=>createHash('sha256').update(x).digest('hex');
for(const doc of [trace,pairs,fixture])for(const [p,h] of Object.entries(doc.sourceHashes))assert.equal(hash(await fs.readFile(p)),h,`Stale input: ${p}`);
const copy=x=>structuredClone(x),labels=['P+','P-','E+','E-'];
const reading=fixture.readings.find(r=>r.id===trace.reading);
const cells=new Map(fixture.cells.map(c=>[c.id,c]));
const centre=[0,0,0,0];let count=0;
for(const c of fixture.cells)for(const v of c.vertices){for(let i=0;i<4;i++)centre[i]+=v[i];count++;}
for(let i=0;i<4;i++)centre[i]/=count;
const shape=vs=>vs.map(v=>v.join(',')).sort().join('|');
const byShape=new Map(fixture.cells.map(c=>[shape(c.vertices),c.id]));
const mirror=Object.fromEntries(fixture.cells.map(c=>[c.id,byShape.get(shape(c.vertices.map(v=>{
 const h=reading.axis.reduce((s,a,i)=>s+a*(v[i]-centre[i]),0)/2;
 return v.map((x,i)=>x-h*reading.axis[i]);
})))]));
for(const id of cells.keys()){assert(mirror[id]);assert.equal(mirror[mirror[id]],id);}
const atlas=buildSu32SignedReferenceAtlas(fixture);
const opposite=fixture.readings.find(r=>r.incomingN===trace.outgoingN);
const oppositeChart=atlas.charts.find(c=>c.reading===opposite.id&&c.source===opposite.incomingN);
const oppositeTemplate=encodeSignedReferences(atlas,oppositeChart.id,[0,0],Object.fromEntries(labels.map(k=>[k,null])));
const entryView={at:trace.incomingN,localToRecordId:Object.fromEntries(labels.map(k=>[k,k])),
 referenceCells:Object.fromEntries(trace.layer2.map(r=>[r.record,r.cell]))};
const exitView={at:trace.outgoingN,localToRecordId:{},referenceCells:{}};
for(const ref of trace.layer2){const local=oppositeTemplate.referenceBinding[mirror[ref.cell]];assert(local);
 exitView.localToRecordId[local]=ref.record;exitView.referenceCells[local]=mirror[ref.cell];}
assert.equal(new Set(Object.values(exitView.localToRecordId)).size,4);
for(const channel of oppositeTemplate.channels){
 const expected=trace.layer3.find(r=>mirror[r.cell]===channel.cell);assert(expected);
 assert.deepEqual([exitView.localToRecordId[channel.P.record],exitView.localToRecordId[channel.E.record]].sort(),[...expected.records].sort());
}
const facesBetween=(a,b)=>fixture.interfaces.filter(f=>f.ports.some(p=>p.split('@')[0]===a)&&f.ports.some(p=>p.split('@')[0]===b));
const faceBetween=(a,b)=>{const fs=facesBetween(a,b);assert.equal(fs.length,1,'A selected hop must be one actual shared face');return fs[0];};
function build(cover){
 const nodes=new Map();
 function node(cell,layer,records){
  assert(cells.has(cell));const data={cell,layer,records:[...new Set(records)].sort()};
  if(nodes.has(cell))assert.deepEqual(nodes.get(cell),data);else nodes.set(cell,data);
 }
 node(trace.incomingN,1,labels);
 for(const r of trace.layer2)node(r.cell,2,[r.record]);
 for(const r of trace.layer3)node(r.cell,3,r.records);
 for(const r of trace.layer4)node(r.cell,4,r.records);
 const prefixNodes=[...nodes.values()];
 for(const n of prefixNodes)node(mirror[n.cell],10-n.layer,n.records);
 const bridges=[];
 for(const r of cover.routes)for(const [source,target] of [[r.sourceP,r.targetE],[r.sourceE,r.targetP]]){
  // Never cross between the two disconnected cells of a paired-tip group.
  // Each lane must traverse ONE actual middle N occurrence on both faces.
  const matches=r.members.filter(m=>facesBetween(source,m).length&&facesBetween(m,target).length);
  assert.equal(matches.length,1,'Lane needs a unique actual middle occurrence');
  bridges.push({channel:r.channel,source,middle:matches[0],target,kind:'peripheral',records:copy(nodes.get(source).records)});
 }
 const central=trace.centralReconciliation.cell;
 for(const r of trace.layer4.filter(x=>x.kind==='shared-reference-join-candidate')){
  bridges.push({channel:central,source:r.cell,middle:central,target:mirror[r.cell],kind:'central-comparison-context',records:copy(r.records)});
 }
 for(const middle of new Set(bridges.map(b=>b.middle)))node(middle,5,bridges.filter(b=>b.middle===middle).flatMap(b=>b.records));
 // A grouped channel need not use both physical tip occurrences in a cover.
 // Retain unused middle cells explicitly, with NO invented records or hops.
 for(const cell of cells.values())if(!nodes.has(cell.id)){
  const midpoint=[0,1,2,3].map(i=>cell.vertices.reduce((s,v)=>s+v[i],0)/cell.vertices.length);
  const h=reading.axis.reduce((s,a,i)=>s+a*(midpoint[i]-centre[i]),0);
  assert(Math.abs(h)<1e-9);assert.equal(cell.role,'neutron');node(cell.id,5,[]);
 }
 const edges=[];
 function edge(from,to,records){
  const face=faceBetween(from,to);assert(!edges.some(e=>e.from===from&&e.to===to));
  edges.push({face:face.id,from,to,fromPort:from+'@'+face.id,toPort:to+'@'+face.id,records:[...records].sort()});
 }
 for(const r of trace.layer2)edge(trace.incomingN,r.cell,[r.record]);
 for(const r of trace.layer3)for(const ref of r.references)edge(ref,r.cell,nodes.get(ref).records);
 for(const r of trace.layer4)for(const input of r.inputCells)edge(input,r.cell,nodes.get(input).records);
 const prefix=copy(edges);
 for(const e of prefix)edge(mirror[e.to],mirror[e.from],e.records);
 for(const b of bridges){edge(b.source,b.middle,b.records);edge(b.middle,b.target,b.records);}
 return {kind:'su32-global-reference-wiring-candidate',cover:cover.index,entry:trace.incomingN,exit:trace.outgoingN,
  nodes:[...nodes.values()].sort((a,b)=>a.cell.localeCompare(b.cell)),edges,bridges,
  boundaryViews:{entry:copy(entryView),exit:copy(exitView)},
  channels:cover.routes.map(r=>({channel:r.channel,members:copy(r.members)})),
  retainedCentralComparisons:copy(trace.centralReconciliation),
  policy:'Opaque identity-preserving edge messages; repeated identities must agree; outgoing selections are fixed by the complete plan. Not native dynamics.'};
}
function reverse(plan){
 const out=copy(plan);[out.entry,out.exit]=[out.exit,out.entry];
 [out.boundaryViews.entry,out.boundaryViews.exit]=[out.boundaryViews.exit,out.boundaryViews.entry];
 out.nodes=out.nodes.map(n=>({...n,layer:10-n.layer}));
 out.edges=out.edges.map(e=>({...e,from:e.to,to:e.from,fromPort:e.toPort,toPort:e.fromPort}));
 out.bridges=out.bridges.map(b=>({...b,source:b.target,target:b.source}));
 // Preparation/derivation provenance is retained, not claimed to run backward.
 return out;
}
function validate(plan){
 const ns=new Map(plan.nodes.map(n=>[n.cell,n]));assert.equal(ns.size,51);
 assert.deepEqual([...ns.keys()].sort(),[...cells.keys()].sort());
 assert.equal(ns.get(plan.entry).layer,1);assert.equal(ns.get(plan.exit).layer,9);
 for(const [side,layer] of [['entry',2],['exit',8]]){
  const view=plan.boundaryViews[side];assert.equal(view.at,plan[side]);
  for(const local of labels){const n=ns.get(view.referenceCells[local]);assert.equal(n.layer,layer);
   assert.deepEqual(n.records,[view.localToRecordId[local]]);}
 }
 assert.equal(new Set(plan.edges.map(e=>e.face)).size,plan.edges.length);
 for(const bridge of plan.bridges)for(const [from,to] of [[bridge.source,bridge.middle],[bridge.middle,bridge.target]]){
  const hop=plan.edges.find(e=>e.from===from&&e.to===to);assert(hop,'Declared lane lost a face hop');
  assert.deepEqual(hop.records,bridge.records);
 }
 for(const e of plan.edges){
  assert.equal(ns.get(e.to).layer,ns.get(e.from).layer+1);
  assert.deepEqual([e.fromPort,e.toPort].sort(),[...faceBetween(e.from,e.to).ports].sort());
  assert.equal(e.face,faceBetween(e.from,e.to).id);
  assert(e.records.length>0);assert.equal(new Set(e.records).size,e.records.length);
  for(const k of e.records){assert(ns.get(e.from).records.includes(k));assert(ns.get(e.to).records.includes(k));}
 }
 for(const n of plan.nodes)for(const side of ['in','out']){
  if(side==='in'&&n.cell===plan.entry||side==='out'&&n.cell===plan.exit)continue;
  const incident=plan.edges.filter(e=>(side==='in'?e.to:e.from)===n.cell);
  assert.deepEqual([...new Set(incident.flatMap(e=>e.records))].sort(),n.records,'All assigned references must be supplied and retained');
 }
 assert.deepEqual(reverse(reverse(plan)),plan);
}
function execute(plan,input,fault=null){
 const states=new Map(),messages=[];
 const merge=(into,from)=>{for(const [k,v] of Object.entries(from)){if(Object.hasOwn(into,k))assert.deepEqual(into[k],v,'Repeated identity disagrees');else into[k]=copy(v);}};
 // Only the ENTRY receives the registry. Other nodes read incoming messages,
 // never an omniscient registry lookup or a cached desired output.
 for(const n of [...plan.nodes].sort((a,b)=>a.layer-b.layer)){
  const state={};if(n.cell===plan.entry)merge(state,input);
  for(const message of messages.filter(m=>m.to===n.cell))merge(state,message.records);
  assert.deepEqual(Object.keys(state).sort(),n.records);states.set(n.cell,state);
  for(const edge of plan.edges.filter(e=>e.from===n.cell)){
   const message={...copy(edge),records:Object.fromEntries(edge.records.map(k=>[k,copy(state[k])]))};
   if(fault&&edge.face===fault.face)message.records[fault.label]={corruptedAppearance:true};
   messages.push(message);
  }
 }
 return {output:states.get(plan.exit),states,messages};
}
// All four complete plans are fixed before any local or payload checks.
const plans=trace.middleAssignments.map(build);
// Enumerate COMPLETE pair-and-physical-location assignments before checking
// local availability. Two paired-tip groups give four location choices each.
const localizedCandidates=plans.flatMap(plan=>pairs.results.find(r=>r.cover===plan.cover).jointAssignments.flatMap(choice=>
 Array.from({length:2**plan.channels.filter(c=>c.members.length===2).length},(_,bits)=>{
  let index=0;
  return {cover:plan.cover,choice:copy(choice),placements:plan.channels.map((channel,i)=>({channel:channel.channel,
   pair:copy(pairs.pairs[choice[i]]),at:channel.members[channel.members.length===2?(bits>>index++)&1:0]}))};
 })));
const localizedSurvivors=[];
let executions=0,edgeMessageChecks=0;const outcomes=[];let witness;
for(const plan of plans){
 validate(plan);const reversed=reverse(plan);validate(reversed);
 const registries=[...Array.from({length:16},(_,bits)=>Object.fromEntries(labels.map((k,i)=>[k,{id:'input:'+k,value:(bits>>i)&1}]))),trace.registry];
 for(const registry of registries){
  const snapshot=copy(plan),forward=execute(plan,registry),back=execute(reversed,forward.output);
  assert.deepEqual(forward.output,registry);assert.deepEqual(back.output,registry);
  for(const n of plan.nodes)assert.deepEqual(forward.states.get(n.cell),back.states.get(n.cell));
  for(const message of [...forward.messages,...back.messages])for(const [k,v] of Object.entries(message.records)){assert.deepEqual(v,registry[k]);edgeMessageChecks++;}
  assert.deepEqual(plan,snapshot);executions+=2;
  if(!witness&&registry===trace.registry)witness={plan,forwardMessages:forward.messages,reverseMessages:back.messages};
 }
 const family=pairs.results.find(r=>r.cover===plan.cover);assert(family);
 const choices=family.jointAssignments.map(choice=>({choice,channels:plan.channels.map((channel,i)=>{
  const pair=pairs.pairs[choice[i]],members=channel.members.map(id=>plan.nodes.find(n=>n.cell===id));
  assert(pair.every(k=>members.some(n=>n.records.includes(k))));
  return {channel:channel.channel,pair,commonMembers:members.filter(n=>pair.every(k=>n.records.includes(k))).map(n=>n.cell)};
 })}));
 const localized=localizedCandidates.filter(c=>c.cover===plan.cover);
 const surviving=localized.filter(c=>c.placements.every(p=>p.pair.every(k=>plan.nodes.find(n=>n.cell===p.at).records.includes(k))));
 localizedSurvivors.push(...surviving);
 outcomes.push({cover:plan.cover,localizedAssignmentsTested:localized.length,localizedAssignmentsSurviving:surviving.length,
  nodes:plan.nodes.length,activeCells:plan.nodes.filter(n=>n.records.length).length,
  inactiveMiddleCells:plan.nodes.filter(n=>!n.records.length).map(n=>n.cell),selectedPhysicalFaces:plan.edges.length,
  peripheralLanes:plan.bridges.filter(b=>b.kind==='peripheral').length,centralContextLanes:plan.bridges.filter(b=>b.kind==='central-comparison-context').length,
  pairAssignments:choices.length,assignmentsWithEveryPairAtOneActualMiddleCell:choices.filter(c=>c.channels.every(ch=>ch.commonMembers.length)).length,
  nonColocatedPairWitness:choices.flatMap(c=>c.channels).find(ch=>ch.commonMembers.length===0)??null});
}
assert(localizedSurvivors.length>0);
 witness.selectedSixPairPlacement=copy(localizedSurvivors.find(c=>c.cover===witness.plan.cover));
let negativeControls=0;const reject=f=>{assert.throws(f);negativeControls++;};
const broken=copy(plans[0]);broken.edges.pop();reject(()=>validate(broken));
const falseFace=copy(plans[0]);falseFace.edges[0].toPort=falseFace.edges[0].fromPort;reject(()=>validate(falseFace));
const teleport=copy(plans[0]);const group=teleport.channels.find(c=>c.members.length===2);
const edge=teleport.edges.find(e=>e.to===group.members[0]);edge.to=group.members[1];edge.toPort=edge.to+'@'+edge.face;
reject(()=>validate(teleport));
reject(()=>execute(plans[0],{'P+':0,'P-':0,'E+':0}));
const comparison=trace.layer4.find(r=>r.kind==='shared-reference-join-candidate');
const operands=comparison.inputCells.map(id=>plans[0].nodes.find(n=>n.cell===id));
const shared=operands[0].records.find(k=>operands[1].records.includes(k));assert(shared);
const wire=plans[0].edges.find(e=>e.to===comparison.cell&&e.from===operands[0].cell);
assert.throws(()=>execute(plans[0],trace.registry,{face:wire.face,label:shared}),/Repeated identity disagrees/);negativeControls++;
const paths=[tracePath,pairsPath,fixturePath,'research/strominger/su32-signed-reference-encoder.mjs',
 'research/strominger/checkers/check_su32_global_reference_wiring.mjs'];
const sourceHashes={};for(const p of paths)sourceHashes[p]=hash(await fs.readFile(p));
const report={schema:'su32.global-reference-wiring-candidate.v1',passed:true,reading:trace.reading,binding:trace.binding,
 completePlans:plans.length,executions,edgeMessageChecks,negativeControls,outcomes,
 localizedAssignmentsTested:localizedCandidates.length,localizedSurvivors,witness,
 result:'Complete assignments retain all 51 cells, explicitly mark inactive middle occurrences, preserve opaque record identities across selected actual face paths, and support exact reversal of the retained plan.',
 addedPolicy:'Site messages may reference the same original record repeatedly. Matching copies are aliases, not fresh independent inputs. Full geometry/history remains in the retained plan; execution is a candidate classical information relay, not a native scattering law.',
 centralTreatment:'Four additional actual-face context lanes through the central N preserve the central comparison branches. Six peripheral grouped channels and all twelve peripheral lanes remain present.',
 scope:['The four covers are alternative complete assignments, not simultaneously selected physical wirings. Unused physical middle occurrences are retained with empty support, not silently removed or treated as active.',
  'Opposite-half record placement uses the fixed geometric reflection correspondence; that correspondence is an explicit candidate attachment policy.',
  'Whole-plan reversal is involutive and the candidate relay recovers input data. This is not reversal of native dynamics or original constructor history.',
  'Group-level availability of a selected pair does not imply both records are present at one actual N occurrence. Non-colocated pairs are reported, not joined across an invented interface.',
  'No rule for joint interaction between separated members of a paired-tip channel is supplied.',
  'No physical cloning, charge/amplitude meaning, native comparison witness, unique cover selection or native transport authority is inferred.'],
 nativeExecution:null,sourceHashes};
const dir='research/strominger/results/su32-global-reference-wiring-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,localizedSurvivors:localizedSurvivors.length,witness:undefined,sourceHashes:undefined},null,2));
