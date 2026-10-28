import * as T from 'three';
import {MarchingCubes} from 'three/addons/objects/MarchingCubes.js';
import {worldPoint} from '../../research/realization-tower/normal-ray-model.mjs';

const vector=p=>new T.Vector3(...worldPoint(p));
let cached;
// One union surface, not intersecting transparent cylinders with sealed joints.
export function sulfurHandlebodySurface(model,resolution=96){
 const cacheKey=JSON.stringify([resolution,model.nodes.map(n=>[n.id,n.position]),model.links.map(l=>[l.from,l.to]),model.ports]);
 if(cached?.key===cacheKey)return cached.value;
 const positions=new Map(model.nodes.map(n=>[n.id,vector(n.position)]));
 const unit=Math.min(...model.links.map(e=>positions.get(e.from).distanceTo(positions.get(e.to))));
 const radius=unit*.145,primitives=[];
 for(const n of model.nodes){const p=positions.get(n.id);primitives.push({a:p,b:p,radius:unit*(n.kind==='N-chamber'?.31:.24)});}
 for(const e of model.links)primitives.push({a:positions.get(e.from),b:positions.get(e.to),radius});
 const mouths=model.ports.map(p=>{const at=vector(p.position),direction=at.clone().sub(positions.get(p.owner)).normalize();primitives.push({a:positions.get(p.owner),b:at.clone().addScaledVector(direction,4*radius),radius});return {...p,at,direction,radius};});
 const box=new T.Box3();for(const p of primitives){box.expandByPoint(p.a);box.expandByPoint(p.b);}box.expandByScalar(unit*.5);
 const origin=box.getCenter(new T.Vector3()),half=Math.max(...box.getSize(new T.Vector3()).toArray())/2,spacing=2*half/resolution;
 const mc=new MarchingCubes(resolution,new T.MeshBasicMaterial(),false,false,150000);mc.isolation=0;mc.field.fill(-4*spacing);
 for(const p of primitives){
  const a=p.a.toArray(),b=p.b.toArray(),o=origin.toArray(),delta=b.map((v,i)=>v-a[i]),length2=delta.reduce((s,v)=>s+v*v,0),pad=p.radius+3*spacing;
  const lower=a.map((v,i)=>Math.max(1,Math.floor((Math.min(v,b[i])-pad-o[i]+half)/spacing))),upper=a.map((v,i)=>Math.min(resolution-2,Math.ceil((Math.max(v,b[i])+pad-o[i]+half)/spacing)));
  for(let z=lower[2];z<=upper[2];z++)for(let y=lower[1];y<=upper[1];y++)for(let x=lower[0];x<=upper[0];x++){
   const q=[o[0]-half+x*spacing,o[1]-half+y*spacing,o[2]-half+z*spacing],t=length2?Math.max(0,Math.min(1,delta.reduce((s,d,i)=>s+(q[i]-a[i])*d,0)/length2)):0;
   const distance=Math.hypot(...q.map((v,i)=>v-a[i]-t*delta[i])),index=x+resolution*(y+resolution*z);
   mc.field[index]=Math.max(mc.field[index],p.radius-distance);
  }
 }
 mc.update();
 const count=mc.geometry.drawRange.count,vertices=mc.geometry.attributes.position.array.slice(0,count*3),normals=mc.geometry.attributes.normal.array.slice(0,count*3);
 for(let i=0;i<vertices.length;i++)vertices[i]=vertices[i]*half+origin.getComponent(i%3);
 mc.geometry.dispose();mc.material.dispose();
 const value={positions:vertices,normals,mouths,radius,resolution,triangles:count/3};cached={key:cacheKey,value};return value;
}

export function createSulfurHandlebody(model,{opacity=1}={}){
 const surface=sulfurHandlebodySurface(model),group=new T.Group(),geometry=new T.BufferGeometry();
 geometry.setAttribute('position',new T.BufferAttribute(surface.positions,3));geometry.setAttribute('normal',new T.BufferAttribute(surface.normals,3));geometry.computeBoundingSphere();
 // Clip the six extended end caps to expose actual tube mouths. No internal
 // caps are present: every shared-face neck belongs to the same union surface.
 const clippingPlanes=surface.mouths.map(p=>new T.Plane().setFromNormalAndCoplanarPoint(p.direction.clone().negate(),p.at));
 const material=new T.MeshStandardMaterial({color:0xa2c7ce,roughness:.48,metalness:.05,side:T.DoubleSide,transparent:true,opacity,depthWrite:opacity===1,clippingPlanes});
 const skin=new T.Mesh(geometry,material);skin.userData.sulfurHandlebodySkin=true;group.add(skin);
 const portColors=[0xe1bc65,0x70b7ba,0xb9a0dc];
 for(const p of surface.mouths){const ring=new T.Mesh(new T.TorusGeometry(p.radius,p.radius*.13,8,32),new T.MeshStandardMaterial({color:portColors[p.pair],roughness:.45}));ring.position.copy(p.at);ring.quaternion.setFromUnitVectors(new T.Vector3(0,0,1),p.direction);group.add(ring);}
 group.add(new T.AmbientLight(0xffffff,1.5));
 const light=new T.DirectionalLight(0xffffff,2.4);light.position.set(4,7,5);group.add(light);
 const fill=new T.DirectionalLight(0x8bb9dd,1);fill.position.set(-5,-2,-4);group.add(fill);
 group.userData.audit={...model.audit,rendering:'single-union-isosurface',resolution:surface.resolution,triangles:surface.triangles,openMouths:6};
 return group;
}
