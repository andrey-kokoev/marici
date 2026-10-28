import {buildOctahedralCoherentRouting} from './octahedral-coherent-routing.mjs';
const centre=vs=>vs[0].map((_,i)=>vs.reduce((s,v)=>s+v[i]/vs.length,0));
let cached;const views=new Map();
export function buildFiveSideOctWiring(groupId='all'){
 if(!cached){
  const routing=buildOctahedralCoherentRouting(2),{fibration}=routing,cells=new Map(fibration.sector.cells.map(c=>[c.id,c])),ports=new Map(routing.ports.map(p=>[p.id,p]));
  const styles=[{label:'coordinate slot 0',colors:[0xffffff]},{label:'coordinate slot 1',colors:[0x168fff,0xffffff]},{label:'coordinate slot 2',colors:[0xff3030,0xffffff]},{label:'coordinate slot 3',colors:[0x168fff]},{label:'boundary-lift seam (not a native adjacency)',colors:[0xe1bc65],dashed:true}];
  const renderPaths=[];
  for(const link of routing.links){
   if(link.kind==='native-interface')continue; // shared face: the same point, not another tube
   renderPaths.push({id:link.id,kind:link.kind,points:link.points,family:link.kind==='boundary-seam'?4:link.axis,radius:link.kind==='boundary-seam'?.009:.023,wireIds:link.wireIds});
  }
  for(const route of routing.routes)for(const [side,id] of [['source',route.ports[0]],['target',route.ports.at(-1)]]){
   const port=ports.get(id),point=centre(cells.get(port.cell).vertices);
   renderPaths.push({id:`${route.id}/${side}`,kind:'charged-fibre-port',cell:port.cell,points:side==='source'?[point,port.point]:[port.point,point],family:route.axis,radius:.014,wireIds:[route.id]});
  }
  const byLink=new Map(routing.links.map(l=>[l.id,l]));
  const strands=routing.routes.map(r=>({...r,family:r.axis,points:r.links.flatMap(id=>byLink.get(id).points)}));
  cached={routing,fibration,coherenceGroups:routing.coherenceGroups,styles,renderPaths,strands,input:fibration.sourceFibers,output:fibration.targetFibers,axis:[-.5,-.5,.5,.5],audit:routing.audit};
 }
 if(groupId==='all')return cached;
 if(views.has(groupId))return views.get(groupId);
 const group=cached.coherenceGroups.find(g=>g.id===groupId);if(!group)throw Error('Unknown coherence group');
 const ids=new Set(group.wireIds),view={...cached,renderPaths:cached.renderPaths.filter(p=>p.wireIds.some(id=>ids.has(id))),strands:cached.strands.filter(s=>ids.has(s.id)),audit:{...cached.audit,selectedGroup:group.id,selectedNCells:group.members.length,selectedWires:ids.size}};
 views.set(groupId,view);return view;
}
