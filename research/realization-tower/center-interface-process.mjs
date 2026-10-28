// Geometry is selected only from the existing esd7 census. P/N/E labels are
// the operator's construction assignments, not a derived native species law.
import {cells,seed} from './normal-ray-model.mjs';
import {assembleComponents} from '../strominger/demos/particle-overlap-tetrahedron/simplex-components.mjs';
export const centerInterfaceStages=Object.freeze([
 'Dot: retained whole at the E handoff.',
 'Expose the actual central esd7 tetrahedron P.',
 'Attach P,E,N,N on the four existing shared faces. These neighboring cells are native octahedral wedges, not reflected regular tetrahedra.',
 'Move each boundary identity to the opposite congruent wedge in its existing octahedron. Two face-connected cells lie between the center and each boundary.',
 'Draw the two reversed arrows through those existing cell positions.',
 'Build the eight arrow cells: P [N N] E; P [P P] P; P [N E] N; P [N P] N. Every consecutive pair shares a full triangular face.',
]);
const ids=[0,1,2,3],roles=['proton','electron','neutron','neutron'];
const gapRoles=[['proton','proton'],['neutron','neutron'],['neutron','electron'],['neutron','proton']];
const key=vs=>vs.map(v=>v.join(',')).sort().join('|');
const pointKey=p=>p.join(',');
const mean=vs=>vs[0].map((_,i)=>vs.reduce((s,p)=>s+p[i]/vs.length,0));
const shared=(a,b)=>a.vertices.filter(v=>b.vertices.some(w=>pointKey(v)===pointKey(w)));
const byGeometry=new Map(cells.map(c=>[key(c.vertices),c]));
const central=byGeometry.get(key(ids.map(i=>ids.map(j=>Number(i===j)))));
if(!central)throw Error('Central unit simplex missing from esd7');
const assembly=assembleComponents();
const native=c=>{
 const cell=byGeometry.get(key(c.addresses));
 if(!cell)throw Error('Assembly component missing from esd7');
 return cell;
};
// Preserve the existing four-wedge cyclic order of each octahedron, rather
// than inventing a tetrahedron or selecting a path by target species.
// Choosing this direction is a display convention, not a uniqueness theorem.
const branches=ids.map(i=>{
 const seedFace=central.vertices.filter((_,j)=>i!==j);
 const first=cells.find(c=>c.id!==central.id&&seedFace.every(v=>c.vertices.some(w=>pointKey(v)===pointKey(w))));
 if(!first)throw Error('Missing complete-face neighbor');
 const group=assembly.groups.find(g=>g.children.some(id=>native(assembly.components[id]).id===first.id));
 if(!group)throw Error('Central neighbor lacks its native octahedral owner');
 const ring=group.children.map(id=>native(assembly.components[id]));
 const start=ring.findIndex(c=>c.id===first.id);
 const route=[central,ring[start],ring[(start+1)%4],ring[(start+2)%4]];
 const interfaces=route.slice(1).map((c,j)=>shared(route[j],c));
 if(interfaces.some(f=>f.length!==3))throw Error('Native ring route must share complete triangular faces');
 return {index:i,owner:group.itemId,route,interfaces};
});
const faceIndices=[[0,1,2],[0,1,3],[0,2,3],[1,2,3]];
function contacts(bodies){
 const faces=new Map();
 for(const b of bodies)for(const f of faceIndices){
  const vertices=f.map(i=>b.components[0][i]),id=key(vertices);
  if(!faces.has(id))faces.set(id,{vertices,owners:[]});faces.get(id).owners.push(b.id);
 }
 return [...faces.values()].filter(f=>f.owners.length===2);
}
export function centerInterfaceProcess(k,step){
 if(!Number.isInteger(k)||k<1||k>7||!Number.isInteger(step)||step<0||step>=centerInterfaceStages.length)throw Error('Invalid center-interface state');
 const bodies=[],labels=[],guides=[];
 function add(id,cell,role,extra={}){
  bodies.push({id,nativeCellId:cell.id,components:[cell.vertices],role,round:0,...extra});
  labels.push({cell:id,role,point:mean(cell.vertices)});
 }
 if(step>=1)add('central-P',central,'proton');
 if(step>=2)for(const b of branches)add(`boundary-${b.index}`,b.route[step>=3?3:1],roles[b.index],{owner:b.owner});
 if(step===4)for(const b of branches){
  const [entry,meeting,exit]=b.interfaces.map(mean);
  guides.push({id:`outward-${b.index}`,points:[entry,meeting],color:0x67c9c2});
  guides.push({id:`inward-${b.index}`,points:[exit,meeting],color:0xe5ae55});
 }
 if(step>=5)for(const b of branches)for(let j=0;j<2;j++)add(`gap-${b.index}-${j}`,b.route[j+1],gapRoles[b.index][j],{branch:b.index,owner:b.owner,direction:j===0?'outward':'inward'});
 const routes=branches.map(b=>({branch:b.index,owner:b.owner,nativeCellIds:b.route.map(c=>c.id),interfaces:b.interfaces,roles:['proton',...gapRoles[b.index],roles[b.index]]}));
 return {k:7,step,end:seed,assignments:[],firstRay:null,rays:[],faceNeighbors:[],faceVertexComparisons:[],neutronNeighbors:[],surfaceNeutronNeighbors:[],closureRounds:[],nextClosure:[],diamonds:[],conflicts:[],
  retainedBodies:bodies,presentationLabels:labels,presentationDot:step===0?mean(central.vertices):null,interfaceGuides:guides,
  retainedContacts:contacts(bodies),
  presentationAudit:{layers:step>=5?4:step>=2?2:step===1?1:0,coherenceBands:0,untypedTetrahedra:0,layerRecords:[],typedCarriers:labels.length,
   nativeRealization:false,nativeGeometry:true,fixedCellSize:true,gapOpen:step>=3&&step<5,fillingAvailable:step>=5,arrowCells:step>=5?8:0,
   branchWords:step>=5?routes.map(r=>r.roles):[],routes,nativeCellIds:bodies.map(b=>b.nativeCellId),junction:'shared triangular face',
   metricPolicy:'Existing esd7 coordinates only. Boundary wedges reorient congruently in their octahedral owner; no scaling or arbitrary translations. The source ring order fixes the displayed route.',
  },
  summary:`Step ${step} — ${centerInterfaceStages[step]}`,canAdvance:step<centerInterfaceStages.length-1,
  history:centerInterfaceStages.slice(0,step+1).map((rule,round)=>({round,rule})),
 };
}
