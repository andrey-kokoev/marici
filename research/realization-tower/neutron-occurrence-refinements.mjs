import {neutronBeltProcess,beltViewerPoint} from './neutron-belt-process.mjs';
import {worldPoint} from './normal-ray-model.mjs';
const sub=(a,b)=>a.map((x,i)=>x-b[i]),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],norm=a=>Math.hypot(...a);
const center=ps=>ps[0].map((_,i)=>ps.reduce((s,p)=>s+p[i]/ps.length,0));
// Parent-bound internal fibers, NOT a tetrahedral volume replacement.
// External faces stay on their actual parent; no unsupported child-port map.
export function neutronOccurrenceRefinements(seeds){
 const native=neutronBeltProcess(7,0),parents=seeds.filter(b=>b.role==='neutron'&&['+N','−N'].includes(b.seedLabel));
 if(parents.length!==4||new Set(parents.map(b=>b.id)).size!==4)throw Error('Expected four distinct reflected N occurrences');
 const complexes=parents.map(parent=>{
  const origin=center(parent.vertices.map(worldPoint));
  const radius=Math.min(...parent.faces.map(f=>{const [a,b,c]=f.map(worldPoint),n=cross(sub(b,a),sub(c,a));return Math.abs(dot(sub(origin,a),n))/norm(n);}));
  const scale=.8*radius/Math.max(...native.retainedBodies.flatMap(b=>b.vertices.map(p=>norm(worldPoint(p)))));
  const transform=p=>beltViewerPoint(worldPoint(p).map((x,i)=>origin[i]+scale*x));
  const copy=parent.id.split(':')[0],id=`neutron-complex:${parent.id}`;
  return {id,parentId:parent.id,label:parent.seedLabel,copy,
   status:'internal carrier; parent-face-to-child-port map unresolved',
   parentPorts:parent.faces.map((face,i)=>({id:`${id}:parent-port:${i}`,face,childPort:null})),
   bodies:native.retainedBodies.map(b=>({...b,id:`${id}:${b.id}`,vertices:b.vertices.map(transform),faces:b.faces.map(f=>f.map(transform)),opacity:.28,
    internalSector:{...b.internalSector,parent:parent.id,copy},refinementParent:parent.id})),
   accounting:'six internal cells, not six additional particle assignments',placement:'uniformly scaled inside parent insphere for display; no volume replacement'};
 });
 return {complexes,bodies:complexes.flatMap(c=>c.bodies)};
}
export function presentNeutronOccurrenceRefinements(proc){
 const {complexes,bodies}=neutronOccurrenceRefinements(proc.retainedBodies);
 return {...proc,attachmentBodies:bodies,interfaceGuides:proc.interfaceGuides.filter(g=>!g.seamFlow),
  neutronRefinementAudit:{complexCount:4,internalCellCount:24,extraParticleAssignments:0,complexes:complexes.map(({bodies,...c})=>({...c,cellIds:bodies.map(b=>b.id)})),attachmentStatus:'Parent faces retained; child-port maps unresolved; no fan-out connections added.'},
  doubleEsd7Audit:{...proc.doubleEsd7Audit,seamLattice:{...proc.doubleEsd7Audit.seamLattice,flows:[],sharedPairs:[]}}};
}
