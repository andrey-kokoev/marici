// Test one geometry-derived comparison against full preparation and continuation.
// Does not compile a new Agda admission or select a physical comparison policy.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildFiveSideOctComparisonDomain} from '../../realization-tower/five-side-oct-comparison-domain.mjs';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,channelOperand} from '../su32-layer4-comparison.mjs';
const root='research/strominger',sector=buildPESymmetricSector(1),byCell=new Map(sector.cells.map(c=>[c.id,c]));
const domain=buildFiveSideOctComparisonDomain(sector,{readingIds:['reading:0:-1']}).readings[0];
const cone=domain.overlaps.find(o=>o.length===4&&o.source==='neutron:0,0,2,1'&&o.residualCycleRank);
const move=cone.moves.find(m=>m.position===2),A=cone.paths.find(p=>p.id===move.from),B=cone.paths.find(p=>p.id===move.to);
const shape=vs=>vs.map(v=>v.join(',')).sort().join('|'),cellAt=new Map(sector.cells.map(c=>[shape(c.vertices),c.id]));
const perms=xs=>xs.length?xs.flatMap((x,i)=>perms(xs.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];
const candidates=[];
for(const permutation of perms([0,1,2,3])){
 const point=v=>permutation.map((j,i)=>v[j]+sector.centre[i]-sector.centre[j]);
 const cells=new Map(sector.cells.map(c=>[c.id,cellAt.get(shape(c.vertices.map(point)))]));
 if([...cells.values()].some(x=>!x))continue;
 if(A.cells.every((c,i)=>cells.get(c)===B.cells[i]))candidates.push({permutation,point,cells});
}
assert.equal(candidates.length,1);const sigma=candidates[0];assert.deepEqual(sigma.permutation,[0,1,3,2]);
for(const c of sector.cells){assert.equal(byCell.get(sigma.cells.get(c.id)).role,c.role);assert.equal(sigma.cells.get(sigma.cells.get(c.id)),c.id);}
const arrowAt=new Map(domain.arrows.map(a=>[JSON.stringify([a.from,a.to]),a])),arrowMap=new Map();
for(const a of domain.arrows){
 const image=arrowAt.get(JSON.stringify([sigma.cells.get(a.from),sigma.cells.get(a.to)]));assert(image);
 assert.equal(shape(sector.faces.find(f=>f.id===a.id).vertices.map(sigma.point)),image.id);arrowMap.set(a.id,image.id);
}
assert.deepEqual(A.arrows.map(a=>arrowMap.get(a)),B.arrows);
const fixturePath=root+'/results/su32-hopf-tests-v1/fixture.json',fixture=JSON.parse(await fs.readFile(fixturePath,'utf8'));
const digest=async p=>createHash('sha256').update(await fs.readFile(p)).digest('hex');
for(const [p,h] of Object.entries(fixture.sourceHashes))assert.equal(await digest(p),h);
const atlas=buildSu32SignedReferenceAtlas(fixture),chart=atlas.charts.find(c=>c.reading===domain.id&&c.source===cone.source&&c.target===cone.target);
assert(chart);const layout=comparisonLayout(atlas,fixture,chart.id,[0,0]),refs=layout.template.referenceBinding;
const labelMap=Object.fromEntries(Object.entries(refs).map(([cell,label])=>[label,refs[sigma.cells.get(cell)]]));
assert.deepEqual(labelMap,{'P+':'P-','P-':'P+','E+':'E+','E-':'E-'});
const registry=Object.fromEntries(Object.values(refs).map(label=>[label,{id:'input:'+label,opaque:{tag:label},entry:{cell:cone.source,slot:label}}]));
const transportRegistry=r=>Object.fromEntries(Object.entries(r).map(([label,value])=>[labelMap[label],structuredClone(value)]));
const transported=transportRegistry(registry);assert.deepEqual(transportRegistry(transported),registry);assert.notDeepEqual(transported,registry);
const left=channelOperand(layout,A.cells[2],registry),rightFixed=channelOperand(layout,B.cells[2],registry),rightTransported=channelOperand(layout,B.cells[2],transported);
const movedLeft={...structuredClone(left),at:sigma.cells.get(left.at),records:Object.fromEntries(Object.entries(left.records).map(([label,r])=>
 [labelMap[label],{referenceCell:sigma.cells.get(r.referenceCell),payload:structuredClone(r.payload)}]))};
assert.deepEqual(movedLeft,rightTransported);assert.notDeepEqual(movedLeft,rightFixed);
// Changing binding rather than registry gives the same distinction: it is not
// the requested target with the original preparation AND original binding.
const movedLayout=comparisonLayout(atlas,fixture,chart.id,[1,0]);
const reindexed=channelOperand(movedLayout,B.cells[2],registry);
assert.equal(reindexed.records['P+'].referenceCell,sigma.cells.get(left.records['P+'].referenceCell));
assert.deepEqual(reindexed.records['P+'].payload,left.records['P+'].payload);assert.notDeepEqual(reindexed,rightFixed);
const outgoing=domain.arrows.filter(a=>a.from===cone.target);assert(outgoing.length>0);
const suffixes=outgoing.map(e=>{
 const transportedEdge=arrowMap.get(e.id);assert(transportedEdge);
 assert.deepEqual([...A.arrows,e.id].map(id=>arrowMap.get(id)),[...B.arrows,transportedEdge]);
 return {sourceEdge:e.id,transportedEdge,target:e.to,transportedTarget:sigma.cells.get(e.to),unchangedEdgePermitted:e.id===transportedEdge};
});
const changedSuffix=suffixes.find(s=>!s.unchangedEdgePermitted);assert(changedSuffix);
assert.notDeepEqual([...A.arrows,changedSuffix.sourceEdge].map(id=>arrowMap.get(id)),[...B.arrows,changedSuffix.sourceEdge]);
const sourceHashes={};for(const p of [root+'/checkers/check_su32_comparison_license.mjs',root+'/pe-symmetric-sector.mjs',
 root+'/su32-signed-reference-encoder.mjs',root+'/su32-layer4-comparison.mjs',fixturePath,
 'research/realization-tower/five-side-oct-comparison-domain.mjs','research/realization-tower/five-side-oct-routing-obligations.mjs',
 root+'/agda/NativeExtensionFamilyAudit.agda',root+'/agda/InternalSourceComparisons.agda',root+'/agda/CanonicalComparisonSynthesis.agda'])sourceHashes[p]=await digest(p);
const result={schema:'su32.comparison-license-audit.v1',passed:true,nativeSu32ComparisonCompiled:false,
 sourceRule:{implementation:'agda/InternalSourceComparisons.agda: compare / derivation',
 obligations:['Actual operand packages and their native derivations','Carrier equivalence with selected-value agreement','Whole-carrier reader law under a declared mode','Continuation via the transported outgoing-edge family'],
 inspectedNotRecompiled:true,scope:'The existing concrete Body/Fragment uses a different four-vertex source graph; no Su-32 instantiation is inferred.'},
 paths:{left:A,right:B},symmetry:{searchedCoordinatePermutations:24,matchingSymmetries:1,permutation:sigma.permutation,
 physicalFormula:['q0','q1','q3+1','q2-1'],nativeCellsChecked:sector.cells.length,orientedInterfacesChecked:arrowMap.size,labelMap},
 preparationTest:{registry,transportedRegistry:transported,left,transportedLeft:movedLeft,rightAtOriginalPreparation:rightFixed,
 rightAtTransportedPreparation:rightTransported,rightAtChangedBinding:reindexed,
 selectedValueLawAtOriginalPreparation:false,selectedValueLawAfterTransport:true},
 continuationTest:{fixedTerminalCell:cone.target,suffixes,untransportedEdgeCounterexample:changedSuffix},
 conclusion:'The unique coordinate symmetry carrying these paths into one another transports the P reference slots. It compares the left preparation with the transported right preparation, not the right path at the original fixed preparation. Continuations must also be transported despite the fixed terminal cell.',
 residual:'A Su-32 record/reader/mode binding and native operand derivations are still required. A source symmetry is not automatically the desired same-preparation reconciliation; no result excludes another admitted contextual comparison.',sourceHashes};
const dir=root+'/results/su32-comparison-license-v1';await fs.mkdir(dir,{recursive:true});await fs.writeFile(dir+'/verification.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({passed:true,nativeSu32ComparisonCompiled:false,symmetry:result.symmetry,
 fixedPreparationPointedness:false,transportedPreparationPointedness:true,
 suffixesChecked:suffixes.length,suffixesRequiringTransport:suffixes.filter(s=>!s.unchangedEdgePermitted).length,
 conclusion:result.conclusion,residual:result.residual},null,2));
