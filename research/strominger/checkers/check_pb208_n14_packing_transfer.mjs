// Compare legacy whole-item Pb packing with the strict primitive N-14 ansatz.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {lead208Chains as chains,lead208Bodies as bodies,lead208Construction as construction} from '../demos/particle-overlap-tetrahedron/lead208-model.mjs';
import {faces,lattice} from '../demos/particle-overlap-tetrahedron/simplex-model.mjs';
import {probeSpace,domainOf,enumerateProbe} from './n14-probe-model.mjs';
const hash=b=>createHash('sha256').update(b).digest('hex'),key=vertices=>vertices.map(p=>p.join(',')).sort().join('|');
const files=['./check_pb208_n14_packing_transfer.mjs','./n14-probe-model.mjs',...['lead208-model.mjs','fiber-space-model.mjs','simplex-model.mjs','simplex-components.mjs','lattice-items.mjs','window-construction-model.mjs'].map(f=>'../demos/particle-overlap-tetrahedron/'+f)],sourceHashes={};
for(const f of files)sourceHashes[f]=hash(await readFile(new URL(f,import.meta.url)));
const shapes={},faceIntersections={},incidence=new Map();
for(const b of bodies){
 const k=b.species+':'+b.shape.kind+':'+b.components.length;shapes[k]=(shapes[k]??0)+1;
 for(const f of b.shape.faces){const k=key(f);if(!incidence.has(k))incidence.set(k,[]);incidence.get(k).push(b);}
}
const bodyContacts={};for(const owners of incidence.values()){
 assert.ok(owners.length<=2);if(owners.length!==2)continue;const k=owners.map(b=>b.species).sort().join('/');bodyContacts[k]=(bodyContacts[k]??0)+1;
}
let windowNecessaryCondition=0;for(const c of chains){
 const a=new Set(c.protonNeutronFace.map(p=>p.join(','))),shared=c.neutronElectronFace.filter(p=>a.has(p.join(','))).length;
 faceIntersections[shared]=(faceIntersections[shared]??0)+1;if(shared===2)windowNecessaryCondition++;
}
assert.equal(windowNecessaryCondition,0);assert.equal(bodyContacts['electron/electron']??0,0);
// Borrow Pb's global resource-allocation idea, not its different particle
// shapes: solve the complete nonadjacent-E assignment on each fixed strict
// N-14 core. With at most 8 possible cells, exact independent-set search is
// cheap. This cannot rescue a search already exhausting all 7-subsets.
const space=probeSpace(),{adjacency}=domainOf(space),raw=enumerateProbe(space,{allowEE:true});assert.equal(raw.complete,true);assert.equal(raw.candidates.length,5632);
const cores=new Map();for(const c of raw.candidates){
 const vertices=new Set(c.nucleus.flatMap(i=>lattice.cells[i])),types=Object.fromEntries(Object.entries(c.types).filter(([v])=>vertices.has(Number(v))));
 const k=JSON.stringify([c.nucleus,types]);if(!cores.has(k))cores.set(k,{nucleus:c.nucleus,types,pool:new Set()});c.electrons.forEach(i=>cores.get(k).pool.add(i));
}
assert.equal(cores.size,2384);
let nodes=0;function maximumIndependent(pool){
 nodes++;if(!pool.length)return [];
 // Most constrained cell first, analogous to Pb's fail-first ordering.
 const selected=[...pool].sort((a,b)=>adjacency[b].filter(e=>pool.includes(e.to)).length-adjacency[a].filter(e=>pool.includes(e.to)).length||a-b)[0];
 const rest=pool.filter(i=>i!==selected),include=[selected,...maximumIndependent(rest.filter(i=>!adjacency[selected].some(e=>e.to===i)))],exclude=maximumIndependent(rest);
 return include.length>=exclude.length?include:exclude;
}
const maximumHistogram={},poolHistogram={},witnesses={};let sevenFeasible=0;
for(const c of cores.values()){
 const pool=[...c.pool].sort((a,b)=>a-b),chosen=maximumIndependent(pool);assert.ok(chosen.every(i=>!adjacency[i].some(e=>chosen.includes(e.to))));
 maximumHistogram[chosen.length]=(maximumHistogram[chosen.length]??0)+1;poolHistogram[pool.length]=(poolHistogram[pool.length]??0)+1;if(chosen.length>=7)sevenFeasible++;
 witnesses[chosen.length]??={nucleus:c.nucleus,types:c.types,eligibleCells:pool,maximumNonadjacentElectrons:chosen};
}
assert.deepEqual(poolHistogram,{'7':1920,'8':464});assert.equal(sevenFeasible,0);
for(const f of files)assert.equal(hash(await readFile(new URL(f,import.meta.url))),sourceHashes[f],'Source changed during review: '+f);
const result={status:'pb-layout-reviewed-and-strict-resource-transfer-tested',sourceHashes,pb:{counts:construction.counts,shapeHistogram:shapes,bodyFaceContacts:bodyContacts,PN_NE_faceIntersectionHistogram:faceIntersections,chains:chains.length,windowNecessaryConditionPassed:windowNecessaryCondition,searchNodes:construction.searchNodes,compositeNeutronChains:construction.compositeNeutrons,geometryOnly:true},strictN14ResourceProbe:{typedCores:cores.size,eligiblePoolHistogram:poolHistogram,maximumNonadjacentElectronsHistogram:maximumHistogram,sevenFeasible,searchNodes:nodes,witnesses},conclusion:'Pb avoids EE face contact through separated whole-item chains with regular E endpoints, but uses larger/composite nuclear shapes and unmarked outward faces. Its 0/82 retained-window score prevents importing its loadout as a phase construction. Joint resource solving transfers as an algorithm, not new admissible geometry; exact independent-set solving confirms it cannot fix neutral N14 in the current ansatz.',scope:'Original Pb loadout and 343-cell strict N14 domain. No isotope-specific exception, new particle shape, broader-domain negative theorem, EE law or physical stability claim. Production/viewer unchanged.'};
await mkdir('research/strominger/results/pb208-n14-packing-transfer',{recursive:true});await writeFile('research/strominger/results/pb208-n14-packing-transfer/verification.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({pb:result.pb,strictN14:{typedCores:cores.size,poolHistogram,maximumHistogram,sevenFeasible}},null,2));
