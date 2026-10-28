import {singleOctahedralProcess} from './single-octahedral-process.mjs';
import {buildSulfur32Wiring,presentSulfurWires} from './sulfur-32-wiring.mjs';
let cachedWiring;

// The geometry is retained even when its wire records are periodically grouped.
export function sulfur32Process(k,step,options={}){
 if(!Number.isInteger(step)||step<0||step>1)throw Error('Sulfur-32 stages are initial geometry and global wiring');
 const base=singleOctahedralProcess(k,1,{...options,nTubeAxis:'off'});
 const {peCoupledRoutingAudit,ambientNeutralAudit,nTubeAudit,emptyRegionAudit,interiorNPairingAudit,...geometry}=base;
 const direction=options.sulfurDirection??'P|E',wired=step===1;
 const result={...geometry,step,canAdvance:!wired,interfaceGuides:[],
  inventory:{...base.inventory,voidRows:[],channelRows:[]},
  sulfur32Audit:{edgeUnits:3,radius:1,sourceProcess:'single-octahedral',fibration:wired?'candidate-global-periodic':'pending',colorCellulation:wired?'geometric-roles-retained':'pending',physicalInventoryEstablished:false,direction},
  summary:`Sulfur-32 · edge 3 · ${base.retainedBodies.length} whole geometric cells · fibration and color-cellulation pending.`,history:[]};
 if(!wired)return result;
 const model=cachedWiring??=buildSulfur32Wiring(),wires=presentSulfurWires(model,direction),byGroup=new Map(model.groups.map(g=>[g.id,g])),byCell=new Map(base.retainedBodies.map(c=>[c.id,c]));
 const row={id:'channel-fibers',label:'Channel fibers',proton:16,neutron:16,electron:16,total:48};
 result.inventory.rows=[...base.inventory.rows,row];result.inventory.displayRows=result.inventory.rows;
 result.interfaceGuides=model.seamGuides;
 const orient=link=>{if(link.kind==='retained-tip-pair')return {...link};const a=byCell.get(link.from),b=byCell.get(link.to),rank=direction==='P|E'?{proton:0,neutron:1,electron:2}:{electron:0,neutron:1,proton:2};return rank[a.role]<rank[b.role]?{...link,directed:true}:{...link,from:link.to,to:link.from,directed:true};};
 result.nativeWiringGraph={nodes:base.nativeWiringGraph.nodes,links:[...base.nativeWiringGraph.links,...model.seamLinks,...model.pairLinks].map(orient)};
 result.presentationLabels=[...base.presentationLabels,...model.groups.filter(g=>g.role==='neutron').flatMap(g=>g.members.map(member=>({cell:member.id,role:'neutron',text:g.label,point:member.vertices[0].map((_,i)=>member.vertices.reduce((s,v)=>s+v[i]/member.vertices.length,0))})))];
 result.sulfur32Audit={...result.sulfur32Audit,...model.counts,closure:model.closure,
  channelPorts:model.channels.map(c=>({id:c.id,label:byGroup.get(c.id).label,members:c.members.map(m=>m.id),slots:wires.filter(w=>w.channel===c.id).sort((a,b)=>a.axis-b.axis).map(w=>({wire:w.id,axis:w.axis,slot:w.slot,from:byGroup.get(w.source).label,to:byGroup.get(w.target).label}))}))};
 result.summary=`Sulfur-32 · 16 dual-directional N channels · 64 retained wires · 2×2 ${direction} ports · global periodic closure.`;
 result.history=[{operation:'global-periodic-fibration',generators:model.generators,sourceCells:51,retainedCellFibers:48,direction}];
 return result;
}
