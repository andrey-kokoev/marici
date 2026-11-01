// Native symmetry and literal-window contact tests; no invented simplex binding.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildSulfur32Wiring,sulfurPeriodGenerators} from '../../realization-tower/sulfur-32-wiring.mjs';
import {periodCoordinates} from '../sulfur-period-covers.mjs';
import {periodVector} from '../native-window-operation.mjs';
const root='research/strominger',base=buildSulfur32Wiring(),sector=buildPESymmetricSector(1);
const R=v=>[v[2],v[0],v[1],v[3]],Ra=a=>[a[2],a[0],a[1]],add=(a,b)=>a.map((x,i)=>x+b[i]),sub=(a,b)=>a.map((x,i)=>x-b[i]);
const shape=vs=>vs.map(v=>v.join(',')).sort().join('|'),anchor=vs=>[0,1,2,3].map(i=>Math.min(...vs.map(v=>v[i])));
const cells=new Map(sector.cells.map(c=>[c.id,c])),cellAt=new Map(sector.cells.map(c=>[shape(c.vertices),c]));
const portAt=new Map();for(const p of base.ports)for(const l of p.lifts)portAt.set(l.cell+'@'+shape(l.vertices),p.id);
const ports=new Map(base.ports.map(p=>[p.id,p])),portAction=new Map(),cellAction=new Map();
for(const c of sector.cells){const image=cellAt.get(shape(c.vertices.map(R)));assert(image);assert.equal(image.role,c.role);cellAction.set(c.id,image.id);}
for(const p of base.ports){
 const images=p.lifts.map(l=>portAt.get(cellAction.get(l.cell)+'@'+shape(l.vertices.map(R))));assert(images.every(Boolean));assert.equal(new Set(images).size,1);
 const target=ports.get(images[0]),h=sub(anchor(target.vertices),anchor(p.vertices.map(R)));
 assert.equal(shape(p.vertices.map(v=>add(R(v),h))),shape(target.vertices));
 assert.equal(target.role,p.role);assert.equal(target.axis,p.axis===3?3:(p.axis+1)%3);
 portAction.set(p.id,{target:target.id,representativeCorrection:periodCoordinates(h)});
}
const edgeKey=(a,b,kind)=>JSON.stringify([kind,...[a,b].sort()]),edgeAt=new Map(base.edges.map(e=>[edgeKey(e.from,e.to,e.kind),e]));
for(const e of base.edges){
 const p=portAction.get(e.from),q=portAction.get(e.to),image=edgeAt.get(edgeKey(p.target,q.target,e.kind));assert(image);
 const actual=image.transport.map(x=>(image.from===p.target?x:-x)||0);
 assert.deepEqual(actual,add(R(e.transport),periodVector(sub(q.representativeCorrection,p.representativeCorrection))));
}
const wireAt=new Map(base.wires.flatMap(w=>w.ports.map(p=>[p,w.id]))),wireAction={};
for(const w of base.wires){const images=new Set(w.ports.map(p=>wireAt.get(portAction.get(p).target)));assert.equal(images.size,1);wireAction[w.id]=[...images][0];}
assert.equal(new Set(Object.values(wireAction)).size,64);
for(const w of base.wires)assert.equal(wireAction[wireAction[wireAction[w.id]]],w.id);
const k=[1,-1,0],d=periodVector(k);assert.deepEqual(d,sub(sulfurPeriodGenerators[0],sulfurPeriodGenerators[1]));
assert.deepEqual(add(add(k,Ra(k)),Ra(Ra(k))),[0,0,0]);
const liftStep=({port,sheet})=>{const action=portAction.get(port);return {port:action.target,sheet:add(add(Ra(sheet),action.representativeCorrection),k)};};
let liftedChecks=0;
for(const p of base.ports)for(const sheet of [[0,0,0],[1,0,0],[0,1,0],[0,0,1]]){
 const start={port:p.id,sheet},one=liftStep(start),three=liftStep(liftStep(one));assert.deepEqual(three,start);
 // The +k deck convention means physical rotation followed by -L(k).
 const physical=p.vertices.map(v=>sub(v,periodVector(sheet))),target=ports.get(one.port).vertices.map(v=>sub(v,periodVector(one.sheet)));
 assert.equal(shape(target),shape(physical.map(v=>sub(R(v),d))));liftedChecks++;
}
const wrongK=[1,0,0],wrongSum=add(add(wrongK,Ra(wrongK)),Ra(Ra(wrongK)));assert.deepEqual(wrongSum,[1,1,1]);
function windowTest(radius){
 const s=buildPESymmetricSector(radius),offsets=[[0,0,0,0],d.map(x=>-x),add(d,R(d)).map(x=>-x)];
 const blocks=offsets.map((offset,index)=>{
  const rotate=v=>index===0?v:index===1?R(v):R(R(v));
  const cs=s.cells.map(c=>({id:c.role+':'+add(rotate(c.id.split(':')[1].split(',').map(Number)),offset).join(','),role:c.role,
   vertices:c.vertices.map(v=>add(rotate(v),offset))}));
  const vertices=[...new Map(cs.flatMap(c=>c.vertices.map(v=>[v.join(','),v]))).values()];
  return {name:['A','B','C'][index],offset,cells:cs,vertices,bounds:[0,1,2,3].map(i=>({min:Math.min(...vertices.map(v=>v[i])),max:Math.max(...vertices.map(v=>v[i]))}))};
 });
 const intersection=(sets)=>[...sets[0]].filter(x=>sets.slice(1).every(s=>s.has(x)));
 const pairwise=[[0,1],[1,2],[2,0]].map(([i,j])=>{
  const A=blocks[i],B=blocks[j],commonVertices=intersection([new Set(A.vertices.map(String)),new Set(B.vertices.map(String))]);
  const commonCells=intersection([new Set(A.cells.map(c=>c.id)),new Set(B.cells.map(c=>c.id))]);
  const separation=A.bounds.map((b,axis)=>({axis,gap:Math.max(B.bounds[axis].min-b.max,b.min-B.bounds[axis].max)})).find(s=>s.gap>0)??null;
  return {blocks:[A.name,B.name],commonVertices,commonCells,separation};
 });
 const triple={vertices:intersection(blocks.map(b=>new Set(b.vertices.map(String)))),cells:intersection(blocks.map(b=>new Set(b.cells.map(c=>c.id))))};
 return {radius,edgeUnits:s.edgeUnits,blockCellCount:s.cells.length,offsets,pairwise,triple,
  pointContactPattern:pairwise.every(p=>p.commonVertices.length===1)&&triple.vertices.length===0};
}
const windows=[windowTest(1),windowTest(2)];
assert(windows[0].pairwise.every(p=>p.commonVertices.length===0&&p.separation));
assert(windows[1].pairwise.every(p=>p.commonCells.length>0));assert(windows[1].triple.cells.length>0);
assert(windows.every(w=>!w.pointContactPattern));
const sourceHashes={};for(const p of [root+'/checkers/check_su32_three_contact_binding.mjs',root+'/pe-symmetric-sector.mjs',root+'/sulfur-period-covers.mjs',
 root+'/native-window-operation.mjs','research/realization-tower/sulfur-32-wiring.mjs',root+'/su32_three_contact_results.md'])sourceHashes[p]=createHash('sha256').update(await fs.readFile(p)).digest('hex');
const result={schema:'su32.three-contact-binding-audit.v1',passed:true,nativeThreeContactConstructionAdmitted:false,
 nativeSymmetry:{cells:cellAction.size,ports:portAction.size,edges:base.edges.length,wires:Object.keys(wireAction).length,liftedChecks,
  portAction:Object.fromEntries(portAction),wireAction,deckIncrement:k,physicalAffineTranslation:d.map(x=>-x),
  orderThree:true,retainedWord:['F','F','F'],historyComparison:null},windows,
 conclusion:'The rotation extends to the native typed port graph, with representative corrections. Literal edge-three windows are disjoint; literal edge-five windows overlap in whole cells, including a triple overlap. Neither realizes the proposed point-contact pattern.',
 firstMissingObject:'A source realization of the proposed five-vertex 4-simplex blocks, their actual occurrences, and typed contact ports. No such binding is supplied by the examined note or the native cell/wire constructors.',
 limits:['Whole windows are explicitly tested interpretations, not an asserted identification of the abstract simplices.',
 'A graph automorphism is not a traversable contact edge or a source-admitted witness transport.',
 'Full-port order-three closure does not identify the retained three-step word with an identity history.',
 'No native contact composite, monodromy or higher filler is constructed.'],sourceHashes};
const dir=root+'/results/su32-three-contact-binding-v1';await fs.mkdir(dir,{recursive:true});await fs.writeFile(dir+'/verification.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({passed:true,nativeThreeContactConstructionAdmitted:false,
 nativeSymmetry:{cells:cellAction.size,ports:portAction.size,edges:base.edges.length,wires:64,liftedChecks},
 windows:windows.map(w=>({edgeUnits:w.edgeUnits,pairwise:w.pairwise.map(p=>({vertices:p.commonVertices.length,cells:p.commonCells.length,separation:p.separation})),triple:{vertices:w.triple.vertices.length,cells:w.triple.cells.length}})),
 conclusion:result.conclusion,firstMissingObject:result.firstMissingObject},null,2));
