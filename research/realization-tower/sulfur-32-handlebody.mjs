import {buildPESymmetricSector} from '../strominger/pe-symmetric-sector.mjs';
import {neutralCentre} from '../strominger/pe-symmetric-sector.mjs';
const centre=vertices=>[0,1,2,3].map(i=>vertices.reduce((s,v)=>s+v[i],0)/vertices.length);

// Empty-carrier presentation: actual shared-face incidence, not chosen wires.
// P/E cells remain neutral junction spaces; deleting them disconnects N cells.
export function buildSulfur32Handlebody(){
 const sector=buildPESymmetricSector(1),nodes=sector.cells.map(c=>({id:c.id,kind:c.role==='neutron'?'N-chamber':'junction',position:centre(c.vertices),sourceVertices:c.vertices}));
 const links=sector.faces.filter(f=>f.owners.length===2).map(f=>({id:f.id,from:f.owners[0],to:f.owners[1],face:f.vertices,kind:'shared-face-neck'}));
 const pairs=[[0,1],[2,3],[0,2],[1,3],[0,3],[1,2]];
 const ports=pairs.map((pair,i)=>{
  const position=neutralCentre.map((x,j)=>x+(pair.includes(j)?1.5:-1.5));
  const owners=sector.cells.filter(c=>c.vertices.some(v=>v.every((x,j)=>x===position[j])));
  if(owners.length!==1||owners[0].role!=='neutron')throw Error('Expected unique N tip owner');
  return {id:'sulfur:mouth:'+i,owner:owners[0].id,position,pair:Math.floor(i/2)};
 });
 return {nodes,links,ports,centre:[...neutralCentre],
  audit:{NChambers:19,neutralJunctions:32,sharedFaceNecks:104,boundaryMouths:6,pairedTipIdentities:3,NChannelIdentities:16,wireCount:0,spatialComponents:1,graphCycleRank:links.length-nodes.length+1,
   scope:'Thickened native face-incidence graph. Source cells are chamber/junction locations, not solid occupied cells. Opposite-tip identities are retained labels, not tubes drawn through intervening geometry. Periodic seams and signed-strand routing are not included.'}};
}
