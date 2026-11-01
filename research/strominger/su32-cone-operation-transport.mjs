// Geometry-certified transport of an existing occurrence chart. This does not
// weaken the edge-three atlas constructor's guard or fabricate an edge-three fixture.
import assert from 'node:assert/strict';
import {validateComparisonNode} from './su32-layer4-comparison.mjs';
const shape=vs=>vs.map(v=>v.join(',')).sort().join('|');
const centre=c=>c.vertices[0].map((_,i)=>c.vertices.reduce((s,v)=>s+v[i],0)/c.vertices.length);
export function identifyCone(sourceFixture,sourceChart,sourceCone,carrier,cone){
 const sourceCells=new Map(sourceFixture.cells.map(c=>[c.id,c])),targetCells=new Map(carrier.cells.map(c=>[c.id,c]));
 const a=centre(sourceCells.get(sourceChart.source)),b=centre(targetCells.get(cone.source)),translation=b.map((x,i)=>x-a[i]);
 const shift=v=>v.map((x,i)=>x+translation[i]);
 const targetByShape=new Map(carrier.cells.map(c=>[shape(c.vertices),c]));
 const cellMap={};
 for(const id of sourceChart.starCells){
  const c=sourceCells.get(id),d=targetByShape.get(shape(c.vertices.map(shift)));assert(d,'No exact native translated cell');
  assert.equal(d.role,c.role);assert.equal(d.kind,c.kind);cellMap[id]=d.id;
 }
 const targetIds=[...new Set(cone.paths.flatMap(p=>p.cells))].sort();
 assert.equal(new Set(Object.values(cellMap)).size,14);assert.deepEqual(Object.values(cellMap).sort(),targetIds);
 assert.equal(cellMap[sourceChart.source],cone.source);assert.equal(cellMap[sourceChart.target],cone.target);
 const sourcePaths=sourceCone.paths.map(p=>JSON.stringify(p.cells.map(c=>cellMap[c]))).sort();
 assert.deepEqual(sourcePaths,cone.paths.map(p=>JSON.stringify(p.cells)).sort());assert.equal(sourcePaths.length,16);
 const faceMap={},targetFaces=new Map(carrier.faces.map(f=>[f.id,f]));
 for(const c of sourceChart.starCells.map(id=>sourceCells.get(id)))for(const f of c.faces){
  const old=shape(f),id=shape(f.map(shift));assert(targetFaces.has(id));faceMap[old]=id;
 }
 // Verify each interface of the source star against actual native target owners.
 let sharedFaces=0;
 for(const f of sourceFixture.interfaces){
  const owners=f.ports.map(p=>p.split('@')[0]);
  if(!owners.every(c=>Object.hasOwn(cellMap,c)))continue;
  const mapped=targetFaces.get(faceMap[f.id]);assert(mapped);
  assert.deepEqual([...mapped.owners].sort(),owners.map(c=>cellMap[c]).sort());sharedFaces++;
 }
 const m=id=>{assert(Object.hasOwn(cellMap,id));return cellMap[id];};
 const chart={...structuredClone(sourceChart),id:JSON.stringify([sourceChart.reading,cone.source,cone.target]),
  source:m(sourceChart.source),target:m(sourceChart.target),starCells:sourceChart.starCells.map(m),
  P:sourceChart.P.map(m),E:sourceChart.E.map(m),
  joints:sourceChart.joints.map(j=>({cell:m(j.cell),P:m(j.P),E:m(j.E)})),
  comparisons:sourceChart.comparisons.map(c=>({...c,cell:m(c.cell),inputs:c.inputs.map(m),sharedCell:m(c.sharedCell)}))};
 return {translation,cellMap,faceMap,sharedFaces,chart};
}
export function targetFixture(carrier){
 return {interfaces:carrier.faces.filter(f=>f.owners.length===2).map(f=>({id:f.id,
  ports:f.owners.map(c=>c+'@'+f.id),requirement:'native shared-face support only',witness:null}))};
}
export function transportNode(sourceLayout,targetLayout,identification,node){
 validateComparisonNode(sourceLayout,node);
 const m=id=>{assert(Object.hasOwn(identification.cellMap,id));return identification.cellMap[id];};
 function go(n){
  const result={...structuredClone(n),anchor:structuredClone(targetLayout.anchor),at:m(n.at),
   records:Object.fromEntries(Object.entries(n.records).map(([label,r])=>[label,{...structuredClone(r),referenceCell:m(r.referenceCell)}]))};
  if(n.children)result.children=n.children.map(go);
  return result;
 }
 const result=go(node);validateComparisonNode(targetLayout,result);return result;
}
