// Build one global support complex from native reference-cell identities.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,reconcileBothOrders} from '../su32-layer4-comparison.mjs';
const fixturePath='research/strominger/results/su32-hopf-tests-v1/fixture.json';
const fixture=JSON.parse(await fs.readFile(fixturePath,'utf8'));
for(const [p,h] of Object.entries(fixture.sourceHashes))assert.equal(createHash('sha256').update(await fs.readFile(p)).digest('hex'),h);
const atlas=buildSu32SignedReferenceAtlas(fixture);
const vertices=[...new Set(atlas.charts.flatMap(c=>[...c.P,...c.E]))].sort();
// A single declared rational test field, restricted to every chart. Not physical amplitudes.
const globalField=Object.fromEntries(vertices.map((v,i)=>[v,i+1]));
const facets=new Map(),occurrences=[];
for(const chart of atlas.charts)for(const p of [0,1])for(const e of [0,1]){
 const layout=comparisonLayout(atlas,fixture,chart.id,[p,e]);
 const referenceByLabel=Object.fromEntries(Object.entries(layout.template.referenceBinding).map(([cell,label])=>[label,cell]));
 const registry=Object.fromEntries(Object.entries(referenceByLabel).map(([label,cell])=>[label,globalField[cell]]));
 const built=reconcileBothOrders(layout,registry);
 const supports=built.comparisons.map(n=>{
  const refs=Object.values(n.records).map(r=>r.referenceCell).sort();
  assert.equal(new Set(refs).size,3);facets.set(JSON.stringify(refs),refs);
  const src=layout.template.comparisons.find(c=>c.cell===n.at);
  return {cell:n.at,sharedRole:src.sharedRole,refs,inputs:n.children.map(c=>c.at)};
 });
 const cyclicLabels=['P+','E+','P-','E-'];
 const square=cyclicLabels.map(k=>referenceByLabel[k]);
 const key=xs=>JSON.stringify([...xs].sort());
 assert.deepEqual(new Set(Object.values(built.channels).map(n=>key(Object.values(n.records).map(r=>r.referenceCell)))),new Set(square.map((v,i)=>key([v,square[(i+1)%4]]))));
 for(const [role,tris] of [['E',[[0,1,2],[0,2,3]]],['P',[[0,1,3],[1,2,3]]]]){
  assert.deepEqual(new Set(supports.filter(s=>s.sharedRole===role).map(s=>key(s.refs))),new Set(tris.map(t=>key(t.map(i=>square[i])))));
 }
 for(const n of [built.byE,built.byP])for(const r of Object.values(n.records))assert.equal(r.payload,globalField[r.referenceCell]);
 occurrences.push({chartId:chart.id,binding:[p,e],square,supports,target:chart.target});
}
const paths=[fixturePath,'research/strominger/su32-layer4-comparison.mjs','research/strominger/su32-signed-reference-encoder.mjs','research/strominger/checkers/export_su32_comparison_support.mjs'];
const sourceHashes={};for(const p of paths)sourceHashes[p]=createHash('sha256').update(await fs.readFile(p)).digest('hex');
const report={schema:'su32.comparison-support.v1',vertices,facets:[...facets.values()].sort((a,b)=>JSON.stringify(a).localeCompare(JSON.stringify(b))),globalField,occurrences,sourceHashes,
 scope:'Global abstract complex of reference supports, not a triangulation of spatial cells. Rational cochains are an added mathematical linearization; signed labels remain directions.'};
const dir='research/strominger/results/su32-cochain-transfer-v1';await fs.mkdir(dir,{recursive:true});await fs.writeFile(`${dir}/support.json`,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({passed:true,vertices:vertices.length,triangles:facets.size,occurrences:occurrences.length,globalFieldChecked:true}));
