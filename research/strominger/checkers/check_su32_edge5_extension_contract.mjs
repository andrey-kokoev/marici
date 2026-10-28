// Edge-5 specification gate plus independent incidence regression at edge 3.
// Does not generate a wiring, select fibres by count, or bind missing operations.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildFiveSideOctRoutingObligations} from '../../realization-tower/five-side-oct-routing-obligations.mjs';
import {buildFiveSideOctComparisonDomain} from '../../realization-tower/five-side-oct-comparison-domain.mjs';
const paths={contract:'research/strominger/contracts/su32-edge5-structural-extension-v1.json',
 working:'research/strominger/results/su32-working-wiring-family-v1/verification.json',
 wiring:'research/strominger/results/su32-global-reference-wiring-v1/verification.json',
 trace:'research/strominger/results/su32-fixed-reading-trace-v1/verification.json'};
const hash=x=>createHash('sha256').update(x).digest('hex'),docs={},sourceHashes={};
for(const [name,path] of Object.entries(paths)){
 const bytes=await fs.readFile(path);sourceHashes[path]=hash(bytes);docs[name]=JSON.parse(bytes);
 for(const [p,h] of Object.entries(docs[name].sourceHashes??{}))assert.equal(hash(await fs.readFile(p)),h,`Stale source: ${p}`);
}
const {contract,working,wiring,trace}=docs,copy=x=>structuredClone(x);
const point=p=>p.join(','),edgeKey=(a,b)=>[point(a),point(b)].sort().join('|');
function edgesOf(cell){
 return [...new Set(cell.faces.flatMap(face=>face.flatMap((a,i)=>face.slice(i+1).map(b=>edgeKey(a,b)))))].sort();
}
// Derive the predicate from native edge incidence, not the previous distance
// calculation or an orbit ID. Candidate contexts remain exactly those retained.
const small=buildPESymmetricSector(1),smallCells=new Map(small.cells.map(c=>[c.id,c]));
const cellEdges=new Map(small.cells.map(c=>[c.id,new Set(edgesOf(c))]));
const sharedEdges=(a,b)=>[...cellEdges.get(a)].filter(e=>cellEdges.get(b).has(e)).sort();
const regression=wiring.localizedSurvivors.map((candidate,id)=>{
 const cover=trace.middleAssignments.find(c=>c.index===candidate.cover);
 const outcome=wiring.outcomes.find(c=>c.cover===candidate.cover);
 const split=cover.routes.filter(r=>r.members.length===2&&r.members.every(m=>!outcome.inactiveMiddleCells.includes(m)));
 assert.equal(split.length,1);
 const tip=candidate.placements.find(p=>p.channel===split[0].channel);assert(tip);
 const pp=candidate.placements.find(p=>p.pair.every(k=>k[0]==='P'));
 const ee=candidate.placements.find(p=>p.pair.every(k=>k[0]==='E'));assert(pp&&ee);
 for(const id of [tip.at,pp.at,ee.at])assert.equal(smallCells.get(id).role,'neutron');
 const toPP=sharedEdges(tip.at,pp.at),toEE=sharedEdges(tip.at,ee.at);
 return {candidate:id,cover:candidate.cover,triple:{T:tip.at,U:pp.at,V:ee.at},
  sharedNativeEdges:{TU:toPP,TV:toEE},passes:toPP.length>0&&toEE.length>0};
});
const accepted=regression.filter(r=>r.passes).map(r=>r.candidate);
const refused=regression.filter(r=>!r.passes).map(r=>r.candidate);
assert.deepEqual(accepted,[...working.workingCandidates.map(c=>c.sourceCandidateId)].sort((a,b)=>a-b));
assert.deepEqual(refused,[...working.controlCandidates.map(c=>c.sourceCandidateId)].sort((a,b)=>a-b));
assert.equal(accepted.length,8);assert.equal(refused.length,8);
// Native adjacency is a placement test, NOT an invented shared-face passage.
for(const r of regression)for(const side of ['TU','TV'])for(const id of r.sharedNativeEdges[side]){
 const vs=id.split('|').map(p=>p.split(',').map(Number));assert.equal(vs.length,2);
 assert.equal(vs[0].reduce((s,x,i)=>s+(x-vs[1][i])**2,0),2);
}
// Enumerate the complete larger carrier and all cone obligations FIRST.
const sector=buildPESymmetricSector(2),obligations=buildFiveSideOctRoutingObligations(sector);
const reading=obligations.readings.find(r=>r.id===contract.reading);assert(reading);
const domain=buildFiveSideOctComparisonDomain(sector,{readingIds:[reading.id]}).readings[0];
const centre=c=>[0,1,2,3].map(i=>c.vertices.reduce((s,v)=>s+v[i],0)/c.vertices.length);
const layer=c=>1+2*(sector.edgeUnits-1-reading.sign*reading.axis.reduce((s,a,i)=>s+a*(centre(c)[i]-sector.centre[i]),0)/2);
const layers=Array.from({length:17},(_,i)=>({layer:i+1,proton:0,neutron:0,electron:0,cells:[]}));
for(const cell of sector.cells){const index=layer(cell);assert(Number.isInteger(index)&&index>=1&&index<=17);
 layers[index-1][cell.role]++;layers[index-1].cells.push(cell.id);}
const edgeIds=[...new Set(sector.cells.flatMap(edgesOf))].sort();
const roleCounts=Object.fromEntries(['proton','neutron','electron'].map(role=>[role,sector.cells.filter(c=>c.role===role).length]));
const cones=domain.overlaps.filter(o=>o.residualCycleRank);
const byId=new Map(sector.cells.map(c=>[c.id,c]));
const coneStarts={};for(const cone of cones){const l=layer(byId.get(cone.source));coneStarts[l]=(coneStarts[l]??0)+1;
 assert.equal(cone.paths.length,16);assert.equal(new Set(cone.paths.flatMap(p=>p.cells)).size,14);}
const inventory={edgeUnits:sector.edgeUnits,wholeCells:sector.cells.length,roleCounts,nativeEdges:edgeIds.length,
 nativeFaces:sector.faces.length,sharedInterfaces:sector.faces.filter(f=>f.owners.length===2).length,layers:layers.length,residualComparisonCones:cones.length};
const {constructor,...expected}=contract.carrier;assert.equal(constructor,'buildPESymmetricSector(2)');assert.deepEqual(inventory,expected);
assert.deepEqual(layers.filter(l=>l.neutron).map(l=>l.neutron),[1,4,9,16,25,16,9,4,1]);
for(const role of ['proton','electron'])assert.deepEqual(layers.filter(l=>l[role]).map(l=>l[role]),[2,6,12,20,20,12,6,2]);
assert.deepEqual(coneStarts,{'1':1,'3':4,'5':9,'7':16,'9':9,'11':4,'13':1});
assert.equal(contract.fibreInventory.requiredCount,80);
assert.equal(contract.fibreInventory.identityDomain,null);assert.equal(contract.workingChoice.edge5MarkedTripleDomain,null);
assert(Object.values(contract.openBindings).every(v=>v===null));
const additional=['research/strominger/pe-symmetric-sector.mjs','research/realization-tower/five-side-oct-routing-obligations.mjs',
 'research/realization-tower/five-side-oct-comparison-domain.mjs','research/strominger/contracts/five-side-oct-routing-obligations-v1.json',
 'research/strominger/checkers/check_su32_edge5_extension_contract.mjs'];
for(const p of additional)sourceHashes[p]=hash(await fs.readFile(p));
const report={schema:'su32.edge5-extension-contract-check.v1',passed:true,
 contractPath:paths.contract,contractHash:sourceHashes[paths.contract],inventory,
 edge3Regression:{predicate:'T shares a native edge with each same-role pair site U,V; no metric threshold or orbit label used.',accepted,controls:refused,regression,
  scope:'Exact on the sixteen tested localized edge-three candidates. Not a universal characterization for arbitrary placements or an edge-five existence proof.'},
 edge5Carrier:{centre:sector.centre,cells:copy(sector.cells),edges:edgeIds,faces:copy(sector.faces),layers,
  comparisonCones:copy(cones),comparisonBoundaries:copy(domain.comparisons),coneStarts},
 solverStatus:'not-formulated; no routing search started',requiredFibreCount:80,
 fibreIdentityDomain:null,fibreBoundaryBinding:null,edge5MarkedTripleInstances:null,
 result:'Versioned structural contract and edge-three incidence regression pass. Complete edge-five geometry and 44 cone obligations retained; no fibre/route or native operation binding fabricated.',
 nextGate:'Specify the 80 fibre occurrence identities, boundary/port binding and placement-instance domain before formulating simultaneous route constraints.',sourceHashes};
const dir='research/strominger/results/su32-edge5-extension-contract-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,sourceHashes:undefined,edge3Regression:{...report.edge3Regression,regression:undefined},
 edge5Carrier:{coneStarts,layers:layers.map(({cells,...l})=>l)}},null,2));
