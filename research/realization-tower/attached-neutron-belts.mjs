import {neutronBeltProcess,beltViewerPoint} from './neutron-belt-process.mjs';
import {worldPoint} from './normal-ray-model.mjs';
const add=(a,b)=>a.map((x,i)=>x+b[i]),sub=(a,b)=>a.map((x,i)=>x-b[i]),scale=(v,s)=>v.map(x=>x*s),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],unit=v=>scale(v,1/Math.hypot(...v));
// Display attachment, not an asserted identification of a rim with a parent face.
export function attachedNeutronBelts(seeds){
 const belt=neutronBeltProcess(7,0),bodies=[],guides=[],labels=[],attachments=[];
 const center=b=>b.vertices[0].map((_,i)=>b.vertices.reduce((s,p)=>s+p[i]/b.vertices.length,0));
 for(const sign of ['+N','−N']){
  const parents=seeds.filter(b=>b.seedLabel===sign),anchors=parents.map(b=>worldPoint(center(b)));
  if(parents.length!==2)throw Error('Expected two shared-corner cells per N attachment');
  const anchor=scale(add(...anchors),.5),axis=unit(anchor),x=unit(cross(Math.abs(axis[2])<.9?[0,0,1]:[1,0,0],axis)),z=cross(x,axis);
  const origin=add(anchor,scale(axis,1.35));
  const transform=p=>{const v=worldPoint(p);return beltViewerPoint(add(origin,add(add(scale(x,v[0]*.7),scale(axis,v[1]*.7)),scale(z,v[2]*.7))));};
  const id=`attached:${sign}`,rim=beltViewerPoint(add(origin,scale(axis,-.35*.7)));
  for(const body of belt.retainedBodies)bodies.push({...body,id:`${id}:${body.id}`,vertices:body.vertices.map(transform),faces:body.faces.map(f=>f.map(transform)),attachment:{parentIds:parents.map(b=>b.id),label:sign,kind:'visual-link'},internalSector:{...body.internalSector,parent:sign}});
  for(const guide of belt.interfaceGuides)guides.push({...guide,points:guide.points.map(transform)});
  for(const parent of parents)guides.push({points:[center(parent),rim],color:0xffce66,connector:true});
  labels.push({cell:id,role:'neutron',text:sign,point:beltViewerPoint(origin)});
  attachments.push({id,parentIds:parents.map(b=>b.id),label:sign,bodyCount:6,kind:'visual-link',excludedCapCount:2});
 }
 return {bodies,guides,labels,attachments};
}
