// Contact positions do not determine orientations. An axis plus a transverse
// reference constructs an oriented port frame; SVG projection supplies neither.
import {auditChannelTransport} from './channel-frame-transport.mjs';
const dot=(a,b)=>a.reduce((sum,x,i)=>sum+x*b[i],0);
const cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
const vector=v=>Array.isArray(v)&&v.length===3&&v.every(Number.isFinite);
const multiply=(a,b)=>a.map(row=>b[0].map((_,j)=>row.reduce((sum,x,k)=>sum+x*b[k][j],0)));
const transpose=a=>a[0].map((_,i)=>a.map(row=>row[i]));
function normalize(v){const scale=Math.max(...v.map(Math.abs));if(scale===0)return null;const scaled=v.map(x=>x/scale),n=Math.hypot(...scaled);return scaled.map(x=>x/n);}
function portFrame(port,label,tolerance){
 if(!port||port.axis===undefined)return {status:'unknown',issue:`${label}: missing directed axis`};
 if(!vector(port.axis))return {status:'refuted',issue:`${label}: invalid axis`};
 const z=normalize(port.axis);if(!z)return {status:'refuted',issue:`${label}: zero axis`};
 if(port.reference===undefined)return {status:'axis-only',axis:z};
 if(!vector(port.reference))return {status:'refuted',issue:`${label}: invalid reference`};
 const reference=normalize(port.reference);if(!reference)return {status:'refuted',issue:`${label}: zero reference`};
 const transverse=reference.map((v,i)=>v-dot(reference,z)*z[i]);if(Math.hypot(...transverse)<=tolerance)return {status:'refuted',issue:`${label}: reference parallel to axis`};
 const x=normalize(transverse),y=cross(z,x),frame=x.map((_,i)=>[x[i],y[i],z[i]]);
 return {status:'oriented',axis:z,frame};
}
export function solveContactFrameAlignment({source,target,tolerance=1e-9}={}){
 if(!Number.isFinite(tolerance)||tolerance<=0||tolerance>1e-3)throw Error('Tolerance must be in (0, 1e-3]');
 const a=portFrame(source,'source',tolerance),b=portFrame(target,'target',tolerance);
 const result={status:'unknown',source:a,target:b,
  convention:'Right-handed port frames have columns x,y,z: z is the directed transport axis, x is the transverse projection of the reference, y = z cross x. Both axes follow the forward traversal convention.',
  scope:'Conditional alignment of supplied 3D port data, not extraction of physical frames from a drawing. Opposing outward surface normals must first be converted to a consistent directed-transport convention.'};
 if([a,b].some(p=>p.status==='refuted')){result.status='refuted';return result;}
 if([a,b].some(p=>p.status==='unknown')){result.freedom='No selected rotation; a point contact alone leaves SO(3) orientation freedom.';return result;}
 if([a,b].some(p=>p.status==='axis-only')){result.status='underdetermined';result.freedom='SO(2): alignment of the directed axes leaves a rotation about the target axis. A transverse frame reference at both ends is still needed.';return result;}
 const rotation=multiply(b.frame,transpose(a.frame)),audit=auditChannelTransport([rotation],{tolerance});
 result.status=audit.status;result.rotation=rotation;result.reverseRotation=transpose(rotation);result.audit=audit;result.freedom='None for these supplied oriented frames: R = F_target F_source^T.';
 return result;
}
