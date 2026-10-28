// Actual cell refinement of the verified cone-over-annulus carrier.
// This is a geometric construction, not a particle assignment or an insertion map.
import geometry from '../voevodsky/results/four_six_center_cones.json' with {type:'json'};
import flux from '../voevodsky/results/mode_flux_charge.json' with {type:'json'};
import {buildFoldedFibration} from './fibration-folded-process.mjs';
import {beltViewerPoint} from './neutron-belt-process.mjs';
import {cellDualGraph} from './cell-dual-graph.mjs';
const rational=s=>{const [a,b='1']=s.split('/');return Number(a)/Number(b);};
const vertices=Object.fromEntries(Object.entries(geometry.belt_scaled_coordinates).map(([id,p])=>{const [x,y,z]=p.map(rational);return [id,beltViewerPoint([Math.sqrt(3)*x,y,z])];}));
const native=buildFoldedFibration().geometry;
export function refineNeutronBelt({id='belt',circulation=1}={}){
 if(![1,-1].includes(circulation))throw Error('Circulation must be +1 or -1');
 const bodies=geometry.belt_tetrahedra.flatMap((names,panel)=>{
  const corners=names.map(n=>vertices[n]);
  // Native ESD7 envelope corners have q_i=-5 and q_j=2 (j!=i).
  const transform=q=>corners[0].map((_,axis)=>corners.reduce((s,p,i)=>s+(2-q[i])/7*p[axis],0));
  return native.map(cell=>({id:`${id}:${panel}:${cell.id}`,kind:cell.kind,role:null,layer:null,
   vertices:cell.vertices.map(transform),faces:cell.faces.map(face=>face.map(transform)),components:[],
   refinement:{carrier:id,panel,sourceCell:cell.id,circulation:circulation*flux.belt_face_signs[panel],sector:flux.sector_pairs.findIndex(pair=>pair.includes(panel)),metric:'affine pullback; not rigidly congruent to native cells'}}));
 });
 const graph=cellDualGraph(bodies),byId=new Map(bodies.map(b=>[b.id,b]));
 const panelContacts=new Map();
 for(const e of graph.links){const a=byId.get(e.from).refinement.panel,b=byId.get(e.to).refinement.panel;if(a===b)continue;const key=[a,b].sort((a,b)=>a-b).join(':');panelContacts.set(key,(panelContacts.get(key)??0)+1);}
 return {id,circulation,bodies,graph,panelContacts:[...panelContacts].map(([pair,count])=>({panels:pair.split(':').map(Number),faces:count})),
  audit:{cellCount:bodies.length,tetrahedra:bodies.filter(b=>b.kind==='tetrahedron').length,octahedra:bodies.filter(b=>b.kind==='octahedron').length,panels:6,excludedCaps:2,centerLinkBetti:[1,1,0,0],parentInsertion:null,metric:'affinely deformed native ESD7 cell lattice',particleAssignments:false}};
}
