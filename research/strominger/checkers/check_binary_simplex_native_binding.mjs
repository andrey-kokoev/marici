// Source-bound follow-up to the LRRR frame candidate. This does NOT install a
// particle evolution rule. It distinguishes frame relabelling from native moves.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
import {applyPhasePermutation,phaseFrame,phaseAdvancePermutations} from '../demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex');
const candidatePath='research/strominger/results/binary-simplex-braid-v1.json';
const candidate=read(candidatePath),checks=[];
function check(name,fn){fn();checks.push(name);}
check('frame candidate receipt matches all its live sources',()=>{for(const [p,h] of Object.entries(candidate.sourceSha256))assert.equal(hash(p),h);});
const engine=new GenerativeAssemblyRules(),rootPacket=engine.packets[engine.root],rootChart=engine.charts[rootPacket.chart];
const names=['C0','M0','C1','M1'];
const targets={L:[...candidate.L,4],R:[...candidate.R,4]};
const payload=[[2,1],[3,-2],[5,3],[7,-4],[11,5]];
function context(chart){return {cell:chart.cell,species:chart.species,aliases:chart.aliases};}
const reframings={};
for(const label of ['L','R']){
 const p=targets[label],marking=Object.fromEntries(names.map((name,i)=>[name,rootChart.aliases[names[p[i]]]]));
 const reframed=new GenerativeAssemblyRules({seedBindings:marking}),chart=reframed.charts[reframed.packets[reframed.root].chart];
 reframings[label]={requestedFourMarkPermutation:p.slice(0,4),source:context(rootChart),target:context(chart),outsideContextPreserved:chart.aliases.C2===rootChart.aliases.C2,initialPacketIsNewlySeeded:true};
}
check('naive L extension fixing the fifth geometric context fails native P completion',()=>assert.equal(reframings.L.outsideContextPreserved,false));
check('R preserves this outside context but is not thereby an admitted operation',()=>assert.equal(reframings.R.outsideContextPreserved,true));
const outgoing=engine.outgoing(engine.root).map(i=>engine.operations[i]);
const firstMoves=outgoing.map(op=>({kind:op.kind,permutation:op.permutation,phaseDelta:op.phaseDelta,target:context(engine.charts[engine.packets[op.target].chart])}));
check('neither proposed frame reflection is a one-step native root operation',()=>{
 for(const p of Object.values(targets))assert.ok(!outgoing.some(op=>JSON.stringify(op.permutation)===JSON.stringify(p)));
});
const pn=outgoing.find(op=>op.kind==='PN');assert.ok(pn);
const ne=engine.outgoing(pn.target).map(i=>engine.operations[i]).find(op=>op.kind==='NE');assert.ok(ne);
const pValue=payload,nValue=applyPhasePermutation(pValue,pn.permutation),eValue=applyPhasePermutation(nValue,ne.permutation);
check('actual PN then NE keeps full coefficients and inverse recovery',()=>{
 assert.ok(engine.validateTransfer(pn));assert.ok(engine.validateTransfer(ne));
 assert.deepEqual(applyPhasePermutation(applyPhasePermutation(eValue,ne.permutation,-1),pn.permutation,-1),payload);
});
check('forging an L coefficient map onto a PN move is rejected by the native validator',()=>{
 const fake={...pn,permutation:targets.L};
 const target={...engine.packets[pn.target],permutation:targets.L};
 assert.throws(()=>engine.validateTransfer(fake,rootPacket,target),/coefficient/);
});
check('native inverse PN is a typed return but not a missing general contravariant operation',()=>{
 const inverse=engine.outgoing(pn.target).map(i=>engine.operations[i]).find(op=>op.kind==='inverse-PN');
 assert.ok(inverse);assert.equal(inverse.target,engine.root);assert.ok(engine.validateTransfer(inverse));
});
const terminal=engine.outgoing(ne.target);
check('the native E endpoint has no automatic onward braid continuation',()=>assert.equal(terminal.length,0));
// A passive reframe of all four vertex slots plus a fixed fifth coordinate is
// invertible algebra, but does not repair the changed geometric C2 reference.
let abstract=payload;
for(const k of 'LRRR')abstract=applyPhasePermutation(abstract,targets[k]);
const qInverse=[...candidate.q.map((_,i)=>candidate.q.indexOf(i)),4];
check('contravariant coefficient order yields the inverse q pullback, not a new native move',()=>assert.deepEqual(abstract,applyPhasePermutation(payload,qInverse)));
// Quantify a conservative short-macro search. Acceptance below compares only
// coefficient permutations; it does not confuse it with chart/port agreement.
const depthLimit=8,stateLimit=20000,queue=[{id:engine.root,word:[]}],seen=new Set([engine.root]),hits={L:[],R:[]};
let capped=false,maxDepth=0;
for(let i=0;i<queue.length;i++){
 const {id,word}=queue[i];maxDepth=Math.max(maxDepth,word.length);
 const packet=engine.packets[id];
 for(const label of ['L','R'])if(JSON.stringify(packet.permutation)===JSON.stringify(targets[label])){
  const chart=engine.charts[packet.chart],desired=reframings[label].target.aliases;
  hits[label].push({word,origin:packet.origin,species:chart.species,cellKey:engine.geometry.cells[chart.cell].key,aliases:chart.aliases,fullDesiredReferenceMatches:chart.species==='proton'&&names.every(n=>chart.aliases[n]===desired[n])&&chart.aliases.C2===desired.C2});
 }
 if(word.length===depthLimit)continue;
 for(const opId of engine.outgoing(id)){
  const op=engine.operations[opId];assert.ok(engine.validateTransfer(op));
  if(seen.has(op.target))continue;
  if(seen.size>=stateLimit){capped=true;break;}
  seen.add(op.target);queue.push({id:op.target,word:[...word,op.kind]});
 }
 if(capped)break;
}
checks.push('bounded search validates every expanded native transfer and retains its full packet state');
// Complete finite over-approximation: forget geometry and origin, but retain
// species and all five coefficient slots. Every current native move belongs
// to these source-defined transition types. Closure proves a no-word result
// for this naive fixed-fifth-slot interpretation, not for arbitrary lifts.
const abstractRules={
 proton:[{target:'proton',permutation:[...phaseAdvancePermutations.proton]},{target:'neutron',permutation:pn.permutation}],
 neutron:[{target:'neutron',permutation:[...phaseAdvancePermutations.neutron]},{target:'proton',permutation:pn.permutation},{target:'electron',permutation:ne.permutation}],
 electron:[]};
const stateKey=(species,p)=>species+':'+p.join(''),abstractQueue=[{species:'proton',permutation:[0,1,2,3,4]}],abstractSeen=new Set([stateKey('proton',[0,1,2,3,4])]);
for(let i=0;i<abstractQueue.length;i++)for(const rule of abstractRules[abstractQueue[i].species]){
 const permutation=rule.permutation.map(j=>abstractQueue[i].permutation[j]),key=stateKey(rule.target,permutation);
 if(!abstractSeen.has(key)){abstractSeen.add(key);abstractQueue.push({species:rule.target,permutation});}
}
check('complete typed coefficient automaton closes with thirty states',()=>{
 assert.equal(abstractQueue.length,30);
 for(const species of ['proton','neutron','electron'])assert.equal(abstractQueue.filter(s=>s.species===species).length,10);
 for(const state of abstractQueue)for(const rule of abstractRules[state.species])assert.ok(abstractSeen.has(stateKey(rule.target,rule.permutation.map(j=>state.permutation[j]))));
});
check('both fixed-fifth-slot reflections are absent at every word length in the over-approximation',()=>{
 for(const permutation of Object.values(targets))for(const species of ['proton','neutron','electron'])assert.ok(!abstractSeen.has(stateKey(species,permutation)));
});
check('every expanded actual native transition is included in the finite abstract machine',()=>{
 for(const op of engine.operations){
  const source=engine.charts[engine.packets[op.source].chart].species,target=engine.charts[engine.packets[op.target].chart].species;
  assert.ok(abstractRules[source].some(r=>r.target===target&&JSON.stringify(r.permutation)===JSON.stringify(op.permutation)));
 }
});
const oldSupport=new Set(Object.values(rootChart.aliases)),newSupport=new Set(Object.values(reframings.L.target.aliases));
const contextGap={shared:[...oldSupport].filter(v=>newSupport.has(v)),oldOnly:[...oldSupport].filter(v=>!newSupport.has(v)),newOnly:[...newSupport].filter(v=>!oldSupport.has(v)),union:[...new Set([...oldSupport,...newSupport])]};
check('L needs a sixth distinct reference if both old and new contexts are retained',()=>{assert.equal(contextGap.shared.length,4);assert.equal(contextGap.oldOnly.length,1);assert.equal(contextGap.newOnly.length,1);assert.equal(contextGap.union.length,6);});
const search={depthLimit,stateLimit,capped,statesDiscovered:seen.size,maxDepthReached:maxDepth,
 semantics:'Reachable native packet states, not simultaneous occupancy. One shortest retained path per state; alternative histories not classified. A coefficient hit is not acceptance of a physical or coherent assembly macro.',
 coefficientHits:Object.fromEntries(Object.entries(hits).map(([k,vs])=>[k,{count:vs.length,fullReferenceMatches:vs.filter(v=>v.fullDesiredReferenceMatches).length,examples:vs.slice(0,5)}]))};
// Recover the actual three-simplex incidence span. Its central cell is a
// common geometric witness, not automatically a map between its two readers.
const reframedEngine=new GenerativeAssemblyRules({seedBindings:Object.fromEntries(names.map(n=>[n,reframings.L.target.aliases[n]]))});
const reframedPN=reframedEngine.outgoing(reframedEngine.root).map(i=>reframedEngine.operations[i]).find(op=>op.kind==='PN');
assert.ok(reframedPN);assert.ok(reframedEngine.validateTransfer(reframedPN));
const bodyVertices=(rules,packet)=>rules.geometry.cells[rules.charts[rules.packets[packet].chart].cell].vertices;
const spanVertices={left:bodyVertices(engine,pn.target),witness:bodyVertices(engine,engine.root),right:bodyVertices(reframedEngine,reframedPN.target)};
const intersection=(a,b)=>a.filter(v=>b.includes(v));
check('two actual native N simplices meet the same P witness on distinct triangular ports',()=>{
 assert.equal(intersection(spanVertices.left,spanVertices.witness).length,3);
 assert.equal(intersection(spanVertices.right,spanVertices.witness).length,3);
 assert.equal(intersection(spanVertices.left,spanVertices.right).length,2);
 assert.equal(new Set(Object.values(spanVertices).map(v=>[...v].sort().join('|'))).size,3);
});
const censusPath='research/voevodsky/results/esd7_explicit_analytical_census.json',census=read(censusPath);
const coordinateToId=new Map(census.vertices.map(v=>[v.barycentric.join(','),v.id]));
const nativeToId=v=>coordinateToId.get(v.split(',').map(Number).map(x=>2-x).join(','));
const sourceId=(vertices,rows)=>{const ids=vertices.map(nativeToId);assert.ok(ids.every(Boolean));return rows.find(r=>[...r.vertices].sort().join('|')===[...ids].sort().join('|'))?.id;};
const witnessSpan={cells:Object.fromEntries(Object.entries(spanVertices).map(([k,v])=>[k,sourceId(v,census.tetrahedra)])),
 leftPort:sourceId(intersection(spanVertices.left,spanVertices.witness),census.triangles),rightPort:sourceId(intersection(spanVertices.right,spanVertices.witness),census.triangles),
 commonEdge:sourceId(intersection(spanVertices.left,spanVertices.right),census.edges),retainedReferenceUnion:contextGap.union,
 operation:'left N --inverse-PN--> P with old reader; [unconstructed context-changing comparison]; P with reversed reader --PN--> right N',
 status:'Actual source incidence and each individual PN leg verified; missing comparison between the two central readers is not filled by identifying their body.'};
check('the geometric witness span binds actual T184, F538 and F403 source IDs',()=>{assert.equal(witnessSpan.cells.witness,'T184');assert.equal(witnessSpan.cells.left,'T242');assert.ok(witnessSpan.cells.right);assert.equal(witnessSpan.leftPort,'F538');assert.equal(witnessSpan.rightPort,'F403');assert.ok(witnessSpan.commonEdge);});
const sourcePaths=[candidatePath,censusPath,'research/nima/generative-phase-assembly.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs'];
const result={status:'passed',disposition:'naive frame-to-native binding rejected; source-valued witness remains unconstructed',checks,
 sourceSha256:Object.fromEntries(sourcePaths.map(p=>[p,hash(p)])),reframings,firstMoves,
 actualPNNE:{word:[pn.kind,ne.kind],permutations:[pn.permutation,ne.permutation],phaseDeltas:[pn.phaseDelta,ne.phaseDelta],input:payload,output:eValue,frames:[rootChart,engine.charts[engine.packets[pn.target].chart],engine.charts[engine.packets[ne.target].chart]].map(c=>phaseFrame(c,0))},
 abstractLRRR:{input:payload,output:abstract,qInversePullback:qInverse,nativeOperation:false},search,
 coefficientClosure:{rules:abstractRules,states:abstractQueue,reflectionsReachable:false,scope:'Complete over-approximation for the current typed native coefficient rules from this seed; rejects only the fixed-fifth-slot extension of L/R.'},contextGap,witnessSpan,
 witnessGate:'A tetrahedral comparison requires two typed composites with a common source and target. A four-mark relabelling with an incompatible fifth context does not supply those composites. No witness is manufactured from coefficient equality.',
 next:'Construct explicit interface/context transport for L and R, or change their binding. Carry the separate chart-grade and native occurrence-origin clocks; do not equate them by name.'};
const out=path.join(root,'research/strominger/results/binary-simplex-native-binding-v1.json');fs.mkdirSync(path.dirname(out),{recursive:true});fs.writeFileSync(out,JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:result.status,checks:checks.length,disposition:result.disposition,search},null,2));
