import {sulfur32Process} from './sulfur-32-process.mjs';
import {removeSulfurTubesTips} from './sulfur-32-tubes-view.mjs';
import {junctionCoordinates,polygonArea,subtractTubesJunction} from './sulfur-32-junction-cut.mjs';
const sub=(a,b)=>a.map((x,i)=>x-b[i]);
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
const centre=vs=>vs[0].map((_,i)=>vs.reduce((s,p)=>s+p[i]/vs.length,0));
const faceKey=vs=>vs.map(v=>v.join(',')).sort().join('|');
const eps=1e-9;
// Includes coplanar contact. Input polygons are convex clipped wall patches.
export function segmentHitsWall(start,end,polygon){
 const p=polygon.map(junctionCoordinates),a=junctionCoordinates(start),b=junctionCoordinates(end);
 let n;
 for(let i=1;i<p.length-1;i++){const candidate=cross(sub(p[i],p[0]),sub(p[i+1],p[0]));if(dot(candidate,candidate)>eps*eps){n=candidate;break;}}
 if(!n)return false;
 n=n.map(x=>x/Math.sqrt(dot(n,n)));
 const da=dot(n,sub(a,p[0])),db=dot(n,sub(b,p[0]));let low=0,high=1;
 if(Math.abs(da)>eps||Math.abs(db)>eps){
  if(Math.abs(da-db)<eps)return false;
  low=high=da/(da-db);if(low<0||low>1)return false;
 }
 const mid=centre(p);
 for(let i=0;i<p.length;i++){
  let inward=cross(n,sub(p[(i+1)%p.length],p[i]));if(dot(inward,sub(mid,p[i]))<0)inward=inward.map(x=>-x);
  const d=dot(inward,sub(a,p[i])),slope=dot(inward,sub(b,a));
  if(Math.abs(slope)<eps){if(d< -eps)return false;continue;}
  const t=-d/slope;if(slope>0)low=Math.max(low,t);else high=Math.min(high,t);
  if(low>high+eps)return false;
 }
 return high>=0&&low<=1&&low<=high+eps;
}

export function auditSulfur32TubesPaths(step=0){
 const model=removeSulfurTubesTips(sulfur32Process(7,step));
 const inner=model.tubesCutPrisms.filter(p=>p.layer===1),outer=model.tubesCutPrisms.filter(p=>p.layer===0);
 const hub=centre(inner[0].prisms.flatMap(p=>p.back));
 const walls=model.tubesCutPrisms.flatMap(p=>p.walls).concat(model.retainedBodies.flatMap(c=>c.faces));
 const ports=outer.flatMap(pair=>pair.prisms.map((prism,i)=>{
  const mouth=centre(prism.front),blockers=walls.flatMap((w,j)=>segmentHitsWall(mouth,hub,w)?[j]:[]);
  return {id:`tip-${pair.tipIndex}/half-${i}`,tip:pair.tipIndex,mouth,hub,blockers};
 }));
 const innerDividerAreas=inner.map(pair=>{
  const shared=pair.prisms[0].walls.find(w=>pair.prisms[1].walls.some(v=>faceKey(v)===faceKey(w)));
  return subtractTubesJunction(shared).reduce((s,w)=>s+polygonArea(w),0);
 });
 const oppositePairs=[[0,1],[2,3],[4,5]].map(tips=>{
  const entry=ports.filter(p=>p.tip===tips[0]),exit=ports.filter(p=>p.tip===tips[1]);
  const routes=entry.flatMap(a=>exit.map(b=>({from:a.id,to:b.id,clear:a.blockers.length===0&&b.blockers.length===0})));
  return {tips,entryOpenings:entry.length,exitOpenings:exit.length,clearEndpointConnections:routes.filter(r=>r.clear).length,routes};
 });
 return {scope:'Geometric opening-to-opening connections through the shared chamber; not earlier wire labels or a count of arbitrary continuous trajectories.',
  innerDividerAreas,ports,oppositePairs,
  chamberGeometry:'The three complete second-layer square prisms are convex and share the origin. Their union is star-shaped; the pairwise-overlap cut removes internal walls. There is no further chamber branch choice.',
  allPortCentrePathsClear:ports.every(p=>!p.blockers.length)};
}
