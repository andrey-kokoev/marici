import * as T from 'three';
import {createCellulationArrow} from './cellulation-arrow.js';
import {createCellulationProposition} from './cellulation-witness-renderer.js';
import {octahedronAt} from '../../research/realization-tower/cellulation-octahedron.mjs';
export function createOctahedralArrows(bridge,cellSize){
 const group=new T.Group(),arrows=bridge.arrows.map(a=>createCellulationArrow(a,cellSize));group.add(...arrows);
 const proposal=createCellulationProposition(bridge.opposite,cellSize);group.add(proposal);
 const dot=new T.Mesh(new T.SphereGeometry(.025*cellSize,16,12),new T.MeshBasicMaterial({color:0xffffff,transparent:true,opacity:0,depthTest:false,depthWrite:false}));dot.position.fromArray(bridge.opposite);dot.renderOrder=12;group.add(dot);
 // The two shared faces are already white on the completed tetrahedra.
 const faces=new T.Mesh(new T.BufferGeometry().setFromPoints(bridge.scaffold.faces.flatMap(f=>f.vertices.map(p=>new T.Vector3(...p)))),new T.MeshBasicMaterial({color:0xffffff,side:T.DoubleSide,transparent:true,opacity:0,depthTest:false,depthWrite:false}));faces.renderOrder=2;group.add(faces);
 const normal=new T.Vector3(...bridge.opposite).sub(new T.Vector3(...bridge.center)).normalize().toArray();
 const anchor={id:'octahedron:opposite',name:'opposite white dot',point:bridge.opposite,normal};
 const audit={};
 function update(elapsed,state={}){
  const frame=octahedronAt(elapsed);arrows.forEach((a,i)=>a.userData.setProgress(frame.progress[i]));
  proposal.visible=frame.fillProgress<1;dot.visible=frame.fillProgress>0;dot.material.opacity=frame.fillProgress;
  faces.visible=frame.fillProgress>0&&!state.edgesOnly;faces.material.opacity=.55*frame.fillProgress*(state.faceOpacity??1);
  Object.assign(audit,frame,{whiteFaceCount:faces.visible&&faces.material.opacity>0?bridge.cell.faces.length:0,newWhiteFaces:bridge.scaffold.faces.length,whiteFaceOpacity:faces.material.opacity,arrows:bridge.arrows,oppositeVertex:bridge.opposite,oppositeNormal:normal,proposalVisible:proposal.visible,whiteDotVisible:dot.visible});return frame.active;
 }
 update(0);return {group,anchor,update,audit};
}
