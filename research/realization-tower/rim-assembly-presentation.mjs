import {buildRimMatchedEsd7} from './rim-matched-esd7.mjs';
const assembly=buildRimMatchedEsd7(),byId=new Map(assembly.parents.map(b=>[b.id,b]));
const center=b=>b.vertices[0].map((_,i)=>b.vertices.reduce((s,p)=>s+p[i]/b.vertices.length,0));
const key=p=>p.map(x=>Math.abs(x)<1e-8?'0.00000000':x.toFixed(8)).join(',');
function edges(bodies){const result=new Map();for(const b of bodies){const keys=new Set(b.faces.flatMap(f=>f.flatMap((a,i)=>f.slice(i+1).map(c=>[key(a),key(c)].sort().join('|')))));for(const k of keys){if(!result.has(k))result.set(k,[]);result.get(k).push(b.id);}}return result;}
const parentEdges=edges(assembly.parents),beltEdges=edges(assembly.bodies),portLinks=[];
const endpoints=k=>k.split('|').map(s=>s.split(',').map(Number));
// Parent rim edges are subdivided; native belt edges are not. Match contained
// segments without subdividing the six volume cells or inventing face contacts.
function containsSegment(outer,inner){
 const [a,b]=endpoints(outer),v=b.map((x,i)=>x-a[i]),vv=v.reduce((s,x)=>s+x*x,0);
 return endpoints(inner).every(p=>{const t=p.reduce((s,x,i)=>s+(x-a[i])*v[i],0)/vv;return t>=-1e-7&&t<=1+1e-7&&Math.hypot(...p.map((x,i)=>x-a[i]-t*v[i]))<1e-7;});
}
for(const [edge,parents] of parentEdges)for(const [beltEdge,belts] of beltEdges)if(containsSegment(beltEdge,edge))for(const parent of parents)for(const belt of belts)portLinks.push({from:parent,to:belt,edge,beltEdge,kind:'rim-subsegment-identification'});
const allById=new Map([...assembly.parents,...assembly.bodies].map(b=>[b.id,b]));
export const rimAssemblyEnvelope=assembly.ports.flatMap(p=>[...p.target,p.apex]);
export function presentRimAssembly(proc){
 const remap=b=>{const placed=byId.get(b.id);return placed?{...b,vertices:placed.vertices,faces:placed.faces}:b;};
 return {...proc,retainedBodies:proc.retainedBodies.map(remap),emptyBodies:proc.emptyBodies.map(remap),presentationWireframes:proc.presentationWireframes.map(remap),attachmentBodies:assembly.bodies,
 presentationLabels:proc.presentationLabels.map(p=>({...p,point:assembly.mapParentPoint(p.point,p.cell.split(':')[0])})),
 interfaceGuides:[...proc.interfaceGuides.filter(g=>!g.seamFlow).map(g=>({...g,points:g.points.map(p=>assembly.mapParentPoint(p))})),...portLinks.map(e=>({points:[center(allById.get(e.from)),center(allById.get(e.to))],color:0xe6bd65,connector:true,rimPort:true}))],
 rimAssemblyAudit:{...assembly.audit,scope:'native six-cell annular belt joined to two ESD7 rims',rimEdgeLinks:portLinks.length,maxVertexGap:Math.max(...assembly.ports.map(p=>p.maxVertexGap)),ports:assembly.ports.map(({map,...p})=>p),ruleScope:'Parent colour rules retain the original glued-pair reference; no belt propagation law is asserted.'},
 doubleEsd7Audit:{...proc.doubleEsd7Audit,sharedInterface:false,seamLattice:{...proc.doubleEsd7Audit.seamLattice,flows:[],sharedPairs:[]}},
 summary:'One native six-cell annular belt, rim-matched between the two ESD7 halves. Parent labels retained; belt particle types unassigned.'};
}
