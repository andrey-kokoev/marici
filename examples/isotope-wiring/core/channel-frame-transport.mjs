// Explicit transport data for a reversible channel. No SVG angle supplies a
// frame rotation. Inverses here are a declared connection rule, not native witnesses.
import {auditFrameReturn} from './frame-return.mjs';
const I=[[1,0,0],[0,1,0],[0,0,1]];
const multiply=(a,b)=>a.map(row=>b[0].map((_,j)=>row.reduce((sum,x,k)=>sum+x*b[k][j],0)));
const transpose=a=>a[0].map((_,i)=>a.map(row=>row[i]));
const isMatrix=a=>Array.isArray(a)&&a.length===3&&a.every(row=>Array.isArray(row)&&row.length===3&&row.every(Number.isFinite));
export function auditChannelTransport(forward,{reverse,tolerance=1e-9}={}){
 if(!Array.isArray(forward)||!forward.length)throw Error('A channel requires at least one segment');
 if(reverse!==undefined&&(!Array.isArray(reverse)||reverse.length!==forward.length))throw Error('Reverse data must follow reverse traversal order with equal length');
 const vertices=Array.from({length:forward.length+1},(_,i)=>({id:`channel:${i}`,role:'N'})),edges=[];
 const backward=reverse??[...forward].reverse().map(r=>isMatrix(r)?transpose(r):undefined);
 forward.forEach((transport,i)=>{
  const id=`segment:${i}`,r=`segment:${i}:reverse`;
  edges.push({id,from:vertices[i].id,to:vertices[i+1].id,support:id,reverse:r,...(transport===undefined?{}:{transport})});
  const back=backward[forward.length-1-i];edges.push({id:r,from:vertices[i+1].id,to:vertices[i].id,support:id,reverse:id,...(back===undefined?{}:{transport:back})});
 });
 const ids=forward.map((_,i)=>`segment:${i}`),backIds=[...ids].reverse().map(id=>id+':reverse');
 const audit=auditFrameReturn({vertices,edges,walks:[{id:'channel-out-and-back',kind:'N',base:vertices[0].id,edges:[...ids,...backIds]}]},{tolerance});
 const result={status:audit.status,segments:forward.length,reversePolicy:reverse===undefined?'Inverse matrices declared by construction':'Explicit reverse matrices supplied in reverse traversal order',audit};
 if(audit.status==='verified'){result.forwardTransport=forward.reduce((h,r)=>multiply(r,h),I);result.reverseTransport=backward.reduce((h,r)=>multiply(r,h),I);}
 return result;
}
export function bindChannelTransport(full,forward,options={}){
 if(!Array.isArray(forward)||forward.length!==full.interface.forward.length)throw Error('Transport count must match the declared channel segments');
 const audit=auditChannelTransport(forward,options);if(audit.status==='refuted')return {status:'refuted',audit};
 const topology=structuredClone(full.model.topology),edges=new Map(topology.edges.map(e=>[e.id,e]));
 const backward=options.reverse??[...forward].reverse().map(r=>r===undefined?undefined:transpose(r));
 full.interface.forward.forEach((id,i)=>{
  const e=edges.get(id),r=edges.get(e?.reverse);if(!e||!r||r.from!==e.to||r.to!==e.from||r.reverse!==e.id)throw Error('Missing channel inverse incidence');
  const f=forward[i],b=backward[forward.length-1-i];
  if(f===undefined)delete e.transport;else e.transport=structuredClone(f);
  if(b===undefined)delete r.transport;else r.transport=structuredClone(b);
 });
 return {status:audit.status,audit,topology,scope:'Only declared channel segments are assigned; neutral loops and PE circulation still need their own transports.'};
}
export function compareDirectAndMediatedTransport({direct,entry,exit,intermediateGauge,tolerance=1e-9}={}){
 const directAudit=auditChannelTransport([direct],{tolerance}),mediatedAudit=auditChannelTransport([entry,exit],{tolerance});
 const result={status:'unknown',direct:directAudit,mediated:mediatedAudit,
  convention:'Column frames: direct endpoint transport R; mediated endpoint transport B A (entry A, then exit B).',
  criterion:'Same external endpoint frames require R = B A. Reversibility alone does not enforce this equality.',
  scope:'Numerical connection comparison, not a physical law or a choice between direct and neutron-mediated contact.'};
 if([directAudit,mediatedAudit].some(r=>r.status==='refuted')){result.status='refuted';return result;}
 if([directAudit,mediatedAudit].some(r=>r.status==='unknown'))return result;
 const difference=(a,b)=>Math.max(...a.flatMap((row,i)=>row.map((x,j)=>Math.abs(x-b[i][j]))));
 result.endpointError=difference(directAudit.forwardTransport,mediatedAudit.forwardTransport);result.status=result.endpointError<=tolerance?'verified':'refuted';
 if(intermediateGauge!==undefined){
  const gaugeAudit=auditChannelTransport([intermediateGauge],{tolerance});
  if(gaugeAudit.status!=='verified'){result.status='refuted';result.gauge={status:'refuted',audit:gaugeAudit};return result;}
  const changedEntry=multiply(intermediateGauge,entry),changedExit=multiply(exit,transpose(intermediateGauge)),changed=auditChannelTransport([changedEntry,changedExit],{tolerance});
  const gaugeError=changed.status==='verified'?difference(changed.forwardTransport,mediatedAudit.forwardTransport):Infinity;
  result.gauge={status:gaugeError<=tolerance?'verified':'refuted',entry:changedEntry,exit:changedExit,endpointError:gaugeError,rule:'A -> H A; B -> B H^-1. Only the intermediate frame convention changes; external endpoint transport is preserved.'};
  if(result.gauge.status==='refuted')result.status='refuted';
 }
 return result;
}
