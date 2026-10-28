import * as T from 'three';
import {mergeGeometries} from 'three/addons/utils/BufferGeometryUtils.js';
import {worldPoint} from '../../research/realization-tower/normal-ray-model.mjs';
// Explicit family-level completion; not extra retained strand identities.
export function createBlueComplement(model){
 const geometries=model.blueCompletion.additionalEdges.map(e=>new T.TubeGeometry(new T.LineCurve3(new T.Vector3(...worldPoint(e.guide[0])),new T.Vector3(...worldPoint(e.guide[1]))),1,.024,12,false));
 const group=new T.Group();group.userData.edgeIds=model.blueCompletion.additionalEdges.map(e=>e.id);
 if(geometries.length){
  const mesh=new T.Mesh(mergeGeometries(geometries),new T.MeshBasicMaterial({color:0x168fff,depthTest:false,depthWrite:false}));
  geometries.forEach(g=>g.dispose());mesh.userData.blueCompletion=true;mesh.layers.set(1);mesh.renderOrder=14;group.add(mesh);
 }
 return group;
}
