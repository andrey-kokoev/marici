// Geometric mediation audit. Does not impose direct E/P adjacency and does not
// silently apply the single-cell two-existing-face rule to a simultaneous group.
import {cells} from './normal-ray-model.mjs';
const exchangeEP=(k,p)=>[p[2]+k-7,p[3],p[0]+7-k,p[1]];
import {assembleComponents} from '../strominger/demos/particle-overlap-tetrahedron/simplex-components.mjs';
const same=(a,b)=>a.every((x,i)=>x===b[i]);
const key=vs=>vs.map(p=>p.join(',')).sort().join('|');
const groups=assembleComponents().groups;
export function neutronMediation(k,assignments,start,end){
 if(!Number.isInteger(k)||k<1||k>7)throw Error('k must be 1..7');
 const roles=new Map(assignments.map(a=>[a.cell,a.role]));
 if(new Set([roles.get(start),roles.get(end)]).size!==2||![roles.get(start),roles.get(end)].every(r=>r==='electron'||r==='proton'))throw Error('Expected opposite charged endpoints');
 const region=cells.filter(c=>c.vertices.every(p=>p[0]<=k-5));
 const available=region.filter(c=>c.id===start||c.id===end||!roles.has(c.id)||roles.get(c.id)==='neutron');
 const adjacency=new Map(available.map(c=>[c.id,available.filter(d=>d.id!==c.id&&d.vertices.filter(p=>c.vertices.some(q=>same(p,q))).length===3).map(d=>d.id)]));
 const distance=new Map([[start,0]]),parents=new Map(),queue=[start];
 for(let i=0;i<queue.length;i++){
  const at=queue[i];if(distance.has(end)&&distance.get(at)>=distance.get(end))continue;
  for(const next of adjacency.get(at)){
   const d=distance.get(at)+1;
   if(!distance.has(next)){distance.set(next,d);parents.set(next,[at]);queue.push(next);}
   else if(distance.get(next)===d)parents.get(next).push(at);
  }
 }
 if(!distance.has(end))return {start,end,connected:false,paths:[],fillerCells:[]};
 const paths=[];
 function recover(at,tail){
  if(at===start){paths.push([start,...tail]);return;}
  for(const previous of parents.get(at))recover(previous,[at,...tail]);
 }
 recover(end,[]);
 const fillerCells=[...new Set(paths.flatMap(p=>p.slice(1,-1)))].sort((a,b)=>a-b),filler=new Set(fillerCells);
 const index=new Map(region.map(c=>[key(c.vertices),c.id]));
 const mirror=id=>index.get(key(cells[id].vertices.map(p=>exchangeEP(k,p))));
 const witnesses=paths.map(path=>({path,faces:path.slice(1).map((id,i)=>({from:path[i],to:id,vertices:cells[id].vertices.filter(p=>cells[path[i]].vertices.some(q=>same(p,q)))}))}));
 const faces=new Map();
 for(const id of fillerCells)for(const omitted of [0,1,2,3]){
  const face=cells[id].vertices.filter((_,i)=>i!==omitted),s=key(face);
  if(!faces.has(s))faces.set(s,{vertices:face,owners:[]});faces.get(s).owners.push(id);
 }
 const boundary=[...faces.values()].filter(f=>f.owners.length===1);
 const attachments=boundary.flatMap(f=>[start,end].filter(id=>f.vertices.every(p=>cells[id].vertices.some(q=>same(p,q)))).map(to=>({...f,to,role:roles.get(to)})));
 const supportCounts=fillerCells.map(id=>{
  const adjacent=region.filter(c=>c.id!==id&&c.vertices.filter(p=>cells[id].vertices.some(q=>same(p,q))).length===3).map(c=>c.id);
  return {cell:id,existing:adjacent.filter(n=>roles.has(n)),withFiller:adjacent.filter(n=>roles.has(n)||filler.has(n)),exteriorFaces:[0,1,2,3].filter(i=>cells[id].vertices.filter(p=>p[i]===(i===0?k-5:2)).length===3)};
 });
 const group=groups.find(g=>g.children.length===fillerCells.length&&g.children.every(id=>filler.has(id)));
 return {start,end,connected:true,existingNeutronMediation:paths.some(p=>p.slice(1,-1).every(id=>roles.get(id)==='neutron')),distance:distance.get(end),paths,reversePaths:paths.map(p=>[...p].reverse()),witnesses,fillerCells,octahedralGroup:group?.id??null,attachments,supportCounts,
  symmetryExchangesEndpoints:mirror(start)===end&&mirror(end)===start,
  symmetryPreservesAllRoutes:paths.every(p=>paths.some(q=>q.join(',')===p.map(mirror).reverse().join(','))),
  symmetryPreservesFiller:fillerCells.every(id=>filler.has(mirror(id))),
  singleCellRuleCanStart:supportCounts.some(s=>!roles.has(s.cell)&&s.exteriorFaces.length===0&&s.existing.length>=2),
  everyCellHasTwoSupportsAfterGroupAttachment:supportCounts.every(s=>s.withFiller.length>=2),
  proposedInternalRole:'neutron',assignmentsChanged:false};
}
