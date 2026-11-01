import * as T from 'three';
export class Polyline extends T.Curve{
 constructor(points){super();this.points=points.map(p=>new T.Vector3(...p));}
 getPoint(t,target=new T.Vector3()){
  const u=t*(this.points.length-1),i=Math.min(this.points.length-1,Math.floor(u));
  return target.copy(this.points[i]).lerp(this.points[Math.min(i+1,this.points.length-1)],u-i);
 }
}
export function createSeedSidePair(pair){
 const group=new T.Group(),up=new T.Vector3(0,1,0);
 group.userData.seedSidePair=pair.id;group.userData.layerIndex=pair.layerIndex;
 for(const conductor of pair.conductors){
  const mesh=new T.Mesh(new T.TubeGeometry(new Polyline(conductor.points),conductor.points.length*2,.022,8,false),new T.MeshBasicMaterial({color:conductor.colour==='blue'?0x438bff:0xff4545}));
  mesh.userData.sidePairConductor=conductor.id;mesh.userData.colour=conductor.colour;group.add(mesh);
 }
 const sleeveMaterial=new T.MeshBasicMaterial({color:0xf3f6ff,transparent:true,opacity:.55,depthWrite:false});
 const arrowMaterial=new T.MeshBasicMaterial({color:0xffffff});
 for(const band of pair.bands.filter(b=>b.role==='white')){
  const a=new T.Vector3(...band.axisPoints[0]),b=new T.Vector3(...band.axisPoints[1]),direction=b.clone().sub(a).normalize();
  const sleeve=new T.Mesh(new T.CylinderGeometry(.12,.12,a.distanceTo(b),12),sleeveMaterial);
  sleeve.position.copy(a).add(b).multiplyScalar(.5);sleeve.quaternion.setFromUnitVectors(up,direction);
  sleeve.userData.sidePairSleeve={start:band.start,end:band.end,sourceEdges:band.sourceEdges};group.add(sleeve);
  const arrow=new T.Mesh(new T.ConeGeometry(.13,.24,12),arrowMaterial);
  arrow.position.copy(sleeve.position);arrow.quaternion.copy(sleeve.quaternion);
  arrow.userData.sidePairDirection={from:band.axisPoints[0],to:band.axisPoints[1]};group.add(arrow);
 }
 return group;
}
