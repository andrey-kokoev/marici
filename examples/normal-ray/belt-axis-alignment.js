import {worldPoint} from '../../research/realization-tower/normal-ray-model.mjs';
const sub=(a,b)=>a.map((v,i)=>v-b[i]),dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],unit=a=>a.map(v=>v/Math.hypot(...a));
// Geometry presentation only: align an opposite-vertex (fourfold) axis,
// not the opposite-face (threefold) axis used by the reference docking pose.
export function alignBeltInnerAxis(surface,layout){
 const origin=worldPoint(layout.origin),target=unit(layout.normal),degree=surface.vertices.map((_,i)=>surface.edges.filter(e=>e.indices.includes(i)).length);
 const poles=surface.vertices.map((p,i)=>({p,i,direction:unit(sub(p,origin))})).filter(p=>degree[p.i]===4);
 const pole=poles.reduce((best,p)=>dot(p.direction,target)>dot(best.direction,target)+1e-12?p:best),from=pole.direction,turn=cross(from,target),sin=Math.hypot(...turn),cos=Math.max(-1,Math.min(1,dot(from,target))),axis=sin>1e-12?turn.map(v=>v/sin):[1,0,0];
 const rotate=p=>{const d=sub(p,origin),k=cross(axis,d);return origin.map((v,i)=>v+cos*d[i]+sin*k[i]+(1-cos)*dot(axis,d)*axis[i]);};
 return {...surface,vertices:surface.vertices.map(rotate),faces:surface.faces.map(f=>({...f,centre:rotate(f.centre)})),cellulation:{...surface.cellulation,vertices:surface.cellulation.vertices.map(rotate),parentLatticeAttachment:{status:'reference-docking-not-current-display',reference:surface.cellulation.parentLatticeAttachment}},axisAlignment:{kind:'opposite-vertex-axis-to-parent-normal',poleIndex:pole.i,sourceAxis:from,targetAxis:target,angleDegrees:Math.atan2(sin,cos)*180/Math.PI,scope:'Rigid rotation about belt centre in Geometry view only; not a new face gluing or cone-containment claim.'}};
}
