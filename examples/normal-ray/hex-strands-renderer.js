import * as T from 'three';
export function createHexStrandsView(model,state){
 const group=new T.Group(),geometry=new T.CylinderGeometry(.013,.013,1,8,1),up=new T.Vector3(0,1,0);
 const object=new T.Object3D(),a=new T.Vector3(),b=new T.Vector3(),direction=new T.Vector3();
 for(const family of model.families){
  if(!family.selected&&state.hexStrandIsolate!==false)continue;
  if(!family.edges.length)continue;
  const color=new T.Color().setHSL(family.index/16,.8,.62),material=new T.MeshBasicMaterial({color,transparent:!family.selected,opacity:family.selected?1:.06,depthWrite:family.selected});
  const mesh=new T.InstancedMesh(geometry,material,family.edges.length);
  family.edges.forEach((edge,index)=>{
   a.fromArray(edge.points[0]);b.fromArray(edge.points[1]);direction.subVectors(b,a);
   object.position.copy(a).add(b).multiplyScalar(.5);object.quaternion.setFromUnitVectors(up,direction.clone().normalize());object.scale.set(1,direction.length(),1);object.updateMatrix();mesh.setMatrixAt(index,object.matrix);
  });
  mesh.userData.hexStrand=family.id;mesh.instanceMatrix.needsUpdate=true;group.add(mesh);
 }
 if(state.bodies){
  group.add(new T.LineSegments(new T.BufferGeometry().setFromPoints(model.context.flat().map(p=>new T.Vector3(...p))),new T.LineBasicMaterial({color:0x78869c,transparent:true,opacity:.14,depthWrite:false})));
 }
 group.userData.audit={...model.audit,visibleFamilies:group.children.filter(o=>o.userData.hexStrand).map(o=>o.userData.hexStrand)};
 return group;
}
