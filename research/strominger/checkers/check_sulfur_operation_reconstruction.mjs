// Incidence reconstruction for the operator's four-stage hypothesis.
// No additive/product/quartic algebra, routes or fillers are invented here.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildFiveSideOctRoutingObligations} from '../../realization-tower/five-side-oct-routing-obligations.mjs';
import {buildFiveSideOctComparisonDomain} from '../../realization-tower/five-side-oct-comparison-domain.mjs';
import {nativeToOrthogonal,comparisonSphereSweep} from '../five-side-oct-hopf-probe.mjs';
const centre=c=>c.vertices[0].map((_,i)=>c.vertices.reduce((s,p)=>s+p[i],0)/c.vertices.length),results=[];
for(const radius of [1,2]){
 const sector=buildPESymmetricSector(radius),obligations=buildFiveSideOctRoutingObligations(sector),byId=new Map(sector.cells.map(c=>[c.id,c])),adj=new Map(sector.cells.map(c=>[c.id,new Set()]));
 for(const f of sector.faces)if(f.owners.length===2){const[a,b]=f.owners;adj.get(a).add(b);adj.get(b).add(a);}
 for(const reading of obligations.readings){
  const axis=Number(reading.id.split(':')[1]),sign=reading.sign,other=[0,1,2].filter(i=>i!==axis),top=sector.edgeUnits-1;
  const coords=c=>nativeToOrthogonal(centre(c),sector.centre),height=c=>sign*coords(c)[axis],layers=new Map();
  for(const c of sector.cells){const h=height(c);if(h<0)continue;const index=1+2*(top-h),key=`${index}:${c.role}`;if(!layers.has(key))layers.set(key,{layer:index,role:c.role,points:[],cells:[]});const p=coords(c),u=p[other[0]]+p[other[1]],v=p[other[0]]-p[other[1]];layers.get(key).points.push([u,v]);layers.get(key).cells.push(c.id);}
  const grids=[...layers.values()].sort((a,b)=>a.layer-b.layer||a.role.localeCompare(b.role)).map(l=>{
   const rows=[...new Set(l.points.map(p=>p[0]))].sort((a,b)=>a-b),columns=[...new Set(l.points.map(p=>p[1]))].sort((a,b)=>a-b),points=new Set(l.points.map(p=>p.join(',')));
   assert.equal(points.size,rows.length*columns.length);for(const u of rows)for(const v of columns)assert(points.has([u,v].join(',')));
   return {layer:l.layer,role:l.role,shape:[rows.length,columns.length],cells:l.cells};
  });
  for(let k=1;k<=sector.edgeUnits;k++){
   assert.deepEqual(grids.find(g=>g.layer===2*k-1&&g.role==='neutron').shape,[k,k]);
   if(k<sector.edgeUnits)for(const role of ['proton','electron'])assert.deepEqual([...grids.find(g=>g.layer===2*k&&g.role===role).shape].sort((a,b)=>a-b),[k,k+1]);
  }
  const P=[...new Set(reading.contexts.map(c=>c.P))],E=[...new Set(reading.contexts.map(c=>c.E))];assert.equal(P.length,2);assert.equal(E.length,2);
  for(const p of P)for(const e of E)assert.equal(reading.contexts.filter(c=>c.P===p&&c.E===e).length,1);
  const diamonds=reading.contexts.map(c=>{for(const reference of [c.P,c.E]){assert(adj.get(reading.incomingN).has(reference));assert(adj.get(reference).has(c.channelOccurrence));}return {jointN:c.channelOccurrence,paths:[[reading.incomingN,c.P,c.channelOccurrence],[reading.incomingN,c.E,c.channelOccurrence]],operationComparison:null};});
  const common=[...adj.get(reading.comparisons[0].cell)].filter(id=>reading.comparisons.every(c=>adj.get(c.cell).has(id))&&byId.get(id).role==='neutron'&&height(byId.get(id))===top-2);
  assert.equal(common.length,1);
  const domain=buildFiveSideOctComparisonDomain(sector,{readingIds:[reading.id]}).readings[0],residuals=domain.overlaps.filter(o=>o.residualCycleRank),cone=residuals.find(o=>o.source===reading.incomingN&&o.target===common[0]);assert(cone);assert.equal(cone.paths.length,16);assert.equal(cone.moves.length,20);
  const sweep=comparisonSphereSweep(sector,cone),coneCells=new Set(cone.paths.flatMap(p=>p.cells));for(const c of reading.comparisons)assert(coneCells.has(c.cell));for(const c of reading.outer)assert(!coneCells.has(c.cell));
  const starts={};for(const o of residuals){const layer=1+2*(top-height(byId.get(o.source)));starts[layer]=(starts[layer]??0)+1;}
  assert.deepEqual(Object.values(starts),radius===1?[1,4,1]:[1,4,9,16,9,4,1]);
  results.push({edgeUnits:sector.edgeUnits,reading:reading.id,grids,firstTwoStepDiamonds:diamonds,layer4Comparisons:reading.comparisons.map(c=>({cell:c.cell,kind:c.kind,inputs:c.inputs,sharedReference:c.sharedReference})),outerCellsRetained:reading.outer,
   firstFourInterfaceCone:{source:cone.source,target:cone.target,sourceLayer:1,targetLayer:5,cellIds:sweep.cellIds,presentations:16,moves:20,sphereSweepDegrees:sweep.sweeps.map(s=>s.degreeRelativeToFirstSweep),filling:null},residualConesBySourceLayer:starts});
 }
}
const sources=['research/strominger/sulfur-operation-reconstruction-v1.md','research/strominger/sulfur-32-reversible-channel-specification.md','research/strominger/global-coherence-standing-assumption.md','research/nima/binary-arity-square-is-the-duoidal-skeleton.md','research/nima/gray-coherence-cube-refactors-the-arity-tetrahedron.md','research/strominger/primitive-packet-type-instance-v1.md','research/strominger/routing-and-quartic-experiments-v1.md','research/strominger/pe-symmetric-sector.mjs','research/realization-tower/five-side-oct-routing-obligations.mjs','research/realization-tower/five-side-oct-comparison-domain.mjs','research/strominger/five-side-oct-hopf-probe.mjs','research/strominger/checkers/check_sulfur_operation_reconstruction.mjs'];
const evidence=[];for(const path of sources)evidence.push({path,sha256:createHash('sha256').update(await fs.readFile(path)).digest('hex')});
const report={schema:'sulfur.operation-reconstruction.v1',constructionAdmitted:false,operationBindingAdmitted:false,quarticMeaningEstablished:false,status:'four-stage incidence skeleton reconstructed; operation dictionary remains conditional',results,evidence,
 scope:'Grid axes are not identified with additive/multiplicative actions. A four-input interchange is not proof of a quartic interaction. The source duoidal theorem requires its own occurrence/factor and transversality adapters. Repeated cone geometry supplies overlapping obligations, not an iteration rule or automatic fillers.'};
if(process.argv.includes('--record')){const dir='research/strominger/results/sulfur-operation-reconstruction-v1';await fs.mkdir(dir,{recursive:true});await fs.writeFile(`${dir}/verification.json`,JSON.stringify(report,null,2)+'\n');}
console.log(JSON.stringify({status:report.status,operationBindingAdmitted:false,readings:results.length,small:results.filter(r=>r.edgeUnits===3).map(r=>({reading:r.reading,coneLayers:[1,5],allConeStarts:r.residualConesBySourceLayer})),large:results.filter(r=>r.edgeUnits===5).map(r=>({reading:r.reading,coneLayers:[1,5],allConeStarts:r.residualConesBySourceLayer}))},null,2));
