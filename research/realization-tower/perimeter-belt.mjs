import {buildFoldedFibration} from './fibration-folded-process.mjs';
import {analyzeSeamLattice} from './seam-lattice.mjs';
import {worldPoint} from './normal-ray-model.mjs';
const m=buildFoldedFibration(),seam=analyzeSeamLattice(m.occurrences),byId=new Map(m.occurrences.map(b=>[b.id,b])),kinds=new Map(m.geometry.map(g=>[g.id,g.kind]));
const center=ps=>ps[0].map((_,i)=>ps.reduce((s,p)=>s+p[i]/ps.length,0));
export function perimeterBeltRule(role,incoming=null){
 if(role==='neutron')return {role:'proton',rule:'N → P'};
 if(role==='electron'&&incoming==='N')return {role:'proton',rule:'E + |N| → P'};
 if(role==='electron'&&incoming==='P')return {role:'neutron',rule:'E + |P| → N'};
 return {role,rule:null};
}
const candidates=seam.pairs.filter(p=>p.cells.every(id=>kinds.get(byId.get(id).sourceGeometry)==='octahedron')).map(p=>({...p,point:center(p.face)}));
const axes=[0,1,2,3].filter(i=>Math.max(...candidates.map(p=>p.point[i]))-Math.min(...candidates.map(p=>p.point[i]))>1e-8);
const maxima=axes.map(i=>Math.max(...candidates.map(p=>p.point[i])));
const perimeter=candidates.filter(p=>axes.some((axis,i)=>Math.abs(p.point[axis]-maxima[i])<1e-8));
const mid=center(perimeter.map(p=>p.point));
// Sort in a two-coordinate chart of the actual triangular face, not a fitted circle.
const u=axes[0],v=axes[1];perimeter.sort((a,b)=>Math.atan2(a.point[v]-mid[v],a.point[u]-mid[u])-Math.atan2(b.point[v]-mid[v],b.point[u]-mid[u]));
if(perimeter.length!==15||axes.some((axis,i)=>perimeter.filter(p=>Math.abs(p.point[axis]-maxima[i])<1e-8).length!==6))throw Error('Expected six dots per side, fifteen unique perimeter ports');
export const perimeterBeltNodes=perimeter.map((p,i)=>({id:`belt:perimeter:${i}`,kind:'face-port',vertices:[p.point],faces:[],components:[],role:perimeterBeltRule('neutron').role,color:0x1265a8,layer:null,
 beltPort:{parents:p.cells,sourceFace:p.face,sourceRole:'neutron',transition:perimeterBeltRule('neutron').rule,index:i},point:p.point}));
export const perimeterBeltLinks=perimeterBeltNodes.flatMap((b,i)=>[
 {from:b.id,to:perimeterBeltNodes[(i+1)%15].id,kind:'perimeter'},
 ...b.beltPort.parents.map(id=>({from:b.id,to:id,kind:'face-port'}))]);
export function presentPerimeterBelt(proc){
 return {...proc,attachmentBodies:perimeterBeltNodes,interfaceGuides:proc.interfaceGuides.filter(g=>!g.seamFlow),
 beltGraphLinks:perimeterBeltLinks,replacedFaceLinks:perimeter.map(p=>p.cells),
 perimeterBeltAudit:{nodes:15,sideCounts:axes.map((axis,i)=>perimeter.filter(p=>Math.abs(p.point[axis]-maxima[i])<1e-8).length),previousLayerPorts:candidates.length,maxDegree:4,
  rules:['N → P','E + |N| → P','E + |P| → N'],scope:'Perimeter face-port graph; no added volume cells. N → P initializes the source N ports; conditional E rules require an explicit incoming letter.',points:perimeterBeltNodes.map(b=>worldPoint(b.point))},
 doubleEsd7Audit:{...proc.doubleEsd7Audit,seamLattice:{...proc.doubleEsd7Audit.seamLattice,flows:[],sharedPairs:[]}}};
}
