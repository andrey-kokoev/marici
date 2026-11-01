// Candidate contextual presentation exchange, not a compiled native rule.
import assert from 'node:assert/strict';
import {encodeSignedReferences,decodeSignedReferences} from './su32-signed-reference-encoder.mjs';
import {channelOperand,compareAt,reconcileBothOrders} from './su32-layer4-comparison.mjs';
import {attachReference,splitAttachment} from './su32-cross-cone-reference-fibre.mjs';
export function contextualExchangeInterface(atlas,fixture,layout,left,right){
 assert.equal(left.cells.length,5);assert.equal(right.cells.length,5);
 for(const i of [0,1,3,4])assert.equal(left.cells[i],right.cells[i]);assert.notEqual(left.cells[2],right.cells[2]);
 assert.equal(left.cells[0],layout.chart.source);assert.equal(left.cells[4],layout.chart.target);
 const comparison=layout.template.comparisons.find(c=>c.cell===left.cells[3]);assert(comparison);
 assert.deepEqual([left.cells[2],right.cells[2]].sort(),[...comparison.inputs].sort());assert.equal(comparison.sharedCell,left.cells[1]);
 for(const path of [left,right]){
  assert.equal(path.arrows.length,4);assert.equal(path.id,JSON.stringify(path.cells));
 }
 for(const path of [left,right])for(let i=0;i<4;i++){
  const matches=fixture.interfaces.filter(f=>{const cs=f.ports.map(p=>p.split('@')[0]);return cs.includes(path.cells[i])&&cs.includes(path.cells[i+1]);});
  assert.equal(matches.length,1);assert.equal(matches[0].id,path.arrows[i]);
 }
 const paths=[structuredClone(left),structuredClone(right)],cell=comparison.cell;
 function make(registry,order=0,antecedent=[]){
  assert(order===0||order===1);assert.deepEqual(JSON.parse(JSON.stringify(antecedent)),antecedent);
  const orderedPaths=order===0?paths:[paths[1],paths[0]],children=orderedPaths.map(p=>channelOperand(layout,p.cells[2],registry));
  return {preparation:encodeSignedReferences(atlas,layout.chart.id,layout.anchor.binding,registry),
   orderedPaths:structuredClone(orderedPaths),point:compareAt(layout,cell,...children),antecedent:structuredClone(antecedent)};
 }
 function validate(state){
  const registry=decodeSignedReferences(atlas,state.preparation),order=paths.findIndex(p=>p.id===state.orderedPaths[0].id);assert(order>=0);
  assert.deepEqual(state,make(registry,order,state.antecedent),'Contextual state changed or lost preparation, operands, paths, or provenance');
  return {registry,order};
 }
 function exchange(state){const {registry,order}=validate(state);return make(registry,1-order,state.antecedent);}
 function perform(state,receipts=[]){
  for(let i=0;i<receipts.length;i++){
   const r=receipts[i];assert.equal(r.kind,'contextual-presentation-exchange');assert.deepEqual(exchange(r.source),r.target);
   if(i)assert.deepEqual(receipts[i-1].target,r.source);
  }
  if(receipts.length)assert.deepEqual(receipts.at(-1).target,state);
  const target=exchange(state);
  return {state:target,receipts:[...structuredClone(receipts),{kind:'contextual-presentation-exchange',source:structuredClone(state),target:structuredClone(target)}]};
 }
 function otherPoint(targetLayout,registry){
  const joint=targetLayout.template.channels.find(c=>c.cell===layout.chart.target);assert(joint);
  const refs=[joint.P,joint.E];assert.equal(refs.filter(r=>r.referenceCell===cell).length,1);
  const other=refs.find(r=>r.referenceCell!==cell);
  const point=reconcileBothOrders(layout,registry).comparisons.find(c=>c.at===other.referenceCell);
  assert(point,'Other input must be an actual comparison from the same preparation');return point;
 }
 function attach(state,targetLayout){
  const {registry}=validate(state);
  return {preparation:structuredClone(state.preparation),orderedPaths:structuredClone(state.orderedPaths),antecedent:structuredClone(state.antecedent),
   consumer:attachReference(layout,targetLayout,cell,layout.chart.target,state.point,otherPoint(targetLayout,registry))};
 }
 function recover(attached,targetLayout){
  const split=splitAttachment(layout,targetLayout,cell,layout.chart.target,attached.consumer);
  const state={preparation:structuredClone(attached.preparation),orderedPaths:structuredClone(attached.orderedPaths),antecedent:structuredClone(attached.antecedent),point:split.point};
  const {registry}=validate(state);assert.deepEqual(split.otherPayload,otherPoint(targetLayout,registry));
  assert.deepEqual(attach(state,targetLayout),attached);return state;
 }
 function exchangeAttached(attached,targetLayout){return attach(exchange(recover(attached,targetLayout)),targetLayout);}
 return {cell,paths,make,validate,exchange,perform,attach,recover,exchangeAttached};
}
