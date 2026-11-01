import {Matrix4,Vector3} from 'three';
export function renderedCellulationWitnessInput(root,cellSize=1){
 root.updateWorldMatrix(true,true);const inverse=root.matrixWorld.clone().invert(),solid=new Map(),key=p=>p.map(x=>Math.round(x*Math.SQRT2/cellSize)).join(',');
 function visit(o){
  if(!o.visible)return;
  if(o.geometry?.type==='SphereGeometry'&&(o.material?.opacity??1)>=1-1e-7){const k=key(new Vector3().setFromMatrixPosition(o.matrixWorld).applyMatrix4(inverse).toArray());if(!solid.has(k)||o.renderOrder>=solid.get(k).order)solid.set(k,{colour:o.material.color.getHex(),order:o.renderOrder});}
  for(const child of o.children)visit(child);
 }
 visit(root);
 return {arrows:renderedCellulationArrows(root),anchors:root.userData.cellulationAnchors.map(a=>({...a,solid:solid.has(key(a.point)),colour:solid.get(key(a.point))?.colour??null})),cells:root.userData.cellulationCells};
}
export function renderedCellulationArrows(root){
 root.updateWorldMatrix(true,true);const inverse=root.matrixWorld.clone().invert(),arrows=[];
 function visit(o){
  if(!o.visible)return;
  const arrow=o.userData.cellulationArrow,shaft=o.children[0];
  if(arrow&&shaft?.visible&&shaft.material?.opacity!==0){
   const transform=new Matrix4().multiplyMatrices(inverse,o.matrixWorld);
   arrows.push({from:new Vector3(...arrow.from).applyMatrix4(transform).toArray(),to:new Vector3(...arrow.to).applyMatrix4(transform).toArray(),color:shaft.material.color.getHex(),order:shaft.renderOrder});
  }
  for(const child of o.children)visit(child);
 }
 visit(root);return arrows;
}
