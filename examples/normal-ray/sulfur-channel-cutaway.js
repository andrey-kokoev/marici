import * as T from 'three';
import {MarchingCubes} from 'three/addons/objects/MarchingCubes.js';
import {worldPoint} from '../../research/realization-tower/normal-ray-model.mjs';
import {singleOctahedralEnvelope} from '../../research/realization-tower/single-octahedral-process.mjs';
import {buildPESymmetricSector} from '../../research/strominger/pe-symmetric-sector.mjs';

// Finite-thickness native honeycomb walls, with real passage subtraction.
// Chambers are empty: the view is not a single opaque filled carrier block.
export function createSulfurChannelCutaway(model,{cut=.5,resolution=96,wallThickness=.08,openExterior=true,cutDirection=[.35,-.85,.4]}={}){
 const sector=buildPESymmetricSector(1),centre=new T.Vector3(...worldPoint(sector.centre));
 const nativeAxes=[model.axis,[.5,-.5,.5,-.5],[.5,-.5,-.5,.5]];
 const vectors=nativeAxes.map(a=>new T.Vector3(...worldPoint(sector.centre.map((x,i)=>x+a[i]))).sub(centre)),scale=vectors[0].length(),axes=vectors.map(v=>v.normalize());
 const envelope=singleOctahedralEnvelope(1).map(p=>new T.Vector3(...worldPoint(p))),half=Math.max(...envelope.flatMap(p=>p.clone().sub(centre).toArray().map(Math.abs)))+.25;
 const R=3*scale,step=2*half/resolution;
 const cutNormal=new T.Vector3(...cutDirection).normalize(),cutExtent=Math.max(...envelope.map(p=>Math.abs(p.clone().sub(centre).dot(cutNormal))))+.05;
 const cutPosition=(2*T.MathUtils.clamp(cut,0,1)-1)*cutExtent;
 const passages=model.edges.map(edge=>{
  const start=new T.Vector3(...worldPoint(edge.guide[0])),end=new T.Vector3(...worldPoint(edge.guide[1])),direction=end.clone().sub(start).normalize();let extent=0;
  for(const strand of model.strands.filter(s=>edge.strandIds.includes(s.id)))for(const p of strand.edgeRuns.find(r=>r.edgeId===edge.id).points){
   const q=new T.Vector3(...worldPoint(p)).sub(start);extent=Math.max(extent,q.clone().addScaledVector(direction,-q.dot(direction)).length());
  }
  return {edgeId:edge.id,start,end,radius:extent+.024+.025,surface:edge.surface};
 });
 const solidValue=(x,y,z)=>{
  const q=[x-centre.x,y-centre.y,z-centre.z];
  const envelopeDistance=(R-axes.reduce((sum,a)=>sum+Math.abs(q[0]*a.x+q[1]*a.y+q[2]*a.z),0))/Math.sqrt(3);
  // Native cell faces lie on integer barycentric-coordinate planes. Restricting
  // their thin slabs to the envelope gives the actual honeycomb wall network.
  const coordinates=axes.map(a=>(q[0]*a.x+q[1]*a.y+q[2]*a.z)/scale);
  let wallDistance=Infinity;
  for(let j=0;j<4;j++){
   const native=sector.centre[j]+coordinates.reduce((sum,v,k)=>sum+v*nativeAxes[k][j],0);
   wallDistance=Math.min(wallDistance,Math.abs(native-Math.round(native))*scale/Math.sqrt(.75));
  }
  return Math.min(envelopeDistance-(openExterior?wallThickness*1.1:0),wallThickness/2-wallDistance,cutPosition-q[0]*cutNormal.x-q[1]*cutNormal.y-q[2]*cutNormal.z);
 };
 const material=new T.MeshBasicMaterial({vertexColors:true,side:T.DoubleSide}),march=new MarchingCubes(resolution,material,false,false,200000);march.isolation=0;
 const field=march.field,n=resolution,n2=n*n;
 for(let z=0;z<n;z++)for(let y=0;y<n;y++)for(let x=0;x<n;x++)field[x+y*n+z*n2]=solidValue(centre.x-half+x*step,centre.y-half+y*step,centre.z-half+z*step);
 // Restrict each capsule subtraction to its local voxel bounds.
 for(const passage of passages){
  const a=passage.start,b=passage.end,r=passage.radius,d=b.clone().sub(a),length2=d.lengthSq();
  const lo=[0,1,2].map(i=>Math.max(0,Math.floor((Math.min(a.getComponent(i),b.getComponent(i))-r-centre.getComponent(i)+half)/step)-1));
  const hi=[0,1,2].map(i=>Math.min(n-1,Math.ceil((Math.max(a.getComponent(i),b.getComponent(i))+r-centre.getComponent(i)+half)/step)+1));
  for(let z=lo[2];z<=hi[2];z++)for(let y=lo[1];y<=hi[1];y++)for(let x=lo[0];x<=hi[0];x++){
   const dx=centre.x-half+x*step-a.x,dy=centre.y-half+y*step-a.y,dz=centre.z-half+z*step-a.z,t=Math.max(0,Math.min(1,(dx*d.x+dy*d.y+dz*d.z)/length2));
   const distance=Math.hypot(dx-t*d.x,dy-t*d.y,dz-t*d.z)-r,index=x+y*n+z*n2;
   field[index]=Math.min(field[index],distance);
  }
 }
 march.update();
 if(march.count>200000*3)throw Error('Carved geometry exceeds its mesh budget');
 const geometry=new T.BufferGeometry(),positions=march.geometry.attributes.position.array.slice(0,march.count*3),normals=march.geometry.attributes.normal.array.slice(0,march.count*3),colors=new Float32Array(march.count*3);
 const cells=sector.cells.map(c=>({...c,lo:[0,1,2,3].map(i=>Math.min(...c.vertices.map(p=>p[i]))),hi:[0,1,2,3].map(i=>Math.max(...c.vertices.map(p=>p[i])))}));
 const palette={proton:new T.Color(0x1265a8),electron:new T.Color(0xa82664),neutron:new T.Color(0xd5dce5)},passageColor=new T.Color(0x35dfcc),light=new T.Vector3(.3,.8,1).normalize();
 const capsules=passages.map(c=>{const d=c.end.clone().sub(c.start);return {x:c.start.x,y:c.start.y,z:c.start.z,dx:d.x,dy:d.y,dz:d.z,length2:d.lengthSq(),radius:c.radius};});
 let passageSurfaceVertices=0;
 for(let i=0;i<march.count;i++){
  const p=new T.Vector3(positions[i*3]*half,positions[i*3+1]*half,positions[i*3+2]*half),coordinates=axes.map(a=>p.dot(a)/scale);
  const native=sector.centre.map((x,j)=>x+coordinates.reduce((sum,v,k)=>sum+v*nativeAxes[k][j],0));
  const cell=cells.find(c=>native.every((x,j)=>x>=c.lo[j]-1e-5&&x<=c.hi[j]+1e-5));
  const normal=new T.Vector3(normals[i*3],normals[i*3+1],normals[i*3+2]).normalize(),shade=.55+.45*Math.max(0,normal.dot(light));
  p.add(centre);
  let passageDistance=Infinity;
  for(const c of capsules){const x=p.x-c.x,y=p.y-c.y,z=p.z-c.z,t=T.MathUtils.clamp((x*c.dx+y*c.dy+z*c.dz)/c.length2,0,1);passageDistance=Math.min(passageDistance,Math.hypot(x-t*c.dx,y-t*c.dy,z-t*c.dz)-c.radius);}
  const carved=Math.abs(passageDistance)<step*.85;if(carved)passageSurfaceVertices++;
  const color=(carved?passageColor:palette[cell?.role]??palette.neutron).clone().multiplyScalar(carved?.9:shade);colors.set(color.toArray(),i*3);
  positions.set(p.toArray(),i*3);
 }
 geometry.setAttribute('position',new T.BufferAttribute(positions,3));geometry.setAttribute('normal',new T.BufferAttribute(normals,3));geometry.setAttribute('color',new T.BufferAttribute(colors,3));geometry.computeBoundingSphere();march.geometry.dispose();
 const mesh=new T.Mesh(geometry,material);mesh.userData.channelCutaway=true;
 mesh.userData.audit={kind:'honeycomb-walls-minus-wire-passages',resolution,cut,wallThickness,openExterior,passageSurfaceVertices,cutNormal:cutNormal.toArray(),carrierCells:sector.cells.length,strands:model.strands.length,passages:passages.length,surfaceGrooves:passages.filter(p=>p.surface).length,interiorPassages:passages.filter(p=>!p.surface).length,triangles:march.count/3,voxelStep:step,approximate:true};
 // Retained samples allow geometric regression tests without relying on screenshots.
 mesh.userData.sampleSolid=p=>{
  let value=solidValue(p.x,p.y,p.z);
  for(const passage of passages){const d=passage.end.clone().sub(passage.start),q=p.clone().sub(passage.start),t=T.MathUtils.clamp(q.dot(d)/d.lengthSq(),0,1);value=Math.min(value,q.addScaledVector(d,-t).length()-passage.radius);}
  return value;
 };
 mesh.userData.passages=passages;
 return mesh;
}
