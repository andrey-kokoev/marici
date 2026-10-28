// Su-32 source fixture for three Hopf adapters; no phase or route assignment.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildFiveSideOctRoutingObligations} from '../../realization-tower/five-side-oct-routing-obligations.mjs';
import {buildFiveSideOctComparisonDomain} from '../../realization-tower/five-side-oct-comparison-domain.mjs';
import {comparisonSphereSweep} from '../five-side-oct-hopf-probe.mjs';

const sector=buildPESymmetricSector(1);
const sites=buildFiveSideOctRoutingObligations(sector);
const domain=buildFiveSideOctComparisonDomain(sector);
const expectedTips=[['neutron:2,2,0,-1','neutron:0,0,2,1'],['neutron:2,0,2,-1','neutron:0,2,0,1'],['neutron:2,0,0,1','neutron:0,2,2,-1']];
assert.equal(sector.edgeUnits,3);
assert.deepEqual([sites.inventory.cells,sites.inventory.P,sites.inventory.N,sites.inventory.E],[51,16,19,16]);
assert.deepEqual(sites.readings.map(r=>r.incomingN).sort(),expectedTips.flat().sort());
const byCell=new Map(sector.cells.map(c=>[c.id,c]));
const centre=c=>c.vertices[0].map((_,i)=>c.vertices.reduce((s,p)=>s+p[i],0)/c.vertices.length);
for(const [a,b] of expectedTips)assert.deepEqual(centre(byCell.get(a)).map((v,i)=>v+centre(byCell.get(b))[i]),sector.centre.map(x=>2*x));
const groupedN=[...expectedTips.map(cells=>({kind:'opposite-tips',cells})),...sector.cells.filter(c=>c.role==='neutron'&&!expectedTips.flat().includes(c.id)).map(c=>({kind:'single',cells:[c.id]}))];
assert.equal(groupedN.length,16);

function validateEntry(reading,interfaces){
 const adjacent=(a,b)=>interfaces.some(f=>f.ports.every(p=>p.startsWith(a+'@')||p.startsWith(b+'@'))&&f.ports.some(p=>p.startsWith(a+'@'))&&f.ports.some(p=>p.startsWith(b+'@')));
 assert.deepEqual(reading.layerProfile.map(l=>l.P+l.N+l.E),[1,4,4,12,9,12,4,4,1]);
 const P=[...new Set(reading.contexts.map(c=>c.P))],E=[...new Set(reading.contexts.map(c=>c.E))];
 assert.equal(P.length,2);assert.equal(E.length,2);assert.equal(reading.contexts.length,4);
 assert.equal(new Set(reading.contexts.map(c=>c.channelOccurrence)).size,4);
 for(const p of P)for(const e of E)assert.equal(reading.contexts.filter(c=>c.P===p&&c.E===e).length,1);
 for(const c of reading.contexts)for(const ref of [c.P,c.E]){assert(adjacent(reading.incomingN,ref));assert(adjacent(ref,c.channelOccurrence));}
 assert.equal(reading.comparisons.length,4);assert.equal(reading.outer.length,8);
 for(const c of reading.comparisons){
  assert.equal(c.inputs.length,2);
  const operands=c.inputs.map(id=>reading.contexts.find(x=>x.channelOccurrence===id));
  assert(operands.every(Boolean));
  const ref=c.kind==='compare-P-at-shared-E'?'E':'P';
  assert(operands.every(x=>x[ref]===c.sharedReference));
  assert(operands[0][ref==='E'?'P':'E']!==operands[1][ref==='E'?'P':'E']);
  for(const id of c.inputs)assert(adjacent(c.cell,id));
 }
}
const uniqueStars=new Set();
const readings=sites.readings.map(reading=>{
 validateEntry(reading,sites.interfaces);
 const d=domain.readings.find(r=>r.id===reading.id);
 const cones=d.overlaps.filter(o=>o.residualCycleRank).map(cone=>{
  assert.equal(cone.paths.length,16);assert.equal(cone.moves.length,20);
  const sweep=comparisonSphereSweep(sector,cone);
  assert.equal(sweep.cellIds.length,14);
  uniqueStars.add([...sweep.cellIds].sort().join('|'));
  return {source:cone.source,target:cone.target,cellIds:sweep.cellIds,paths:cone.paths,moves:cone.moves,cycleBasis:cone.cycleBasis,sweep,operationMap:null};
 });
 assert.equal(cones.length,6);
 const entry=cones.find(c=>c.source===reading.incomingN);assert(entry);
 assert(reading.outer.every(o=>!entry.cellIds.includes(o.cell)));
 // Shared-reference comparisons form ONE four-cycle, not two circle factors.
 const squareVertices=reading.contexts.map(c=>c.channelOccurrence).sort();
 const squareEdges=reading.comparisons.map(c=>({vertices:c.inputs,comparisonCell:c.cell,kind:c.kind,sharedReference:c.sharedReference}));
 for(const v of squareVertices)assert.equal(squareEdges.filter(e=>e.vertices.includes(v)).length,2);
 const walk=[squareVertices[0]];
 while(walk.length<4){const next=squareEdges.filter(e=>e.vertices.includes(walk.at(-1))).flatMap(e=>e.vertices).filter(v=>!walk.includes(v)).sort()[0];assert(next);walk.push(next);}
 assert(squareEdges.some(e=>e.vertices.includes(walk[3])&&e.vertices.includes(walk[0])));
 for(const kind of new Set(squareEdges.map(e=>e.kind))){const pair=squareEdges.filter(e=>e.kind===kind);assert.equal(pair.length,2);assert.equal(new Set(pair.flatMap(e=>e.vertices)).size,4);}
 const referenceSquare={vertices:squareVertices,edges:squareEdges,coordinateWalk:walk,coordinateChoice:'lexical audit coordinate only; not phase orientation',cycleRank:1,eachComparisonKind:'two disjoint edges, not a circle',circleRealization:null,secondCircleFactor:null,joinWeight:null,diagonalAction:null};
 const overlaps=[];
 for(let i=0;i<cones.length;i++)for(let j=i+1;j<cones.length;j++){
  const shared=cones[i].cellIds.filter(c=>cones[j].cellIds.includes(c));
  if(shared.length)overlaps.push({cones:[i,j],sharedCells:shared,transition:null});
 }
 return {...reading,referenceSquare,cones,coneOverlaps:overlaps,comparisons:d.comparisons};
});
assert.equal(uniqueStars.size,6);
const hostileDuplicate=structuredClone(sites.readings[0]);hostileDuplicate.contexts[1]=hostileDuplicate.contexts[0];
assert.throws(()=>validateEntry(hostileDuplicate,sites.interfaces));
const hostileMissingComparison=structuredClone(sites.readings[0]);hostileMissingComparison.comparisons.pop();
assert.throws(()=>validateEntry(hostileMissingComparison,sites.interfaces));
const hostileReference=structuredClone(sites.readings[0]);hostileReference.comparisons[0].sharedReference='absent';
assert.throws(()=>validateEntry(hostileReference,sites.interfaces));
const incoming=sites.readings[0].incomingN;
assert.throws(()=>validateEntry(sites.readings[0],sites.interfaces.filter(f=>!f.ports.some(p=>p.startsWith(incoming+'@')))));
const sources=['research/strominger/sulfur-32-reversible-channel-specification.md','research/strominger/sulfur-operation-reconstruction-v1.md','research/strominger/pe-symmetric-sector.mjs','research/realization-tower/five-side-oct-routing-obligations.mjs','research/realization-tower/five-side-oct-comparison-domain.mjs','research/strominger/five-side-oct-hopf-probe.mjs','research/strominger/checkers/check_su32_hopf_fixture.mjs'];
const hashes={};for(const p of sources)hashes[p]=createHash('sha256').update(await fs.readFile(p)).digest('hex');
const report={schema:'su32.hopf-fixture.v1',status:'passed-incidence-and-hostile-checks',obligation:'route/coherencer compatibility preceded by attachment transport',edgeUnits:3,inventory:sites.inventory,groupedN,cells:sector.cells,interfaces:sites.interfaces,boundary:sites.boundaries,readings,uniqueStars:uniqueStars.size,negativeControls:['duplicate reference-product member','deleted comparison edge','wrong shared reference','deleted incoming interfaces'],sourceHashes:hashes,nativeHopfBinding:false,scope:'Six readings of the same 51-cell carrier. Null operation maps and transitions remain null. Six vertex stars are not six independent phase sources. Opposite-tip groups are not proved path identifications.'};
if(process.argv.includes('--record')){const out='research/strominger/results/su32-hopf-tests-v1';await fs.mkdir(out,{recursive:true});await fs.writeFile(`${out}/fixture.json`,JSON.stringify(report,null,2)+'\n');}
console.log(JSON.stringify({status:report.status,inventory:report.inventory,readings:readings.length,uniqueStars:uniqueStars.size,conesPerReading:readings.map(r=>r.cones.length),negativeControls:report.negativeControls,nativeHopfBinding:false},null,2));
