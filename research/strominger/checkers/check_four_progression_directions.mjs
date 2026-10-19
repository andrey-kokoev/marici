// Source-generated displacement ranks; do not infer control from ambient axes.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
const input='research/strominger/results/hydrogen-edge-attachment/verification.json',samples=JSON.parse(await readFile(input)).rows,depthBound=12,rows=[];
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b),point=s=>s.split(',').map(Number),sub=(a,b)=>a.map((x,i)=>x-b[i]);
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
function span(records,key){const echelon=[],witnesses=[];for(const r of records){let v=r[key].map(BigInt);for(const e of echelon){const j=e.findIndex(x=>x!==0n);if(v[j]!==0n){const x=v[j],p=e[j];v=v.map((y,i)=>p*y-x*e[i]);let g=0n;for(const y of v)g=gcd(g,y);if(g)v=v.map(y=>y/g);}}
 const pivot=v.findIndex(x=>x!==0n);if(pivot<0)continue;let g=0n;for(const x of v)g=gcd(g,x);v=v.map(x=>x/g*(v[pivot]<0n?-1n:1n));echelon.push(v);echelon.sort((a,b)=>a.findIndex(x=>x!==0n)-b.findIndex(x=>x!==0n));witnesses.push(r);}
 return {rank:echelon.length,generators:witnesses};}
function geometry(r,id){const p=r.packets[id],c=r.charts[p.chart],vertices=r.geometry.cells[c.cell].vertices.map(point),center4=[0,1,2,3].map(i=>vertices.reduce((s,v)=>s+v[i],0));assert.equal(center4.reduce((a,b)=>a+b,0),4);return {p,c,center4};}
function relativeAliases(c){const origin=point(c.aliases.C0);return Object.fromEntries(Object.entries(c.aliases).map(([k,v])=>[k,sub(point(v),origin)]));}
function record(r,id,word,root){const x=geometry(r,id),d=sub(x.center4,root.center4),grade=x.p.origin-root.p.origin;assert.equal(d.reduce((a,b)=>a+b,0),0);return {id,species:x.c.species,origin:x.p.origin,word,displacementTimesFour:d,spatial:d.slice(0,3),combined:[...d.slice(0,3),grade],permutation:x.p.permutation};}
const allMacros=[];
for(const sample of samples){const r=new GenerativeAssemblyRules({seedBindings:sample.seedBindings}),root=geometry(r,r.root),reference=relativeAliases(root.c),q=[{id:r.root,word:[]}],seen=new Set([r.root]),all=[],steps=[],restored=[],full=[];
 for(const {id,word} of q){const x=geometry(r,id),rec=record(r,id,word,root);all.push(rec);
  if(x.c.species==='proton'&&same(relativeAliases(x.c),reference)){restored.push(rec);if(same(x.p.permutation,root.p.permutation)){full.push(rec);allMacros.push({...rec,marking:sample.marking});}}
  if(word.length===depthBound)continue;
  for(const oi of r.outgoing(id)){const op=r.operations[oi];r.validateTransfer(op);const target=geometry(r,op.target);
   if(op.kind==='reader-phase-advance'||op.kind==='NN-phase-advance'){const d=sub(target.center4,x.center4);steps.push({kind:op.kind,species:x.c.species,spatial:d.slice(0,3),combined:[...d.slice(0,3),op.phaseDelta],displacementTimesFour:d});}
   if(!seen.has(op.target)){seen.add(op.target);q.push({id:op.target,word:[...word,op.kind]});}
  }
 }
 const summaries={reachableBodies:{spatial:span(all,'spatial'),combined:span(all,'combined')},sameCarrierSteps:{spatial:span(steps,'spatial'),combined:span(steps,'combined')},restoredReference:{count:restored.length,spatial:span(restored,'spatial'),combined:span(restored,'combined')},restoredReferenceAndCoefficients:{count:full.length,spatial:span(full,'spatial'),combined:span(full,'combined')}};
 assert.ok(summaries.reachableBodies.spatial.rank<=3&&summaries.reachableBodies.combined.rank<=4);
 // Replay each restored full-frame generator from its endpoint. Local rules
 // should reproduce the same translation and grade increment without reset.
 const replays=[];for(const generator of summaries.restoredReferenceAndCoefficients.combined.generators){let id=generator.id;const start=geometry(r,id),referenceStart=relativeAliases(start.c);for(const kind of generator.word){const op=r.outgoing(id).map(i=>r.operations[i]).find(o=>o.kind===kind);assert.ok(op);r.validateTransfer(op);id=op.target;}const finish=geometry(r,id),d=sub(finish.center4,start.center4);assert.deepEqual(d,generator.displacementTimesFour);assert.equal(finish.p.origin-start.p.origin,generator.combined[3]);assert.deepEqual(relativeAliases(finish.c),referenceStart);assert.deepEqual(finish.p.permutation,start.p.permutation);replays.push({word:generator.word,twiceDisplacementTimesFour:sub(finish.center4,root.center4),twiceOrigin:finish.p.origin});}
 const generators=summaries.restoredReferenceAndCoefficients.combined.generators,commutingSquares=[];
 const follow=word=>{let id=r.root;for(const kind of word){const op=r.outgoing(id).map(i=>r.operations[i]).find(o=>o.kind===kind);assert.ok(op);r.validateTransfer(op);id=op.target;}return id;};
 for(let i=0;i<generators.length;i++)for(let j=i+1;j<generators.length;j++){const a=follow([...generators[i].word,...generators[j].word]),b=follow([...generators[j].word,...generators[i].word]);assert.equal(a,b);commutingSquares.push({generators:[i,j],sameFullPacket:true,origin:r.packets[a].origin,distinctWordsRetained:true});}
 rows.push({marking:sample.marking,states:seen.size,distinctCells:new Set([...seen].map(i=>r.charts[r.packets[i].chart].cell)).size,...summaries,generatorReplays:replays,commutingSquares});
}
const union={spatial:span(allMacros,'spatial'),combined:span(allMacros,'combined')};const profile={};for(const r of rows){const x=r.restoredReferenceAndCoefficients;const key=`spatial ${x.spatial.rank}, combined ${x.combined.rank}`;profile[key]=(profile[key]??0)+1;}
const files=[input,'research/strominger/four-progression-directions-protocol-v1.md','research/strominger/checkers/check_four_progression_directions.mjs','research/nima/generative-phase-assembly.mjs','research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs'],hashes={};for(const p of files)hashes[p]=createHash('sha256').update(await readFile(p)).digest('hex');const result={status:'native-progression-ranks-measured',depthBound,seedMarkings:24,profiles:profile,rows,unionAcrossDifferentMarkings:union,sourceHashes:hashes,scope:'Finite source-generated integer displacement spans and repeated native-word witnesses. Four-coordinate spatial hyperplane has rank three; appended realization grade is independent only if proved by generated vectors. Rank is not reversible control or a continuous manifold dimension. No new spatial moves, negative grades, origin reset, five-dimensional configuration claim or production/viewer changes.'};const out='research/strominger/results/four-progression-directions';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({profiles:profile,unionSpatialRank:union.spatial.rank,unionCombinedRank:union.combined.rank,firstMarking:rows[0].marking,firstAllSpatialRank:rows[0].reachableBodies.spatial.rank,firstStepSpatialRank:rows[0].sameCarrierSteps.spatial.rank,firstMacroGenerators:rows[0].restoredReferenceAndCoefficients.combined.generators}));
