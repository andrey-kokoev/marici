import * as T from 'three';

// Welded ring sweep along a native polyline. Miter rings stay centred on the
// honeycomb vertices; unlike spline smoothing, bends do not cut across cells.
export function createHoneycombTubeGeometry(points,radius,{closed=false,sides=24}={}){
 const centres=closed?points.slice(0,-1):points;
 if(centres.length<2)throw Error('Tube needs at least two distinct vertices');
 const positions=[],indices=[],rings=[];
 const direction=(a,b)=>b.clone().sub(a).normalize();
 const initial=closed?direction(centres.at(-1),centres[0]):direction(centres[0],centres[1]);
 let normal=new T.Vector3().crossVectors(initial,Math.abs(initial.y)<.9?new T.Vector3(0,1,0):new T.Vector3(1,0,0)).normalize();
 for(let i=0;i<centres.length;i++){
  const incoming=i>0?direction(centres[i-1],centres[i]):closed?direction(centres.at(-1),centres[0]):null;
  const outgoing=i<centres.length-1?direction(centres[i],centres[i+1]):closed?direction(centres[i],centres[0]):null;
  const base=incoming??outgoing,tangent=incoming&&outgoing?incoming.clone().add(outgoing).normalize():base;
  if(tangent.lengthSq()<.5)throw Error('Cannot sweep a tube through a reversing cusp');
  const frameNormal=normal.clone().applyQuaternion(new T.Quaternion().setFromUnitVectors(base,tangent));
  const frameBinormal=new T.Vector3().crossVectors(tangent,frameNormal).normalize();
  const bend=incoming&&outgoing?outgoing.clone().sub(incoming).normalize():new T.Vector3();
  const cosine=Math.max(.001,base.dot(tangent)),ring=[];
  for(let k=0;k<sides;k++){
   const angle=2*Math.PI*k/sides,offset=frameNormal.clone().multiplyScalar(radius*Math.cos(angle)).addScaledVector(frameBinormal,radius*Math.sin(angle));
   offset.addScaledVector(bend,offset.dot(bend)*(1/cosine-1));
   const p=centres[i].clone().add(offset);positions.push(...p.toArray());ring.push(p);
  }
  rings.push(ring);
  if(incoming&&outgoing)normal.applyQuaternion(new T.Quaternion().setFromUnitVectors(incoming,outgoing));
 }
 const spans=closed?centres.length:centres.length-1;
 for(let i=0;i<spans;i++)for(let k=0;k<sides;k++){
  const a=i*sides+k,b=i*sides+(k+1)%sides,c=((i+1)%centres.length)*sides+k,d=((i+1)%centres.length)*sides+(k+1)%sides;
  indices.push(a,c,b,b,c,d);
 }
 const geometry=new T.BufferGeometry();geometry.setAttribute('position',new T.Float32BufferAttribute(positions,3));geometry.setIndex(indices);geometry.computeVertexNormals();
 geometry.userData={ringCount:rings.length,sides,closed};
 return {geometry,rings};
}
