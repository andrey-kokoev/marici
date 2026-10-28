// Finite rooted, slot-indexed adapter for EXISTING candidate join operations.
// No cyclic action, filler, physical continuation, or general operad claimed.
import assert from 'node:assert/strict';
import {validateComparisonNode,compareAt,reconcileAt} from './su32-layer4-comparison.mjs';
const copy=x=>structuredClone(x);
const sorted=xs=>[...xs].sort();
function exact(x,fields){assert(x&&typeof x==='object');assert.deepEqual(sorted(Object.keys(x)),sorted(fields));}
export function comparisonPort(node){
 return copy({kind:node.kind,anchor:node.anchor,at:node.at,records:node.records});
}
// Expansion chooses which of the two supplied comparison children are internal
// vertices. Unexpanded children stay complete boundary operands with provenance.
export function decomposeRootedComparison(layout,root,expandedChildren=[0,1]){
 validateComparisonNode(layout,root);assert.equal(root.kind,'reconciliation');
 assert(expandedChildren.every(i=>i===0||i===1));assert.equal(new Set(expandedChildren).size,expandedChildren.length);
 const vertices=[],boundary=[];
 function visit(node,id){
  assert(['comparison','reconciliation'].includes(node.kind));
  const vertex={id,kind:node.kind,at:node.at,output:comparisonPort(node),inputs:[]};vertices.push(vertex);
  for(let i=0;i<node.children.length;i++){
   const child=node.children[i],childId=id+'/'+i;
   const internal=id==='root'&&expandedChildren.includes(i);
   vertex.inputs.push({source:{kind:internal?'vertex':'boundary',id:childId},expected:comparisonPort(child)});
   if(internal)visit(child,childId);else boundary.push({id:childId,operand:copy(child)});
  }
 }
 visit(root,'root');return {kind:'su32-rooted-comparison-diagram-candidate',anchor:copy(layout.anchor),root:'root',vertices,boundary};
}
// Reconstruct by compareAt/reconcileAt, NOT by returning a cached root or
// accepting a list of compatible records as an already-admitted realization.
export function glueRootedComparison(layout,diagram){
 exact(diagram,['kind','anchor','root','vertices','boundary']);
 assert.equal(diagram.kind,'su32-rooted-comparison-diagram-candidate');assert.deepEqual(diagram.anchor,layout.anchor);
 assert(Array.isArray(diagram.vertices)&&Array.isArray(diagram.boundary));
 const vertices=new Map(diagram.vertices.map(v=>[v.id,v])),boundary=new Map(diagram.boundary.map(b=>[b.id,b.operand]));
 assert.equal(vertices.size,diagram.vertices.length,'Duplicate operation vertex');
 assert.equal(boundary.size,diagram.boundary.length,'Duplicate boundary slot');
 assert([...vertices.keys()].every(k=>!boundary.has(k)),'Vertex and boundary IDs overlap');
 const visited=new Set(),usedBoundary=new Set();
 function evaluate(id){
  assert(!visited.has(id),'Expected a tree, not a cycle or multiply-used operation vertex');visited.add(id);
  const v=vertices.get(id);assert(v,'Missing operation vertex');exact(v,['id','kind','at','output','inputs']);
  assert.equal(v.inputs.length,2,'These source operations are binary');
  const children=v.inputs.map(port=>{
   exact(port,['source','expected']);exact(port.source,['kind','id']);let node;
   if(port.source.kind==='vertex')node=evaluate(port.source.id);
   else{
    assert.equal(port.source.kind,'boundary');assert(!usedBoundary.has(port.source.id),'Boundary occurrences must be retained separately');
    usedBoundary.add(port.source.id);node=boundary.get(port.source.id);assert(node,'Missing boundary operand');
    validateComparisonNode(layout,node);
   }
   assert.deepEqual(comparisonPort(node),port.expected,'Connected port values/types disagree');return node;
  });
  let result;
  if(v.kind==='comparison')result=compareAt(layout,v.at,...children);
  else{assert.equal(v.kind,'reconciliation');assert.equal(v.at,layout.chart.target);result=reconcileAt(layout,...children);}
  assert.deepEqual(comparisonPort(result),v.output,'Declared local output is not the result of its operation');
  return result;
 }
 const result=evaluate(diagram.root);
 assert.equal(visited.size,vertices.size,'Unreachable operation vertex');assert.equal(usedBoundary.size,boundary.size,'Unretained boundary operand');
 return result;
}
