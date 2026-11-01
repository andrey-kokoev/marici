import * as T from 'three';
export function createNNPEComposition(layout,state){
 const group=new T.Group();group.visible=state.bodies!==false;
 for(const operation of layout.groups)for(const plane of operation.planes){
  const geometry=new T.BufferGeometry().setFromPoints(plane.corners.map(p=>new T.Vector3(...p)));geometry.setIndex([0,1,2,0,2,3]);geometry.computeVertexNormals();
  const mesh=new T.Mesh(geometry,new T.MeshBasicMaterial({color:plane.colour,side:T.DoubleSide,transparent:true,opacity:.4*(state.faceOpacity??1),depthWrite:false}));mesh.userData.nnpePlane=plane.name;mesh.visible=!state.edgesOnly;group.add(mesh);
  group.add(new T.LineLoop(new T.BufferGeometry().setFromPoints(plane.corners.map(p=>new T.Vector3(...p))),new T.LineBasicMaterial({color:plane.colour,transparent:true,opacity:.7})));
 }
 for(const join of layout.joins)group.add(new T.Line(new T.BufferGeometry().setFromPoints(join.points.map(p=>new T.Vector3(...p))),new T.LineBasicMaterial({color:0xe8b85d})));
 group.userData.audit={planeMeshes:group.children.filter(o=>o.userData.nnpePlane).length,intersectionPoints:0,portMeshes:0,labelSprites:0};
 return group;
}
