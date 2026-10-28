import * as T from 'three';
import {ConvexGeometry} from 'three/addons/geometries/ConvexGeometry.js';

// Locate disjoint circular ports before cutting back any segment. Return null
// when the available native-edge length cannot accommodate an honest joint.
export function planTubeJunction(centre,ports){
 const radius=Math.max(...ports.map(p=>p.radius));let factor=1.1;
 for(let i=0;i<ports.length;i++)for(let j=i+1;j<ports.length;j++){
  const cosine=T.MathUtils.clamp(ports[i].direction.dot(ports[j].direction),-1,1);
  if(cosine>.9999)return null;
  factor=Math.max(factor,1.05*Math.sqrt((1+cosine)/(1-cosine)));
 }
 const distance=Math.min(radius*factor,...ports.map(p=>.42*p.edgeLength));
 if(distance<=radius)return null;
 for(let i=0;i<ports.length;i++)for(let j=0;j<ports.length;j++)if(i!==j){
  const cosine=ports[i].direction.dot(ports[j].direction);
  if(distance*cosine+ports[j].radius*Math.sqrt(Math.max(0,1-cosine*cosine))>=distance-1e-6)return null;
 }
 return {centre,radius,distance,ports};
}

// Convex, open-port junction skin. Its boundary vertices are the very same
// ring samples used by the incident swept tubes; there are no hidden end caps.
export function createTubeJunctionGeometry(centre,radius,rings){
 const sphere=new T.IcosahedronGeometry(radius,1),points=rings.flat().map(p=>p.clone());
 for(let i=0;i<sphere.attributes.position.count;i++)points.push(new T.Vector3().fromBufferAttribute(sphere.attributes.position,i).add(centre));
 sphere.dispose();
 const hull=new ConvexGeometry(points),planes=rings.map(r=>{
  const c=r.reduce((sum,p)=>sum.add(p),new T.Vector3()).divideScalar(r.length);
  const normal=new T.Vector3().crossVectors(r[1].clone().sub(r[0]),r[2].clone().sub(r[0])).normalize();return new T.Plane().setFromNormalAndCoplanarPoint(normal,c);
 });
 const positions=[],indices=[],vertices=new Map(),attribute=hull.attributes.position;
 for(let i=0;i<attribute.count;i+=3){
  const triangle=[0,1,2].map(k=>new T.Vector3().fromBufferAttribute(attribute,i+k));
  if(planes.some(plane=>triangle.every(p=>Math.abs(plane.distanceToPoint(p))<1e-5)))continue;
  for(const p of triangle){const key=p.toArray().map(x=>Math.round(x*1e6)).join(',');if(!vertices.has(key)){vertices.set(key,positions.length/3);positions.push(...p.toArray());}indices.push(vertices.get(key));}
 }
 hull.dispose();const geometry=new T.BufferGeometry();geometry.setAttribute('position',new T.Float32BufferAttribute(positions,3));geometry.setIndex(indices);geometry.computeVertexNormals();geometry.userData.portCount=rings.length;
 return geometry;
}
