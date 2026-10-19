import assert from 'node:assert/strict';
import {mkdir,writeFile} from 'node:fs/promises';
import './check_simplex_components.mjs';
import {createHelium3Tunnel} from '../demos/particle-overlap-tetrahedron/helium3-tunnel-model.mjs';
import {deriveHelium4Core,applyHelium4CoreLoop} from '../demos/particle-overlap-tetrahedron/helium4-core-probe.mjs';
import {windowModeCoefficients} from '../demos/particle-overlap-tetrahedron/deuterium-tunnel-model.mjs';
import {lattice,worldPoint} from '../demos/particle-overlap-tetrahedron/simplex-model.mjs';
import {itemKey} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
const sub=(a,b)=>a.map((x,i)=>x-b[i]),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
const model=createHelium3Tunnel({complementCoefficients:[[9,-7],[-5,6]]});for(let i=0;i<4;i++)model.step();
const before=model.snapshot(),bytes=JSON.stringify(before),probe=deriveHelium4Core(before);
assert.equal(JSON.stringify(before),bytes);assert.deepEqual(model.snapshot(),before);assert.deepEqual(probe.items.slice(0,5),before.items);assert.deepEqual(probe.bindings,before.bindings);
assert.deepEqual(probe.counts,{proton:2,neutron:2,electron:2});for(const species of ['proton','neutron','electron'])assert.equal(probe.items.filter(i=>i.species===species).length,2);
assert.equal(probe.newVertexCount,0);assert.equal(probe.newCarrierCount,1);assert.equal(probe.items[5].window,null,'Do not silently select an unresolved reader frame');assert.equal(probe.items[5].candidateReaders.length,4);
const keys=lattice.cells.map(c=>itemKey(c.map(i=>lattice.nodes[i].address))),ids=probe.items.map(i=>keys.indexOf(i.key));assert.deepEqual(ids,[0,13,16,24,14,7]);assert.equal(new Set(ids).size,6);assert.ok(ids.every(i=>i>=0));
// The fresh base-lattice check above supplies positive-volume/disjointness
// evidence. Additionally verify that the four nuclear cells close a convex core.
const nucleus=probe.items.filter(i=>i.species!=='electron'),common=nucleus[0].vertices.filter(v=>nucleus.every(i=>i.vertices.some(p=>itemKey([p])===itemKey([v]))));assert.equal(itemKey(common),itemKey([probe.bindings.M0,probe.bindings.M1]));
const faces=new Map();for(const cell of nucleus)for(const face of cell.faces){const key=itemKey(face);if(!faces.has(key))faces.set(key,{face,cell,count:0});faces.get(key).count++;}
const boundary=[...faces.values()].filter(f=>f.count===1);assert.equal(boundary.length,8);assert.equal([...faces.values()].filter(f=>f.count===2).length,4);
for(const {face,cell} of boundary){const ps=face.map(worldPoint);let normal=cross(sub(ps[1],ps[0]),sub(ps[2],ps[0]));if(dot(normal,sub(worldPoint(cell.center),ps[0]))>0)normal=normal.map(x=>-x);for(const v of nucleus.flatMap(i=>i.vertices))assert.ok(dot(normal,sub(worldPoint(v),ps[0]))<1e-10);}
assert.equal(probe.ordinaryNeutronExitToRetainedElectron,false);const unusedElectrons=[...new Set(probe.alternatives.flat().map(c=>keys.indexOf(c.continuationElectron.key)))].sort((a,b)=>a-b);assert.deepEqual(unusedElectrons,[6,8]);
assert.deepEqual(probe.variants.map(v=>v.order),[3,2,2,3]);assert.ok(probe.variants.every(v=>!v.oneLoopIdentity));
let tested=0;
for(const variant of probe.variants){
 for(const branch of ['common','positive','negative'])for(const phaseExponent of [0,1,2]){
  const input=[...windowModeCoefficients({branch,phaseExponent}),[9,-7],[-5,6]],one=applyHelium4CoreLoop(input,variant);
  assert.deepEqual(one.slice(3),input.slice(3));assert.deepEqual(applyHelium4CoreLoop(one,variant,-1),input);
  if(branch==='common')assert.deepEqual(one,input);else assert.notDeepEqual(one,input);
  let current=input;for(let turn=0;turn<variant.order;turn++)current=applyHelium4CoreLoop(current,variant);assert.deepEqual(current,input);tested++;
 }
 for(let i=0;i<5;i++){const basis=Array.from({length:5},(_,j)=>[i===j?1:0,0]);assert.deepEqual(applyHelium4CoreLoop(applyHelium4CoreLoop(basis,variant),variant,-1),basis);}
}
// An active-window omega factor is NOT a global scalar on a five-slot packet
// with nonzero complement. Keep those full states distinct.
const sample=[...windowModeCoefficients({branch:'positive',phaseExponent:0}),[9,-7],[-5,6]],one=applyHelium4CoreLoop(sample,probe.variants[0]),omega=[-.5,Math.sqrt(3)/2];
const phased=sample.map(([a,b])=>[a*omega[0]-b*omega[1],a*omega[1]+b*omega[0]]);assert.ok(one[4].some((x,i)=>Math.abs(x-phased[4][i])>1));
const out='research/strominger/results/helium4-core';await mkdir(out,{recursive:true});
await writeFile(out+'/candidate.json',JSON.stringify({status:probe.status,counts:probe.counts,items:probe.items,bindings:probe.bindings,interfaces:probe.interfaces,readers:probe.alternatives.map(cs=>cs.map(c=>({exchangeMiddleM:c.exchangeMiddleM,window:c.window,aliases:c.aliases,forwardElectronCell:keys.indexOf(c.continuationElectron.key)}))),scope:probe.scope},null,2)+'\n');
await writeFile(out+'/verification.json',JSON.stringify({status:'pass-diagnostic-not-admitted',candidateStatus:probe.status,counts:probe.counts,cellIds:ids,retainedHelium3Prefix:true,newCarriers:1,newVertices:0,convexNuclearCore:true,nuclearBoundaryFaces:8,sharedNuclearEdge:['M0','M1'],forwardContinuationElectronCells:unusedElectrons,forwardContinuationReachesRetainedElectrons:false,variants:probe.variants.map(v=>({exchangeMiddleM:v.choices,permutation:v.permutation,operatorOrder:v.order,oneLoopIdentity:v.oneLoopIdentity})),characterPhaseCases:tested,allFiveSlotsRetained:true,inverseLoopsRestore:true,commonSectorDoesNotDetermineHolonomy:true,nonzeroComplementPreventsGlobalPhaseQuotient:true,viewerAdmitted:false,physicalStabilityDerived:false,scope:probe.scope},null,2)+'\n');
console.log('PASS helium-4 diagnostic: unique added neutron in cell 7; convex 2P/2N core. Reader choices give order-3 or order-2 holonomy; retained-electron exits remain unresolved. This historical reader probe is not the corrected phase-first viewer model.');
