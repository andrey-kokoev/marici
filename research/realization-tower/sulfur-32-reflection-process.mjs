import {buildReflectionBundle} from './sulfur-32-reflection-bundle.mjs';
import certificate from '../strominger/results/regular-simplex-reflection-v1/verification.json' with {type:'json'};
const number=x=>{const [a,b='1']=String(x).split('/');return Number(a)/Number(b);};
export const reflectionStages=['Regular 4-simplex','Clone white reflection','Clone first 120° rotation','Clone outer-red reflection','Clone second 120° rotation'];
export function projectReflection(p,{reflectionAngle=35}={}){
 const [u,v,s,t]=p.map(number),x=Math.SQRT2*(u+v/2),y=Math.sqrt(1.5)*v,z=2/Math.sqrt(3)*s+t/(2*Math.sqrt(3)),w=Math.sqrt(5)/2*t;
 const angle=reflectionAngle*Math.PI/180;return [x*Math.cos(angle)+w*Math.sin(angle),y,z];
}
export function sulfur32ReflectionProcess(k,step=4,options={}){
 if(!Number.isInteger(step)||step<0||step>4)throw Error('Reflection stage must be 0..4');
 const stage=certificate.stages[step],copies=stage.copies.map(c=>({...c,vertices:c.vertices4.map(p=>projectReflection(p,options))}));
 const present=new Set(copies.map(c=>c.id));
 const cells=certificate.geometryGroups.filter(g=>g.copies.some(id=>present.has(id))).map(g=>{
  const histories=g.copies.filter(id=>present.has(id));return {id:g.cell,histories,copy:copies.find(c=>c.id===histories[0])};
 });
 const cellIds=new Set(cells.map(c=>c.id));
 const contacts=certificate.contacts.filter(e=>e.cells.every(id=>cellIds.has(id))).map(e=>({...e,points:e.vertices.map(p=>projectReflection(p,options))}));
 const nodes=cells.map(c=>({id:c.id,copies:c.histories,point:[0,1,2].map(i=>c.copy.vertices.reduce((s,p)=>s+p[i],0)/5)}));
 const centers=new Map(nodes.map(n=>[n.id,n.point]));
 const links=contacts.map(c=>({source:c.cells[0],target:c.cells[1],points:[centers.get(c.cells[0]),[0,1,2].map(i=>(c.points[0][i]+c.points[1][i])/2),centers.get(c.cells[1])],seam:c.map}));
 const reflectionBundle=buildReflectionBundle(certificate,step,p=>projectReflection(p,options));
 const envelope=certificate.stages[4].copies.flatMap(c=>c.vertices4.map(p=>projectReflection(p,options)));
 if(options.reflectionView!=='geometry'){
  const low=envelope.reduce((a,p)=>p[1]<a[1]?p:a),high=envelope.reduce((a,p)=>p[1]>a[1]?p:a);
  envelope.push(low.map((x,i)=>x-(i===1?1.6:0)),high.map((x,i)=>x+(i===1?1.6:0)));
 }
 return {k,step,canAdvance:step<4,reflectionBundle,reflectionWiring:{nodes,links},assignments:[],rays:[],retainedBodies:[],history:copies,
  copies,reflectionCells:cells,reflectionContacts:contacts,reflectionCycle:certificate.centralCircuit.cells,
  reflectionAudit:{stage:reflectionStages[step],histories:copies.length,cells:cells.length,contacts:contacts.length,wholeFrameReturn:step===4?'identity':null},
  summary:`Sulfur-32 reflection · ${reflectionStages[step]} · ${copies.length} histories · ${cells.length} regular 4-simplexes`,
  envelope};
}
