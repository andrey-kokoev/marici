// Proposed information-level completion. Not a native transport, DG witness,
// physical interaction, simplicial filler, or replacement for the source API.
import assert from 'node:assert/strict';
import {validateComparisonNode} from './su32-layer4-comparison.mjs';
const copy=x=>structuredClone(x);
const keys=x=>Object.keys(x).sort();
function exact(x,names){assert(x&&typeof x==='object');assert.deepEqual(keys(x),[...names].sort());}
function freeze(x){if(x&&typeof x==='object'&&!Object.isFrozen(x)){Object.freeze(x);for(const v of Object.values(x))freeze(v);}return x;}
function reference(r){assert(['E+','E-'].includes(r),'Only the two supplied E-reference views are admitted');}
function validateCore(layout,core){
 exact(core,['kind','anchor','at','records','derivations']);
 assert.equal(core.kind,'su32-central-reference-core-candidate');
 assert.deepEqual(core.anchor,layout.anchor);assert.equal(core.at,layout.chart.target);
 exact(core.derivations,['byE','byP']);
 for(const [name,role] of [['byE','E'],['byP','P']]){
  const n=core.derivations[name];validateComparisonNode(layout,n);assert.equal(n.kind,'reconciliation');
  assert(n.children.every(c=>layout.template.comparisons.find(t=>t.cell===c.at).sharedRole===role),'Wrong retained reconciliation route');
  assert.deepEqual(core.records,n.records);
 }
 assert.deepEqual(JSON.parse(JSON.stringify(core)),core,'Core must be losslessly serializable');
 return true;
}
function deriveView(layout,core,activeReference){
 reference(activeReference);
 const site=layout.template.comparisons.find(c=>c.sharedRecord===activeReference);assert(site);
 const sourceComparison=core.derivations.byE.children.find(c=>c.at===site.cell);assert(sourceComparison);
 const other=activeReference==='E+'?'E-':'E+';
 return {at:core.at,activePair:Object.fromEntries(['P+','P-'].map(k=>[k,copy(core.records[k])])),
  reference:{label:activeReference,record:copy(core.records[activeReference])},
  complement:{label:other,record:copy(core.records[other])},sourceComparison:copy(sourceComparison)};
}
export function validateCentralReferencePacket(layout,packet){
 const seen=new Set(),cores=new Set();let current=packet;
 while(current!==null){
  assert(!seen.has(current),'Cyclic provenance is not admitted');seen.add(current);
  exact(current,['kind','core','activeReference','view','parent','operation']);
  assert.equal(current.kind,'su32-central-reference-packet-candidate','A complete central packet is required');
  if(!cores.has(current.core)){validateCore(layout,current.core);cores.add(current.core);}
  assert.deepEqual(current.view,deriveView(layout,current.core,current.activeReference),'Reader/view does not match the retained core and selected reference');
  if(current.parent===null)assert.equal(current.operation,null);
  else{
   assert(current.parent&&typeof current.parent==='object');
   assert.deepEqual(current.core,current.parent.core,'Reference selection cannot replace the retained core');
   assert.deepEqual(current.operation,{kind:'select-retained-E-reference',from:current.parent.activeReference,to:current.activeReference,at:current.core.at});
  }
  current=current.parent;
 }
 assert(seen.size>0,'A complete central packet is required');return true;
}
export function prepareCentralReferencePacket(layout,byE,byP,activeReference='E+'){
 const core={kind:'su32-central-reference-core-candidate',anchor:copy(layout.anchor),at:layout.chart.target,
  records:copy(byE.records),derivations:{byE:copy(byE),byP:copy(byP)}};
 validateCore(layout,core);
 const packet={kind:'su32-central-reference-packet-candidate',core,activeReference,
  view:deriveView(layout,core,activeReference),parent:null,operation:null};
 validateCentralReferencePacket(layout,packet);return freeze(packet);
}
export function selectCentralReference(layout,packet,activeReference){
 validateCentralReferencePacket(layout,packet);reference(activeReference);
 // Snapshot caller-owned validated data before retaining it. Never freeze or
 // modify a mutable caller object as a side effect.
 const parent=freeze(copy(packet));
 const next={kind:'su32-central-reference-packet-candidate',core:parent.core,activeReference,
  view:deriveView(layout,parent.core,activeReference),parent,
  operation:{kind:'select-retained-E-reference',from:parent.activeReference,to:activeReference,at:parent.core.at}};
 validateCentralReferencePacket(layout,next);return freeze(next);
}
export function currentCentralReferenceState(layout,packet){
 validateCentralReferencePacket(layout,packet);
 return copy({core:packet.core,activeReference:packet.activeReference,view:packet.view});
}
export function centralReferenceHistory(layout,packet){
 validateCentralReferencePacket(layout,packet);const history=[];
 for(let p=packet;p.parent!==null;p=p.parent)history.push(copy(p.operation));
 return history.reverse();
}
export function centralReferenceBoundary(layout,packet){
 validateCentralReferencePacket(layout,packet);
 return {at:packet.core.at,anchor:copy(packet.core.anchor)};
}
