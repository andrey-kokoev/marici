import {growSimplex,simplexScene,applyProcess1,auditStrands} from './hex-edge-grid-model.generated.mjs';
const seed=growSimplex(-14,-14,4,2),process=applyProcess1(seed);
export const hexStrandStages=[simplexScene(seed),process.whiteStep,process.redStep,process.step3,process.step4,process.step5,process.step6,process];
export const hexStrandStageNames=['Seed · four binary choices','Reflect crossing white','Reflect crossing red','Point reflection','Rotate 120° clockwise','Point reflection','Rotate 120° clockwise','Point reflection'];
export const hexStrandIds=hexStrandStages[0].strands.map(s=>s.id);
export function buildHexStrandsView({hexStrandStage=0,hexStrandSpacing=.24,hexStrandSelection='all',hexStrandCopy=-1}={}){
 if(!Number.isInteger(hexStrandStage)||hexStrandStage<0||hexStrandStage>7)throw Error('Hex strand stage must be 0..7');
 const scene=hexStrandStages[hexStrandStage],audit=auditStrands(scene),vertices=[...scene.vertices.values()];
 const xs=vertices.map(v=>v.x),ys=vertices.map(v=>v.y),cx=(Math.min(...xs)+Math.max(...xs))/2,cy=(Math.min(...ys)+Math.max(...ys))/2;
 const project=(v,z=0)=>[(v.x-cx)*.12,-(v.y-cy)*Math.sqrt(3)*.12,z];
 const families=scene.strands.map((s,index)=>{
  const traces=hexStrandCopy>=0?s.traces.filter((_,i)=>i===hexStrandCopy):s.traces;
  const edgeIds=[...new Set(traces.flatMap(t=>t.edges))],z=(index-7.5)*hexStrandSpacing;
  return {id:s.id,index,selected:hexStrandSelection==='all'||hexStrandSelection===s.id,copyCount:s.traces.length,shownCopies:traces.length,
   edges:edgeIds.map(id=>{const e=scene.edges.get(id);return {id,points:[project(scene.vertices.get(e.a),z),project(scene.vertices.get(e.b),z)]};})};
 });
 const context=[...scene.edges.values()].map(e=>[project(scene.vertices.get(e.a)),project(scene.vertices.get(e.b))]);
 const points=vertices.map(v=>project(v)),xmin=Math.min(...points.map(p=>p[0]))-.1,xmax=Math.max(...points.map(p=>p[0]))+.1,ymin=Math.min(...points.map(p=>p[1]))-.1,ymax=Math.max(...points.map(p=>p[1]))+.1,zmax=7.5*hexStrandSpacing+.1;
 const envelope=[xmin,xmax].flatMap(x=>[ymin,ymax].flatMap(y=>[-zmax,zmax].map(z=>[x,y,z])));
 return {families,context,envelope,audit:{stage:hexStrandStage,strands:audit.strands,traceCopies:audit.traceCopies,unassignedSeams:audit.unassignedEdges.length,selection:hexStrandSelection,copy:hexStrandCopy,spacing:hexStrandSpacing,depthIsDisplayOnly:true}};
}
