import {buildStackedCellInterface} from './stacked-cell-interface.mjs';
import {auditFrameReturn} from './frame-return.mjs';
// Full-model bottleneck trial. Wrapper spans remain coherence metadata;
// they no longer independently authorize an upstream shell-1 transport port.
export function buildStackedFullInterface(original,{mode='direct'}={}){
 const isolated=buildStackedCellInterface(original,{mode}),model=structuredClone(original),{from,to}=isolated.interface;
 const sourceSpace=original.spaces.find(s=>s.ports.B===from),targetSpace=original.spaces.find(s=>s.ports.T===to);
 const sourceOwners=new Set([sourceSpace.id,...original.PEComplexes.filter(p=>p.space===sourceSpace.id).map(p=>p.PE)]),sourceIds=new Set(original.topology.vertices.filter(v=>sourceOwners.has(v.owner)).map(v=>v.id));
 const changes=[],removed=new Set(),edges=model.topology.edges;
 for(const wrapper of model.wrappers){
  const upstream=wrapper.gateways.filter(g=>g.space===sourceSpace.id);
  for(const gateway of upstream){
   const e=edges.find(e=>e.id===gateway.attachment),r=edges.find(r=>r.id===e?.reverse);
   if(!e||!r||e.from!==from||r.to!==from||e.kind!=='space-to-wrapper')throw Error('Unexpected upstream wrapper interface');
   if(wrapper.id===isolated.interface.wrapperProvenance){
    // One anchor retains the wrapper cycle; retaining both perimeter terminals
    // at the same contact would add a second artificial interface cycle.
    removed.add(e.id);removed.add(r.id);
    wrapper.gateways=wrapper.gateways.filter(g=>g!==gateway);
    wrapper.attachmentPolicy='Single downstream anchor; coherence loop, not a second transfer channel';
    changes.push({wrapper:wrapper.id,action:'remove-upstream-terminal',edge:e.id,oldFrom:from,remainingAnchor:to});
   }else{
    e.from=to;r.to=to;
    const prior=structuredClone(gateway);gateway.shell=targetSpace.shell;gateway.space=targetSpace.id;gateway.spacePort='T';gateway.originalGateway=prior;
    e.provenance={...e.provenance,rule:'Explicit downstream delegation through the single shell-1 interface',originalFrom:from};r.provenance=structuredClone(e.provenance);
    wrapper.attachmentPolicy='Upstream span participates through the bottleneck; physical terminal delegated downstream';
    changes.push({wrapper:wrapper.id,action:'delegate-downstream',edge:e.id,oldFrom:from,newFrom:to});
   }
  }
 }
 if(changes.length!==3||changes.filter(c=>c.action==='remove-upstream-terminal').length!==1)throw Error('Unexpected shell-1 attachment set');
 model.topology.edges=edges.filter(e=>!removed.has(e.id));
 model.attachments=model.attachments.filter(a=>!removed.has(a.id));
 for(const change of changes.filter(c=>c.action==='delegate-downstream')){const a=model.attachments.find(a=>a.id===change.edge);if(!a)throw Error('Missing attachment record');a.from=to;}
 const known=new Set(model.topology.vertices.map(v=>v.id));
 for(const v of isolated.topology.vertices)if(!known.has(v.id))model.topology.vertices.push(structuredClone(v));
 model.topology.edges.push(...isolated.topology.edges.filter(e=>e.kind==='stacked-interface').map(e=>structuredClone(e)));
 for(const id of isolated.interface.channelSupports){const e=model.topology.edges.find(e=>e.id===id);model.attachments.push({id,kind:'stacked-interface',from:e.from,to:e.to});}
 const allEdges=new Map(model.topology.edges.map(e=>[e.id,e])),allVertices=new Set(model.topology.vertices.map(v=>v.id));
 for(const e of allEdges.values()){const r=allEdges.get(e.reverse);if(!allVertices.has(e.from)||!allVertices.has(e.to)||!r||r.reverse!==e.id||r.from!==e.to||r.to!==e.from||r.support!==e.support)throw Error('Invalid full-model reverse incidence');}
 function reach(start,without){const adj=new Map([...allVertices].map(v=>[v,[]]));for(const e of allEdges.values())if(e.support!==without)adj.get(e.from).push(e.to);const seen=new Set([start]),q=[start];for(let i=0;i<q.length;i++)for(const v of adj.get(q[i]))if(!seen.has(v)){seen.add(v);q.push(v);}return seen;}
 const bridges=isolated.interface.channelSupports.map(support=>({support,disconnectedWhenRemoved:!reach(from,support).has(to)}));
 const crossingSupports=[...new Set([...allEdges.values()].filter(e=>sourceIds.has(e.from)!==sourceIds.has(e.to)).map(e=>e.support))];
 if(crossingSupports.length!==1||!isolated.interface.channelSupports.includes(crossingSupports[0]))throw Error('Shell 1 retains an extra exit');
 if(bridges.some(b=>!b.disconnectedWhenRemoved)||reach(from).size!==allVertices.size)throw Error('Channel fails global bottleneck test');
 model.components=[[...reach(from)]];
 model.counts={...model.counts,wrapperAttachments:model.attachments.filter(a=>a.kind==='wrapper-terminal').length,components:1,stackedChannels:1};
 model.transfer={...structuredClone(isolated.transfer),PEExcursion:isolated.transfer.excursion};
 model.topology.walks.push({id:'full-stacked-excursion',base:isolated.transfer.forwardVertices[0],kind:'PE',edges:isolated.transfer.excursion});
 model.status='candidate';model.policy='Single reversible shell-1 bottleneck; wrapper spans are coherence metadata, with explicitly delegated downstream terminals.';
 model.residuals=['Downstream delegation is a trial attachment rule, not extracted from projected enclosure.','The 1+2 wrapper now has one anchor rather than two transport terminals; previous two-terminal transfer/coherence audits do not apply unchanged.','3D metric geometry, frame transport, and physical interpretation of the existing 1+2 wrapper remain unspecified.'];
 const supports=new Set([...allEdges.values()].map(e=>e.support));
 return {model,mode,changes,interface:{...isolated.interface,bridgeChecks:bridges,globalShell1ExitSupports:crossingSupports},
  counts:{...model.counts,vertices:allVertices.size,supports:supports.size,cycleRank:supports.size-allVertices.size+1},
  checks:{wholeModelConnected:true,oneShell1Exit:true,eachChannelSegmentIsBridge:true,reverseIncidence:true},
  frameAudit:auditFrameReturn(model.topology),status:'verified-for-declared-bottleneck',
  scope:'Global connectivity and shell-1 cut checked in this modified candidate; not uniqueness of paths inside neutral space or verification of physical frame return.'};
}
