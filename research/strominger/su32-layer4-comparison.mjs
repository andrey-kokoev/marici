// Candidate set-valued comparison at sourced incidences. No phase assignment.
import assert from 'node:assert/strict';
import {encodeSignedReferences} from './su32-signed-reference-encoder.mjs';
const copy=x=>structuredClone(x);
const keys=x=>Object.keys(x).sort();
const labels=['P+','P-','E+','E-'];
export function comparisonLayout(atlas,fixture,chartId,binding){
 const chart=atlas.charts.find(c=>c.id===chartId);assert(chart);
 const template=encodeSignedReferences(atlas,chartId,binding,Object.fromEntries(labels.map(k=>[k,null])));
 const adjacent=(a,b)=>fixture.interfaces.some(f=>{const cs=f.ports.map(p=>p.split('@')[0]);return cs.includes(a)&&cs.includes(b);});
 for(const c of chart.comparisons){for(const n of c.inputs)assert(adjacent(n,c.cell));assert(adjacent(c.cell,chart.target));}
 return {chart,template,anchor:{chartId,binding:[...binding]}};
}
function channelRefs(layout,cell){
 const c=layout.template.channels.find(c=>c.cell===cell);assert(c,'Not a joint N occurrence');
 return Object.fromEntries([c.P,c.E].map(r=>[r.record,r.referenceCell]));
}
function merge(left,right,shared){
 assert.deepEqual(keys(left).filter(k=>Object.hasOwn(right,k)),[...shared].sort(),'Wrong overlap');
 for(const k of shared)assert.deepEqual(left[k],right[k],'Shared record disagrees in identity or payload');
 return {...copy(left),...copy(right)};
}
export function channelOperand(layout,cell,registry){
 const refs=channelRefs(layout,cell);
 for(const k of keys(refs)){
  assert(Object.hasOwn(registry,k),'Missing input record');
  assert.deepEqual(JSON.parse(JSON.stringify(registry[k])),registry[k],'Payload must survive JSON encoding');
 }
 const node={kind:'channel',anchor:copy(layout.anchor),at:cell,records:Object.fromEntries(keys(refs).map(k=>[k,{referenceCell:refs[k],payload:copy(registry[k])}]))};
 validateComparisonNode(layout,node);return node;
}
function comparisonRecords(layout,cell,children){
 const c=layout.template.comparisons.find(c=>c.cell===cell);assert(c,'Not a layer-4 comparison');
 assert.equal(children.length,2);assert(children.every(n=>n.kind==='channel'));
 assert.deepEqual(children.map(n=>n.at).sort(),[...c.inputs].sort());
 return merge(children[0].records,children[1].records,[c.sharedRecord]);
}
function reconciliationRecords(layout,children){
 assert.equal(children.length,2);assert(children.every(n=>n.kind==='comparison'));
 const cs=children.map(n=>layout.template.comparisons.find(c=>c.cell===n.at));assert(cs.every(Boolean));
 assert.equal(cs[0].sharedRole,cs[1].sharedRole);
 assert.notEqual(cs[0].sharedRecord,cs[1].sharedRecord);
 const overlapRole=cs[0].varyingRole;
 return merge(children[0].records,children[1].records,[overlapRole+'+',overlapRole+'-']);
}
export function validateComparisonNode(layout,node){
 assert.deepEqual(node.anchor,layout.anchor,'Different occurrence or sign binding');
 if(node.kind==='channel'){
  assert.deepEqual(keys(node),['anchor','at','kind','records']);
  const refs=channelRefs(layout,node.at);assert.deepEqual(keys(node.records),keys(refs));
  for(const k of keys(refs)){assert.deepEqual(keys(node.records[k]),['payload','referenceCell']);assert.equal(node.records[k].referenceCell,refs[k]);}
 }else{
  assert.deepEqual(keys(node),['anchor','at','children','kind','records']);
  assert(Array.isArray(node.children));for(const c of node.children)validateComparisonNode(layout,c);
  let expected;
  if(node.kind==='comparison')expected=comparisonRecords(layout,node.at,node.children);
  else{assert.equal(node.kind,'reconciliation');assert.equal(node.at,layout.chart.target);expected=reconciliationRecords(layout,node.children);assert.deepEqual(keys(expected),[...labels].sort());}
  assert.deepEqual(node.records,expected,'Derived comparison data or operand history changed');
 }
 return true;
}
export function compareAt(layout,cell,left,right){
 const children=[left,right];for(const c of children)validateComparisonNode(layout,c);
 const node={kind:'comparison',anchor:copy(layout.anchor),at:cell,children:copy(children),records:comparisonRecords(layout,cell,children)};
 validateComparisonNode(layout,node);return node;
}
export function reconcileAt(layout,left,right){
 const children=[left,right];for(const c of children)validateComparisonNode(layout,c);
 const node={kind:'reconciliation',anchor:copy(layout.anchor),at:layout.chart.target,children:copy(children),records:reconciliationRecords(layout,children)};
 validateComparisonNode(layout,node);return node;
}
export function reconcileBothOrders(layout,registry){
 const channels=Object.fromEntries(layout.chart.joints.map(j=>[j.cell,channelOperand(layout,j.cell,registry)]));
 const comparisons=layout.template.comparisons.map(c=>compareAt(layout,c.cell,...c.inputs.map(id=>channels[id])));
 const atShared=role=>comparisons.filter(n=>layout.template.comparisons.find(c=>c.cell===n.at).sharedRole===role);
 const byE=reconcileAt(layout,...atShared('E')),byP=reconcileAt(layout,...atShared('P'));
 assert.deepEqual(byE.records,byP.records);
 assert.notDeepEqual(byE.children,byP.children,'Construction orders must remain distinct');
 return {channels,comparisons,byE,byP,agreement:{at:layout.chart.target,records:copy(byE.records),left:byE,right:byP,kind:'record-agreement-with-both-derivations',nativeFiller:null}};
}
export function readRecords(layout,node){
 validateComparisonNode(layout,node);return Object.fromEntries(keys(node.records).map(k=>[k,copy(node.records[k].payload)]));
}
