import * as T from 'three';
import {createCellulationArrow} from './cellulation-arrow.js';
import {cellulationWitnessAt} from '../../research/realization-tower/cellulation-witness.mjs';
export function createCellulationProposition(point,cellSize,colour=0xffffff){
 const ring=new T.Mesh(new T.RingGeometry(.021*cellSize,.025*cellSize,48),new T.MeshBasicMaterial({color:colour,side:T.DoubleSide,transparent:true,depthTest:false,depthWrite:false}));
 ring.position.fromArray(point);ring.renderOrder=11;ring.userData.cellulationBillboard=true;return ring;
}
export function createCellulationWitness(witness,cellSize){
 const group=new T.Group(),proposal=createCellulationProposition(witness.proposedVertex,cellSize),red=0xff3030;group.add(proposal);
 const dot=new T.Mesh(new T.SphereGeometry(.025*cellSize,16,12),new T.MeshBasicMaterial({color:0xffffff,transparent:true,depthTest:false,depthWrite:false}));dot.position.fromArray(witness.proposedVertex);dot.renderOrder=12;group.add(dot);
 const plane=new T.Mesh(new T.BufferGeometry().setFromPoints(witness.faces.flatMap(face=>face.map(p=>new T.Vector3(...p)))),new T.MeshBasicMaterial({color:red,side:T.DoubleSide,transparent:true,opacity:0,depthTest:false,depthWrite:false}));plane.renderOrder=2;group.add(plane);
 const returns=[0,1].map(i=>createCellulationArrow({from:witness.returnPath[i],to:witness.returnPath[i+1],colour:0xffffff},cellSize));returns.forEach(a=>group.add(a));
 const turnMarkers=[...witness.priorTurnMarkers.map(marker=>({...marker,prior:true})),{...witness.turnMarker,prior:false}].map(marker=>{
  const outline=createCellulationProposition(marker.point,cellSize,red);
  const solid=new T.Mesh(new T.SphereGeometry(.025*cellSize,16,12),new T.MeshBasicMaterial({color:red,transparent:true,opacity:0,depthTest:false,depthWrite:false}));solid.position.fromArray(marker.point);solid.renderOrder=12;group.add(outline,solid);
  return {...marker,outline,solid};
 });
 const audit={};
 function update(elapsed,state={},vertexFillProgress=0){
  const frame=cellulationWitnessAt(elapsed,witness.stage);returns[0].userData.setProgress(frame.first);returns[1].userData.setProgress(frame.second);
  dot.visible=witness.stage===5&&frame.witnessed;proposal.visible=!dot.visible;plane.visible=witness.faces.length>0&&frame.witnessed&&!state.edgesOnly;plane.material.opacity=.55*frame.fillProgress*(state.faceOpacity??1);
  const markerAudit=turnMarkers.map(marker=>{
   const appeared=marker.prior||frame.first===1;
   marker.outline.visible=appeared&&vertexFillProgress<1;marker.solid.visible=appeared&&vertexFillProgress>0;marker.solid.material.opacity=vertexFillProgress;
   return {id:marker.id,name:marker.name,point:marker.point,outlineVisible:marker.outline.visible,solidVisible:marker.solid.visible,fillProgress:vertexFillProgress};
  });
  Object.assign(audit,frame,{turnMarkers:markerAudit,proposalVisible:proposal.visible,whiteDotVisible:dot.visible,redFaceVisible:plane.visible&&plane.material.opacity>0,redFaceCount:plane.visible&&plane.material.opacity>0?witness.faces.length:0,colouredFaces:witness.faces,faceOpacity:plane.material.opacity,returnPath:witness.returnPath,proposedVertex:witness.proposedVertex});
  return frame.active;
 }
 update(0);return {group,update,audit};
}
