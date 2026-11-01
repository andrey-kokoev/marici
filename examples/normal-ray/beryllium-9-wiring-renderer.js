import * as T from 'three';
export function createBeryllium9Wiring(model){
 const group=new T.Group();
 for(const wire of model.wires){
  const curve=new T.CurvePath();for(let i=1;i<wire.points.length;i++)curve.add(new T.LineCurve3(new T.Vector3(...wire.points[i-1]),new T.Vector3(...wire.points[i])));
  const material=new T.MeshBasicMaterial({color:wire.colour}),mesh=new T.Mesh(new T.TubeGeometry(curve,320,.018,8,false),material);
  mesh.userData.wireId=wire.id;mesh.userData.strandId=wire.strandId;group.add(mesh);
 }
 group.userData.audit=model.audit;return group;
}
