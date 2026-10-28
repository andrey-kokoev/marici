// Proposed root-independent attachment/recovery interface on a fixed motif.
// Bidirectional carriage is an explicit added policy, not a native dynamics law.
import assert from 'node:assert/strict';
import {compareAt,reconcileAt,reconcileBothOrders,validateComparisonNode} from './su32-layer4-comparison.mjs';
const copy=x=>structuredClone(x);
export function referencePortType(packet){
 return {kind:packet.kind,anchor:copy(packet.anchor),origin:packet.at,
  referenceCells:Object.fromEntries(Object.entries(packet.records).map(([k,r])=>[k,r.referenceCell]))};
}
export function buildUndirectedAttachmentProblem(layout,fixture){
 const interfaces=fixture.interfaces.map(f=>({id:f.id,cells:f.ports.map(p=>p.split('@')[0]).sort(),
  ports:copy(f.ports),nativeRequirement:f.requirement,nativeWitness:copy(f.witness)}));
 assert(interfaces.every(f=>f.cells.length===2&&f.cells[0]!==f.cells[1]));
 assert.equal(new Set(interfaces.map(f=>f.id)).size,interfaces.length);
 // Null payloads define structural port signatures only. No actual missing
 // record or result is cached in this problem object.
 const template=reconcileBothOrders(layout,{'P+':null,'P-':null,'E+':null,'E-':null});
 const plus=layout.template.comparisons.find(c=>c.sharedRecord==='E+'),minus=layout.template.comparisons.find(c=>c.sharedRecord==='E-');
 const c=template.comparisons.find(n=>n.at===plus.cell),b=template.comparisons.find(n=>n.at===minus.cell);
 const out=reconcileAt(layout,c,b);
 const nodes=[{id:'C',cell:plus.cell,kind:'comparison'},{id:'R',cell:layout.chart.target,kind:'reconciliation'},
  {id:'a',cell:c.children[0].at,kind:'boundary'},{id:'b',cell:c.children[1].at,kind:'boundary'},
  {id:'other',cell:b.at,kind:'boundary'},{id:'out',cell:layout.chart.target,kind:'boundary'}];
 const byNode=new Map(nodes.map(n=>[n.id,n]));
 function wire(id,ends,packet,readout=false){
  const cells=ends.map(x=>byNode.get(x.node).cell);
  const face=readout?null:interfaces.find(f=>JSON.stringify(f.cells)===JSON.stringify([...cells].sort()));
  if(readout)assert.equal(cells[0],cells[1]);else assert(face,'No actual shared face for wire');
  return {id,ends,portType:referencePortType(packet),attachment:readout?{kind:'local-readout',cell:cells[0]}:{kind:'shared-face',interfaceId:face.id}};
 }
 const wires=[wire('a-C',[{node:'a',slot:0},{node:'C',slot:0}],c.children[0]),
  wire('b-C',[{node:'b',slot:0},{node:'C',slot:1}],c.children[1]),
  wire('C-R',[{node:'C',slot:2},{node:'R',slot:0}],c),
  wire('other-R',[{node:'other',slot:0},{node:'R',slot:1}],b),
  wire('R-out',[{node:'R',slot:2},{node:'out',slot:0}],out,true)];
 return {kind:'su32-undirected-attachment-candidate',anchor:copy(layout.anchor),interfaces,nodes,wires};
}
export function orientAttachmentProblem(layout,problem,root){
 assert.equal(problem.kind,'su32-undirected-attachment-candidate');assert.deepEqual(problem.anchor,layout.anchor);
 const nodes=new Map(problem.nodes.map(n=>[n.id,n]));assert.equal(nodes.size,problem.nodes.length);
 assert.equal(new Set(problem.wires.map(w=>w.id)).size,problem.wires.length);
 assert.equal(nodes.get(root)?.kind,'boundary');
 const adjacent=new Map(problem.nodes.map(n=>[n.id,[]]));
 for(const w of problem.wires){
  assert.equal(w.ends.length,2);assert.notEqual(w.ends[0].node,w.ends[1].node);
  for(let i=0;i<2;i++){const end=w.ends[i],other=w.ends[1-i];assert(nodes.has(end.node));
   adjacent.get(end.node).push({wire:w,end,other});}
  const cells=w.ends.map(e=>nodes.get(e.node).cell).sort();
  if(w.attachment.kind==='shared-face'){
   const f=problem.interfaces.find(f=>f.id===w.attachment.interfaceId);assert(f);
   assert.deepEqual(cells,f.cells,'Face endpoints do not match attached cells');
   assert.deepEqual([...f.ports].sort(),cells.map(cell=>cell+'@'+f.id).sort(),'Native face-occurrence identities changed');
   assert(f.cells.includes(w.portType.origin),'Packet origin must belong to this interface');
  }else{
   assert.equal(w.attachment.kind,'local-readout');assert.equal(cells[0],cells[1]);assert.equal(cells[0],w.attachment.cell);
   assert.equal(w.portType.origin,w.attachment.cell);
  }
 }
 for(const n of problem.nodes){
  const ports=adjacent.get(n.id);assert.deepEqual(ports.map(p=>p.end.slot).sort(),n.kind==='boundary'?[0]:[0,1,2]);
  assert(n.kind==='boundary'||['comparison','reconciliation'].includes(n.kind));
 }
 assert.equal(problem.wires.length,problem.nodes.length-1,'The selected operation shape must be a tree');
 const distance=new Map([[root,0]]),queue=[root];
 for(let i=0;i<queue.length;i++)for(const {other} of adjacent.get(queue[i]))if(!distance.has(other.node)){
  distance.set(other.node,distance.get(queue[i])+1);queue.push(other.node);
 }
 assert.equal(distance.size,nodes.size,'Disconnected operation shape');
 // Choose the orientation from the WHOLE fixed tree before evaluating readers.
 const oriented=problem.wires.map(w=>{
  const [a,b]=w.ends;const from=distance.get(a.node)>distance.get(b.node)?a:b,to=from===a?b:a;
  const fromCell=nodes.get(from.node).cell,toCell=nodes.get(to.node).cell;
  const face=problem.interfaces.find(f=>w.attachment.kind==='shared-face'&&f.id===w.attachment.interfaceId);
  return {wire:w.id,from:from.node,to:to.node,fromCell,toCell,
   fromFacePort:face?fromCell+'@'+face.id:null,toFacePort:face?toCell+'@'+face.id:null,
   attachment:copy(w.attachment),producerSlot:from.slot,consumerSlot:to.slot};
 });
 return {root,oriented};
}
function completeVertex(layout,vertex,ports,missing){
 const invoke=(a,b)=>{
  if(vertex.kind==='comparison')return compareAt(layout,vertex.cell,a,b);
  assert.equal(vertex.kind,'reconciliation');assert.equal(vertex.cell,layout.chart.target);return reconcileAt(layout,a,b);
 };
 let result;
 if(missing===2)result=invoke(ports[0],ports[1]);
 else{
  const retained=ports[2];validateComparisonNode(layout,retained);
  assert.equal(retained.kind,vertex.kind);assert.equal(retained.at,vertex.cell);
  result=copy(retained.children[missing]);
  const completed=[...ports];completed[missing]=result;
  assert.deepEqual(invoke(completed[0],completed[1]),retained,'Known operands violate the single original operation relation');
 }
 ports[missing]=result;return result;
}
export function recoverAtBoundary(layout,problem,root,known){
 const orientation=orientAttachmentProblem(layout,problem,root);
 const boundaries=problem.nodes.filter(n=>n.kind==='boundary').map(n=>n.id);
 assert.deepEqual(Object.keys(known).sort(),boundaries.filter(k=>k!==root).sort(),'Supply exactly the other boundary states, never the requested answer');
 const nodes=new Map(problem.nodes.map(n=>[n.id,n])),wires=new Map(problem.wires.map(w=>[w.id,w]));
 const messages=[],vertices=[];
 function send(nodeId,wireId){
  const vertex=nodes.get(nodeId),wire=wires.get(wireId);let packet;
  if(vertex.kind==='boundary'){packet=copy(known[nodeId]);validateComparisonNode(layout,packet);}
  else{
   const ports=[null,null,null];const outputEnd=wire.ends.find(e=>e.node===nodeId);assert(outputEnd);
   for(const incoming of orientation.oriented.filter(a=>a.to===nodeId))ports[incoming.consumerSlot]=send(incoming.from,incoming.wire);
   assert.equal(ports.filter(x=>x===null).length,1);assert.equal(ports[outputEnd.slot],null);
   packet=completeVertex(layout,vertex,ports,outputEnd.slot);
   vertices.push({node:nodeId,requestedPort:outputEnd.slot,relationPorts:copy(ports)});
  }
  assert.deepEqual(referencePortType(packet),wire.portType,'Wrong record type, reference attachment or origin on wire');
  const arc=orientation.oriented.find(a=>a.wire===wireId);assert.equal(arc.from,nodeId);
  messages.push({...copy(arc),retainedOrigin:packet.at,packet:copy(packet)});
  return packet;
 }
 const incoming=orientation.oriented.filter(a=>a.to===root);assert.equal(incoming.length,1);
 const result=send(incoming[0].from,incoming[0].wire);
 assert.equal(messages.length,problem.wires.length);assert.equal(vertices.length,problem.nodes.length-boundaries.length);
 return {root,result,orientation,messages,vertices,
  policy:'Bidirectional shared-face carriage and solving the retained operation relation; proposed, not native execution.'};
}
