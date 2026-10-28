import * as T from 'three';
import {worldPoint} from '../../research/realization-tower/normal-ray-model.mjs';
import {buildSulfurTubeNetwork} from '../../research/realization-tower/sulfur-32-tube-network.mjs';
import {createHoneycombTubeGeometry} from './honeycomb-tube-geometry.js';
import {planTubeJunction,createTubeJunctionGeometry} from './tube-junction-geometry.js';

export function createSulfurNTubeMarkers(model,{selectedIdentity='all'}={}){
 const root=new T.Group(),network=buildSulfurTubeNetwork(model),edges=new Map(model.edges.map(e=>[e.id,e])),records=new Map();
 const groups=model.channelGroups.map(g=>({id:g.id,edgeIds:model.edges.filter(e=>e.carrierCells.some(c=>g.members.includes(c))).map(e=>e.id)}));
 const info=(id,shape,position,nGroups,sourceCells,edgeIds,strandIds,radius,closed=false)=>({id,kind:'tube',shape,role:'N',geometryId:null,position,worldPosition:worldPoint(position),layers:null,constructionStep:null,
  tube:{groups:nGroups.map(id=>({id,label:network.identities.find(g=>g.id===id).label})),sourceCells,edgeIds,strands:strandIds.map(id=>({id,polarities:{...model.strands.find(s=>s.id===id).polarities}})),radius,closed}});
 const material=(color,opacity)=>new T.MeshBasicMaterial({color,transparent:true,opacity,side:T.DoubleSide,depthTest:false,depthWrite:false});
 for(const segment of network.segments){
  if(selectedIdentity!=='all'&&!segment.nGroups.includes(selectedIdentity))continue;
  let extent=0;
  for(const id of segment.edgeIds){
   const edge=edges.get(id),a=new T.Vector3(...worldPoint(edge.guide[0])),direction=new T.Vector3(...worldPoint(edge.guide[1])).sub(a).normalize();
   for(const strand of model.strands.filter(s=>edge.strandIds.includes(s.id)))for(const p of strand.edgeRuns.find(r=>r.edgeId===id).points){
    const relative=new T.Vector3(...worldPoint(p)).sub(a);extent=Math.max(extent,relative.clone().addScaledVector(direction,-relative.dot(direction)).length());
   }
  }
  records.set(segment.id,{segment,radius:extent+.024+.012,points:segment.points.map(p=>new T.Vector3(...worldPoint(p)))});
 }
 const plans=[];let deferredJunctions=0;
 for(const junction of network.junctions){
  if(junction.ports.some(p=>!records.has(p.segmentId)))continue;
  const centre=new T.Vector3(...worldPoint(junction.point)),ports=junction.ports.map(p=>{
   const r=records.get(p.segmentId),first=p.end==='start',neighbour=first?r.points[1]:r.points.at(-2);
   return {...p,radius:r.radius,direction:neighbour.clone().sub(centre).normalize(),edgeLength:neighbour.distanceTo(centre)};
  });
  const plan=planTubeJunction(centre,ports);if(!plan){deferredJunctions++;continue;}
  plans.push({...plan,junction});
 }
 for(const plan of plans)for(const port of plan.ports){const r=records.get(port.segmentId),index=port.end==='start'?0:r.points.length-1;r.points[index]=plan.centre.clone().addScaledVector(port.direction,plan.distance);}
 let endCollars=0;
 for(const record of records.values()){
  const {segment,radius,points}=record,{geometry,rings}=createHoneycombTubeGeometry(points,radius,{closed:segment.closed});record.rings=rings;
  const position=segment.points[0].map((_,i)=>segment.points.reduce((sum,p)=>sum+p[i]/segment.points.length,0));
  const hoverInfo=info(segment.id,'continuous tube segment',position,segment.nGroups,[...segment.sourceCells],[...segment.edgeIds],[...segment.strandIds],radius,segment.closed);
  const piece=new T.Group();piece.userData={...segment,radius,hoverInfo,renderPoints:points.map(p=>p.toArray())};root.add(piece);record.piece=piece;
  const shell=new T.Mesh(geometry,material(0x67e8f9,.14));shell.userData={nTubeOpacityScale:1,tubePart:true};shell.layers.set(1);shell.renderOrder=12;piece.add(shell);
  if(!segment.closed)for(const ring of [rings[0],rings.at(-1)]){
   const curve=new T.CatmullRomCurve3(ring,true),collar=new T.Mesh(new T.TubeGeometry(curve,64,.009,8,true),material(0xffce66,.85));
   collar.userData={nTubeOpacityScale:.85/.14,tubePart:true,endCollar:true};collar.layers.set(1);collar.renderOrder=14;piece.add(collar);endCollars++;
  }
 }
 for(const plan of plans){
  const rings=plan.ports.map(p=>{const r=records.get(p.segmentId);return p.end==='start'?r.rings[0]:r.rings.at(-1);});
  const segments=plan.ports.map(p=>records.get(p.segmentId).segment),unique=field=>[...new Set(segments.flatMap(s=>s[field]))];
  const hub=new T.Mesh(createTubeJunctionGeometry(plan.centre,plan.radius,rings),material(0x67e8f9,.14));
  hub.userData={nTubeOpacityScale:1,tubeJunction:true,portCount:rings.length,hoverInfo:info(plan.junction.id,'automatic tube junction',plan.junction.point,unique('nGroups'),unique('sourceCells'),unique('edgeIds'),unique('strandIds'),plan.radius)};
  hub.layers.set(1);hub.renderOrder=12;records.get(plan.ports[0].segmentId).piece.add(hub);
 }
 root.userData.groups=groups;root.userData.identities=network.identities;
 root.userData.audit={groups:groups.length,pieces:root.children.length,schematic:true,alignedToWiring:true,...network.audit,selectedIdentity,visibleIdentities:selectedIdentity==='all'?groups.length:network.identities.filter(g=>g.id===selectedIdentity).length,sharedSegments:network.segments.filter(s=>s.nGroups.length>1).length,identities:network.identities,junctions:plans.length,deferredJunctions,endCollars};
 return root;
}
