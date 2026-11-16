import { buildShell } from './model.js';

export function createSpanLayer(THREE, scene, track) {
  const shell=buildShell(),positions=shell.vertices.map(v=>new THREE.Vector3(...v.position));
  const faceGeometry=track(new THREE.BufferGeometry().setFromPoints(shell.triangles.flatMap(face=>face.map(i=>positions[i]))));
  faceGeometry.computeVertexNormals();
  const faceMaterial=track(new THREE.MeshBasicMaterial({color:0xf4c430,transparent:true,opacity:0.12,side:THREE.DoubleSide,depthWrite:false}));
  scene.add(new THREE.Mesh(faceGeometry,faceMaterial));
  const wireGeometry=track(new THREE.BufferGeometry().setFromPoints(shell.edges.flatMap(edge=>edge.map(i=>positions[i]))));
  scene.add(new THREE.LineSegments(wireGeometry,track(new THREE.LineBasicMaterial({color:0xffd891}))));
  return {
    update({opacity}){faceMaterial.opacity=opacity;},
    snapshot:()=>({order:shell.order,vertexCount:shell.vertices.length,edgeCount:shell.edges.length,triangleCount:shell.triangles.length,opacity:faceMaterial.opacity}),
  };
}
