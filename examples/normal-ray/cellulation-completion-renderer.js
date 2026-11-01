import * as T from 'three';
import {createCellulationArrow} from './cellulation-arrow.js';
import {cellulationCompletionAt} from '../../research/realization-tower/cellulation-completion.mjs';
export function createCellulationCompletion(model,cellSize){
 const group=new T.Group(),arrow=createCellulationArrow(model.arrow,cellSize);group.add(arrow);
 const faces=new T.Mesh(new T.BufferGeometry().setFromPoints(model.faces.flatMap(face=>face.map(p=>new T.Vector3(...p)))),new T.MeshBasicMaterial({color:0xffffff,side:T.DoubleSide,transparent:true,opacity:0,depthTest:false,depthWrite:false}));faces.renderOrder=2;group.add(faces);
 const audit={};
 function update(elapsed,state={}){
  const frame=cellulationCompletionAt(elapsed);arrow.userData.setProgress(frame.arrowProgress);
  faces.visible=frame.faceFillProgress>0&&!state.edgesOnly;faces.material.opacity=.55*frame.faceFillProgress*(state.faceOpacity??1);
  Object.assign(audit,frame,{connectingArrow:model.arrow,whiteFaces:model.faces,whiteFaceCount:faces.visible&&faces.material.opacity>0?model.faces.length:0,whiteFaceOpacity:faces.material.opacity});return frame.active;
 }
 update(0);return {group,update,audit};
}
