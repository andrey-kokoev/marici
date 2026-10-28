import {deriveBeltFlux} from './belt-flux-audit.mjs';
// Explicit terminal bundle graph. Grouping retains the current parent records;
// it does not claim a native field fibration or a P/E conversion at the terminal.
export function buildBeltTerminalWiring(layout,parent,mapParentPoint){
 const flux=deriveBeltFlux(layout),bundles=[],links=[];
 for(const [copy,vertexLabel,index,incoming,outgoing] of [['original','+N',0,'P','E'],['clone','−N',5,'E','P']]){
  const binding=parent.bindings.find(b=>b.text===vertexLabel&&b.copies.includes(copy));if(!binding)throw Error('Missing same-sign N binding');
  const members=parent.occurrences.filter(o=>o.copy===copy),owners=members.filter(o=>o.boundary.includes(vertexLabel));if(owners.length!==1)throw Error('Expected one N seed owner per parent');
  const id=`belt:terminal:${copy}:${vertexLabel}`,point=mapParentPoint(binding.point,copy),layer=layout.layers[index];
  const body={id,kind:'terminal-bundle',point,vertices:[point],faces:[],components:[],role:null,color:0x76cfcf,beltTerminal:{copy,vertexLabel,layer:layer.layer,owner:owners[0].id,incomingDirection:incoming,outgoingDirection:outgoing,memberIds:members.map(m=>m.id),fieldFibration:null,directionConversion:null}};
  bundles.push({body,retainedFiber:{base:{copy,vertexLabel,nativePoint:[...binding.point]},members:structuredClone(members),scope:'Lossless grouping of the current parent occurrence records at one marked N vertex. Native field/phase maps remain unbound.'}});
  const tubes=Array.from({length:4},(_,slot)=>({id:`${id}:tube:${slot}`,slot,label:slot<3?`${outgoing}${slot+1}`:incoming,direction:slot<3?outgoing:incoming,flow:slot<3?'parent-to-belt':'belt-to-parent',lanes:[],flux:0,nativeFieldMap:null,faceBinding:null}));
  body.beltTerminal.tubes=tubes;
  for(const node of layer.nodes){const towardBelt=node.direction===outgoing;if(!towardBelt&&node.direction!==incoming)throw Error('Unexpected terminal heading');
   const tube=tubes[towardBelt?node.arm:3];if(!tube)throw Error('Missing directional tube');
   const edge={id:`belt:terminal-wire:${copy}:${node.slot}`,kind:'belt-transport',from:towardBelt?id:node.id,to:towardBelt?node.id:id,direction:node.direction,terminal:id,parent:copy,vertexLabel,star:node.group,arm:node.arm,starCentre:node.starCentre,flux:flux.nodeRates[node.id],rule:'same-sign-N-terminal-to-four-stars',tube:tube.id,tubeSlot:tube.slot,lane:node.group,nativeFieldMap:null};
   links.push(edge);tube.lanes.push({lane:node.group,star:node.group,arm:node.arm,linkId:edge.id,from:edge.from,to:edge.to,flux:edge.flux});tube.flux+=edge.flux;
  }
  for(const tube of tubes){tube.lanes.sort((a,b)=>a.lane-b.lane);if(tube.lanes.length!==4||new Set(tube.lanes.map(l=>l.lane)).size!==4)throw Error('Each directional tube must retain four distinct star lanes');}
 }
 return {bundles,links,scope:'Declared terminal wiring. No parent translation/rotation or octahedral belt geometry is applied.'};
}
export function restoreTerminalFiber(bundle){return structuredClone(bundle.retainedFiber.members);}
