// Source: proton-neutron-assembly.html#placeFaceOnRim and neutron-rim-port-transport.md.
// One checked rim attachment primitive. NOT the two-belt interwoven assembly.
import source from '../voevodsky/results/four_six_center_cones.json' with {type:'json'};
import {buildFoldedFibration} from './fibration-folded-process.mjs';
import {fibrationDisplayEnvelope} from './fibration12-process.mjs';
import {worldPoint} from './normal-ray-model.mjs';
import {beltViewerPoint,neutronBeltProcess} from './neutron-belt-process.mjs';
const add=(a,b)=>a.map((x,i)=>x+b[i]),sub=(a,b)=>a.map((x,i)=>x-b[i]),mul=(a,s)=>a.map(x=>x*s),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],norm=a=>Math.hypot(...a),unit=a=>mul(a,1/norm(a));
const center=ps=>mul(ps.reduce(add,[0,0,0]),1/ps.length);
const frame=ps=>{const x=unit(sub(ps[1],ps[0])),z=unit(cross(x,sub(ps[2],ps[0])));return [x,cross(z,x),z];};
const rational=s=>{const [a,b='1']=s.split('/');return Number(a)/Number(b);};
export function placeFaceOnRim(face,target){
 const a=frame(face),b=frame(target),ca=center(face),cb=center(target);
 for(let i=0;i<3;i++)for(let j=i+1;j<3;j++)if(Math.abs(norm(sub(face[i],face[j]))-norm(sub(target[i],target[j])))>1e-8)throw Error('Rim metric mismatch');
 return p=>add(cb,b.reduce((s,v,i)=>add(s,mul(v,dot(sub(p,ca),a[i]))),[0,0,0]));
}
export function buildRimMatchedEsd7(){
 const m=buildFoldedFibration(),original=fibrationDisplayEnvelope.slice(0,4),clone=fibrationDisplayEnvelope.slice(4),same=(a,b)=>norm(sub(a,b))<1e-8;
 const shared=original.filter(p=>clone.some(q=>same(p,q))),triangle=shared.map(worldPoint);
 if(shared.length!==3)throw Error('Expected shared ESD7 face');
 const scale=norm(sub(triangle[0],triangle[1]))/Math.sqrt(3);
 const rimPoints=Object.fromEntries(Object.entries(source.belt_scaled_coordinates).map(([id,p])=>{const [x,y,z]=p.map(rational);return [id,mul([Math.sqrt(3)*x,y,z],scale)];}));
 const parents=[],ports=[];
 for(const [copy,prefix,side,envelope] of [['original','L',-1,original],['clone','U',1,clone]]){
  const apex=worldPoint(envelope.find(p=>!shared.some(q=>same(p,q))));
  let names=[`${prefix}0`,`${prefix}1`,`${prefix}2`],target=names.map(n=>rimPoints[n]),map=placeFaceOnRim(triangle,target);
  if(side*(map(apex)[1]-center(target)[1])<=0){names=[names[0],names[2],names[1]];target=names.map(n=>rimPoints[n]);map=placeFaceOnRim(triangle,target);}
  if(side*(map(apex)[1]-center(target)[1])<=0)throw Error('Parent apex not outside belt');
  const transform=q=>beltViewerPoint(map(worldPoint(q)));
  for(const o of m.occurrences.filter(o=>o.copy===copy))parents.push({...o,kind:m.geometry.find(g=>g.id===o.sourceGeometry).kind,vertices:o.vertices.map(transform),faces:o.faces.map(f=>f.map(transform))});
  ports.push({copy,rim:names,source:shared,target:target.map(beltViewerPoint),apex:beltViewerPoint(map(apex)),maxVertexGap:Math.max(...triangle.map((p,i)=>norm(sub(map(p),target[i])))),map:transform});
 }
 const belt=neutronBeltProcess(7,0),transform=q=>beltViewerPoint(mul(worldPoint(q),scale));
 const bodies=belt.retainedBodies.map(b=>({...b,opacity:.22,vertices:b.vertices.map(transform),faces:b.faces.map(f=>f.map(transform))}));
 const n=cross(sub(triangle[1],triangle[0]),sub(triangle[2],triangle[0])),originalApex=worldPoint(original.find(p=>!shared.some(q=>same(p,q)))),originalSide=dot(sub(originalApex,triangle[0]),n);
 const mapParentPoint=(p,copy)=>ports.find(port=>port.copy===(copy??(dot(sub(worldPoint(p),triangle[0]),n)*originalSide>=-1e-8?'original':'clone'))).map(p);
 return {parents,bodies,ports,mapParentPoint,audit:{scope:'single-belt rim attachment primitive; not interwoven pair',parentCells:parents.length,beltCells:bodies.length,beltScale:scale,rimGap:source.gap,capConesAdded:0,interwovenPair:false,sharedFaceGluingReplaced:true,beltMetric:'uniformly scaled native six-cone geometry',parentMetric:'rigid motions only'}};
}
