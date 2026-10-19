import {lattice,cellNeighbors,placementAtCell,layerReferenceCellId} from './simplex-model.mjs';
export const atomDefinitions={
 hydrogen:{name:'Hydrogen-1',proton:1,neutron:0,electron:1},
 deuterium:{name:'Deuterium',proton:1,neutron:1,electron:1},
 helium:{name:'Helium-4',proton:2,neutron:2,electron:2},
};
const adjacency=lattice.cells.map((_,id)=>cellNeighbors(id).filter(i=>i>=0));
const centers=lattice.cells.map(cell=>cell.reduce((s,id)=>s.map((x,i)=>x+lattice.nodes[id].point[i]/4),[0,0,0]));
const distance2=(a,b)=>a.reduce((s,x,i)=>s+(x-b[i])**2,0);
const colors={proton:0x6baec8,neutron:0xd7ae77,electron:0xf19ad0};
// Body-local carrier notation; these aliases do not assign a global role to
// a shared lattice node. Qualify each alias by particle instance in the UI.
const vertexLabels={proton:['C0','M0','C1','M1'],neutron:['M0','C1','M1','C2'],electron:['M1','C1','C2','M2']};
// A display occupancy rule only: connected face-adjacent nucleus, with each
// tetrahedral electron sharing a full face with a nuclear cell. No orbital/energy claim.
export function makeAtom(kind,anchor=layerReferenceCellId){
 const definition=atomDefinitions[kind];if(!definition)throw RangeError('Unknown atom');
 if(!lattice.cells[anchor])throw RangeError('Unknown anchor cell');
 const nucleus=[anchor],used=new Set(nucleus),required=definition.proton+definition.neutron;
 while(nucleus.length<required){
  const candidates=[...new Set(nucleus.flatMap(id=>adjacency[id]))].filter(id=>!used.has(id));
  candidates.sort((a,b)=>distance2(centers[a],centers[anchor])-distance2(centers[b],centers[anchor])||a-b);
  if(!candidates.length)throw Error('Insufficient adjacent nuclear cells');
  nucleus.push(candidates[0]);used.add(candidates[0]);
 }
 const depths=lattice.cells.map(()=>Infinity),queue=[...nucleus];nucleus.forEach(id=>depths[id]=0);
 for(let i=0;i<queue.length;i++)for(const next of adjacency[queue[i]])if(depths[next]===Infinity){depths[next]=depths[queue[i]]+1;queue.push(next);}
 const electrons=[];
 while(electrons.length<definition.electron){
  const candidates=lattice.cells.map((_,id)=>id).filter(id=>depths[id]===1&&!used.has(id));
  candidates.sort((a,b)=>{
   if(electrons.length){const sep=id=>Math.min(...electrons.map(e=>distance2(centers[id],centers[e])));return sep(b)-sep(a)||a-b;}
   return distance2(centers[a],centers[anchor])-distance2(centers[b],centers[anchor])||a-b;
  });
  if(!candidates.length)throw Error('Insufficient electron display cells');
  electrons.push(candidates[0]);used.add(candidates[0]);
 }
 const roles=[];for(let i=0;i<Math.max(definition.proton,definition.neutron);i++){if(i<definition.proton)roles.push('proton');if(i<definition.neutron)roles.push('neutron');}
 const counters={proton:0,neutron:0,electron:0};
 const occupants=[...nucleus.map((cellId,i)=>({cellId,species:roles[i]})),...electrons.map(cellId=>({cellId,species:'electron'}))];
 const bodies=occupants.map(({cellId,species})=>{
  const ordinal=++counters[species],id=species+ordinal,symbol=({proton:'P',neutron:'N',electron:'e'})[species]+ordinal;
  const nodeIds=lattice.cells[cellId],names=nodeIds.map((_,i)=>id+'.v'+i);
  return {id,species,symbol,cellId,nodeIds,names,vertexLabels:[...vertexLabels[species]],color:colors[species],center:centers[cellId]};
 });
 const nodeIds=Object.fromEntries(bodies.flatMap(b=>b.names.map((name,i)=>[name,b.nodeIds[i]])));
 const electronAttachments=electrons.map(cellId=>{const nuclearCellId=nucleus.find(n=>adjacency[cellId].includes(n));if(nuclearCellId===undefined)throw Error('Electron has no nuclear face attachment');return {cellId,nuclearCellId,faceNodeIds:lattice.cells[cellId].filter(id=>lattice.cells[nuclearCellId].includes(id))};});
 return {kind,name:definition.name,electronAttachments,counts:{proton:definition.proton,neutron:definition.neutron,electron:definition.electron},nucleus,electrons,
  anchor:placementAtCell(anchor).anchor,bodies,nodeIds,
  coordinates:Object.fromEntries(Object.entries(nodeIds).map(([name,id])=>[name,lattice.nodes[id].coordinate])),
  points:Object.fromEntries(Object.entries(nodeIds).map(([name,id])=>[name,lattice.nodes[id].point]))};
}
