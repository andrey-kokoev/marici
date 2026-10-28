import test from 'node:test';
import assert from 'node:assert/strict';
import {buildPESymmetricSector} from '../research/strominger/pe-symmetric-sector.mjs';
import {buildFiveSideOctComparisonDomain} from '../research/realization-tower/five-side-oct-comparison-domain.mjs';
import {normalizedComparisonGeometry} from '../research/strominger/checkers/check_five_side_oct_comparison_domain.mjs';
const sector=buildPESymmetricSector(2),packet=buildFiveSideOctComparisonDomain(sector,{readingIds:['reading:0:-1']}),r=packet.readings[0];

test('comparison domain retains native paths and contexts without selecting a solution',()=>{
 assert.equal(packet.constructionAdmitted,false);assert.deepEqual(packet.selectedWireRoutes,[]);assert.deepEqual(packet.selectedGroups,[]);
 const faces=new Map(sector.faces.map(f=>[f.id,f])),arrows=new Map(r.arrows.map(a=>[a.id,a])),comparisons=new Map(r.comparisons.map(c=>[c.id,c]));
 assert.equal(r.arrows.length,560);assert.equal(r.comparisons.length,360);
 for(const a of r.arrows){assert.deepEqual(new Set(faces.get(a.id).owners),new Set([a.from,a.to]));assert(faces.get(a.id).vertices.every(v=>v[a.axis]===faces.get(a.id).vertices[0][a.axis]));}
 for(const c of r.comparisons){assert.equal(c.comparisonMap,null);assert.equal(c.fillingWitness,null);for(const p of c.alternatives){assert.equal(p.cells[0],c.source);assert.equal(p.cells[2],c.target);for(let i=0;i<2;i++){assert.equal(arrows.get(p.arrows[i]).from,p.cells[i]);assert.equal(arrows.get(p.arrows[i]).to,p.cells[i+1]);}}}
 for(const o of r.overlaps){
  const ps=new Map(o.paths.map(p=>[p.id,p]));
  for(const p of o.paths)for(let i=0;i<p.arrows.length;i++){assert.equal(arrows.get(p.arrows[i]).from,p.cells[i]);assert.equal(arrows.get(p.arrows[i]).to,p.cells[i+1]);}
  for(const m of o.moves){const a=ps.get(m.from),b=ps.get(m.to),c=comparisons.get(m.comparison);assert(c);assert.notEqual(a.cells[m.position],b.cells[m.position]);assert(a.cells.every((x,i)=>i===m.position||x===b.cells[i]));assert.equal(c.source,a.cells[m.position-1]);assert.equal(c.target,a.cells[m.position+1]);assert.deepEqual(m.contextBefore,a.arrows.slice(0,m.position-1));assert.deepEqual(m.contextAfter,a.arrows.slice(m.position+1));assert.equal(m.witness,null);}
 }
});
test('all source-required prefix boundaries require adjacent, not opposite, N faces',()=>{
 for(const radius of [1,2])for(let axis=0;axis<3;axis++)for(const sign of [-1,1]){
  const view=buildFiveSideOctComparisonDomain(buildPESymmetricSector(radius),{readingIds:[`reading:${axis}:${sign}`],maxLength:3}).readings[0];
  assert.equal(view.prefixChecks.length,4);
  for(const c of view.prefixChecks){assert.equal(c.representableBySameAxisNPassages,false);assert.equal(c.turns.length,2);for(const t of c.turns){assert.notEqual(t.entryAxis,t.exitAxis);assert.equal(t.commonEdgeVertices.length,2);assert.equal(t.commonEdgeVertices[0].reduce((s,x,i)=>s+(x-t.commonEdgeVertices[1][i])**2,0),2);}}
 }
});
function rank(rows){
 const pivots=new Map();
 for(const row of rows){let bits=new Set(row);while(bits.size){const p=Math.max(...bits);if(!pivots.has(p)){pivots.set(p,bits);break;}const next=new Set(bits);for(const e of pivots.get(p))next.has(e)?next.delete(e):next.add(e);bits=next;}}
 return pivots.size;
}
test('formal closed boundaries and disjoint interchange spans are independently checked',()=>{
 let residual=0;
 for(const o of r.overlaps){
  for(const c of o.cycleBasis){assert.equal(c.fillingWitness,null);for(let i=0;i<c.steps.length;i++){const step=c.steps[i],next=c.steps[(i+1)%c.steps.length],edge=o.moves[step.edge];assert.equal(step.to,next.from);assert.deepEqual(new Set([step.from,step.to]),new Set([edge.from,edge.to]));}}
  assert.equal(rank(o.cycleBasis.map(c=>c.steps.map(s=>s.edge))),o.cycleRank);
  for(const square of o.disjointSquares){const degree=new Map();for(const i of square)for(const n of [o.moves[i].from,o.moves[i].to])degree.set(n,(degree.get(n)??0)+1);assert.equal(degree.size,4);assert([...degree.values()].every(d=>d===2));const positions=[...new Set(square.map(i=>o.moves[i].position))].sort();assert.equal(positions.length,2);assert(positions[1]-positions[0]>=2);}
  assert.equal(rank(o.disjointSquares),o.disjointSquareRank);assert.equal(o.residualCycleRank,o.cycleRank-o.disjointSquareRank);residual+=o.residualCycleRank;
 }
 assert.equal(r.summary.formalCycleRank,768);assert.equal(r.summary.disjointSquareRank,724);assert.equal(residual,44);
 assert(r.overlaps.filter(o=>o.length===3).every(o=>o.cycleRank===0));
});
test('residual diagrams are exact translates, shared by small and large carriers',()=>{
 const residual=r.overlaps.filter(o=>o.residualCycleRank);assert.equal(residual.length,44);
 const signatures=new Set(residual.map(o=>normalizedComparisonGeometry(sector,o)));assert.equal(signatures.size,1);
 for(const o of residual)assert.deepEqual([o.paths.length,o.moves.length,o.cycleRank,o.disjointSquareRank,o.residualCycleRank],[16,20,5,4,1]);
 const small=buildPESymmetricSector(1),sr=buildFiveSideOctComparisonDomain(small,{readingIds:['reading:0:-1']}).readings[0],smallResidual=sr.overlaps.filter(o=>o.residualCycleRank);assert.equal(smallResidual.length,6);
 assert.deepEqual(new Set(smallResidual.map(o=>normalizedComparisonGeometry(small,o))),signatures);
});
test('diagnostic ranks do not depend on cell naming or input enumeration',()=>{
 const rename=new Map(sector.cells.map((c,i)=>[c.id,`renamed:${sector.cells.length-i}`]));
 const changed={...sector,cells:[...sector.cells].reverse().map(c=>({...c,id:rename.get(c.id),faces:[...c.faces].reverse()})),faces:[...sector.faces].reverse().map(f=>({...f,owners:f.owners.map(id=>rename.get(id)).reverse()}))};
 const other=buildFiveSideOctComparisonDomain(changed,{readingIds:['reading:0:-1']}).readings[0];assert.deepEqual(other.summary,r.summary);
 assert.deepEqual(new Set(other.overlaps.filter(o=>o.residualCycleRank).map(o=>normalizedComparisonGeometry(changed,o))),new Set(r.overlaps.filter(o=>o.residualCycleRank).map(o=>normalizedComparisonGeometry(sector,o))));
 assert.throws(()=>buildFiveSideOctComparisonDomain(sector,{maxLength:5}),/Diagnostic path lengths/);
});
