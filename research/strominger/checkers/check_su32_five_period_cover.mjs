import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildNativeAxisPortGraph} from '../native-axis-port-graph.mjs';
import {buildSulfur32Wiring,groupSulfurPayloads,restoreSulfurPayloads} from '../../realization-tower/sulfur-32-wiring.mjs';
import {fiveCoverCharacters,periodCoordinates,characterValue,projectNativeWindow,buildFivePeriodCover} from '../sulfur-period-covers.mjs';
const root='research/strominger',base=buildSulfur32Wiring(),sector=buildPESymmetricSector(2),bulk=buildNativeAxisPortGraph(sector);
const projection=projectNativeWindow(sector,bulk,base),byPort=new Map(projection.ports.map(p=>[p.physicalPort,p]));
const chars=fiveCoverCharacters();assert.equal(chars.length,31);
assert.throws(()=>periodCoordinates([1,-1,0,0]));assert.throws(()=>buildFivePeriodCover(base,[0,0,0]));
const points=[];for(let a=0;a<5;a++)for(let b=0;b<5;b++)for(let c=0;c<5;c++)points.push([a,b,c]);
const kernels=chars.map(v=>points.filter(p=>characterValue(v,p)===0).map(p=>p.join(',')).join('|'));
assert.equal(new Set(kernels).size,31);assert(chars.every(v=>points.filter(p=>characterValue(v,p)===0).length===25));
for(const v of points.filter(p=>p.some(Boolean))){
 const kernel=points.filter(p=>characterValue(v,p)===0).map(p=>p.join(',')).join('|');assert(kernels.includes(kernel));
}
const occurrenceCounts=base.groups.map(g=>({baseCell:g.id,role:g.role,count:projection.cells.filter(c=>c.baseCell===g.id).length}));
assert(occurrenceCounts.filter(c=>c.role!=='neutron').every(c=>c.count===5));
const edgeKey=(from,to,kind)=>JSON.stringify([kind,...[from,to].sort()]);
const cases=[];let projectionEdgeChecks=0,payloadRoundTrips=0;
for(const character of chars){
 const cover=buildFivePeriodCover(base,character),prefix='c5:'+character.join(',')+':';
 const lift=(id,a)=>prefix+id+'@'+characterValue(character,a);
 const mapped=new Map(projection.ports.map(p=>[p.physicalPort,lift(p.basePort,p.periodCoordinates)]));
 const coverEdges=new Set(cover.edges.map(e=>edgeKey(e.from,e.to,e.kind)));
 for(const e of bulk.edges){assert(coverEdges.has(edgeKey(mapped.get(e.from),mapped.get(e.to),e.kind==='shared-native-face'?'shared-quotient-face':e.kind)));projectionEdgeChecks++;}
 const wireAt=new Map(cover.wires.flatMap(w=>w.ports.map(p=>[p,w.id])));
 for(const c of bulk.components)assert.equal(new Set(c.ports.map(p=>wireAt.get(mapped.get(p)))).size,1);
 const coverage={};for(const role of ['proton','neutron','electron']){
  const groups=cover.groups.filter(g=>g.role===role);assert.equal(groups.length,80);
  const fibres=new Map(groups.map(g=>[g.id,[]]));
  for(const c of projection.cells.filter(c=>c.role===role))fibres.get(lift(c.baseCell,c.periodCoordinates)).push(c.physicalCell);
  const collision=[...fibres].find(([,cs])=>cs.length>1),histogram={};for(const cs of fibres.values())histogram[cs.length]=(histogram[cs.length]??0)+1;
  coverage[role]={covered:[...fibres.values()].filter(cs=>cs.length>0).length,missing:histogram[0]??0,occupancyHistogram:histogram,
   collisionWitness:collision?{coverCell:collision[0],physicalCells:collision[1]}:null};
 }
 assert.equal(cover.wires.length,320);
 // Arbitrary distinct wire contents remain intact in both inherited presentations.
 const rows=cover.wires.map((w,i)=>({wire:w.id,payload:{index:i,opaque:[null,false,{character}]}}));
 for(const direction of ['P|E','E|P']){
  const grouped=groupSulfurPayloads(cover,rows,direction);assert.equal(grouped.length,80);
  assert.deepEqual(restoreSulfurPayloads(grouped),[...rows].sort((a,b)=>a.wire.localeCompare(b.wire)));payloadRoundTrips++;
 }
 // Collision of actual same-axis ports, not merely equality of a compressed cell count.
 const cs=coverage.proton.collisionWitness?.physicalCells;assert(cs&&cs.length>=2);
 const ps=cs.slice(0,2).map(cell=>bulk.ports.find(p=>p.cell===cell&&p.axis===0));assert.notEqual(ps[0].id,ps[1].id);
 assert.equal(mapped.get(ps[0].id),mapped.get(ps[1].id));
 const noncollapseWitness={physicalPorts:ps.map(p=>p.id),commonCoverPort:mapped.get(ps[0].id),
  incompatibleContents:[{opaque:'A'},{opaque:'B'}],reason:'One cover-port value cannot realize both distinct prescribed physical-port contents.'};
 cases.push({character,counts:cover.counts,coverage,noncollapseWitness,
  windowRealizationPassed:coverage.proton.covered===80&&coverage.electron.covered===80});
}
const success=cases.filter(c=>c.windowRealizationPassed);assert.equal(success.length,0);
const sourceHashes={};for(const p of [root+'/contracts/su32-five-period-cover-v1.json',root+'/sulfur-period-covers.mjs',
 root+'/native-axis-port-graph.mjs',root+'/pe-symmetric-sector.mjs',root+'/checkers/check_su32_five_period_cover.mjs',
 'research/realization-tower/sulfur-32-wiring.mjs'])sourceHashes[p]=createHash('sha256').update(await fs.readFile(p)).digest('hex');
const histogram={};for(const c of cases){const key=['proton','neutron','electron'].map(r=>c.coverage[r].covered).join('/');histogram[key]=(histogram[key]??0)+1;}
const summary={covers:31,projectionEdgeChecks,payloadRoundTrips,coveredCellHistogramPNE:histogram,
 maximumPWindowCoverage:Math.max(...cases.map(c=>c.coverage.proton.covered)),maximumEWindowCoverage:Math.max(...cases.map(c=>c.coverage.electron.covered)),windowRealizations:success.length};
const result={schema:'su32.five-period-cover.v1',passed:true,windowRealizationPassed:false,
 conclusion:'All 31 five-sheeted period covers exist and receive every native bulk edge, but none separates the 80 physical P/E cell occurrences. Five-per-base-cell multiplicity does not make this window a fundamental domain.',
 summary,baseOccurrenceCounts:occurrenceCounts,physicalProjection:projection,cases,sourceHashes,
 disposition:'Reject the five-sheeted period-cover realization of this fixed window; retain the cover family as a conditional construction, not an operator-authorized replacement carrier.',
 residual:'No source-justified non-periodic or richer-fibre realization of all 80 named physical P/E fibres has been constructed.'};
const dir=root+'/results/su32-five-period-cover-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({passed:true,windowRealizationPassed:false,summary,conclusion:result.conclusion,residual:result.residual},null,2));
