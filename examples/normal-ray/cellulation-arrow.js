import * as T from 'three';
// Keep the segment, but put a half-sized direction marker at its midpoint.
export function createCellulationArrow(arrow,cellSize){
 const group=new T.Group(),from=new T.Vector3(...arrow.from),to=new T.Vector3(...arrow.to),direction=to.clone().sub(from),length=direction.length();direction.normalize();
 group.userData.cellulationArrow=arrow;
 const head=.08*cellSize,rotation=new T.Quaternion().setFromUnitVectors(new T.Vector3(0,1,0),direction);
 const material=()=>new T.MeshBasicMaterial({color:arrow.colour,transparent:true,depthTest:false,depthWrite:false});
 const shaft=new T.Mesh(new T.CylinderGeometry(.004*cellSize,.004*cellSize,length,12),material());shaft.quaternion.copy(rotation);shaft.renderOrder=5;group.add(shaft);
 const tip=new T.Mesh(new T.ConeGeometry(.0225*cellSize,head,16),material());tip.position.copy(from).lerp(to,.5);tip.quaternion.copy(rotation);tip.renderOrder=6;group.add(tip);
 group.userData.setProgress=value=>{
  const p=Math.max(0,Math.min(1,value));shaft.scale.y=p;shaft.position.copy(from).addScaledVector(direction,length*p/2);shaft.visible=p>0;tip.visible=p>=.5+head/(2*length);
 };
 group.userData.setProgress(1);return group;
}
