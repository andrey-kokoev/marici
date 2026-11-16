// Metric hypothesis, deliberately separate from the drawn K4 topology.
import {solveContactFrameAlignment} from './contact-frame-alignment.mjs';
import {bindChannelTransport} from './channel-frame-transport.mjs';
const sub=(a,b)=>a.map((x,i)=>x-b[i]),add=(a,b)=>a.map((x,i)=>x+b[i]);
export function studyTetrahedralContact(full,{height=1/Math.sqrt(2),sourceDepth=1,targetDepth=1,sourceLeg='outgoing',targetLeg='outgoing'}={}){
 if(full.mode!=='direct')throw Error('This contact geometry trial requires the direct interface; mediator pose is not specified');
 if(!Number.isFinite(height)||height<=0||height>1e6)throw Error('Height must be finite and in (0, 1e6]');
 if(![1,-1].includes(sourceDepth)||![1,-1].includes(targetDepth))throw Error('Depth order must be +1 or -1');
 if(!['incoming','outgoing'].includes(sourceLeg)||!['incoming','outgoing'].includes(targetLeg))throw Error('Unknown PE reference leg');
 const model=full.model,vertices=new Map(model.topology.vertices.map(v=>[v.id,v])),edges=new Map(model.topology.edges.map(e=>[e.id,e]));
 const sourceSpace=model.spaces.find(s=>s.ports.B===full.interface.from),targetSpace=model.spaces.find(s=>s.ports.T===full.interface.to);
 if(!sourceSpace||!targetSpace)throw Error('Expected a bottom-to-top cell contact');
 function marker(space,port,leg){
  const p=model.PEComplexes.find(p=>p.space===space.id&&p.mainPort===port),w=model.topology.walks.find(w=>w.base===p?.base);if(!p||!w)throw Error('No PE circulation at contact');
  const e=edges.get(leg==='outgoing'?w.edges[0]:w.edges.at(-1)),other=vertices.get(leg==='outgoing'?e.to:e.from).position;
  const named=Object.entries(space.ports).filter(([,id])=>JSON.stringify(vertices.get(id).position)===JSON.stringify(other));if(named.length!==1)throw Error('Ambiguous projected PE leg');
  return {pair:p.pair,leg,port:named[0][0],convention:'Reference points outward from the PE vertex along the selected geometric leg, even when that leg carries incoming circulation.'};
 }
 const a=marker(sourceSpace,'B',sourceLeg),b=marker(targetSpace,'T',targetLeg),hs=height*sourceDepth,ht=height*targetDepth;
 const lift=h=>({T:[0,-1,h],R:[1,0,-h],B:[0,1,h],L:[-1,0,-h]});
 const upper=lift(hs),offset=[0,2,hs-ht],lower=Object.fromEntries(Object.entries(lift(ht)).map(([p,v])=>[p,add(v,offset)]));
 const sourceCenter=[0,0,0],targetCenter=offset,contact=upper.B;
 // Forward channel axes: leave the upper center toward its vertex, then
 // enter the lower center from its vertex. This is a stated radial-axis rule.
 const source={axis:sub(contact,sourceCenter),reference:sub(upper[a.port],contact)},target={axis:sub(targetCenter,lower.T),reference:sub(lower[b.port],lower.T)};
 const alignment=solveContactFrameAlignment({source,target});
 if(alignment.status!=='verified')throw Error('Candidate contact frames are degenerate');
 const channel=bindChannelTransport(full,[alignment.rotation]);
 return {status:'conditional',parameters:{height,sourceDepth,targetDepth,sourceLeg,targetLeg},sourceMarker:a,targetMarker:b,
  embedding:{source:upper,target:lower,sourceCenter,targetCenter,contact},portData:{source,target},alignment,channelAudit:channel.audit,
  assumptions:['A normalized square projection is lifted with T/B at +h and L/R at -h; depth signs are explicit parameters.','h = 1/sqrt(2) is the regular-tetrahedron hypothesis, not a metric fact from the diagram.','Cells meet at source B / target T; the lower cell is translated to make contact exact.','Forward axes follow center-to-contact and contact-to-center radial directions.','Selected PE geometric legs provide transverse references, with an explicitly chosen correspondence.'],
  limits:['Only this contact receives a conditional rotation; PE and neutron-loop transport remain unspecified.','Projection fixes neither depth order nor the radial-axis/leg-correspondence rule.','This embedding is local to the two contacting cells, not a global 3D packing of Ca46.']};
}
