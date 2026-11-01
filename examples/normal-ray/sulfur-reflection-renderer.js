import * as T from 'three';
import {createSulfurIncomingBundle} from './sulfur-incoming-bundle-renderer.js';
const pairs=[];for(let i=0;i<5;i++)for(let j=i+1;j<5;j++)pairs.push([i,j]);
const triangles=[];for(let i=0;i<5;i++)for(let j=i+1;j<5;j++)for(let k=j+1;k<5;k++)triangles.push([i,j,k]);
function createWiring(model,state){
 const group=createSulfurIncomingBundle(model.reflectionBundle),selected=state.reflectionCopy??'all';
 for(const mesh of group.children){
  const strand=model.reflectionBundle.strands.find(s=>s.id===mesh.userData.incomingStrand);
  mesh.material.transparent=true;mesh.material.opacity=(state.reflectionWireOpacity??.85)*(selected==='all'||strand.copyId===selected?1:.08);
  mesh.userData.reflectionCopy=strand.copyId;mesh.userData.reflectionDecisions=strand.decisions;
 }
 if(state.bodies)for(const cell of model.reflectionCells){
  const vs=cell.copy.vertices.map(p=>new T.Vector3(...p));
  group.add(new T.LineSegments(new T.BufferGeometry().setFromPoints(pairs.flatMap(([a,b])=>[vs[a],vs[b]])),new T.LineBasicMaterial({color:0x617088,transparent:true,opacity:.13,depthWrite:false})));
 }
 group.userData.audit={...model.reflectionAudit,...model.reflectionBundle.audit,view:'wiring',wireMeshes:group.children.filter(c=>c.userData.incomingStrand).length,wireOpacity:state.reflectionWireOpacity??.85,angle:state.reflectionAngle??35,selectedCopy:selected,
  strandIds:model.reflectionBundle.strands.map(s=>s.id),colors:model.reflectionBundle.strands.map(s=>s.label),input:model.reflectionBundle.input,output:model.reflectionBundle.output};
 return group;
}
export function createSulfurReflection(model,state){
 if(state.reflectionView!=='geometry')return createWiring(model,state);
 const group=new T.Group(),selected=state.reflectionCopy??'all';
 for(const cell of model.reflectionCells){
  const vs=cell.copy.vertices.map(p=>new T.Vector3(...p)),active=selected==='all'||cell.histories.includes(selected);
  const color=model.reflectionCycle.includes(cell.id)?0x6fbeff:0xd6dce9;
  const lines=new T.LineSegments(new T.BufferGeometry().setFromPoints(pairs.flatMap(([a,b])=>[vs[a],vs[b]])),new T.LineBasicMaterial({color,transparent:true,opacity:active?1:.12}));
  group.add(lines);
  if(state.bodies&&!state.edgesOnly){
   const faces=new T.BufferGeometry().setFromPoints(triangles.flatMap(t=>t.map(i=>vs[i])));
   group.add(new T.Mesh(faces,new T.MeshBasicMaterial({color,side:T.DoubleSide,transparent:true,opacity:(active?.055:.008)*(state.faceOpacity??1),depthWrite:false})));
  }
  if(active)for(let i=0;i<5;i++){
   const sphere=new T.Mesh(new T.SphereGeometry(i>2?.035:.025,10,6),new T.MeshBasicMaterial({color:i===3?0xff739d:i===4?0xffd36b:color}));sphere.position.copy(vs[i]);group.add(sphere);
  }
 }
 if(state.reflectionCycle!==false){
  const centers=new Map(model.reflectionCells.map(c=>[c.id,c.copy.vertices.slice(0,3).reduce((sum,p)=>sum.add(new T.Vector3(...p)),new T.Vector3()).divideScalar(3)]));
  const cycle=model.reflectionCycle,segments=[];
  for(let i=0;i<cycle.length;i++){const a=centers.get(cycle[i]),b=centers.get(cycle[(i+1)%cycle.length]);if(a&&b)segments.push(a,b);}
  group.add(new T.LineSegments(new T.BufferGeometry().setFromPoints(segments),new T.LineBasicMaterial({color:0x20dbd0,depthTest:false,transparent:true,opacity:.9})));
 }
 group.userData.audit={...model.reflectionAudit,view:'geometry',angle:state.reflectionAngle??35,selectedCopy:selected};
 return group;
}
