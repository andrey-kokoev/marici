import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildFiveSideOctComparisonDomain} from '../../realization-tower/five-side-oct-comparison-domain.mjs';
const digest=x=>createHash('sha256').update(x).digest('hex');

// Exact translation normalization of the native geometry AND presentation
// graph, not merely a comparison of node counts. Does not transport maps.
export function normalizedComparisonGeometry(sector,overlap){
 const cells=new Map(sector.cells.map(c=>[c.id,c])),source=cells.get(overlap.source),origin=[0,1,2,3].map(i=>Math.min(...source.vertices.map(p=>p[i])));
 const cell=id=>{const c=cells.get(id);return `${c.role}:${c.vertices.map(p=>p.map((x,i)=>x-origin[i]).join(',')).sort().join('|')}`;};
 const paths=new Map(overlap.paths.map(p=>[p.id,JSON.stringify(p.cells.map(cell))]));
 return JSON.stringify({paths:[...paths.values()].sort(),moves:overlap.moves.map(m=>JSON.stringify({presentations:[paths.get(m.from),paths.get(m.to)].sort(),position:m.position})).sort()});
}
export function summarizeComparisonDomain(radius){
 const sector=buildPESymmetricSector(radius),readings=[];let representative;
 for(let axis=0;axis<3;axis++)for(const sign of [-1,1]){
  const id=`reading:${axis}:${sign}`,r=buildFiveSideOctComparisonDomain(sector,{readingIds:[id]}).readings[0],residual=r.overlaps.filter(o=>o.residualCycleRank),templates=new Set();
  for(const o of residual){
   const sig=digest(normalizedComparisonGeometry(sector,o));templates.add(sig);
   assert.equal(o.source.split(':')[0],'neutron');assert.equal(o.target.split(':')[0],'neutron');
   assert.deepEqual([o.paths.length,o.moves.length,o.cycleRank,o.disjointSquareRank,o.residualCycleRank],[16,20,5,4,1]);
   if(!representative)representative={reading:id,geometryDigest:sig,diagram:o};
  }
  assert.equal(templates.size,1,'Residual comparison diagrams are not exact translates');
  assert(r.prefixChecks.every(c=>!c.representableBySameAxisNPassages&&c.turns.every(t=>t.entryAxis!==t.exitAxis&&t.commonEdgeVertices.length===2)));
  readings.push({id,summary:r.summary,prefixChecks:r.prefixChecks,translationTemplateCount:templates.size,residualSites:residual.map(o=>({source:o.source,target:o.target,geometryDigest:digest(normalizedComparisonGeometry(sector,o))}))});
 }
 return {radius,edgeUnits:sector.edgeUnits,readings,representative};
}
async function main(){
 const small=summarizeComparisonDomain(1),large=summarizeComparisonDomain(2);
 for(let i=0;i<6;i++)assert.equal(small.readings[i].residualSites[0].geometryDigest,large.readings[i].residualSites[0].geometryDigest,'Size-dependent comparison template');
 const paths=['research/strominger/five-side-oct-comparison-domain-v1.md','tests/five-side-oct-comparison-domain.test.mjs','research/realization-tower/five-side-oct-comparison-domain.mjs','research/realization-tower/five-side-oct-routing-obligations.mjs','research/strominger/pe-symmetric-sector.mjs','research/strominger/sulfur-32-reversible-channel-specification.md','research/strominger/source-incidence-selects-the-coherence-nerve.md','research/strominger/checkers/check_five_side_oct_comparison_domain.mjs'];
 const evidence=[];for(const path of paths)evidence.push({path,sha256:digest(await fs.readFile(path))});
 const report={schema:'five-side-oct.comparison-domain-receipt.v1',status:'incidence-and-representation-obstruction-verified',constructionAdmitted:false,scope:'Native incidence, exact geometric translations, and finite GF(2) presentation-graph cycle ranks only. Not a nonabelian coherence/filling computation, a new channel count, or a complete obligation complex.',small,large,evidence};
 if(process.argv.includes('--record')){const dir='research/strominger/results/five-side-oct-comparison-domain-v1';await fs.mkdir(dir,{recursive:true});await fs.writeFile(`${dir}/verification.json`,JSON.stringify(report,null,2)+'\n');}
 console.log(JSON.stringify({status:report.status,constructionAdmitted:false,small:small.readings[0].summary,large:large.readings[0].summary,readingsChecked:12,exactTranslatedResidualTemplate:true,knownPrefixBoundariesExcludedByOldAxisGrammar:large.readings.reduce((n,r)=>n+r.summary.prefixBoundariesExcludedByOldAxisGrammar,0)},null,2));
}
// Keep normalization available to independent tests without running the receipt.
if(process.argv[1]?.replaceAll('\\','/').endsWith('/check_five_side_oct_comparison_domain.mjs'))await main();
