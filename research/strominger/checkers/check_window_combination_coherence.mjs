// Commuting translation/combination squares, not physical state cloning.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules,enumerateAssemblies} from '../../nima/generative-phase-assembly.mjs';
import {makeLatticeItem} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
const source='research/strominger/results/hydrogen-edge-attachment/verification.json',samples=JSON.parse(await readFile(source)).rows,shifts=[];for(let i=0;i<4;i++)for(let j=0;j<4;j++)if(i!==j){const s=[0,0,0,0];s[i]=1;s[j]=-1;shifts.push(s);}
const zero=[0,0,0,0],move=(p,s)=>p.split(',').map((x,i)=>Number(x)+s[i]).join(','),same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
function shifted(seed,s){const r=new GenerativeAssemblyRules({seedBindings:seed}),owner=makeLatticeItem('tetrahedron',s),cell=r.geometry.register(owner,owner.components[0]),a=Object.fromEntries(Object.entries(seed).map(([k,v])=>[k,move(v,s)]));r.root=r.packet(r.completeP(cell,a),0,[0,1,2,3,4]);return r;}
function state(r,id,s=zero){const p=r.packets[id],c=r.charts[p.chart];return {species:c.species,origin:p.origin,aliases:Object.fromEntries(Object.entries(c.aliases).map(([k,v])=>[k,move(v,s.map(x=>-x))])),permutation:p.permutation};}
function audit(r,ids,s=zero){const d=r.describe(ids);if(!d.valid)return {valid:false,reason:d.reason};const x=r.inspect(ids,d);return {valid:true,counts:x.counts,contacts:d.contacts.map(c=>JSON.stringify({kind:c.kind,face:c.face.map(v=>move(v,s.map(x=>-x))).sort()})).sort(),allContactsWitnessed:x.allContactsWitnessed,allCellsOnEntryExitPaths:x.allCellsOnEntryExitPaths,allPacketsCanReachExit:x.allPacketsCanReachExit,certifiedExit:x.certifiedExit};}
let squares=0,candidateSquares=0,coefficientEntries=0,certified=0;const rejections={},rows=[],frameHolonomies=[];
for(const sample of samples){
 const enumeration=enumerateAssemblies({maxTransitions:3,maxStates:20000,seedBindings:sample.seedBindings,inspect:false});assert.ok(enumeration.complete);const r=enumeration.rules;
 for(const s of shifts){
  const t=shifted(sample.seedBindings,s),mapping=new Map([[r.root,t.root]]),queue=[[r.root,t.root,0]];
  for(const [a,b,depth] of queue){assert.deepEqual(state(r,a),state(t,b,s));if(depth===4)continue;const left=r.outgoing(a).map(i=>r.operations[i]),right=t.outgoing(b).map(i=>t.operations[i]);assert.equal(left.length,right.length);
   for(const op of left){const other=right.find(o=>o.kind===op.kind);assert.ok(other);r.validateTransfer(op);t.validateTransfer(other);assert.deepEqual(op.permutation,other.permutation);if(mapping.has(op.target))assert.equal(mapping.get(op.target),other.target);else{mapping.set(op.target,other.target);queue.push([op.target,other.target,depth+1]);}}
  }
  for(const node of enumeration.nodes){
   const ids=node.packets,translated=ids.map(i=>mapping.get(i));assert.ok(translated.every(i=>i!==undefined));const before=audit(r,ids),after=audit(t,translated,s);assert.deepEqual(after,before);squares++;if(before.certifiedExit)certified++;
   // Combined data is a collection of construction maps, not simultaneous
   // cloned states. Compare each of their five symbolic root coefficients.
   const combine=(engine,list,shift)=>list.map(i=>JSON.stringify(state(engine,i,shift))).sort();assert.deepEqual(combine(r,ids,zero),combine(t,translated,s));coefficientEntries+=5*ids.length;
   for(const id of ids)for(const oi of r.outgoing(id)){const op=r.operations[oi],target=mapping.get(op.target);assert.notEqual(target,undefined);const extended=[...new Set([...ids,op.target])],shiftedExtended=[...new Set([...translated,target])];const a=audit(r,extended),b=audit(t,shiftedExtended,s);assert.deepEqual(a,b);candidateSquares++;if(!a.valid)rejections[a.reason]=(rejections[a.reason]??0)+1;}
  }
 }
 // Test endpoint coherence independently of rigid translations. Group by
 // actual marked chart and absolute origin, leaving coefficients out of key.
 const q=[[r.root,0,[]]],seen=new Set([r.root]),groups=new Map();let explored=0;
 for(const [id,depth,word] of q){explored++;const p=r.packets[id],key=p.chart+'@'+p.origin,group=groups.get(key)??new Map();group.set(p.permutation.join(','),{id,word,permutation:p.permutation});groups.set(key,group);if(depth===8)continue;
  for(const oi of r.outgoing(id)){const op=r.operations[oi];if(!seen.has(op.target)){seen.add(op.target);q.push([op.target,depth+1,[...word,op.kind]]);}}
 }
 let distinctFrameEndpoints=0;for(const [key,g] of groups)if(g.size>1){distinctFrameEndpoints++;if(frameHolonomies.length<8){
   const paths=[...g.values()];for(const path of paths){let id=r.root;const collection=[id];for(const kind of path.word){id=r.operations[r.outgoing(id).find(i=>r.operations[i].kind===kind)].target;collection.push(id);}assert.equal(id,path.id);path.retainedCombinationAudit=audit(r,[...new Set(collection)]);}
   const p=paths[0].permutation,q=paths[1].permutation,h=q.map(i=>p.indexOf(i));let power=[0,1,2,3,4],order=0;do{power=h.map(i=>power[i]);order++;assert.ok(order<=120);}while(!same(power,[0,1,2,3,4]));
   frameHolonomies.push({marking:sample.marking,chartOrigin:key,paths,relativeCoefficientPermutation:h,relativePermutationOrder:order});
  }}
 rows.push({marking:sample.marking,configurationsThroughThreeAdditions:enumeration.nodes.length,nativePathStatesThroughEight:explored,sameMarkedOriginWithDifferentCoefficientFrames:distinctFrameEndpoints});
}
const sources=[source,'research/strominger/checkers/check_window_combination_coherence.mjs','research/nima/generative-phase-assembly.mjs','research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs'];const hashes={};for(const f of sources)hashes[f]=createHash('sha256').update(await readFile(f)).digest('hex');
const result={status:'bounded-translation-combination-squares-commute',seedMarkings:24,translationDirections:12,configurationDepth:3,pathDepth:8,squares,candidateSquares,symbolicCoefficientEntriesCompared:coefficientEntries,certifiedExitSquares:certified,rejectedCandidateSquares:rejections,rows,coefficientFrameHolonomyExamples:frameHolonomies,sourceHashes:hashes,scope:'Native retained construction-map collections, not simultaneous clones or a tensor product of physical states. Compares full contact/admission/exit predicates, origins, alias bindings and five-slot maps under rigid translation; both accepted and rejected candidate combinations covary. Endpoint frame tests are bounded and do not identify distinct histories. No globally sewn 36-amplitude PNE field, path-independent field transport or torus topology certified.'};const out='research/strominger/results/window-combination-coherence';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({status:result.status,squares,candidateSquares,coefficientEntries,certified,rejections,sameMarkedOriginWithDifferentCoefficientFrames:rows.reduce((s,r)=>s+r.sameMarkedOriginWithDifferentCoefficientFrames,0)}));
