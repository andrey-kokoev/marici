// A retained, occurrence-coloured two-corolla fragment extracted from existing
// comparison constructors. No native inverse, arbitrary-tree operad, or physical
// P/E colour duality is manufactured by this adapter.
import assert from 'node:assert/strict';
import {compareAt,reconcileAt,validateComparisonNode} from './su32-layer4-comparison.mjs';
import {buildUndirectedAttachmentProblem,referencePortType} from './su32-undirected-reference-attachment.mjs';
export const key=x=>JSON.stringify(x,(_,v)=>v&&typeof v==='object'&&!Array.isArray(v)?Object.fromEntries(Object.keys(v).sort().map(k=>[k,v[k]])):v);
const copy=structuredClone;
export function signature(layout,fixture){
 const problem=buildUndirectedAttachmentProblem(layout,fixture);
 const colours=problem.wires.flatMap(w=>w.ends.map(e=>({wire:w.id,end:e.node,packetType:copy(w.portType)})));
 return {problem,colours};
}
export function dual(sig,colour){
 assert(sig.colours.some(c=>key(c)===key(colour)),'Colour outside this occurrence signature');
 const other=sig.colours.filter(c=>c.wire===colour.wire&&c.end!==colour.end);assert.equal(other.length,1);return copy(other[0]);
}
export function corolla(layout,sig,vertex,values){
 const v=sig.problem.nodes.find(n=>n.id===vertex);assert(['comparison','reconciliation'].includes(v?.kind));
 assert.equal(values.length,3);values.forEach(n=>validateComparisonNode(layout,n));
 const output=v.kind==='comparison'?compareAt(layout,v.cell,values[0],values[1]):reconcileAt(layout,values[0],values[1]);
 assert.deepEqual(values[2],output,'Not a row of the existing operation');
 const ports=values.map((value,slot)=>{
  const w=sig.problem.wires.find(w=>w.ends.some(e=>e.node===vertex&&e.slot===slot));assert(w);
  assert.equal(key(referencePortType(value)),key(w.portType),'Wrong occurrence-bound packet type');
  const colour=sig.colours.find(c=>c.wire===w.id&&c.end===vertex);
  return {slot,colour:copy(colour),value:copy(value)};
 });
 return {vertex,ports,sourceNode:copy(output)};
}
export function rotate(operation,n=1){
 const p=operation.ports,k=((n%p.length)+p.length)%p.length;
 return {...copy(operation),ports:copy([...p.slice(k),...p.slice(0,k)])};
}
export function rooted(sig,operation,root){
 assert(Number.isInteger(root)&&root>=0&&root<operation.ports.length);
 const p=rotate(operation,root).ports;
 return {output:{...copy(p[0]),colour:dual(sig,p[0].colour)},inputs:copy(p.slice(1))};
}
export function glue(sig,left,i,right,j){
 const a=left.ports[i],b=right.ports[j];assert(a&&b);
 assert.equal(key(dual(sig,a.colour)),key(b.colour),'Gluing requires opposite arcs of the same typed wire');
 assert.equal(key(a.value),key(b.value),'Full internal packet must match, including provenance');
 // Definition 3.2: the cyclic order remaining after cutting the two ports.
 const ports=[...left.ports.slice(0,i),...right.ports.slice(j+1),...right.ports.slice(0,j),...left.ports.slice(i+1)];
 return {ports:copy(ports),vertices:[copy(left),copy(right)],internal:{left:copy(a),right:copy(b)}};
}
export function decompose(layout,sig,output){
 validateComparisonNode(layout,output);assert.equal(output.kind,'reconciliation');
 const [c,b]=output.children;assert.equal(c.kind,'comparison');
 const left=corolla(layout,sig,'C',[...c.children,c]),right=corolla(layout,sig,'R',[c,b,output]);
 return {left,right};
}
export function assemble(layout,sig,local){
 // Revalidate instead of trusting caller-constructed corolla records.
 const restore=o=>{
  const ports=[...o.ports].sort((a,b)=>a.slot-b.slot);
  const restored=corolla(layout,sig,o.vertex,ports.map(p=>p.value));
  assert.deepEqual(restored,{...o,ports},'Corolla annotations disagree with its source operation');
  return restored;
 };
 const left=restore(local.left),right=restore(local.right);
 glue(sig,left,2,right,0);
 return copy(right.sourceNode);
}
